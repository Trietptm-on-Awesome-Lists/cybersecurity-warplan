# Write your MySQL query statement below
DELETE per1 FROM Person per1,
    Person per2
WHERE
    per1.Email = per2.Email AND per1.Id > per2.Id
