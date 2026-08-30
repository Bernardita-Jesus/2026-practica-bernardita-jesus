# Semana-06

```text

berni@Dita MINGW64 /c/Users/berni/github
$ cd /c/Users/berni/github/

berni@Dita MINGW64 /c/Users/berni/github
$ ls
2026-practica-bernardita-jesus  Rack  popusintes-cajas-paneles

berni@Dita MINGW64 /c/Users/berni/github
$ cd Rack/

berni@Dita MINGW64 /c/Users/berni/github/Rack
$ cd plugins/

berni@Dita MINGW64 /c/Users/berni/github/Rack/plugins
$ cd
Fundamental/     popusintes-rack/

berni@Dita MINGW64 /c/Users/berni/github/Rack/plugins
$ cd popusintes-rack/

berni@Dita MINGW64 /c/Users/berni/github/Rack/plugins/popusintes-rack
$ git pull

berni@Dita MINGW64 /c/Users/berni/github/Rack/plugins/popusintes-rack
$ make dep
make: Nothing to be done for 'dep'.

berni@Dita MINGW64 /c/Users/berni/github/Rack/plugins/popusintes-rack
$ make

berni@Dita MINGW64 /c/Users/berni/github/Rack/plugins/popusintes-rack
$ male dist
-bash: male: command not found

berni@Dita MINGW64 /c/Users/berni/github/Rack/plugins/popusintes-rack
$ make dist
rm -rf dist
mkdir -p dist/piruetas-popusintes
cp plugin.dll dist/piruetas-popusintes/
strip -s dist/piruetas-popusintes/plugin.dll
cp -r --parents LICENSE res plugin.json dist/piruetas-popusintes/
cd dist && tar --no-xattrs -c piruetas-popusintes | zstd -19 -o "piruetas-popusintes"-"2.1.1"-win-x64.vcvplugin
/*stdin*\            : 32.51%   (   550 KiB =>    179 KiB, piruetas-popusintes-2.1.1-win-x64.vcvplugin)

berni@Dita MINGW64 /c/Users/berni/github/Rack/plugins/popusintes-rack
$ cd ..

berni@Dita MINGW64 /c/Users/berni/github/Rack/plugins
$ cd ..

berni@Dita MINGW64 /c/Users/berni/github/Rack
$ 
```

### Módulos VCV Rack

Recta y Embo tenían el tamaño de los LED diferentes, por lo que Aaron corrigió en el código esas medidas para tomarlas en relación con el módulo Combo, con LED de tamaño mediano.

Esto me dio la oportunidad de aprender a actualizar los cambios y hacer git pull.

### SemVer

Versionamiento semántico.

El último número de versión corresponde a correcciones de errores, el siguiente a mejoras y el primero a un cambio radical.

VCV Library, en donde se van subiendo los archivos de todas las personas a Issues.

## paneles

añadir fotos de los paneles*

### propuestas de mejora

## Salidas

### Clase de efectos visuales y formas

El día jueves 27 de agosto asistí a una **clase del Magíster en Artes Mediales** de la Universidad de Chile, impartida por el profesor **Christian Oyarzún**. La clase estuvo enfocada en la creación de gráficas algorítmicas, efectos visuales y formas mediante programación en p5.js.

#### Gráficas algorítmicas

Durante la clase trabajamos con **Sofwave**, una herramienta para crear visuales e imágenes basadas en algoritmos y geometría analítica.

Esta forma de trabajar se relaciona con el diseño paramétrico que estoy desarrollando en OpenSCAD, ya que en ambos casos se utilizan reglas, variables y fórmulas matemáticas para construir formas. Al modificar una variable o un dato numérico, las formas pueden cambiar automáticamente de acuerdo con las relaciones establecidas.

También trabajamos con la condición **IF** y con valores **booleanos**, que permiten establecer dos estados y tomar decisiones dentro del código.

#### Operadores lógicos

Los operadores lógicos permiten establecer instrucciones y relaciones dentro del código. En JavaScript, los principales son:

* **AND:** &&
* **OR:** ||
* **NOT:** !

También vimos otros conceptos relacionados, como **NAND** y **NOR**, que corresponden a operaciones derivadas de AND y OR.

Dentro de las funciones utilizadas en el código se encuentran:

- **translate:** permite trasladar un elemento y establecer su ubicación.
- **rotate:** permite rotar elementos.
- **push / pop:** permiten guardar y recuperar transformaciones dentro del código.
- **millis:** permite trabajar con el tiempo y generar cambios en función de este.
- **constrain:** permite establecer restricciones a los valores.

También se abordaron conceptos relacionados con la visualización digital, como **aliasing, antialiasing y moiré**.

#### map

La función **map** permite escalar valores y establecer una relación entre distintos rangos. Esto permite correlacionar un valor con otro y utilizarlo como referencia para modificar diferentes elementos dentro de una composición.

También vimos la lógica de construcción de una grilla a partir de dos funciones sinusoidales, donde las relaciones matemáticas permiten generar y modificar las formas de manera sistemática.

#### Referentes de gráficas algorítmicas

Algunos de los referentes revisados durante la clase fueron:

- Mark Wilson
- Vera Molnár
- Jean-Pierre Hébert
- Roman Verostko
- Victor Vasarely

Esta clase me ayudó a comprender de una manera más amplia el potencial de las matemáticas dentro del diseño. Al trabajar actualmente en el modelado de piezas 3D en OpenSCAD, he estado utilizando medidas, variables y relaciones entre elementos para construir objetos de manera paramétrica.

La clase me permitió reconocer que esta misma lógica puede aplicarse a otros medios, como las gráficas y los efectos visuales. Las matemáticas pueden convertirse en funciones, referencias y reglas capaces de generar formas y comportamientos de manera organizada.

Esto me ayudó a entender que el diseño paramétrico no se limita al modelado 3D, sino que puede ser una forma de pensar y construir: establecer reglas, relaciones y variables que permitan explorar diferentes resultados a partir de un mismo sistema.




