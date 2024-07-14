# Motorwash

## Gestor de lavadero de vehículos profesional

### Proyecto final para la materia PYTHON de [CoderHouse](https://www.coderhouse.com), comisión #57810

Alumno: Pacheco, Martín

Profesor: Beltrán, Norman

Tutor: Gomez, Demian

[Demo video](https://youtu.be/UX0RG3PpmOw)

## Brief

App web para la gestión de procesos de un lavadero profesional de vehículos, con registro de clientes, vehículos, tareas y empleados.

La finalidad de la app es poder contar con un seguimiento básico de tareas a realizar sobre los vehículos que ingresan al establecimiento, con la opción de desarrollar a futuro un sistema de aviso al cliente, cuando su vehículo se encuentre próximo a ser retirado (a través de email y WhatsApp).

Al ingresar al home, se muestran las tareas en curso, estando registrado o no.

Si se loguea como usuario, se pueden acceder a las distintas vistas de los modelos. Además, existe la posibilidad de cargar un ávatar y modificar información del perfil. Por el momento, no se definen grupos de usuarios con distintos accesos y permisos. A futuro, se evalúa implementar grupos para clientes (quienes pueden seguir en tiempo real el estado de su vehículo), empleados (quienes irán cargando y completando tareas) y administradores (funciones de Empleados y con posibilidad de ABM en la base de datos).

### Modelos utilizados

`Client`
`Vehicle`
`Task`
`Employee`

#### Para ingresar como superusuario en la ruta `/admin`:

`username: admincoder`
`password: admin1234`

##### A tener en cuenta:

    - Se recomienda utilizar un entorno virtual (venv) que contenga las siguientes dependencias:

        `pillow`

    - Se omite el uso de variables de entorno con el fin de aportar seguridad y manejo de SECRET_KEY

    - Se incluye base de datos con información previamente cargada de los modelos utilizados, con el fin de brindar una mejor experiencia de corrección

##### Changelog:

-   [Entrega final - 14/07/24]:

    -   Detalles visuales finales en app y about

    -   Links agregados en pagina about

    -   Agregado testlist.xls y link a video demo en readme

-   [Previo a Entrega final - 12/07/24]:

    -   Mejorada la interfaz de usuario

    -   Corrección de bugs en las operaciones de base de datos

    -   Agregada la página /about con información del autor

-   [Tercera Preentrega - 28/06/24]: Agregado y consulta a DB funcional en cada categoría. Faltan detalles visuales e integración correcta de bloques en html para no perder de vista los botones de acción.
