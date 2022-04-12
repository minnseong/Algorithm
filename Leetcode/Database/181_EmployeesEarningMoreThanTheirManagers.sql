-- leetcode 04/12 2022
-- 181. Employees Earning More Than Their Managers

Select e.name AS Employee
From Employee e
WHERE (SELECT salary FROM Employee Where e.managerId = id) <= e.salary;

Select a.name as Employee
From Employee as a, Employee as b
Where a.managerId = b.Id and a.salary > b.salary;