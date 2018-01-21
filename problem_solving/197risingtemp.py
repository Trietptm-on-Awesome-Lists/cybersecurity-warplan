# Write your MySQL query statement below
# Can us a join, or a subquery
SELECT Id from Weather w1 WHERE w1.Temperature > (Select Temperature FROM Weather WHERE id = (w1.id - 1))
# Had to add DATE_SUB, one test failed, id doesnt work
SELECT Id from Weather w1 WHERE w1.Temperature > (Select Temperature FROM Weather WHERE Date = DATE_SUB(w1.Date, INTERVAL 1 DAY))
