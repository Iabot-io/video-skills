# Video skills · IAbot.io

**Habilidades abiertas para agentes de IA que producen y revisan vídeos a partir
de un encargo, archivos y herramientas autorizadas.**

Publicadas por [IAbot.io](https://iabot.io). Usan el formato abierto
[Agent Skills](https://agentskills.io/specification), con plantillas y un ayudante
de inspección de medios.

## Habilidades

| Skill | Trabajo y entregable |
| --- | --- |
| [hyperframes-project-video](skills/hyperframes-project-video/SKILL.md) | Convertir un encargo en una composición editable de HyperFrames, previsualizarla y entregar su vídeo. |
| [architectural-presentation-video](skills/architectural-presentation-video/SKILL.md) | Preparar una presentación audiovisual con planos, renders y textos trazables al mismo proyecto. |
| [video-delivery-review](skills/video-delivery-review/SKILL.md) | Comprobar metadatos del archivo y revisar imagen, sonido y requisitos de entrega. |

## Instalación

```sh
npx skills add iabot-io/video-skills --list
npx skills add iabot-io/video-skills
npx skills add iabot-io/video-skills --skill hyperframes-project-video
```

Instalar una skill no instala HyperFrames, FFmpeg, un navegador ni conexiones de
terceros. Cada `SKILL.md` indica sus requisitos. Se mantienen los permisos y el
presupuesto del entorno que la utilice.

## Ejemplos de uso

- «Crea un vídeo de 30 segundos con estas imágenes y textos. Usa HyperFrames y
  entrega también la composición editable».
- «Presenta este proyecto de reforma con el plano y estos tres renders. Distingue
  estado actual y propuesta y conserva los nombres de cada estancia».
- «Revisa si este MP4 cumple 1920 × 1080, 25 fps y 30 segundos, y comprueba si se
  cortan los rótulos o el final del audio».

## HyperFrames y licencias

[HyperFrames](https://github.com/heygen-com/hyperframes) es un proyecto de HeyGen,
independiente de IAbot.io. Esta colección aporta procedimientos de producción y
entrega; no redistribuye su código ni sus skills oficiales. Consulta sus requisitos
y licencia en el proyecto original. Cada imagen, fuente, vídeo o audio utilizado
en una composición conserva sus propios derechos.

Las instalaciones con telemetría habilitada del CLI de skills contribuyen al
descubrimiento según las reglas de [skills.sh](https://www.skills.sh/docs/faq).
No se promete indexación inmediata ni posición en el directorio.

## Comprobación local

```sh
python3 -m pip install -r scripts/requirements-validation.txt
python3 scripts/validate_skills.py
```

El ayudante `inspect_video.py` necesita `ffprobe` en PATH. Su informe técnico debe
acompañarse de una revisión audiovisual: los metadatos no prueban que las imágenes
y el sonido sean correctos.

## English

Open video production skills for AI agents: HyperFrames project delivery,
architecture presentations and media verification. Spanish instructions with
English discovery metadata; deliver in the user's language. Licensed under
[MIT](LICENSE), published by [IAbot.io](https://iabot.io).
