-- leetcode 04/24 2022
-- 182. Duplicate Emails

Select Email
From Person
Group by Email
Having COUNT(Email) > 1;