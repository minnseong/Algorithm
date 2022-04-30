-- Programmers 04/30 2022
-- 헤비 유저가 소유한 장소

SELECT p.ID, p.NAME, p.HOST_ID
From PLACES p
WHERE p.HOST_ID IN (
    SELECT HOST_ID
    FROM PLACES
    GROUP BY HOST_ID
    HAVING COUNT (*) > 1
)
ORDER BY p.ID;