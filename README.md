# Rutas de senderismo a medida en Suiza

## Problema

Corro en Suiza y me gusta entrenar de forma progresiva, muchas veces en sitios que no conozco. Siempre sé exactamente la distancia que quiero hacer, el desnivel y desde dónde salgo (en transporte público). Por ejemplo, sé que quiero correr 17 km con 800 m de desnivel y que salgo de una estación de tren concreta. Mi problema es que pierdo mucho tiempo creando un recorrido que encaje con lo que quiero.

Ahora mismo, para preparar un recorrido tengo que:

1. Ir a [map.geo.admin.ch](https://map.geo.admin.ch/) de swisstopo y dibujar un recorrido a mano, tramo por tramo, empezando en una estación de tren o una parada de autobús.
2. Mirar la distancia y el desnivel del recorrido. Si no son los que quiero, añado o quito tramos y vuelvo a mirar. Muchas veces tengo que repetirlo varias veces.

Este proceso me hace perder mucho tiempo (unas 2 o 3 horas por semana): tengo que dibujar el recorrido a mano y después cambiarlo hasta que tenga la distancia y la dificultad que quiero. Como corro 2 o 3 veces por semana, pierdo mucho tiempo haciendo estos cálculos, y creo que no soy el único. Además, prefiero usar los datos de swisstopo porque son suizos, oficiales y fiables.

## Conceptos

- **Trail:** correr por caminos de montaña o de campo, no por carretera. Normalmente hay subidas y bajadas.
- **Distancia:** los kilómetros que tiene el recorrido.
- **Desnivel positivo:** la suma de todos los metros que se suben durante el recorrido. Las bajadas no se cuentan. Por ejemplo, si subo 300 m, bajo 100 m y subo otra vez 200 m, el desnivel positivo es 500 m.
- **Dificultad:** en Suiza, cada camino tiene una categoría oficial, marcada con colores en las señales:
  - *Wanderweg* (amarillo): camino fácil, para todo el mundo.
  - *Bergwanderweg* (blanco-rojo-blanco): camino de montaña, más empinado y estrecho. Hay que tener buen equilibrio.
  - *Alpinwanderweg* (blanco-azul-blanco): camino alpino, muy difícil. A veces hay que usar las manos.
- **Tramo:** un trozo de camino entre dos cruces. Los datos oficiales dan los caminos en tramos, no en recorridos completos.
- **Recorrido:** varios tramos seguidos, desde la salida hasta la llegada.

## Datos

En Suiza, la Confederación publica datos oficiales, gratuitos y que se pueden descargar. Hay dos fuentes útiles para este problema:

1. **Caminos de senderismo (swissTLM3D Wanderwege)**, en [opendata.swiss](https://opendata.swiss/fr/dataset/swisstlm3d-wanderwege/resource/e1b5fac2-fedf-42d4-a2e4-27287c02504b). Es un fichero `.gpkg` con todos los caminos de senderismo de Suiza. Cada camino es una línea de puntos (x, y, z). De este fichero se puede extraer la posición, la altitud y la dificultad. Este fichero solo contiene tramos.
2. **Paradas de transporte público (Traffic Points)**, en [opentransportdata.swiss](https://data.opentransportdata.swiss/en/dataset/traffic-point-v2). Es un fichero `.csv` con la posición de todas las paradas (autobús, tren, etc.).

Más detalles sobre los datos: [docs/datos.md](docs/datos.md)

## Análisis

Los caminos de estos ficheros son solo tramos sueltos, no recorridos completos. Hay más de 400 000 tramos que se cruzan entre ellos, así que calcular a mano todas las combinaciones posibles es imposible. Hay que analizar estas combinaciones, calcular la distancia y el desnivel de cada una, comprobar que hay una parada cerca del inicio y del final, y filtrar las que mejor encajan con lo que pido.

## ¿Por qué en la nube?

Muchos corredores y senderistas de toda Suiza tienen la misma necesidad y usan los mismos datos oficiales. Además, hay muchísimos datos (cientos de miles de tramos y de puntos en el mapa), así que tiene sentido tenerlos en un solo sitio, compartido por todos.

## Referencias

- swissTLM3D Wanderwege: https://opendata.swiss/fr/dataset/swisstlm3d-wanderwege/resource/e1b5fac2-fedf-42d4-a2e4-27287c02504b
- Traffic Points: https://data.opentransportdata.swiss/en/dataset/traffic-point-v2

## Tarjeta de rol

![Fotografía de la tarjeta de rol](img/tarjeta.jpg)

## Documentación adicional

- [configuración de GitHub](img/ssh_github.png)
- [configuración de SSH](img/ssh_test.png)