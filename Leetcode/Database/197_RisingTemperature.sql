-- leetcode 05/04 2022
-- 197. Rising Temperature

SELECT DISTINCT w2.id 
FROM Weather w1, Weather w2 
Where DATEDIFF(w2.recordDate, w1.recordDate) = 1 and w1.temperature < w2.temperature