# Write your MySQL query statement below
SELECT(
    SELECT Salary  FROM Employee
    WHERE Salary != (SELECT max(Salary) From Employee)
    Order By Salary DESC
    Limit 1) as SecondHighestSalary
