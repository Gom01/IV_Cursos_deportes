# Custom hiking routes in Switzerland

## Problem

I run in Switzerland and I like to train progressively, often in places I don't know. I always know exactly the distance I want to do, the elevation gain, and the start and end points (by public transport). For example, I know I want to run 17 km with 800 m of elevation gain, starting from a specific station and arriving at another station (which can be the same one). My problem is that I lose a lot of time creating a route that fits what I want.

Right now, to prepare a route I have to:

1. Go to swisstopo's [map.geo.admin.ch](https://map.geo.admin.ch/) and draw a route by hand, section by section, starting at a train station or a bus stop and ending at another stop.
2. Check the distance and elevation gain of the route. If they are not what I want, I add or remove sections and check again. I often have to repeat this several times.

This process makes me lose a lot of time (about 2 or 3 hours per week): I have to draw the route by hand and then change it until it has the distance and difficulty I want. Since I run 2 or 3 times a week, I lose a lot of time doing these calculations, and I don't think I'm the only one. Also, I prefer to use swisstopo data because it is Swiss, official and reliable.

## Concepts

- **Trail:** running on mountain or country paths, not on roads. There are usually ups and downs.
- **Distance:** the number of kilometres of the route.
- **Positive elevation gain:** the sum of all the metres climbed during the route. Descents are not counted. For example, if I climb 300 m, go down 100 m and climb another 200 m, the positive elevation gain is 500 m.
- **Difficulty:** in Switzerland, each path has an official category, marked with colours on the signs:
  - *Wanderweg* (yellow): easy path, for everyone.
  - *Bergwanderweg* (white-red-white): mountain path, steeper and narrower. You need good balance.
  - *Alpinwanderweg* (white-blue-white): alpine path, very difficult. Sometimes you have to use your hands.
- **Section:** a piece of path between two junctions. The official data gives the paths as sections, not as complete routes.
- **Route:** several sections in a row, from the start to the finish.

## Data

### 1. Hiking paths (swissTLM3D Wanderwege)

Source: [opendata.swiss](https://opendata.swiss/fr/dataset/swisstlm3d-wanderwege/resource/e1b5fac2-fedf-42d4-a2e4-27287c02504b) ([download zip](https://data.geo.admin.ch/ch.swisstopo.swisstlm3d-wanderwege/swisstlm3d-wanderwege/swisstlm3d-wanderwege_2056_5728.gpkg.zip))

- Format: it is a database (SQLite type) stored in a single file. Inside there is a table, and each row of the table is a path section.
- The position of each section (the `geometry` column) is not written as text, but in binary. It is a small GeoPackage header followed by a format called WKB. To read it, I will open the database with the `sqlite3` module, which comes with Python, and I will write the code myself that removes the header and converts the binary into a list of points (x, y, z).
- Number of rows: 409 276, that is, 409 276 sections.
- License: free to use, but citing the source (author, title and link to the data) is mandatory.

Columns I use:

- `uuid`: unique identifier of each section. It helps me know which sections make up a route.
- `wanderwege`: official difficulty category of the section (Wanderweg, Bergwanderweg or Alpinwanderweg). It helps me avoid proposing paths that are more difficult than what the user asks for.
- `geometry`: list of points (x, y, z) of the section. x and y are LV95 coordinates (the official Swiss system, in metres) and z is the altitude. It helps me calculate the distance and the elevation gain, and know which sections touch each other.

Example (the `geometry` column already decoded):

| uuid | wanderwege | geometry |
|:---|:---|:---|
| {579B1CED-A0E7-4822-8176-15FCCC599584} | Wanderweg | LINESTRING Z (2733196.966 1124595.195008 327.766, 2733196.49… |
| {99723204-7184-49E5-BCB1-33F4DF6B36DE} | Wanderweg | LINESTRING Z (2649034.050001 1205933.323827 876.312, 2649040… |
| {67CFA3B2-1E89-4CF7-8CE0-2FE7E1894161} | Wanderweg | LINESTRING Z (2632948.242 1166916.728003 597.922, 2632942.35… |
| {19AE62E9-A3F2-42AA-BB77-9864D424202C} | Wanderweg | LINESTRING Z (2689383.021 1246142.787996 643.166, 2689379.20… |

### 2. Public transport stops (Traffic Points)

Source: [opentransportdata.swiss](https://data.opentransportdata.swiss/en/dataset/traffic-point-v2) ([download csv](https://data.opentransportdata.swiss/dataset/b06d90be-91c6-440e-ab97-09f579d2fad0/resource/49566b25-e2df-4211-b628-9ada782a512a/download/actual-date-world-traffic-point.csv))

- Format: CSV separated by `;`. I can read it with the `csv` module, which comes with Python.
- Number of rows: 62 275 (each row is a platform; the same stop can have several rows).
- License: free to use, but citing the source is mandatory.

Columns I use:

- `designationOfficial`: name of the stop. It lets me find the stop that the user gives as the start and end point.
- `lv95East`, `lv95North`: LV95 coordinates of the stop, in the same system as the paths. They help me calculate the distance between the stop and the start or end of the route.
- `uicCountryCode`: country code (85 = Switzerland). It helps me remove the stops that are not in Switzerland.

Example:

| designationOfficial | lv95East | lv95North | uicCountryCode |
|:---|---:|---:|---:|
| Thierachern, mittlerer Schwand | 2611233.9 | 1178712.0 | 85 |
| Zug, Kistenfabrik | 2681910.0 | 1226157.0 | 85 |
| Wädenswil, Burstel | – | – | 85 |

Some data has to be cleaned because values are missing. For example, some stops have no position (like Wädenswil, Burstel) and must be discarded.

## Analysis

The paths in these files are only separate sections, not complete routes. But they touch each other at junctions, and that way they form a network. There are more than 400 000 sections, so it is impossible to try every possible combination, by hand or with a computer. We need a method that starts at the departure station and ends at the arrival station, building the route section by section and following the network. At each step, it calculates the distance, elevation gain and difficulty so far, and immediately discards the routes that no longer match my criteria (too long, too much elevation gain or too difficult). At the end, it keeps the routes that reach the arrival station with the requested distance and elevation gain, and chooses the best ones.

## Why in the cloud?

Many runners and hikers all over Switzerland have the same need and use the same official data. Also, there is a huge amount of data (hundreds of thousands of sections and points on the map), so it makes sense to keep it in a single place, shared by everyone.

## Planning
- [User journey](docs/user-journey.md)
- [Personas](docs/personas.md)
- [Milestones](docs/planificacion.md)
- [User stories](docs/historias-de-usuario.md)

## Role card

- [Photo of the role card](img/tarjeta.jpg)

## Additional documentation

- [GitHub Configuración](img/ssh_github.png)
- [SSH Configuración](img/ssh_test.png)


### Requirements

They only need to be installed once, outside the project:

- Python 3.14.
- uv (dependency manager) and just (task tool):

  ```bash
  git clone https://github.com/Gom01/IV_Cursos_deportes.git
  cd IV_Cursos_deportes
  pip install uv rust-just
  ```

### Tasks

```bash
just install
just test
just check
```

- `just install`: creates the virtual environment and installs the development dependencies, with the versions pinned in `uv.lock`.
- `just test`: runs the tests with pytest. There are no tests at the moment.
- `just check`: only checks the syntax of the code, including the model entities. It compiles the files without running them, so it detects syntax errors without launching the program.

- [docs/automatizacion.md](docs/automatizacion.md)