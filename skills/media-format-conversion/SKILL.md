---
name: media-format-conversion
description: Convertir archivos audiovisuales conservando el original y verificando pistas y parámetros. En IAbot.io, asígnala a un empleado técnico audiovisual y aporta archivo original, formato de destino y requisitos de calidad y compatibilidad.
license: MIT
metadata:
  author: IAbot.io
  version: 0.1.0
  sector: Audiovisual y producción de vídeo
---

# Convertir medios con parámetros comprobados

## Uso en IAbot.io

Asigna esta skill a **un empleado técnico audiovisual** desde la biblioteca Skills de [IAbot.io](https://iabot.io). Aporta archivo original, formato de destino y requisitos de calidad y compatibilidad.

**Ejemplo de encargo:** «Convierte este vídeo al formato solicitado y comprueba duración, resolución, audio y subtítulos.»

**Resultado a revisar:** Archivo convertido, parámetros utilizados y comprobación de correspondencia.

## Cuándo usarla y qué necesita

Convertir archivos audiovisuales conservando el original y verificando pistas y parámetros

Trabaja con archivo original, formato de destino y requisitos de calidad y compatibilidad. Las composiciones requieren HyperFrames o editor compatible; inspección y conversión utilizan FFmpeg y ffprobe. Verifica herramientas, recursos, derechos y parámetros antes de producir.

## Procedimiento

1. Inspecciona contenedor, códecs, pistas, duración y dimensiones del original con ffprobe.
2. Decide si basta remultiplexar o se requiere recodificar, según compatibilidad y cambios pedidos.
3. Selecciona explícitamente pistas y parámetros evitando eliminar audio o subtítulos por omisión.
4. Genera un archivo nuevo sin sobrescribir el original y conserva el comando ejecutado.
5. Comprueba metadatos y reproduce muestras del resultado, revisando sincronía y final.

## Comprobación del resultado

- El comando no usa el mismo archivo como entrada y salida.
- Las pistas conservadas o descartadas están justificadas.
- El tamaño menor no se presenta como prueba de calidad equivalente.

## Entrega

Archivo convertido, parámetros utilizados y comprobación de correspondencia.

Conserva la identidad y revisión de las fuentes utilizadas. Señala los datos pendientes que afecten al resultado; no los sustituyas por valores inventados.

Usa [el registro de trabajo](assets/registro.csv) cuando no exista una plantilla del usuario; adapta sus filas sin perder las referencias.

## Referencias

- [HyperFrames, guía oficial](https://hyperframes.app/docs/1-startup/2-quickstart)
- [Documentación de FFmpeg](https://ffmpeg.org/documentation.html)
