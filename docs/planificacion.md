# Planificación

## Hito 0: Modelo del problema

**Producto:** el modelo de los conceptos que aparecen en las historias de usuario, sin lógica de negocio.

**Validación:**

- Cada elemento del modelo corresponde a un concepto que aparece en las HU (tramo, parada, recorrido…): para cada uno se puede indicar en qué HU aparece.
- Con el modelo se puede representar un tramo real de swisstopo y una parada real de opentransportdata, y al compararlos con los mismos en las fuentes oficiales tienen los mismos datos.


**Historias de usuario:** HU1

## Hito 1: Distancia y desnivel de un recorrido

**Producto:** la primera parte de la lógica de negocio sobre el modelo del Hito 0, con sus tests automáticos.

**Validación:**

- Elijo algunos tramos reales del fichero y dibujo el mismo camino en map.geo.admin.ch. Apunto la distancia y el desnivel que muestra.
- Estos valores se escriben en tests automáticos, que comprueban que mi código da el mismo resultado, con menos de un 5 % de diferencia.


**Historias de usuario:** HU2

## Hito 2: Recorridos entre dos estaciones

**Producto:** la lógica de negocio que resuelve una petición entre dos estaciones, sobre lo entregado en los hitos anteriores, con sus tests automáticos.

**Validación:** tests automáticos con los datos reales de una zona pequeña cerca de mi casa.

- Con una petición real entre dos estaciones reales (por ejemplo 10 km y 500 m de desnivel), sale al menos un recorrido.
- Todos los recorridos que salen empiezan y terminan a menos de 500 m de las estaciones elegidas (unos 5 minutos andando, porque Christine no quiere andar mucho hasta el camino).
- Todos tienen una distancia y un desnivel a más o menos un 10 % de lo que pido (por ejemplo, entre 15,3 y 18,7 km si pido 17 km).
- Ningún recorrido tiene un tramo más difícil que la dificultad máxima elegida, y sus tramos están seguidos.
- El primer recorrido es el que tiene la menor diferencia total con lo que pido (en distancia y desnivel).
- Una petición imposible (por ejemplo 200 km en esa zona) no da ningún recorrido.

**Historias de usuario:** HU3, HU4

## Más adelante

Estos tres hitos son internos: es código para mí, el desarrollador. Después vendrá el primer producto externo: un servicio en la nube que cualquier corredor o senderista pueda usar.