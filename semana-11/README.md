# Semana-11

## Resumen de días, temas y horas

| Fecha      | Día      | Temas                                                | Lugar     | Horas día / hora semana |
| :--------- | :------- | :--------------------------------------------------- | :-------- | :---------------------- |
| 2026-10-05 | Lunes    |                                                      |           | 000 / 000               |
| 2026-10-06 | Martes   |                                                      |           | 000 / 000               |
| 2026-10-08 | Jueves   |                                                      |           | 000 / 000               |
| 2026-10-09 | Viernes  |                                                      |           | 000 / 000               |
| 2026-10-10 | Sábado   |                                                      |           | 000 / 000               |
| 2026-10-11 | Domingo  |                                                      |           | 000 / 000               |

## Tacto 42

**Tacto 42** es un amplificador para micrófono piezoeléctrico (de contacto), que va dentro de una caja Hammond. La semana pasada diseñé la caja en **OpenSCAD** y la imprimí en 3D en la Bambu Lab; para probar las perforaciones que encajen los elementos, la caja solo tiene:

- Entrada XLR.

- Salida para jack TS de 1/4" o de 1/8".

Como referencia, sigo el estándar de pedales como el **Boss CH-2**, con la **entrada a la derecha y la salida a la izquierda**. Un ejemplo de amplificador piezoeléctrico es el **Drum Thing de Electro-Faustus**.

Esta semana mi objetivo es pasar de la caja impresa en 3D a la caja de aluminio Hammond.

Antes de comenzar a diagramar dónde debería ir cada elemento, que en el fondo son tres, como mencioné: la entrada jack, la salida XLR y la PCB, desarmé un pedal para poder ver otro tipo de soluciones de diseño que han tomado algunas marcas en sus productos al utilizar cajas Hammond.

Desarme pedal

Agregar foto del desarme*

https://www.3m.com/3M/en_US/dual-lock-reclosable-fasteners-us/

### Caja Hammond

Esta es la caja Hammond que vamos a utilizar para el producto.

https://www.katode.cl/cajas-de-aluminio/159-caja-aluminio-1590a-ultra-pequena.html

### Limitaciones del corte láser en aluminio

- **Láser CO2:** Es el láser más común y no corta aluminio. El aluminio refleja casi toda la luz de este tipo de láser. No alcanza a fundir el metal. Además, ese reflejo puede dañar los espejos y el lente de la máquina.

- **Grosor:** El grosor máximo depende de la potencia del láser de fibra; a mayor grosor, más potencia y peor terminación del borde. Tengo que preguntarle al proveedor qué grosores corta.

- **Marcado vs. corte:** Algunos láseres, como los que hay en la universidad, solo sirven para grabar o marcar la superficie, no para atravesar el metal.

- **Forma de la pieza:** El corte láser trabaja sobre planchas planas. La caja Hammond ya viene armada en 3D, así que no se podría cortar en una cortadora láser plana; las perforaciones para los jacks o la salida XLR se deberían hacer con taladro y brocas escalonadas, usando una guía de corte, o plantilla, pegada sobre la caja.

### Plantillas y guías de corte

- **Plantilla de papel impresa:** Imprimo el plano con los agujeros a escala 1:1, lo pegaría con cinta a la caja y marcaría cada centro con un punzón antes de taladrar. Las plantillas se perderían.

- **Plantilla de acrílico o MDF cortada en láser:** Corto una placa con los agujeros en la cortadora láser, la apoyo sobre las caras de la caja y marco o perforo a través de ella. Se podría reutilizar.

- **Jig impreso en 3D:** Es una pieza que encaja sobre la caja como una tapa, con los agujeros ya ubicados. No se mueve al taladrar.


