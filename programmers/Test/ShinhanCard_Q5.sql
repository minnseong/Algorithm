-- 신한카드 코딩테스트 10/13 2022
-- Q5

SELECT b.name as NAME, COUNT(b.name) as COUNT
FROM employees e JOIN branches b
ON e.branch_id = b.id
GROUP BY b.name
HAVING COUNT(b.name) >= 3
ORDER By b.id ASC;
