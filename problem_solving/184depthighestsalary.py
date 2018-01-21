# Write your MySQL query statement below
SELECT d.Name as "Department", e.Name as "Employee", e.Salary as "Salary"  FROM Employee e
JOIN Department d ON e.DepartmentId = d.id
AND e.Salary = (Select max(Salary) from Employee WHERE Employee.DepartmentId = d.id) 
