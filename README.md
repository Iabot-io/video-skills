# Audiovisual y producción de vídeo · Skills para empleados IA de IAbot.io

Encargos audiovisuales, HyperFrames, edición de archivos y revisión de subtítulos y entregables.

Procedimientos abiertos y concretos para agentes IA, con entradas, criterios de revisión y entregables. Publicados por [IAbot.io](https://iabot.io), plataforma de empleados IA con memoria, aplicaciones y ordenador virtual Linux.

## Habilidades y uso

| Skill | Empleado en IAbot.io | Entrega que revisar |
| --- | --- | --- |
| [Producción de vídeos con HyperFrames](skills/hyperframes-project-video/SKILL.md) | un empleado de producción audiovisual | Vídeo, proyecto editable y relación de requisitos y recursos. |
| [Presentaciones audiovisuales de arquitectura](skills/architectural-presentation-video/SKILL.md) | un empleado audiovisual del proyecto | Presentación audiovisual y referencias de los planos y rótulos utilizados. |
| [Revisar entregas de vídeo](skills/video-delivery-review/SKILL.md) | un empleado de control de calidad audiovisual | Informe de metadatos, revisión audiovisual y defectos localizados. |
| [Revisar subtítulos y sincronía](skills/subtitle-timing-review/SKILL.md) | un empleado de edición y accesibilidad audiovisual | Subtítulos revisados y registro de intervalos dudosos. |
| [Convertir medios con parámetros comprobados](skills/media-format-conversion/SKILL.md) | un empleado técnico audiovisual | Archivo convertido, parámetros utilizados y comprobación de correspondencia. |
| [Preparar un briefing audiovisual ejecutable](skills/audiovisual-production-brief/SKILL.md) | un empleado de coordinación audiovisual | Briefing, escaleta y lista de recursos y decisiones para producción. |

## Instalación y uso en IAbot.io

```sh
npx skills add Iabot-io/video-skills --list
npx skills add Iabot-io/video-skills
```

En la plataforma, abre **Skills**, revisa la habilidad e impórtala con el ámbito adecuado. Adjunta sus entradas y da el encargo al empleado. Consulta [la guía de uso en IAbot.io](USO-EN-IABOT.md) para el recorrido completo.

## Ejemplos

- **Producción de vídeos con HyperFrames:** «Crea un vídeo con estos recursos y entrega la composición editable y el archivo final revisado.»
- **Presentaciones audiovisuales de arquitectura:** «Presenta este proyecto con los planos y renders adjuntos, distinguiendo estado actual y propuesta.»
- **Revisar entregas de vídeo:** «Revisa este MP4 frente a la especificación y separa la comprobación técnica de la visual y sonora.»

Consulta el [vídeo de demostración y su proyecto editable de HyperFrames](examples/iabot-intro/README.md).

## Herramientas y límites

Las composiciones requieren HyperFrames o editor compatible; inspección y conversión utilizan FFmpeg y ffprobe. Verifica herramientas, recursos, derechos y parámetros antes de producir.

La colección no instala aplicaciones ni concede accesos. Las referencias se comprueban según la fecha, jurisdicción y alcance del encargo. Los resultados profesionales o administrativos conservan sus responsables y revisiones.

## Fuentes de referencia

- [HyperFrames, guía oficial](https://hyperframes.app/docs/1-startup/2-quickstart)
- [Documentación de FFmpeg](https://ffmpeg.org/documentation.html)

Las fuentes orientan el método; su enlace no significa que una institución certifique o avale estas skills.

## Comprobación y licencia

```sh
python3 -m pip install -r scripts/requirements-validation.txt
python3 scripts/validate_skills.py
```

Se comprueban formato, recursos y referencias locales. Esa validación no acredita por sí sola un recorrido con un empleado real ni resultados en datos de producción. [Licencia MIT](LICENSE).

Agent Skills for AI employees and agents. Each skill includes an IAbot.io usage example and remains usable in compatible agents outside the platform.
