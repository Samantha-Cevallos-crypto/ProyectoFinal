# Readme
# Proyecto Segundo Parcial - GUI con Base de Datos (ServicioGimnasio)

## Integrantes del Grupo
* Cevallos Mendoza Samantha Nikole
# - Laura Fernanda Guillén Vargas
# - Cristhian Isaac Estrella Espinoza
# - Evelyn Noemi Burbano Mora
# - Janeth Maria Verdezoto García

**Jornada:** Vespertina  
**Asignatura:** Programación Orientada a Objetos  
---
### Enlace del video demostrativo
https://1drv.ms/f/c/5ee4c4ee5e6f75b9/IgDm_DdzYocDT6sKB8ZYfNk6AS710tMpul3vcbnP__zeQ1c

---


## Descripción General del Sistema
Este sistema es una aplicación de escritorio diseñada bajo el patrón arquitectónico MVC (Modelo-Vista-Controlador) que gestiona el registro de clientes y los servicios contratados en un gimnasio. El software permite centralizar la información de los usuarios vinculados a un plan específico (Gimnasio, personal trainning , membresia anual), garantizando la persistencia de los datos en un entorno relacional, la integridad de la información mediante validaciones estrictas y una experiencia de usuario fluida y libre de errores en la persistencia.

---

## Funcionalidades Implementadas (CRUD Completo)
El sistema gestiona de forma interactiva la tabla Servicio de la base de datos a través de las siguientes operaciones de la interfaz:
* **Guardar (Create):** Inserta nuevos registros validados en la base de datos.
* **Buscar (Read):** Consulta y extrae la información de un cliente mediante su número de cédula, poblando automáticamente los campos de la interfaz gráfica.
* **Actualizar (Update):** Modifica los datos existentes de un registro previamente indexado por su cédula.
* **Eliminar (Delete):** Remueve permanentemente un registro del sistema, incluyendo una capa de confirmación de seguridad previa.
* **Limpiar:** Restablece todos los componentes visuales del formulario a su estado inicial.

---

## Tecnologías Utilizadas
* **Lenguaje de Programación:** Python 3.x
* **Interfaz Gráfica (GUI):** PySide6 (Qt for Python)
* **Base de Datos:** Sistema de Gestión de Bases de Datos Relacionales (SGBD compatible con la capa DAO)
* **Librerías del Núcleo:**
    * re (Expresiones regulares de Python para validación lógica).
    * PySide6.QtGui.QRegularExpressionValidator (Para restricciones nativas en tiempo real).

---

## Explicación de las Validaciones Implementadas
El proyecto cuenta con un sistema de doble filtro de seguridad para asegurar la calidad de los datos ingresados:

1. **Validación Reactiva (En tiempo real):** Utiliza QRegularExpressionValidator para restringir las pulsaciones del teclado del usuario en la vista de la siguiente manera:
    * Cédula y Búsqueda: Permite exclusivamente el ingreso de caracteres numéricos (máximo 10 dígitos).
    * Nombre y Apellido: Admite únicamente letras (incluyendo tildes y la letra Ñ) y espacios.
    * Precio: Restringe la entrada a números decimales y bloquea por completo la digitación de valores negativos desde el teclado.

2. **Validación Lógica (Filtro de Fondo):** Centralizada en el método privado _validar_formulario antes de interactuar con la base de datos:
    * Sanitiza las entradas removiendo espacios vacíos en los extremos con el método .strip().
    * Comprueba la obligatoriedad de todos los campos del formulario.
    * Usa expresiones regulares estrictas para confirmar que la cédula posea exactamente 10 dígitos y que el correo electrónico cumpla con una estructura sintáctica estándar (RFC).

---

## Estructura del Proyecto
```text
├── datos/
│   └── conexion.py         # Capa de datos (Clase ServicioDAO para operaciones SQL)
├── GUI/
│   └── vtn_principal.py    # Interfaz gráfica generada o convertida desde Qt Designer
├── persona.py              # Controlador principal (Clase PersonaServicio - Lógica del negocio)
├── main.py                 # Archivo de arranque de la aplicación
└── README.md               # Documentación del proyecto

## Estado Final del Proyecto
El proyecto se encuentra 100% Funcional y cumple con todos los requerimientos establecidos para la evaluación del segundo parcial. 

Se ha completado con éxito la integración del patrón arquitectónico MVC, logrando que el controlador (`PersonaServicio`) gestione de forma óptima el flujo de datos entre la interfaz gráfica en PySide6 y la persistencia en el backend a través de la clase `ServicioDAO`. Las operaciones de creación, lectura, actualización y eliminación (CRUD) operan de manera síncrona con la base de datos `ServicioGimnasio`. 

Además, el sistema es tolerante a fallos gracias a la implementación de bloques de control de excepciones que evitan cierres inesperados ante errores de duplicidad de llaves primarias o formatos de entrada incorrectos.

---
## Descripción de la Base de Datos
* **Base de Datos:** ServicioGimnasio
* **Tabla:** Servicio

### Esquema de la Tabla
| Campo | Tipo de Dato | Restricciones / Descripción |
| :--- | :--- | :--- |
| `cedula` | VARCHAR(10) / TEXT | Primary Key (Llave Primaria) - Única e irrepetible |
| `nombre` | VARCHAR / TEXT | Not Null (Obligatorio) |
| `apellido` | VARCHAR / TEXT | Not Null (Obligatorio) |
| `email` | VARCHAR / TEXT | Not Null - Formato de correo electrónico |
| `servicio` | VARCHAR / TEXT | Not Null - Nombre del plan seleccionado |
| `descripcion` | TEXT | Not Null - Detalles del servicio |
| `precio` | DECIMAL / FLOAT | Not Null - Valor numérico no negativo |
```
ESTADO FINAL

El proyecto se encuentra 100% Funcional y cumple con todos los requerimientos establecidos para la evaluación del segundo parcial.

Se ha completado con éxito la integración del patrón arquitectónico MVC, logrando que el controlador (PersonaServicio) gestione de forma óptima el flujo de datos entre la interfaz gráfica en PySide6 y la persistencia en el backend a través de la clase ServicioDAO. Las operaciones de creación, lectura, actualización y eliminación (CRUD) operan de manera síncrona con la base de datos ServicioGimnasio.

Además, el sistema es tolerante a fallos gracias a la implementación de bloques de control de excepciones que evitan cierres inesperados ante errores de duplicidad de llaves primarias o formatos de entrada incorrectos.




