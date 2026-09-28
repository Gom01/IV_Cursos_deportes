# Rutas de senderismo a medida en Suiza

## Problema

Corro en Suiza y me gusta entrenar de forma progresiva, muchas veces en sitios que no conozco. Casi siempre sé exactamente la distancia que quiero hacer, el desnivel y más o menos dónde quiero ir. Por ejemplo, sé que quiero correr 17 km con 800 m de desnivel.

Ahora mismo, para preparar un recorrido tengo que:

1. Mirar ideas de recorridos en [AllTrails](https://www.alltrails.com/) para ver lo que ya existe y lo que es interesante (sitios con vistas, etc.). Pero no puedo descargar los datos GPX sin pagar.
2. Ir a [map.geo.admin.ch](https://map.geo.admin.ch/) de swisstopo y dibujar mi recorrido a mano. Tengo que mirar dónde están las paradas de transporte público y corregir el trazado. Después puedo descargar el GPX, pero tengo que calcular y adaptar yo mismo la distancia y el desnivel.
3. Enviar el resultado a mi reloj para tener el trazado y poder ir a correr.

Esto me hace perder mucho tiempo (unas 2 horas por semana): primero tengo que encontrar un recorrido que me guste, después crearlo a mano y cambiarlo hasta que tenga la distancia y la dificultad que quiero. Como corro 2 o 3 veces por semana, pierdo mucho tiempo haciendo estos cálculos, y creo que no soy el único. Además, prefiero usar los datos de swisstopo porque son suizos, oficiales y fiables.

## Datos

En Suiza, la Confederación publica datos oficiales, gratuitos y que se pueden descargar. Hay dos fuentes útiles para este problema:

1. **Caminos de senderismo (swissTLM3D Wanderwege)**, en [opendata.swiss](https://opendata.swiss/fr/dataset/swisstlm3d-wanderwege/resource/e1b5fac2-fedf-42d4-a2e4-27287c02504b). Es un fichero `.gpkg` con todos los caminos de senderismo de Suiza. Cada camino es una línea de puntos (x, y, z). De este fichero se puede extraer la posición, la altitud, el tipo de camino y su dificultad.
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