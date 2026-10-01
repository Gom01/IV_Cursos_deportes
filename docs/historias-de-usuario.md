# Historias de usuario

## [HU1] Caminos señalizados y paradas reales ([#2](https://github.com/Gom01/IV_Cursos_deportes/issues/2))

Flavien: como corredor, quiero que mis recorridos pasen solo por caminos señalizados y empiecen y terminen en paradas que existen de verdad, para correr solo por caminos señalizados y seguros.

**Verificación:** cada tramo de un recorrido existe en la red oficial de swisstopo, y las paradas de salida y de llegada existen en la lista oficial de opentransportdata.

## [HU2] Distancia y desnivel de un recorrido ([#3](https://github.com/Gom01/IV_Cursos_deportes/issues/3))

Flavien: como corredor, quiero saber la distancia y el desnivel positivo reales de un recorrido, para saber si encaja con mi entrenamiento sin tener que calcularlo a mano.

**Verificación:** elijo algunos tramos reales del fichero. Dibujo el mismo camino en map.geo.admin.ch y apunto la distancia y el desnivel que muestra. Estos valores se escriben en un test automático, que comprueba que mi código da casi el mismo resultado.

## [HU3] Recorridos entre dos estaciones ([#4](https://github.com/Gom01/IV_Cursos_deportes/issues/4))

Flavien: como corredor sin coche, quiero recibir recorridos entre mi estación de salida y mi estación de llegada, con la distancia y el desnivel que pido, ordenados del más parecido al menos parecido a lo que pido, para no pasar una hora dibujándolos a mano. Otros corredores sin coche tienen la misma necesidad.

**Verificación:** si pido 17 km y 800 m de desnivel, todos los recorridos que salen tienen entre 15,3 y 18,7 km y entre 720 y 880 m de desnivel. Empiezan y terminan a menos de 500 m de las estaciones elegidas. El primero es el que tiene la menor diferencia total con lo que pido (en distancia y en desnivel).

## [HU4] No acabar en un camino demasiado difícil ([#5](https://github.com/Gom01/IV_Cursos_deportes/issues/5))

Christine: como senderista poco deportista, quiero elegir la dificultad máxima de los caminos, para no encontrarme en un camino demasiado difícil para mí y lesionarme.

**Verificación:** si elijo «Wanderweg» como dificultad máxima, ningún tramo de los recorridos que salen es «Bergwanderweg» ni «Alpinwanderweg».