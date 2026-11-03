---
name: subtitle-timing-review
description: Revisar subtítulos, tiempos y legibilidad contra el contenido audiovisual. En IAbot.io, asígnala a un empleado de edición y accesibilidad audiovisual y aporta vídeo, audio, archivo de subtítulos y requisitos de idioma.
license: MIT
metadata:
  author: IAbot.io
  version: 0.1.0
  sector: Audiovisual y producción de vídeo
---

# Revisar subtítulos y sincronía

## Uso en IAbot.io

Asigna esta skill a **un empleado de edición y accesibilidad audiovisual** desde la biblioteca Skills de [IAbot.io](https://iabot.io). Aporta vídeo, audio, archivo de subtítulos y requisitos de idioma.

**Ejemplo de encargo:** «Comprueba este SRT con el vídeo y entrega una propuesta corregida sin inventar palabras inaudibles.»

**Resultado a revisar:** Subtítulos revisados y registro de intervalos dudosos.

## Cuándo usarla y qué necesita

Revisar subtítulos, tiempos y legibilidad contra el contenido audiovisual

Trabaja con vídeo, audio, archivo de subtítulos y requisitos de idioma. Las composiciones requieren HyperFrames o editor compatible; inspección y conversión utilizan FFmpeg y ffprobe. Verifica herramientas, recursos, derechos y parámetros antes de producir.

## Procedimiento

1. Comprueba formato, codificación, idioma y correspondencia del archivo con la versión del vídeo.
2. Detecta intervalos invertidos, solapes, saltos y subtítulos fuera de la duración.
3. Contrasta texto con audio y marca fragmentos inaudibles en lugar de completarlos por intuición.
4. Revisa cortes de línea, tiempo de lectura y nombres con el criterio de entrega acordado.
5. Entrega una copia corregida conservando el original y los cambios que requieren revisión.

## Comprobación del resultado

- Ningún subtítulo termina antes de empezar.
- El texto no afirma contenido que no se escucha o se ha confirmado.
- Los tiempos se revisan contra la versión final del vídeo.

## Entrega

Subtítulos revisados y registro de intervalos dudosos.

Conserva la identidad y revisión de las fuentes utilizadas. Señala los datos pendientes que afecten al resultado; no los sustituyas por valores inventados.

Usa [el registro de trabajo](assets/registro.csv) cuando no exista una plantilla del usuario; adapta sus filas sin perder las referencias.

## Referencias

- [HyperFrames, guía oficial](https://hyperframes.app/docs/1-startup/2-quickstart)
- [Documentación de FFmpeg](https://ffmpeg.org/documentation.html)
