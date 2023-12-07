UPDATE inproceedings
	SET  pubid = publications.pubid
FROM publications
	WHERE inproceedings.title = publications.title;
	
SELECT inpro.author
     , COUNT(DISTINCT inpro.title) AS papers
FROM inproceedings inpro
WHERE inpro.title LIKE '%SIGMOD%' OR inpro.title LIKE '%PVLDB%'
GROUP BY inpro.author
HAVING COUNT(DISTINCT inpro.title) >= 10
