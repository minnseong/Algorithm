-- Programmers 03/19 2022
-- String, Date

1. 루시와 엘라 찾기 
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME IN ("Lucy", "Ella", "Pickle", "Rogan", "Sabrina", "Mitty")
ORDER BY ANIMAL_ID ASC;

2. 이름에 el이 들어가는 동물 찾기
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE ANIMAL_TYPE = 'Dog' AND NAME LIKE '%el%'
ORDER BY NAME ASC;

3. 중성화 여부 파악하기
SELECT ANIMAL_ID, NAME, IF((SEX_UPON_INTAKE LIKE 'Neutered%') or (SEX_UPON_INTAKE LIKE 'Spayed%'), 'O', 'X') AS 중성화
FROM ANIMAL_INS
ORDER BY ANIMAL_ID ASC;

4. 오랜 기간 보호한 동물(2)
SELECT INS.ANIMAL_ID, INS.NAME
FROM ANIMAL_INS INS INNER JOIN ANIMAL_OUTS OUTS
ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
ORDER BY DATE(OUTS.DATETIME) - DATE(INS.DATETIME) DESC LIMIT 2
-- ORDER BY DATEDIFF(OUTS.DATETIME, INS.DATETIME) DESC LIMIT 2
-- TIMESTAMPDIFF 시간차이

5. DATETIME에서 DATE로 형 변환
SELECT ANIMAL_ID, NAME, date_format(DATETIME, '%Y-%m-%d') AS 날짜
FROM ANIMAL_INS
ORDER BY ANIMAL_ID ASC;