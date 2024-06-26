-- Programmers 02/26 2022
-- SUM, MAX, MIN

1. 최댓값 구하기
SELECT DATETIME FROM ANIMAL_INS ORDER BY DATETIME DESC LIMIT 1;

2. 최솟값 구하기
SELECT MIN(DATETIME) FROM ANIMAL_INS;

3. 동물 수 구하기
SELECT COUNT(ANIMAL_ID) FROM ANIMAL_INS;

4. 중복 제거하기
SELECT COUNT(DISTINCT(NAME)) FROM ANIMAL_INS;