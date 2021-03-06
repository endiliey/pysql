SELECT title, AVG(stars)
FROM Movie
INNER JOIN Rating USING(mID)
GROUP BY title
ORDER BY AVG(stars) DESC, title
