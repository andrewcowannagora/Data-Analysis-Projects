-- table manipulation / join


SELECT 
	CASE WHEN LEN(Data1.InitialAccount1) < 16 THEN CONCAT(Data1.Branchcode,'-', Data1.InitialAccount1) ELSE  Data1.InitialAccount1 END AS Account#,
	Data1.IntNRTnum, Data1.chrProv, Data1.vchProduct1
INTO clean_account
FROM Data1

SELECT d1.*, d3.Income_amt
FROM clean_account AS d1
JOIN Data2 AS d2
	ON d1.Account# = d2.Account#
JOIN Data3 AS d3
	ON d2.CUST_ID = d3.CUST_ID



SELECT d1.*, d3.Income_amt
FROM (SELECT 
		CASE WHEN LEN(Data1.InitialAccount1) < 16 THEN CONCAT(Data1.Branchcode,'-', Data1.InitialAccount1) ELSE  Data1.InitialAccount1 END AS Account#,
		Data1.IntNRTnum, Data1.chrProv, Data1.vchProduct1
		FROM Data1) AS d1
JOIN Data2 AS d2
	ON d1.Account# = d2.Account#
JOIN Data3 AS d3
	ON d2.CUST_ID = d3.CUST_ID



SELECT 
CASE WHEN LEN(InitialAccount1) < 16 THEN CONCAT(Branchcode,'-', InitialAccount1) ELSE  InitialAccount1 END AS Account#,
IntNRTnum, 
chrProv, 
vchProduct1
INTO clean_account
FROM Dataset1


SELECT d1.*, d3.Income_amt
FROM clean_account AS d1
JOIN Dataset2 AS d2
	ON d1.Account# = d2.Account#
JOIN Dataset3 AS d3
	ON d2.CUST_ID = d3.CUST_ID


DECLARE @StartDate DATE = '20110901'
  , @EndDate DATE = '20111001'

SELECT  DATEADD(DAY, nbr - 1, @StartDate)
FROM    ( SELECT    ROW_NUMBER() OVER ( ORDER BY c.object_id ) AS Nbr
          FROM      sys.columns c
        ) nbrs
WHERE   nbr - 1 <= DATEDIFF(DAY, @StartDate, @EndDate)

--
WITH Dates AS (
        SELECT
         [Date] = CONVERT(DATE,'09/01/2011')
        UNION ALL SELECT
         [Date] = DATEADD(DAY, 1, [Date])
        FROM
         Dates
        WHERE
         Date < '10/10/2011'
) 
SELECT
 [Date]
FROM
 Dates
 --OPTION (MAXRECURSION 45)