# Semana-04

| Fecha      | Día      | Temas                                                | Lugar     | Horas día / hora semana |
| :--------- | :------- | :--------------------------------------------------- | :-------- | :---------------------- |
| 2026-08-10 | Lunes    | planificación, git, VCV Rack, referentes             | LID       | 007 / 007               |
| 2026-08-14 | Viernes  | lectura referentes, lectura tesis                    | Casa      | 002 / 009               |
| 2026-08-15 | Sábado   | github, OpenScad                                     | Casa      | 003 / 012               |

## Entorno de desarrollo

Lo que estoy trabajando actualmente se relaciona con la **computación física**, los **objetos interactivos** y el **diseño de interacción**.

Para producir software, es necesario trabajar dentro de un **entorno de desarrollo**.

También como referente tenemos a **Arduino** y sus creadores, por su relación con el desarrollo de proyectos de computación física y objetos interactivos.

**Interacción háptica**; la interacción entre una persona y un objeto mediante el sentido del tacto.

Además, aparece el concepto de **rules of thumb**, entendido como una forma de trabajar o aproximarse **al ojímetro**, es decir, mediante una estimación basada en la experiencia, en vez de una medición.

Esto seria como diseño Heurístico, iterar, observar los resultados y ajustar progresivamente; de este procesoso tomamos estas aproximaciones y nuestros rules of thumb.

Yo tengo que proponer nuestras **rules of thumb**.

Wavetable Synthesis.

### GitHub

GitHub alberga una gran cantidad de repositorios y proyectos de software que conviven dentro de la plataforma. Muchas empresas, organizaciones y personas suben allí sus proyectos y colaboran en ellos.

Yo cada vez he ido aprendiendo más sobre GitHub, no solo a utilizarlo, sino también a imaginar cómo funciona; entender el sistema de copias, escribir desde la terminal, subir archivos que se encuentran en más de una carpeta y luego agregarlos todos de una sola vez. Con la práctica, estas herramientas se han vuelto cada vez más **cómodas y amenas** de utilizar.

Agradezco mucho haber aprendido a utilizar esta herramienta y poder seguir aprendiendo de ella. También he estado organizando mis métodos de registro, volviendo a darle valor como un medio para **captar y compartir mis aprendizajes**.

Además de todo esto, [Mateo](https://github.com/matbutom) y [@Janis](https://github.com/janisepulveda) me mostraron que existe un **top de committers a nivel nacional**, que, en el fondo, registra la cantidad de cambios y aportaciones que realiza cada persona. Luego estuve leyendo que, para aparecer en este ranking, es necesario tener al menos 32 seguidores.

Me quiero dar la tarea de reunirlos y eventualmente, **aparecer en el top de committers**.

https://committers.top/chile

### VCV Rack

Para poder visualizar los cambios y modificaciones de los sintetizadores que estoy utilizando como referencia para modelar los paneles, cloné el repositorio de **VCV Rack** desde GitHub.

El proceso corresponde a la configuración de un **entorno de desarrollo local**, que no está destinado al consumo o distribución pública, sino a trabajar directamente sobre el código y realizar modificaciones.

Al ser un proyecto de código abierto en gran parte, puedo acceder a su código, modificarlo y realizar mis propias versiones. Esto me permite comprender su funcionamiento.

Para configurar este entorno fue necesario instalar **MSYS2**, una aplicación que funciona como una terminal y que permite utilizar comandos y herramientas que no están de la misma manera en Windows PowerShell. Por este motivo, utilizaré MSYS2 como terminal para trabajar con el repositorio.

Una vez configurado el entorno, cloné el repositorio de VCV Rack desde GitHub. Dentro del repositorio, descargué sus submódulos y posteriormente compilé el programa.

```bash
make dep

make

make run
```

Estos tres comandos forman parte de la **trilogía fundamental para configurar, compilar y ejecutar Rack**

- **make dep**: instala y configura las dependencias necesarias.

- **make**: compila el proyecto.

- **make run**: corre VCV Rack.

### Plugins

Dentro de Rack se encuentran los **plugins**, que son los espacios donde se desarrollan los módulos que utilizaré. En este caso, trabajaré con los elementos de Rack de **Piruetas / Popusintes**.

Dentro de los plugins se incorporan los diferentes módulos que posteriormente aparecen dentro de VCV Rack.

Para mantener actualizado un repositorio utilizaré **git clone y git pull**

```bash
git clone
```

y

```bash
git pull
```

**git clone** permite descargar inicialmente un repositorio, mientras que **git pull** permite incorporar las actualizaciones agregadas posteriormente.

### Actualización y compilación

Cuando [Aarón](https://github.com/montoyamoraga) actualice el proyecto, debo incorporar los cambios y volver a realizar el proceso de compilación. Para ello, debo hacer nuevamente:

```bash
make dep
make
make dist
```

De esta manera, puedo mantener mi entorno de desarrollo **actualizado y visualizar los cambios** realizados en los sintetizadores y plugins sobre los cuales estoy trabajando.

## Referentes

### Arte sonoro

Bjork, atmosfera fria

Arcade Fire

Arp 2600

https://patshiu.com/

Monologue Korg

### Lectura