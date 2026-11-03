---
name: video-delivery-review
description: Review a delivered video against requested resolution, frame rate, duration, audio and visual requirements, combining ffprobe metadata with playback and representative frame inspection.
license: MIT
metadata:
  author: IAbot.io
  version: "0.1.0"
---

# Comprobar una entrega de vídeo

Necesita Python 3, `ffprobe` de FFmpeg y una forma de reproducir u observar el
vídeo. Trabaja sobre el archivo final que se va a entregar, no solo su proyecto
o una previsualización anterior.

## Identidad y requisitos

Identifica archivo, revisión y especificación solicitada: tamaño, relación de
aspecto, duración, fps, códec, audio, idioma y subtítulos. Conserva el original;
esta revisión no recodifica ni sube archivos.

Ejecuta el ayudante desde esta carpeta, indicando solo expectativas acordadas:

```sh
python3 scripts/inspect_video.py video.mp4 --out informe.json --width 1920 --height 1080 --fps 25 --duration 30
```

El informe contiene SHA-256, tamaño del archivo, pistas y metadatos de duración.
El código 2 indica que no hay vídeo o que falla alguna expectativa; el código 1,
que no se pudo inspeccionar. Si hay varias pistas de vídeo, el informe identifica
la seleccionada y conserva todas las pistas para revisarlas.

## Comprobación audiovisual

1. Abre el archivo y observa principio, final y cada transición importante.
   Busca fotogramas negros inesperados, recortes, rótulos ilegibles y recursos
   ausentes. Reproduce también las partes con movimiento y sonido.
2. Escucha voz y música: comprueba idioma, sincronía, cortes y claridad. Una pista
   de audio declarada no demuestra sonido audible o correcto.
3. Contrasta textos, cifras, imágenes y licencias con las fuentes del encargo.
   Revisa subtítulos y zonas seguras en el tamaño de destino cuando correspondan.
4. Si detectas un defecto, identifica el intervalo y su causa antes de modificar
   la composición. Verifica la exportación corregida como un archivo nuevo.

## Informe

Entrega el resultado por requisito, con evidencia y pendientes. Los metadatos
no verifican el contenido de todos los fotogramas, la calidad, el audio ni la
ausencia de fotogramas dañados. Si no pudiste reproducir el archivo, conserva
esa limitación y no declares aprobada la revisión audiovisual.

Referencia: [documentación de ffprobe](https://ffmpeg.org/ffprobe.html).
