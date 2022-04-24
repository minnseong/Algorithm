-- leetcode 04/24 2022
-- 183. Customers Who Never Order

Select c.name as Customers
From Customers c
Where c.id not in (Select o.customerId From Orders o);