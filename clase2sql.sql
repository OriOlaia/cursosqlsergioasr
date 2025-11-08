select *
from employee
order by first_name

select *
from employee
where id=10002 or id=10001

select *
from employee
where first_name like '%z'

select *
from employee
inner join salary on employee.id=salary.employee_id

select e.id, e.first_name, e.gender, s.amount 
from employee e inner join salary s on e.id=s.employee_id 
where e.id=10001 or e.id=10002
order by s.amount desc

select e.id as legajo, e.first_name as nombre,	e.last_name as apellido, s.amount
from employee e inner join salary s on e.id=s.employee_id
where s.amount between 70000 and 80000  

select e.id as legajo, e.first_name as nombre, e.gender as genero, e.last_name as apellido, count (*) as aumentos
from employee e inner join salary s on e.id=s.employee_id 
where e.id=10001 or e.id=10002
group by e.id
order by e.first_name desc

select e.id, e.first_name, e.last_name, t.title 
from employee e inner join title t on e.id = t.employee_id 

select e.id, e.first_name, e.last_name, s.amount
from employee e inner join salary s on e.id = s.employee_id
where e.id=10002
--and s.to_date='9999-01-01'
order by s.from_date


select *
from department_employee de inner join employee e
on de.employee_id = e.id inner join department d
on de.department_id = d.id

Realizar un reporte:
Legajo
Apellido
Nombre
Departamento donde trabaja
Ultimo Salario
Titulo

select e.id as Legajo, e.last_name as Apellido, e.first_name as Nombre, d.dept_name as Departamento, s.amount as Salario, t.title as Titulo
from employee e inner join department_employee de 
on de.employee_id = e.id inner join department d
on de.department_id = d.id inner join salary s 
on s.employee_id = e.id  inner join title t
on e.id = t.employee_id 
where s.to_date = '9999-01-01' and de.to_date = '9999-01-01' and t.to_date = '9999-01-01' 

insert into employee (id, birth_date, first_name, last_name,gender,hire_date)
values (999999,'2001-05-01','Juan','Martinez','M','2024-03-01')

select *
from employee e
where id=999999

update employee
set first_name = 'Ruben Nicolas'
where id=999999

delete from employee where id=999999

select AVG(s.amount)
from salary s

select d.dept_name as departamento, AVG(s.amount), sum (s.amount)
from department_employee de inner join department d 
on de.department_id = d.id inner join salary s 
on de.employee_id = s.employee_id
group by d.dept_name

select *
from salary s full outer join employee e
on s.employee_id = e.id
where e.id = 999999

select *
from department d cross join department d2
order by d.id, d2.id

select *
from employee e 
where e.id = 999999
union all
select *
from employee e 
where e.id >= 10001 and e.id <=10010

select 'Total empeados', count(*)
from employee e 
union all
select 'Salario Promedio', avg(s.amount)
from salary s
union all
select 'Total de departamentos', count(*)
from department d

create view report_empresa as
select 'Total empeados', count(*)
from employee e 
union all
select 'Salario Promedio', avg(s.amount)
from salary s
union all
select 'Total de departamentos', count(*)
from department d

select *
from report_empresa

drop view report_empresa

with empleados as (select * from employee),
emp_depto as (select * from department_employee d),
salario as (select * from salary)
select * from empleados, emp_depto, salario
where emp_depto.employee_id = empleados.id 
and emp_depto.employee_id = salario.employee_id

Realizar un reporte:
Legajo
Apellido
Nombre
Departamento donde trabaja

select e.id as Legajo, e.last_name as Apellido, e.first_name as Nombre, d.dept_name as Departamento, s.amount as Salario, t.title as Titulo
from employee e inner join department_employee de 
on de.employee_id = e.id inner join department d
on de.department_id = d.id inner join salary s 
on s.employee_id = e.id  inner join title t
on e.id = t.employee_id 
where s.to_date = '9999-01-01' and de.to_date = '9999-01-01' and t.to_date = '9999-01-01'

select e.id, e.first_name, e.last_name, d.dept_name, s.amount 
from employee e, department_employee de, department d, salary s
where e.id = de.employee_id and de.department_id = d.id and e.id = s.employee_id 
and de.to_date='9999-01-01' and s.to_date='9999-01-01'

select *
into employee_nuevo
from employee e
where e.id=999999