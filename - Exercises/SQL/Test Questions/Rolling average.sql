-- calculate rolling average for lastest 3 days


SELECT SUM(Transaction_Amount) / COUNT(DISTINCT Transaction_Date)
FROM rolling
WHERE Transaction_Date IN 
	(SELECT DISTINCT TOP 3 Transaction_Date
	FROM rolling 
	ORDER BY Transaction_Date DESC)


SELECT TOP 3 d1.Transaction_Date, 
		AVG(d1.Amount) OVER (ORDER BY d1.Transaction_Date ROWS BETWEEN 2 PRECEDING AND 2 FOLLOWING) AS MovingAverage
FROM (SELECT DISTINCT Transaction_Date, SUM(Transaction_Amount) AS Amount
		FROM rolling
		GROUP BY Transaction_Date) AS d1
ORDER BY d1.Transaction_Date DESC

