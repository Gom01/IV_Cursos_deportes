# Datos

## 1. Caminos de senderismo (swissTLM3D Wanderwege)

Fuente: [opendata.swiss](https://opendata.swiss/fr/dataset/swisstlm3d-wanderwege/resource/e1b5fac2-fedf-42d4-a2e4-27287c02504b) ([descargar zip](https://data.geo.admin.ch/ch.swisstopo.swisstlm3d-wanderwege/swisstlm3d-wanderwege/swisstlm3d-wanderwege_2056_5728.gpkg.zip))

- Nombre del fichero: `SWISSTLM3D_WANDERWEGE.gpkg`
- Formato: base de datos SQLite (GeoPackage). La columna `geometry` está guardada en binario (formato WKB), no en texto.
- Número de filas: 409 276 (cada fila es un tramo)

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

## 2. Paradas de transporte público (Traffic Points)

Fuente: [opentransportdata.swiss](https://data.opentransportdata.swiss/en/dataset/traffic-point-v2)

- Nombre del fichero: `actual-date-world-traffic-point.csv`
- Formato: CSV separado por `;`.
- Número de filas: 62 275 (cada fila es un andén; una misma parada puede tener varias filas)

Columnas que uso:

- `designationOfficial`: nombre de la parada. Me sirve para decir al usuario dónde empieza y dónde termina el recorrido.
- `lv95East`, `lv95North`: coordenadas LV95 de la parada, en el mismo sistema que los caminos. Me sirven para calcular la distancia entre la parada y el inicio o el final del recorrido.
- `uicCountryCode`: código del país (85 = Suiza). Me sirve para quitar las paradas que no están en Suiza.

Ejemplo:

| designationOfficial | lv95East | lv95North | uicCountryCode |
|:---|---:|---:|---:|
| Thierachern, mittlerer Schwand | 2611233.9 | 1178712.0 | 85 |
| Zug, Kistenfabrik | 2681910.0 | 1226157.0 | 85 |
| Wädenswil, Burstel | – | – | 85 |

Hay que limpiar algunos datos porque faltan valores. Por ejemplo, algunas paradas no tienen posición (como Wädenswil, Burstel) y hay que descartarlas.