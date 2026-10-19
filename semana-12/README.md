# Semana-12

## Resumen de días, temas y horas

| Fecha      | Día      | Temas                                                | Lugar     | Horas día / hora semana |
| :--------- | :------- | :--------------------------------------------------- | :-------- | :---------------------- |
| 2026-10-12 | Lunes    |                                                      |           | 005 / 005               |
| 2026-10-13 | Martes   |                                                      |           | 000 / 000               |
| 2026-10-15 | Jueves   | Registro fotográfico                                 | LID       | 003 / 008               |
| 2026-10-16 | Viernes  |                                                      |           | 000 / 000               |
| 2026-10-17 | Sábado   |                                                      |           | 000 / 000               |
| 2026-10-18 | Domingo  | OpenSCAD, Plantillas de perforación                  | Casa      | 005 / 013               |

## Fuente de poder Eurorack

Esta semana llegaron las PCB diseñadas por [Aarón](https://github.com/montoyamoraga) junto a [Mati](https://github.com/misaaaaaa). Corresponden a una fuente de poder para sintetizadores en formato Eurorack, pensada para utilizarse en los **Popusintes**.

La idea es incorporarla a las cajas y paneles que estamos desarrollando y, además, ofrecerla como un **producto independiente**. Una vez recibidas las PCB, probamos la fuente de poder conectándola a distintos módulos de sintetizadores para comprobar su funcionamiento.

Como parte de esta práctica e investigación, tomé registros fotográficos del proceso para documentar y compartir el desarrollo de los Popusintes. Esto busca contribuir a la popularización de la síntesis electrónica, visibilizando el trabajo que hay detrás de su fabricación y generando conversación y difusión en torno a este tema.

## Tacto 48

Esta semana seguí trabajando en el repositorio de **[Tacto 48](https://github.com/Bernardita-Jesus/tacto48)**, en la carpeta **[modelado-caja](https://github.com/Bernardita-Jesus/tacto48/tree/main/modelado-caja)**. Pasé de la caja impresa en 3D a la **caja de aluminio 1590A** de Katode, y creé la versión **v0.0.2** del diseño.

### Control de versiones

Antes de empezar, moví todo el diseño anterior, la caja impresa de 50 × 40 × 80 mm, a una carpeta llamada **v0.0.1**, con su código y sus STL. Así puedo volver a esa versión si lo necesito, y la carpeta principal queda solo con el diseño nuevo.

### Caja 1590A de referencia

Modelé la caja de aluminio en **OpenSCAD** con las medidas del plano de Hammond: 92,6 × 38,5 × 31 mm, paredes de 1,75 mm y piso de 1,6 mm. Esta caja no se imprime; me sirve como referencia para ubicar las perforaciones y diseñar las plantillas.

La caja tiene **ángulo de desmoldeo**: se achica 0,65 mm por lado desde el borde hasta el fondo. Lo incluí en el modelo para que las plantillas calcen bien.

Las perforaciones de la caja son:

- **Extremo del jack:** Jack TS de 3,5 mm, con un agujero de 6,2 mm.

- **Extremo del XLR:** XLR hembra Rean RC3FDL, con un agujero de 24,2 mm y dos tornillos M3 en diagonal. Giré la base del conector para que cupiera en la altura de la caja.

- **Fondo:** Dos agujeros para tornillos M3, donde se atornilla la PCB rev-b.

### Plantillas para perforar

Diseñé dos **plantillas imprimibles**, una para cada extremo de la caja. Son tapas que entran por el extremo y abrazan los cuatro lados con una falda de 15 mm, así no se mueven al perforar. Esto corresponde a la opción del jig impreso en 3D que planteé la semana pasada.

- **Marcas:** En cada perforación, la plantilla tiene un agujero de 1,5 mm para marcar el centro con punzón o con la broca guía.

- **Anillos grabados:** Alrededor de cada marca hay un anillo grabado que muestra el diámetro final de la perforación.

- **Versión grabada:** Cada plantilla lleva grabada la versión **v0.0.2**.

Los dos agujeros de la PCB en el fondo no van en la plantilla. Por el ángulo de desmoldeo, los bordes cambian según la altura, así que los marco a mano midiendo 12,5 mm desde el centro del fondo.

### Brocas

En el README de la carpeta anoté las brocas HSS para aluminio que voy a usar en el taladro de pedestal:

- **2 mm:** Para las perforaciones guía.

- **3,5 mm:** Para los tornillos M3.

- **6 mm o 6,5 mm:** Para el jack.

- **Broca escalonada hasta 24 mm:** Para el XLR.
