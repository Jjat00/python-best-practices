# Buenas Prácticas de Programación en Python

En este repositorio se dan algunos consejos sobre cómo crear código 
en python correctamente, o al menos es un buen punto de inicio.


## 1. Crear un repositorio

El primer paso que debemos realizar antes de crear nuestro primer archivo es inicializar unrepositorio git. Crear un repositorio para el código e implementar un control de versiones ayuda al trabajo en equipo y a la reutilización de código para optimizar tiempo de desarrollo. 

**Para inicializar un repositorio:**

```
git init
```

## 2. Crear un entorno virtual

Como segundo paso, lo ideal es que para cada proyecto, aplicación o paquete que se desee construir es necesario crear un entorno virtual, esto para poder manajar todas las dependencias de librerías que tendrá el proyecto o código.

**Pasos para crear un entorno virtual en python**

Ir a al directorio root del proyecto y ejecutar:

```
python -m venv venv
```

con el anterior comando se creará un nuevo directorio llamado venv, el nombre venv puede ser el reemplazado por el que usted decida, pero es recomendable llamar al entorno virtual como 'venv'.

**Activar entorno virtual**

En windows

```
.\venv\Scripts\activate.bat
```

Una vez estemos dentro del entorno virtual notese que en la consola todo va estar precedido de (venv)

## 3. Tener una estructura de directorios para el código

Después de haber inicializado git y después de activar el entorno virtual es hora de empezar a escribir nuestro código, pero antes es necesario saber que debemos organizar cada script  de código en su respectivo directorio. Esto dependerá de la arquitectura de software que se vaya a implementar. 
Aquí un ejemplo de estructura de directorios:

![ejemplo estructura de código](images/estructura_codigo.JPG)

En la anterior imagen se muestra un ejemplo de estructura de directorios y archivos, esto puede variar, sin embargo, los archivos que nunca deben faltar en nuestro proyecto son:

* .gitignore

    En este archivo pondremos los nombres de los archivos o directorios que no queremos que sean agregados a nuestro repositorio en github. Por ejemplo, el directorio venv nunca deberá ser incluido en el repositorio, para ello es generado el archivo llamado **requirements.txt** que será detallado más adelante.

    Algunos ejemplos de archivos típicos que deben estar en .gitignore son: venv, __pycache__, private keys, etc.

* LICENSE.md

    En este archivo debemos especificar el tipo de lincencia que queremos para nuestro paquete o aplicación. Algunas opciones son: GNU AGPLv3, GNU GPLv3, Mozilla Public License 2.0 GNU LGPLv3, Apache License 2.0, MIT License, The Unlicense.

    La licencia más usada en github es la MIT license.

* README.md

    Este archivo siempre debe estar en cualquier proyecto que desarrollemos y aquí debe ir una descripción general de nuestro proyecto y la información necesaria que necesita otro desarrollador para que pueda usar nuestro paquete o aplicación. Ppodemos usar markdown o html para crear este archivo.

* requirements.txt

    Este archivo es muy importante para permitir pasar código de un desarrollador a otro.
    Aquí irán todas las dependecias que nuestro proyecto nececita para poder ser ejecutado en otro ordenador.
    Este archivo se puede generar automaticamente por medio de la siguiente linea de comando:

    ```
    pip freeze > requirements.txt
    ```

    para ejecutar la anterior linea de comando asegurese de tener el entorno virtual activado.

## 4. Acoger las recomendaciones de estilo dadas por el PEP8

el [PEP8](https://www.python.org/dev/peps/pep-0008/) contiene algunas grandes recomendaciones dadas por la comunidad. Esto para que el código de los desarrolladores de Python se vea y se sienta igual.

Entre las recomendaciones dadas, se resaltan las siguientes:

**Utilice convenciones de nomenclatura adecuadas para variables, funciones, métodos y más.**

* Variables, funciones, métodos, paquetes, módulos: this_is_a_variable
* Clases y excepciones: CapWords
* Métodos protegidos y funciones internas: _single_leading_underscore
* Métodos privados: __double_leading_underscore
* Constantes: CAPS_WITH_UNDERSCORES

Aquí también es importante mencionar **El Zen de Python**, podemos vizualizarlo
ejecutando la siguiente liena de código dentro de python:

```
>>> import this
```

y obtendremos las siguientes recomendaciones:

```
El zen de Python, por Tim Peters

Lo bello es mejor que lo feo.
Explícito es mejor que implícito.
Mejor es simple que complejo.
Complejo es mejor que complicado.
Plano es mejor que anidado.
Es mejor escaso que denso.
La legibilidad cuenta.
Los casos especiales no son lo suficientemente especiales como para romper las reglas.
Aunque la practicidad vence a la pureza.
Los errores nunca deben pasar silenciosamente.
A menos que esté explícitamente silenciado.
Ante la ambigüedad, rechace la tentación de adivinar.
Debe haber una, y preferiblemente solo una, forma obvia de hacerlo.
Aunque esa forma puede no ser obvia al principio a menos que seas holandés.
Ahora es mejor que nunca.
Aunque a menudo nunca es mejor que * ahora mismo *.
Si la implementación es difícil de explicar, es una mala idea.
Si la implementación es fácil de explicar, puede ser una buena idea.
Los espacios de nombres son una gran idea, ¡hagamos más de eso!
```

## 5. Hacer uso de POO

Para hacer un código reutilizable o modular es siempre recomendable que hagamos uso
de la programación orientada a objetos, de esta manera nuestro código tiene algunas ventajas
como: reutilización, modularidad, polimorfismo, encapsulación de datos y herencia.

## 6. Crear un repositorio con templeates de código

De mano con la anterior recomendación, tener un repositorio en el cual guardemos
códigos de nuestros antiguos proyectos (obviamente usando POO y modulares) es de vital 
importancia para acelerar el desarrollo de aplicaciones que sean similares a las 
aplicaciones ya hechas. Entre más enriquecido esté nuestro repositorio de templates
más rápido ejecutaremos futuros proyectos. Solamente es copiar y pegar, y una que otra
modificación. 

## 7. Otras recomendaciones

En el código:

* Sangria: 4 spaces
* Logitud máxima de linea (código): 79
* Logitud máxima de linea (comentarios): 72

Si se usa operadores en diferentes lineas de código hacerlo así

```Python
income = (gross_wages
          + taxable_interest
          + (dividens - qualified_dividends)
          - ira_deduction)
``` 

Para importar librerias, hacerlo en el siguiente orden: primero las librerias que son parte
de python (os, json, ++), después siguen las librerias de terceros (cve, numpy, ++), por
último las librerias personales.

Otra recomendación es importar justamente los métodos necesarios y no todo el paquete completo,
ejemplo:

**forma correcta**

```Python
import os
import sys
``` 

```Python
from subprocess import Popen, PIPE
``` 

**forma incorrecta**

```Python
import sys, os
``` 

**Sphinx** es una herramienta para crear fácilmente documentación inteligente y hermosa

**Usar métodod mágicos**

## 8. Extenciones en Visual Studio Code


## More information about this


-> [best practices](https://data-flair.training/blogs/python-best-practices)