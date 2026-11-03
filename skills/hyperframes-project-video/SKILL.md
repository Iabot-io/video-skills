---
name: hyperframes-project-video
description: Producir una composición editable de HyperFrames y verificar el vídeo exportado. En IAbot.io, asígnala a un empleado de producción audiovisual y aporta briefing, recursos autorizados, duración y formatos de entrega.
license: MIT
metadata:
  author: IAbot.io
  version: 0.1.0
  sector: Audiovisual y producción de vídeo
---

# Producir un vídeo con HyperFrames

## Uso en IAbot.io

Asigna esta skill a **un empleado de producción audiovisual** desde la biblioteca Skills de [IAbot.io](https://iabot.io). Aporta briefing, recursos autorizados, duración y formatos de entrega.

**Ejemplo de encargo:** «Crea un vídeo con estos recursos y entrega la composición editable y el archivo final revisado.»

**Resultado a revisar:** Vídeo, proyecto editable y relación de requisitos y recursos.

## Preparar el encargo

Identifica objetivo, audiencia, duración, relación de aspecto, idioma, canal y
formatos de entrega. Reutiliza las decisiones ya dadas. Si falta una decisión
reversible, adopta una opción razonable y comunícala; pregunta por lo que cambie
materialmente el contenido o requiera recursos que el usuario no ha autorizado.

Inventaría imágenes, clips, logos, fuentes, textos y audio reales. Conserva
procedencia y licencia de cada recurso. Identifica qué material es definitivo y
qué es una propuesta. No generes testimonios, cifras o resultados comerciales
como si hubieran sido aportados.

## Composición editable

1. Usa [la plantilla de guion](assets/guion-video.csv) o el guion del usuario para
   fijar orden, tiempos, recurso, texto en pantalla y función de cada plano.
2. Abre el proyecto existente o prepara uno con la versión instalada. Mantén los
   recursos junto al proyecto y evita depender de enlaces temporales para entregar
   un editable que deba reabrirse.
3. Construye la composición con los mecanismos de tiempo y animación admitidos
   por esa versión. Toda animación debe reconstruirse al buscar un instante;
   no bases su estado visual solo en tiempo transcurrido, azar o red. Usa los
   [controles de composición](references/composition-checks.md) para revisar el
   contrato técnico y los requisitos del entorno.
4. Ajusta encuadre y tipografía al tamaño final. Comprueba saltos de línea,
   contraste, zonas seguras, duración de lectura y subtítulos si se solicitaron.
5. Alinea voz, música y transiciones. Usa recursos autorizados; no actives servicios
   de voz, generación o render remoto de pago sin el alcance correspondiente.

## Previsualizar, renderizar y entregar

Ejecuta las comprobaciones disponibles en el CLI y observa fotogramas de comienzo,
cambios de escena y final. Reproduce la composición para revisar ritmo y sonido.
Un chequeo de estructura no acredita sincronización ni legibilidad.

Renderiza con los parámetros acordados usando la vía disponible y autorizada.
Conserva el estado de un render en curso; un retraso no autoriza duplicarlo.
Abre el vídeo exportado y comprueba duración, tamaño, principio, final y transiciones.

Entrega el vídeo, la composición editable y los recursos redistribuibles pedidos.
Incluye versión de HyperFrames y requisitos para reabrirla; documenta los recursos
externos que no se puedan redistribuir. Distingue proyecto guardado, previsualización
y archivo final realmente renderizado.

## Ejemplo reproducible

Consulta el [vídeo de IAbot.io y su proyecto editable](https://github.com/Iabot-io/video-skills/tree/main/examples/iabot-intro):
una composición de 12 segundos con escenas, logotipo y comprobaciones de entrega.
Utilízalo como referencia de estructura y sustituye el contenido por el encargo
real; sus cifras corresponden al catálogo publicado el 3 de noviembre de 2026.
Descarga el proyecto completo si vas a editarlo: es un ejemplo del repositorio y
no se copia al ordenador por importar las instrucciones de esta skill.
