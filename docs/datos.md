## Datos

1. **Caminos de senderismo (swissTLM3D Wanderwege)**, en [opendata.swiss](https://opendata.swiss/fr/dataset/swisstlm3d-wanderwege/resource/e1b5fac2-fedf-42d4-a2e4-27287c02504b). Es un fichero `.gpkg` con todos los caminos de senderismo de Suiza. Cada camino es una línea de puntos (x, y, z). De este fichero se puede extraer la posición, la altitud, el tipo de camino y su dificultad.

   - Nombre del fichero: `SWISSTLM3D_WANDERWEGE.gpkg` ([descargar zip](https://data.geo.admin.ch/ch.swisstopo.swisstlm3d-wanderwege/swisstlm3d-wanderwege/swisstlm3d-wanderwege_2056_5728.gpkg.zip))
   - Número de filas: 409 276
   - Datos interesantes:
     - `geometry`: lista de puntos (x, y, z) en coordenadas LV95
     - `wanderwege`: categoría oficial de dificultad del camino
     - `uuid`: identificador único de cada tramo

   ![opendata.swiss](img/paths.png)

   Ejemplo:

   | uuid | wanderwege | objektart | belagsart | geometry |
   |:---|:---|:---|:---|:---|
   | {579B1CED-A0E7-4822-8176-15FCCC599584} | Wanderweg | 3m Strasse | Hart | LINESTRING Z (2733196.966 1124595.195008 327.766, 2733196.49… |
   | {99723204-7184-49E5-BCB1-33F4DF6B36DE} | Wanderweg | Markierte Spur | k_W | LINESTRING Z (2649034.050001 1205933.323827 876.312, 2649040… |
   | {67CFA3B2-1E89-4CF7-8CE0-2FE7E1894161} | Wanderweg | 4m Strasse | Hart | LINESTRING Z (2632948.242 1166916.728003 597.922, 2632942.35… |
   | {19AE62E9-A3F2-42AA-BB77-9864D424202C} | Wanderweg | 4m Strasse | Hart | LINESTRING Z (2689383.021 1246142.787996 643.166, 2689379.20… |

2. **Paradas de transporte público (Traffic Points)**, en [opentransportdata.swiss](https://data.opentransportdata.swiss/en/dataset/traffic-point-v2). Es un fichero `.csv` con la posición de todas las paradas (autobús, tren, etc.).

   - Nombre del fichero: `actual-date-world-traffic-point.csv` ([página de descarga](https://data.opentransportdata.swiss/dataset/b06d90be-91c6-440e-ab97-09f579d2fad0/resource/49566b25-e2df-4211-b628-9ada782a512a/download/actual-date-world-traffic-point.csv))
   - Número de filas: 62 275
   - Datos interesantes:
     - `designationOfficial`: nombre de la parada
     - `lv95East`, `lv95North`: coordenadas en LV95
     - `height`: altitud de la parada
     - `uicCountryCode`: código del país (85 = Suiza)

   ![opentransportdata.swiss](img/transports.png)

   Ejemplo:

   | designationOfficial | lv95East | lv95North | height | uicCountryCode |
   |:---|---:|---:|---:|---:|
   | Thierachern, mittlerer Schwand | 2611233.9 | 1178712.0 | 563.0 | 85 |
   | Zug, Kistenfabrik | 2681910.0 | 1226157.0 | 426.0 | 85 |
   | Wädenswil, Burstel | – | – | – | 85 |

   Algunas paradas no tienen coordenadas (como Wädenswil, Burstel) y hay que descartarlas.

Más información en este notebook de Jupyter: [análisis de los datos](analysis.ipynb)