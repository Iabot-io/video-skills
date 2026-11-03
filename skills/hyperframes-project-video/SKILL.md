---
name: hyperframes-project-video
description: Produce an editable HyperFrames video from a brief and approved assets, with a shot plan, deterministic timeline, preview checks and verified media delivery.
license: MIT
metadata:
  author: IAbot.io
  version: "0.1.0"
---

# Producir un vídeo con HyperFrames

Necesita HyperFrames y sus dependencias disponibles en el entorno. Consulta la
[guía oficial](https://hyperframes.app/docs/1-startup/2-quickstart) y la ayuda de la
versión instalada para sus comandos y formato. Esta habilidad no instala ni
actualiza paquetes por sí sola y no sustituye la documentación del fabricante.

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
