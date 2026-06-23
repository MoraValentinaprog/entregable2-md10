# Workshop Django - Módulo 10

Este proyecto es una aplicación web funcional desarrollada en Django.

## Guía de Inicio Rápido

### 1. Clonar el repositorio
git clone https://github.com/MoraValentinaprog/entregable2-md10.git
cd workshop

### 2. Configurar el Entorno Virtual
python -m venv env
En Windows: .\env\Scripts\activate

### 3. Instalar Dependencias
pip install -r requirements.txt

### 4. Ejecutar Migraciones y Servidor
cd workshop
python manage.py migrate
python manage.py runserver

Accede a http://127.0.0.1:8000/ en tu navegador.


# Proyecto Integrador Django - Catálogo y Blog

Este repositorio contiene la resolución final de las prácticas de desarrollo web utilizando el framework Django. El proyecto está estructurado en un esquema de múltiples aplicaciones para separar las responsabilidades lógicas.

## Estructura del Proyecto

* **Core (Catálogo):** Aplicación destinada a la gestión de un catálogo de documentales. Implementa validaciones personalizadas para fechas de estreno y enlaces canónicos.
* **Blog (Publicaciones):** Aplicación completa para la gestión de un blog. Incluye entidades interconectadas (Autores, Etiquetas y Publicaciones) y restricciones de longitud de caracteres.

## Características Técnicas Implementadas

* **Arquitectura MTV:** Separación clara entre Modelos, Vistas y Plantillas.
* **Modelado Relacional:** Uso avanzado de `ForeignKey` y `ManyToManyField` con sus respectivos `related_name`.
* **Validaciones Nativas y Personalizadas:** Implementación de `MinLengthValidator` y sobreescritura del método `clean()` en ambas aplicaciones para garantizar la integridad de los datos.
* **Entorno Seguro:** Separación de credenciales sensibles mediante variables de entorno (`django-environ`).
* **Administrador Avanzado:** Panel de control de Django enriquecido con filtros, campos de búsqueda y traducciones nativas (`verbose_name`).
* **Testing:** Pruebas unitarias para validar las reglas de negocio del sistema.

## Instalación y Ejecución Local

1. Clonar el repositorio.
2. Crear un entorno virtual e instalar las dependencias: `pip install -r requirements.txt`
3. Crear un archivo `.env` en la raíz del proyecto y definir la variable `SECRET_KEY`.
4. Ejecutar las migraciones: `python manage.py migrate`
5. Iniciar el servidor: `python manage.py runserver`

---
