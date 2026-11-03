"""Inspect a local video with ffprobe; never modify or upload the source file."""

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
import subprocess
import sys


def number(value):
    try:
        parsed = float(Fraction(str(value)))
        return parsed if math.isfinite(parsed) and parsed >= 0 else None
    except (ValueError, ZeroDivisionError, TypeError):
        return None


def positive(value):
    parsed = number(value)
    if parsed is None or parsed <= 0:
        raise argparse.ArgumentTypeError("Expected a positive finite number")
    return parsed


def digest(path):
    result = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            result.update(chunk)
    return result.hexdigest()


def inspect(path, expectations):
    process = subprocess.run(
        ["ffprobe", "-v", "error", "-show_format", "-show_streams", "-of", "json", str(path)],
        capture_output=True, text=True, timeout=30, check=False,
    )
    if process.returncode:
        raise ValueError("ffprobe could not read the input as valid media")
    probe = json.loads(process.stdout)
    if not isinstance(probe, dict) or not isinstance(probe.get("streams"), list):
        raise ValueError("ffprobe returned an invalid media description")
    streams = probe["streams"]
    videos = [s for s in streams if s.get("codec_type") == "video"
              and not s.get("disposition", {}).get("attached_pic")]
    video = videos[0] if videos else {}
    media_format = probe.get("format", {})
    actual = {
        "width": video.get("width"), "height": video.get("height"),
        "fps": number(video.get("avg_frame_rate")) or number(video.get("r_frame_rate")),
        "duration": number(video.get("duration")) or number(media_format.get("duration")),
    }
    issues = [] if videos else ["No video stream found"]
    checks = []
    for key in ("width", "height", "fps", "duration"):
        expected = expectations.get(key)
        if expected is None:
            continue
        tolerance = expectations["duration_tolerance"] if key == "duration" else 0.01 if key == "fps" else 0
        value = actual[key]
        passed = isinstance(value, (int, float)) and abs(value - expected) <= tolerance
        checks.append({"field": key, "expected": expected, "actual": value,
                       "tolerance": tolerance, "passed": passed})
        if not passed:
            issues.append(f"{key} does not match the requested value")
    return {
        "file": str(path), "sha256": digest(path), "bytes": path.stat().st_size,
        "selected_video_stream": video.get("index"), "actual": actual,
        "streams": [{key: s.get(key) for key in (
            "index", "codec_type", "codec_name", "width", "height", "avg_frame_rate",
            "r_frame_rate", "duration", "nb_frames", "sample_rate", "channels", "disposition",
        ) if key in s} for s in streams],
        "format": media_format.get("format_name"), "checks": checks,
        "metadata_ok": not issues, "issues": issues, "visual_review_required": True,
        "audio_review_required": any(s.get("codec_type") == "audio" for s in streams),
        "limitations": "Metadata inspection does not decode every frame or verify picture, sound, content or rights.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("video", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    for name in ("width", "height", "fps", "duration"):
        parser.add_argument("--" + name, type=positive)
    parser.add_argument("--duration-tolerance", type=positive, default=0.1)
    args = parser.parse_args()
    source = args.video.resolve()
    output = args.out.resolve()
    if source == output or (source.exists() and output.exists() and source.samefile(output)):
        parser.error("The report must not overwrite the input video")
    try:
        if not source.is_file():
            raise ValueError("Input video is not a local file")
        report = inspect(source, vars(args))
        output.write_text(json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False) + "\n")
    except (OSError, ValueError, subprocess.TimeoutExpired) as error:
        print(f"Inspection failed: {error}", file=sys.stderr)
        return 1
    print(json.dumps({"report": str(output), "metadata_ok": report["metadata_ok"],
                      "issues": report["issues"]}, ensure_ascii=False))
    return 0 if report["metadata_ok"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
