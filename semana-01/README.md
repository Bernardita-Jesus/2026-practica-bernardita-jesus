# semana-01

## Semana de adaptación

### Copia del repositorio

Reunión Lunes 20 de julio, invierno 2026

Hice una copia del repositorio de la práctica en mi computador desde la terminal. Estoy utilizando **Windows PowerShell** y **Visual Studio Code** para subir varios archivos a la nube de **GitHub**.

Voy a hacer una distinción; hay dos versiones de este repositorio. Una es el **repositorio remoto**, que está alojado en GitHub, y la otra es la **copia local** que se encuentra en mi computador.

Por el momento, lo que tengo que hacer es abrir la terminal y encontrar mi repositorio.

Con **cd** busco este espacio y puedo simplemente escribir github, luego 2026 y presionar la tecla **Tab** para que autocomplete la búsqueda, ya que realmente no tengo ningún otro repositorio copiado. Por eso, me redirige automáticamente a la única opción disponible.

```bash

PS C:\Users\berni> cd .\github\2026-practica-bernardita-jesus\
PS C:\Users\berni\github\2026-practica-bernardita-jesus>
```

Luego consulto el estado de mi repositorio con el comando **git status** para conocer los cambios que se han realizado.

```bash
PS C:\Users\berni\github\2026-practica-bernardita-jesus> git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   semana-01/README.md

no changes added to commit (use "git add" and/or "git commit -a")
PS C:\Users\berni\github\2026-practica-bernardita-jesus>
```

En este caso, modifiqué el archivo README de la carpeta semana-01, que, por cierto, corresponde a estos mismos apuntes.

Con el comando **git add .** se preparan todos los cambios realizados para el próximo commit. También es posible agregar únicamente un archivo o una carpeta específica, indicando su ruta en lugar del punto (.).

```bash
PS C:\Users\berni\github\2026-practica-bernardita-jesus> git add .
PS C:\Users\berni\github\2026-practica-bernardita-jesus>
```

Con el comando **git commit -m** se crea un commit con un mensaje que nombra los cambios realizados. Es necesario haber agregado previamente los archivos con git add, ya que solo los cambios preparados serán incluidos en el commit.

```bash
PS C:\Users\berni\github\2026-practica-bernardita-jesus> git commit -m "ejemplo de cambio"
[main 8c1098b] ejemplo de cambio
 1 file changed, 36 insertions(+), 2 deletions(-)
PS C:\Users\berni\github\2026-practica-bernardita-jesus>
```

Por último, para enviar los cambios al repositorio en GitHub, utilizamos el comando **git push**. Para que este comando funcione, es necesario haber agregado previamente los archivos con **git add** y haber creado un commit con **git commit -m**. De esta manera los cambios se sincronizan con el repositorio en GitHub.

```bash
PS C:\Users\berni\github\2026-practica-bernardita-jesus> git push
fatal: unable to access 'https://github.com/Bernardita-Jesus/2026-practica-bernardita-jesus.git/': Could not resolve host: github.com
PS C:\Users\berni\github\2026-practica-bernardita-jesus>
```

En este caso, y qué interesante haberlo podido probar, me dice que hubo un error fatal, ya que por las lluvias se me cortó la luz y no tengo internet, por lo que esta función es de las pocas que sí requieren conexión a Internet.

**git stash**: con esto se guardan temporalmente los cambios sin hacer un commit, dejando el repositorio como estaba en el último commit.

**git pull**: con esto se conecta a lo que se subió a GitHub, se actualiza el repositorio local y se pone al día con los cambios del repositorio.

**git push y git pull** son los comandos que requieren conexión a Internet, ya que son los que se conectan con el repositorio en GitHub.

Comandos

```bash
code .
open .
mkdir
gr
history
pwd
cd
```

kdir: 

Punto (.) podriamos definirlo como aquí mismo, dos puntos (..)

```bash
git add .
git status
git commit -m
git push
```

## tareas

referentes diseño parametrico

openescad, direfencia con rhino, justificar lo parametrico

investigar valores materiales, viabilidad

pla o cnc

revisar que parametros pueden y deben ser editables

registro fotografico

parla y relo

cual va a ser el primer sintetizador que voy a investigar, va a ser relo

