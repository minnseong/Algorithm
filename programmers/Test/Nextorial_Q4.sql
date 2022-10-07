# 넥토리얼 코딩테스트 10/07 2022
# Q4 - 100

SELECT DISTINCT c.party, COUNT(*) AS CNT
FROM Results r
JOIN Candidates c ON r.candidate_id = c.id
WHERE r.votes = (SELECT MAX(votes) FROM Results rr WHERE rr.constituency_id = r.constituency_id)
GROUP BY (c.party)
ORDER BY CNT DESC;