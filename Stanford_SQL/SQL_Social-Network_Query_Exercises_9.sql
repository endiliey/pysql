SELECT name, grade
FROM Highschooler
WHERE ID IN (SELECT ID2 FROM Likes GROUP BY ID2 HAVING COUNT(ID2) > 1)
