-- Proyecto Segundo Parcial - GUI con Base de Datos
-- Asignatura: Programación Orientada a Objetos
-- Script de creación de la base de datos y tabla utilizadas por el proyecto.
-- Motor: SQL Server

CREATE DATABASE ServicioGimnasio;
GO

USE ServicioGimnasio;
GO

CREATE TABLE Servicio (
    cedula          VARCHAR(10)   PRIMARY KEY,
    nombre          VARCHAR(100)  NOT NULL,
    apellido        VARCHAR(100)  NOT NULL,
    email           VARCHAR(150),
    servicio        VARCHAR(100)  NOT NULL,
    descripcion     VARCHAR(150),
    precio          DECIMAL(10,2) NOT NULL,
    fecha_registro  DATETIME      DEFAULT GETDATE()
);
GO

-- Usuario de aplicación con permisos de lectura/escritura sobre la base
-- (ejecutar conectado como 'sa' u otra cuenta con rol sysadmin)
-- CREATE LOGIN admin_SAP WITH PASSWORD = '1234';
-- CREATE USER admin_SAP FOR LOGIN admin_SAP;
-- ALTER ROLE db_datareader ADD MEMBER admin_SAP;
-- ALTER ROLE db_datawriter ADD MEMBER admin_SAP;
-- GO

-- Consulta de verificación
SELECT * FROM Servicio;
