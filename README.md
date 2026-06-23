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
## EJERCICIO MD 4
# Panel de Administración y Migraciones en Django

Este repositorio contiene la resolución del ejercicio práctico centrado en la configuración avanzada de la interfaz de administración y la sincronización de la base de datos a través de migraciones en Django.

## Funcionalidades Implementadas

* **Sincronización de Base de Datos:** Ejecución de `makemigrations` y `migrate` para reflejar la estructura relacional de los modelos (Author, Tag, Post) en las tablas físicas.
* **Gestión de Autores:** Panel configurado con `list_display` (Nombre, Email) y `search_fields` para facilitar la búsqueda de usuarios por credenciales.
* **Gestión de Etiquetas:** Interfaz administrativa simplificada para la categorización temática.
* **Gestión de Publicaciones (Posts):** Panel avanzado con `list_display` (Título, Autor, Fecha), `list_filter` (Fecha, Autor) y `search_fields` (Título, Contenido y Nombre del Autor), integrando navegación jerárquica por fechas y selección horizontal de etiquetas.

## Reflexión Teórica: Gestión de Datos y Migraciones

Las configuraciones personalizadas en `admin.py` (como `list_display` y `search_fields`) facilitan exponencialmente la gestión de datos porque transforman los registros brutos de la base de datos en una interfaz visual e interactiva. Permiten a los administradores localizar y filtrar información en tiempo real sin necesidad de escribir sentencias SQL manuales. Por otro lado, las migraciones mantienen la base de datos sincronizada actuando como un sistema de control de versiones estructural; escanean los modelos de Python, detectan los cambios lógicos y generan automáticamente las instrucciones precisas para alterar las tablas físicas de forma segura y predecible.

## Despliegue y Rollback de Base de Datos

En entornos de producción, la sincronización de la base de datos debe manejarse con precaución.

* **Despliegue (Migrar hacia adelante):**
  Para aplicar los últimos cambios estructurales al servidor de producción, ejecute:
  `python manage.py migrate`

* **Rollback (Revertir migraciones):**
  Si una actualización corrompe el sistema y es necesario volver a un estado anterior seguro, identifique el número de migración previa (ej. `0001_initial`) y ejecute:
  `python manage.py migrate nombre_de_la_app 0001`
  Para vaciar completamente las tablas de una app:
  `python manage.py migrate nombre_de_la_app zero`

## Vistas CRUD y Seguridad

Se implementó el ciclo completo de gestión de datos (CRUD) para el modelo `Post` utilizando Vistas Basadas en Clases (CBV) de Django.
* **Lectura:** Implementación de `ListView` y `DetailView` para la visualización pública del catálogo de artículos.
* **Escritura y Modificación:** Uso de `CreateView`, `UpdateView` y `DeleteView` para la gestión de contenido.
* **Seguridad:** Se aplicó el mixin `LoginRequiredMixin` para restringir el acceso a las vistas de modificación exclusivamente a usuarios autenticados, protegiendo la integridad de la base de datos.

## Guía de Despliegue Local (Deployment)
Para inicializar este proyecto desde cero en un entorno local y asegurar su correcto funcionamiento, ejecute estrictamente los siguientes comandos en la terminal de la raíz del proyecto:

1. **Crear y activar el entorno virtual:**
   ```bash
   python -m venv env
   env\Scripts\activate
