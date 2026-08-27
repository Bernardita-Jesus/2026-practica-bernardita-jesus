# Semana-06

´´´test

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
´´´

### Módulos VCV Rack

Recta y Embo tenían el tamaño de los LED diferentes, por lo que Aaron corrigió en el código esas medidas para tomarlas en relación con el módulo Combo, con LED de tamaño mediano.

Esto me dio la oportunidad de aprender a actualizar los cambios y hacer git pull.

### SemVer

Versionamiento semántico.

El último número de versión corresponde a correcciones de errores, el siguiente a mejoras y el primero a un cambio radical.

VCV Library, en donde se van subiendo los archivos de todas las personas a Issues.

## paneles

## salidas

### Clase ...

El día jueves 27 de agosto, fui a una clase del magister artes mediales universidad de chile, impartida por el profesor **Christian Oyarzún**

#### Gráficas algorítmicas

Sofwave, para hacer visuales e imágenes basadas en algoritmos y geometría analítica.

Es como el diseño paramétrico, reglas y fórmulas matemáticas donde las formas cambian de manera automática al modificar variables o datos numéricos.

´´´text
function setup() {
  createCanvas(420, 420);colorMode(HSB);
}
function draw() {
  background("#ffaa00");
  for(let i=0;i<500;i++){
    let x = random(width);
    let y = random(height);
    let s = random(2,20);
    
    
    push();
    translate(x,y);ellipse(0,0,s,s);
    pop();
  }
  noLoop();
}

´´´

#### Condicion IF

boolean, dos operadores, dos estados

#### Referentes de Gráficas algorítmicas

Mark Wilson

Vera Molnár

Jean-Pierre Hébert

Roman Verostko

#### Operadores lógicos

Con estos operadores podemos dar instrucciones. Estos tres operadores tienen sus propios símbolos en JavaScript:

- **AND: &&**
- **OR: ||**
- **NOT: !**

Tenemos funciones de base en el código. Aquí podemos usar **translate**, trasladar y darle una ubicación. También podemos ubicar radios, ángulos, **s**, **h** y darles valores random.

Podemos rotar, trasladar, hacer **push** y **pop**. También se le puede agregar **millis**.

**Constrain:** restricciones.

**NAND:** lo contrario de AND.

**NOR:** lo contrario de OR. Si ambas no están, no existe en este lenguaje.







