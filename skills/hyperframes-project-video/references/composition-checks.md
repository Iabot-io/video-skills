# Comprobar una composición de HyperFrames

Consulta la versión instalada y su ayuda antes de usar comandos o ejemplos de
otra versión. La [guía oficial](https://hyperframes.app/docs/1-startup/2-quickstart)
describe el contrato de la composición; estos controles ayudan a revisarlo:

- La raíz declara identidad, anchura y altura de la composición.
- Los elementos temporizados declaran comienzo, duración y pista, además de la
  clase `clip` cuando el formato de esa versión la utiliza.
- Una animación GSAP se registra en la colección de timelines de la composición
  y se crea pausada para que el motor pueda buscar cada instante.
- Cargar fuentes, imágenes o audio debe terminar antes de capturar los fotogramas.
  Comprueba el estado inicial tras una carga limpia, no solo después de reproducir.
- Revisar un instante tras avanzar y después de retroceder debe dar la misma
  composición. Detecta así animaciones dependientes de efectos acumulativos.

El entorno del inicio rápido utiliza Node.js 22 o posterior y FFmpeg para
codificación local. Sigue las dependencias declaradas por la versión del proyecto.
La previsualización se abre con `npx hyperframes preview` y el ejemplo oficial
exporta con `npx hyperframes render --output output.mp4`. Estos comandos pueden
resolver paquetes con npm; usa la instalación existente y las políticas del
entorno, y no conviertas una revisión de vídeo en una actualización automática.
