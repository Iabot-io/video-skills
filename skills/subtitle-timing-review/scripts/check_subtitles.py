"""Check SRT timing and numbering; does not verify the words against the audio."""

import argparse
import json
from pathlib import Path
import re
import sys


TIMING = re.compile(r"^(\d{2,}):(\d{2}):(\d{2})[,.](\d{3})\s*-->\s*(\d{2,}):(\d{2}):(\d{2})[,.](\d{3})(?:\s+.*)?$")


def seconds(parts):
    hours, minutes, secs, milliseconds = map(int, parts)
    if minutes >= 60 or secs >= 60:
        raise ValueError("Minutes and seconds must be below 60")
    return hours * 3600 + minutes * 60 + secs + milliseconds / 1000


def inspect(text, duration=None):
    text = text.lstrip("\ufeff").replace("\r\n", "\n").replace("\r", "\n").strip()
    blocks = re.split(r"\n[ \t]*\n", text) if text else []
    issues = []
    cues = []
    active_end = None
    active_block = None
    previous_start = None
    for position, block in enumerate(blocks, 1):
        lines = block.splitlines()
        if len(lines) < 3 or not lines[0].strip().isdigit():
            issues.append({"block": position, "code": "INVALID_SRT_BLOCK"})
            continue
        number = int(lines[0].strip())
        if number != position:
            issues.append({"block": position, "code": "NON_SEQUENTIAL_NUMBER", "number": number})
        match = TIMING.fullmatch(lines[1].strip())
        if not match:
            issues.append({"block": position, "code": "INVALID_TIMING"})
            continue
        try:
            start = seconds(match.groups()[:4])
            end = seconds(match.groups()[4:])
        except ValueError:
            issues.append({"block": position, "code": "INVALID_TIMESTAMP"})
            continue
        if end <= start:
            issues.append({"block": position, "code": "NON_POSITIVE_DURATION"})
        if previous_start is not None and start < previous_start:
            issues.append({"block": position, "code": "OUT_OF_ORDER"})
        if active_end is not None and start < active_end:
            issues.append({"block": position, "code": "OVERLAP", "overlaps_with_block": active_block,
                           "review_required": True})
        if duration is not None and end > duration:
            issues.append({"block": position, "code": "AFTER_MEDIA_END"})
        content = "\n".join(lines[2:]).strip()
        if not content:
            issues.append({"block": position, "code": "EMPTY_TEXT"})
        cues.append({"number": number, "start": start, "end": end, "characters": len(content)})
        previous_start = start
        if active_end is None or end > active_end:
            active_end, active_block = end, position
    if not blocks:
        issues.append({"code": "NO_CUES"})
    return {"format": "SRT", "cues": cues, "issues": issues,
            "structural_ok": not issues, "audio_and_readability_review_required": True,
            "limits": "Overlap can be intentional; review it. The check does not transcribe, rate readability or certify accessibility."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--out", type=Path)
    parser.add_argument("--duration", type=float)
    args = parser.parse_args()
    if args.duration is not None and (args.duration <= 0 or not args.duration < float("inf")):
        parser.error("Duration must be a positive finite number")
    if args.out and (args.out.resolve() == args.input.resolve() or
                     (args.out.exists() and args.input.exists() and args.out.samefile(args.input))):
        parser.error("Report must not overwrite subtitles")
    try:
        report = inspect(args.input.read_text(encoding="utf-8-sig"), args.duration)
        rendered = json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False) + "\n"
        if args.out:
            args.out.write_text(rendered)
        else:
            print(rendered, end="")
        return 0 if report["structural_ok"] else 2
    except (OSError, UnicodeError) as error:
        print(f"Could not inspect subtitles: {type(error).__name__}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
