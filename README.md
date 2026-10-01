# Rutas de senderismo a medida en Suiza

## Problema

Corro en Suiza y me gusta entrenar de forma progresiva, muchas veces en sitios que no conozco. Siempre sé exactamente la distancia que quiero hacer, el desnivel y el punto de salida y de llegada (en transporte público). Por ejemplo, sé que quiero correr 17 km con 800 m de desnivel, que salgo de una estación concreta y que llego a otra estación (que puede ser la misma). Mi problema es que pierdo mucho tiempo creando un recorrido que encaje con lo que quiero.

Ahora mismo, para preparar un recorrido tengo que:

1. Ir a [map.geo.admin.ch](https://map.geo.admin.ch/) de swisstopo y dibujar un recorrido a mano, tramo por tramo, empezando en una estación de tren o una parada de autobús y terminando en otra parada.
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

### 1. Caminos de senderismo (swissTLM3D Wanderwege)

Fuente: [opendata.swiss](https://opendata.swiss/fr/dataset/swisstlm3d-wanderwege/resource/e1b5fac2-fedf-42d4-a2e4-27287c02504b) ([descargar zip](https://data.geo.admin.ch/ch.swisstopo.swisstlm3d-wanderwege/swisstlm3d-wanderwege/swisstlm3d-wanderwege_2056_5728.gpkg.zip))

- Formato: es una base de datos (tipo SQLite) guardada en un solo fichero. Dentro hay una tabla, y cada fila de la tabla es un tramo de camino.
- La posición de cada tramo (la columna `geometry`) no está escrita como texto, sino en binario. Es una pequeña cabecera de GeoPackage seguida de un formato llamado WKB. Para leerla, abriré la base con el módulo `sqlite3`, que viene incluido en Python, y escribiré yo mismo el código que quita la cabecera y convierte el binario en una lista de puntos (x, y, z).
- Número de filas: 409 276, es decir, 409 276 tramos.
- Licencia: uso libre, pero es obligatorio citar la fuente (autor, título y enlace a los datos).

Columnas que uso:

- `uuid`: identificador único de cada tramo. Me sirve para saber qué tramos forman un recorrido.
- `wanderwege`: categoría oficial de dificultad del tramo (Wanderweg, Bergwanderweg o Alpinwanderweg). Me sirve para no proponer caminos más difíciles de lo que pide el usuario.
- `geometry`: lista de puntos (x, y, z) del tramo. x e y son coordenadas LV95 (el sistema oficial de Suiza, en metros) y z es la altitud. Me sirve para calcular la distancia y el desnivel, y para saber qué tramos se tocan.

Ejemplo (la columna `geometry` ya decodificada):

| uuid | wanderwege | geometry |
|:---|:---|:---|
| {579B1CED-A0E7-4822-8176-15FCCC599584} | Wanderweg | LINESTRING Z (2733196.966 1124595.195008 327.766, 2733196.49… |
| {99723204-7184-49E5-BCB1-33F4DF6B36DE} | Wanderweg | LINESTRING Z (2649034.050001 1205933.323827 876.312, 2649040… |
| {67CFA3B2-1E89-4CF7-8CE0-2FE7E1894161} | Wanderweg | LINESTRING Z (2632948.242 1166916.728003 597.922, 2632942.35… |
| {19AE62E9-A3F2-42AA-BB77-9864D424202C} | Wanderweg | LINESTRING Z (2689383.021 1246142.787996 643.166, 2689379.20… |

### 2. Paradas de transporte público (Traffic Points)

Fuente: [opentransportdata.swiss](https://data.opentransportdata.swiss/en/dataset/traffic-point-v2) ([descargar csv](https://data.opentransportdata.swiss/dataset/b06d90be-91c6-440e-ab97-09f579d2fad0/resource/49566b25-e2df-4211-b628-9ada782a512a/download/actual-date-world-traffic-point.csv))

- Formato: CSV separado por `;`. Puedo leerlo con el módulo `csv`, que viene incluido en Python.
- Número de filas: 62 275 (cada fila es un andén; una misma parada puede tener varias filas).
- Licencia: uso libre, pero es obligatorio citar la fuente.

Columnas que uso:

- `designationOfficial`: nombre de la parada. Esto me permite encontrar la parada que el usuario indica como punto de partida y de llegada.
- `lv95East`, `lv95North`: coordenadas LV95 de la parada, en el mismo sistema que los caminos. Me sirven para calcular la distancia entre la parada y el inicio o el final del recorrido.
- `uicCountryCode`: código del país (85 = Suiza). Me sirve para quitar las paradas que no están en Suiza.

Ejemplo:

| designationOfficial | lv95East | lv95North | uicCountryCode |
|:---|---:|---:|---:|
| Thierachern, mittlerer Schwand | 2611233.9 | 1178712.0 | 85 |
| Zug, Kistenfabrik | 2681910.0 | 1226157.0 | 85 |
| Wädenswil, Burstel | – | – | 85 |

Hay que limpiar algunos datos porque faltan valores. Por ejemplo, algunas paradas no tienen posición (como Wädenswil, Burstel) y hay que descartarlas.

## Análisis

Los caminos de estos ficheros son solo tramos sueltos, no recorridos completos. Pero se tocan en los cruces, y así forman una red. Hay más de 400 000 tramos, así que es imposible probar todas las combinaciones posibles, ni a mano ni con un ordenador. Hace falta un método que empiece en la estación de salida y termine en la estación de llegada, construyendo el recorrido tramo por tramo y siguiendo la red. En cada paso, calcula la distancia, el desnivel y la dificultad que ya lleva, y descarta enseguida los recorridos que ya no encajan con mis criterios (demasiado largos, con demasiado desnivel o demasiado difíciles). Al final, se queda con los recorridos que llegan a la estación de llegada con la distancia y el desnivel pedidos, y elige los mejores.

## ¿Por qué en la nube?

Muchos corredores y senderistas de toda Suiza tienen la misma necesidad y usan los mismos datos oficiales. Además, hay muchísimos datos (cientos de miles de tramos y de puntos en el mapa), así que tiene sentido tenerlos en un solo sitio, compartido por todos. Así, los usuarios pueden usarlo desde su móvil, aunque tengan poco espacio en él.

## Planificación
- [User journey](docs/user-journey.md)
- [Personas](docs/personas.md)
- [Hitos](docs/planificacion.md) ([ver en GitHub](https://github.com/Gom01/IV_Cursos_deportes/milestones))
- Historias de usuario:
  - [HU1: Trabajar con los datos oficiales](https://github.com/Gom01/IV_Cursos_deportes/issues/2)
  - [HU2: Distancia y desnivel de un recorrido](https://github.com/Gom01/IV_Cursos_deportes/issues/3)
  - [HU3: Recorridos entre dos estaciones](https://github.com/Gom01/IV_Cursos_deportes/issues/4)
  - [HU4: No acabar en un camino demasiado difícil](https://github.com/Gom01/IV_Cursos_deportes/issues/5)
  - [Historia de usarios](docs/historias-de-usuario.md)
## Tarjeta de rol

- [Fotografía de la tarjeta de rol](img/tarjeta.jpg)

## Documentación adicional

- [configuración de GitHub](img/ssh_github.png)
- [configuración de SSH](img/ssh_test.png)