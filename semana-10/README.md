# Semana-10

## Resumen de días, temas y horas

| Fecha      | Día      | Temas                                                | Lugar     | Horas día / hora semana |
| :--------- | :------- | :--------------------------------------------------- | :-------- | :---------------------- |
| 2026-09-28 | Lunes    | GitHub, OpenSCAD, Impresión 3D                       | LID       | 009 / 009               |
| 2026-09-29 | Martes   | OpenSCAD, Impresión 3D                               | República 180 | 005 / 014               |
| 2026-10-01 | Jueves   |                                                      |           | 000 / 000               |
| 2026-10-02 | Viernes  |                                                      |           | 000 / 000               |
| 2026-10-03 | Sábado   |                                                      |           | 000 / 000               |
| 2026-10-04 | Domingo  | Documentación                                        | Casa      | 003 / 017               |


## Componentes

Fuimos a buscar a Pedro de Valdivia los componentes que llegaron de **[Thonk](https://www.thonk.co.uk/)** desde Inglaterra. Pedimos **fuentes de poder, perillas, potenciómetros, tornillos, golillas** y todos los componentes necesarios para poder seguir desarrollando los **Popusintes**.

## VCV Rack

Hacer copia de Popusíntesis.

## Tacto 42

### Caja para amplificador piezoeléctrico

**Tacto 42** es un amplificador para micrófono piezoeléctrico (de contacto). Esta semana diseñé su caja en **OpenSCAD**, basándome en el formato de la caja Hammond 1590A, para imprimirla en 3D y probar que los conectores calcen en las perforaciones. Por el momento, la caja solo tiene:

- Entrada XLR.

- Salida para jack TS de 1/4" o de 1/8".

Como base tomé este modelo de caja 1590A imprimible en 3D:

https://cults3d.com/es/modelo-3d/artilugios/1590a-pedal-case-enclosure-3d-printable

#### Diseño e impresión

En la siguiente captura se puede ver el código principal de **Tacto 42** en **OpenSCAD** y el ensamble de la caja con sus tapas.

![captura](./imagenes/captura-21.png)

En la siguiente captura se puede ver la impresión de las tapas de la caja desde la cámara de la Bambu Lab, en Bambu Studio.

![captura](./imagenes/captura-20.png)

En la siguiente foto se pueden ver las tapas ya impresas en 3D, versión **v0.0.1**, por fuera y por dentro: una con el conector XLR y otra con el jack de 1/8".

![foto](../semana-11/imagenes/foto-34.jpg)

#### Referencias

- **Boss CH-2:** Es un pedal que cumple con el estándar de tener la **entrada a la derecha y la salida a la izquierda**, y lo tomo como referencia para ubicar los conectores.

- **Drum Thing de Electro-Faustus:** Es un ejemplo de amplificador piezoeléctrico.

- **Por investigar:** Micrófono condensador y preamplificador para piezo.

#### Componentes y proveedores

- https://audiosystemsmusic.cl/products/rea0024

- Jack mono GLS: https://www.cabezacuadrada.cl/product/jack-mono-gls/

- Jack mono cerrado: https://www.cabezacuadrada.cl/product/jack-mono-cerrado/

- Búsqueda de componentes en Katode: https://www.katode.cl/busqueda
