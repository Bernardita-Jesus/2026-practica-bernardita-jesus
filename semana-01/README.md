# semana-01

## Semana de adaptación

Reunión Lunes 20 de julio, invierno 2026

Hice una copia del repositorio de la practica en mi computador desde la terminal, estoy utilizando Windows PowerShell y visual studio code para subir varios archivos a la nube de github

por el momento lo que tengo que hacer es abrir la terminal y encontrar mi repositorio

con cd busco este espacio, y puedo simplemente escribir github, 2026 y tab para que autocomplete mi busqueda, ya que realmente no tengo ningun repositorio mas copiado asique me redirige a mi unica opcion

```bash

PS C:\Users\berni> cd .\github\2026-practica-bernardita-jesus\
PS C:\Users\berni\github\2026-practica-bernardita-jesus>
```

luego consulto con git status cual es el estado de mi repositorio, para saber los cambios que se realizaron

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

en este caso yo modifique el readme de la semana-01, que por cierto, son estos mismos apuntes





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

git add .: con espacio punto, se preparan todos los cambios subidos, pero tambien se puede subir solo una carpeta.

git status: para comprobar el estado, si hubieron cambios.

git commit -m: para subir el nombre del del cambio, es necesario subir esto y tiene que haber algo agregado.

git push: si se agregaron algo, y se comenta, finalmente se puede subir, con push se envia a la nuve.

git pull: con esto se conecta a lo que se subio a la nube, se actualiza, se pone al dia.

git stash: con esto rebobina al ultimo commit.

git push y git pull es el unico momento que se conecta con la nube

## tareas

referentes diseño parametrico

openescad, direfencia con rhino, justificar lo parametrico

investigar valores materiales, viabilidad

pla o cnc

revisar que parametros pueden y deben ser editables

registro fotografico

parla y relo

cual va a ser el primer sintetizador que voy a investigar, va a ser relo

