# Planificación

## Hito 0: Modelo del problema

**Producto:** mi código con los elementos del problema, leídos desde los ficheros oficiales, sin cálculos todavía:

- `Tramo`: un trozo de camino. Tiene un `uuid`, una lista de puntos (x, y, z) y la dificultad oficial (`wanderwege`).
- `Parada`: una parada de tren o autobús. Tiene un nombre y una posición (x, y).
- `Criterios`: lo que pido. La distancia, el desnivel, la dificultad máxima, la estación de salida y la estación de llegada.
- `Recorrido`: varios tramos seguidos, entre la estación de salida y la estación de llegada.

**Dónde:** `src/`.

**Validación:**

- Creo `Tramo` y `Parada` a partir de líneas reales de los ficheros de swisstopo y de opentransportdata, y compruebo que todos los datos están bien guardados (puntos, altitud, dificultad, nombre y posición).
- Creo unos `Criterios` con una petición real mía: 17 km, 800 m de desnivel y dos estaciones reales.
- Creo un `Recorrido` con tramos reales del fichero que están seguidos.

**Historias de usuario:** HU1

## Hito 1: Distancia y desnivel de un recorrido

**Producto:** mi código que calcula la distancia y el desnivel positivo de un tramo, y después de un recorrido (varios tramos seguidos, teniendo en cuenta el sentido en que se recorre cada tramo).

**Dónde:** `src/`, `tests/`.

**Validación:**

- Elijo algunos tramos reales del fichero y dibujo el mismo camino en map.geo.admin.ch. Apunto la distancia y el desnivel que muestra.
- Estos valores se escriben en tests automáticos, que comprueban que mi código da el mismo resultado, con menos de un 5 % de diferencia.

**Historias de usuario:** HU2

## Hito 2: Recorridos entre dos estaciones

**Producto:** mi código que une tramos para crear recorridos entre la estación de salida y la estación de llegada, que cumplen lo que pido:

- **Estaciones:** el recorrido empieza y termina a menos de 500 m de las estaciones elegidas (unos 5 minutos andando, porque Christine no quiere andar mucho hasta el camino).
- **Distancia y desnivel:** se parecen a lo que pido, más o menos un 10 %. Por ejemplo, entre 15,3 y 18,7 km si pido 17 km, eso me vale para entrenar.
- **Dificultad:** ningún tramo es más difícil que la dificultad máxima elegida.

Los recorridos se ordenan del más parecido al menos parecido a lo que pido (primero el que tiene la menor diferencia total en distancia y desnivel).

**Dónde:** `src/`, `tests/`.

**Validación:** tests automáticos con los datos reales de una zona pequeña cerca de mi casa.

- Con una petición real entre dos estaciones reales (por ejemplo 10 km y 500 m de desnivel), sale al menos un recorrido.
- Todos los recorridos que salen empiezan y terminan a menos de 500 m de las estaciones elegidas, tienen una distancia y un desnivel a más o menos un 10 %, no tienen ningún tramo más difícil que el máximo, y sus tramos están seguidos.
- El primer recorrido es el que tiene la menor diferencia con lo que pido.
- Una petición imposible (por ejemplo 200 km en esa zona) no da ningún recorrido.

**Historias de usuario:** HU3, HU4

## Más adelante

Estos tres hitos son internos: es código para mí, el desarrollador. Después vendrá el primer producto externo: un servicio en la nube que cualquier corredor o senderista pueda usar.