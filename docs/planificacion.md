# Planificación

## Hito 0

Hito interno, para el objetivo 2. Trabaja solo con la [HU1](historias-de-usuario.md).

**Producto:** código sin lógica de negocio. Cada parte del código sale de un issue en el que se ha analizado la HU1. Para analizar el problema se usa el diseño dirigido por el dominio

**Validación:** el hito es válido si:

- Cada issue sale de la HU1 y es un problema, no una tarea.
- Cada parte del código viene de un issue, y el issue explica por qué es así.
- Los issues usan las mismas palabras del problema, para que quien programa y yo entendamos lo mismo.
- Se han pensado los errores que pueden pasar al crear cada parte.
- Cada commit dice qué issue resuelve.

## Hito 1

Hito interno, para el objetivo 4. Sigue con el problema de la [HU1](historias-de-usuario.md), a partir de lo hecho en el Hito 0. El problema se divide en problemas más pequeños que se pueden comprobar con tests.

**Producto:** el código del Hito 0 con la lógica de negocio que resuelve la HU1, y sus tests, que se ejecutan con una sola orden.

**Validación:** todos los tests pasan con esa orden y comprueban el problema de la HU1 tal como está descrito, con datos reales de swisstopo y de opentransportdata. Además compruebo que:

- Cada test viene de un issue, y cada issue de la HU1.
- Los tests también comprueban los errores posibles.
- Cada commit dice qué issue resuelve.

## Más adelante

Después de estos dos hitos internos vendrá el primer producto para los usuarios: un servicio en la nube.