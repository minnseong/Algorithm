-- leetcode 04/12 2022
-- 175 Combine Two Tables

Select p.firstName, p.LastName, a.City, a.state
From Person p left Join Address a
on p.personId = a.personId;