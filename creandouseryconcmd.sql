--Creamos un nuevo usuario--
create user juan with password '1234'; --Para entrar desde cmd (como admin) y escribir este comando: psql -U juan -d cursosqlsergio -h localhost -p 5432--

grant select on employees.salary to juan; --Da permiso para usar select * from employees.salary; ejecutando en el cmd despues de conectar con el nuevo user--

grant usage on schema employees to juan; --Da permiso para usar la esquema empleados al usuario juan--

revoke usage on schema employees from juan; --Quita el permiso del uso de la esquema empleados al user juan--

--Ejercicio 2
--Creando otro usuario: Ana--
create user ana with password '12345';

drop user ana; --Borrar usuario--

--grant select on employees.salary to ana;
--revoke select on employees.salary from ana;

--grant usage on schema employees to ana;
--revoke usage on schema employees from ana;

grant select on all tables in schema employees to ana; --Permiso de seleccion todas las tablas en la esquema employees--
--revoke select on all tables in schema employees from ana;

revoke select on employees.salary from ana; --quita permiso de selección en la tabla empleados.salario--