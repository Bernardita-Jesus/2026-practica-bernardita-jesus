# Semana-06

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

### Módulos VCV Rack

Recta y Embo tenían el tamaño de los LED diferentes, por lo que Aaron corrigió en el código esas medidas para tomarlas en relación con el módulo Combo, con LED de tamaño mediano.

Esto me dio la oportunidad de aprender a actualizar los cambios y hacer git pull.

### SemVer

Versionamiento semántico.

El último número de versión corresponde a correcciones de errores, el siguiente a mejoras y el primero a un cambio radical.

VCV Library, en donde se van subiendo los archivos de todas las personas a Issues.

