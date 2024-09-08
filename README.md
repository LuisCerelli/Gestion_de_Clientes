# Sistema de Gestión de Clientes y Mascotas
Este proyecto consiste en un programa que permite gestionar clientes y sus respectivas mascotas o activos relacionados (vehículos, prendas, etc.). A través de un menú interactivo, el usuario puede registrar clientes, agregarles mascotas y generar historiales de visitas para cada mascota.

### Descripción del funcionamiento
El código está organizado en varias funciones que realizan tareas específicas:

### Registro de Clientes: 
Permite registrar nuevos clientes en el sistema, guardando su nombre, apellido y número único (RUT).
### Agregar Mascota o Activo:
Relaciona una mascota (o cualquier activo) con un cliente registrado. Cada mascota incluye un nombre y tipo.
### Listar Clientes: 
Genera una lista de todos los clientes con sus respectivas mascotas.
### Imprimir Historial de Visitas:
Crea un archivo de texto para cada cliente con las visitas de control de sus mascotas, incluyendo detalles de la fecha y el resumen de la visita.
### Menú Principal:
Ofrece una interfaz de usuario donde se puede elegir entre las distintas acciones mencionadas anteriormente.
### Ejemplo de Uso
El programa está diseñado para ser ejecutado en un entorno de consola, donde se pueden ingresar los datos directamente. Un ejemplo de interacción sería el siguiente:

## Utilidad para Ingeniería de Datos
Este código puede ser particularmente útil en la **ingeniería de datos** al permitir la **gestión y almacenamiento de datos** relacionados con clientes y sus activos. Aunque es un ejemplo básico, puede ser fácilmente escalable para integrarse con bases de datos relacionales o sistemas de almacenamiento en la nube, proporcionando un primer paso hacia el manejo de grandes volúmenes de información. Además, la capacidad de generar reportes en formato de archivo es una funcionalidad clave que puede extenderse a otros tipos de procesamiento de datos, como la exportación a CSV o la integración con pipelines de datos más complejos.
El enfoque modular y escalable del código puede ser adaptado a sistemas de registro en distintos sectores, como clínicas veterinarias, talleres mecánicos o inventarios de clientes en comercios. De esta forma, la lógica de manipulación de datos puede ser fácilmente reutilizada y mejorada para proyectos más grandes, lo que lo convierte en una base adecuada para futuras implementaciones.
