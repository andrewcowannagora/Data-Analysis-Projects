--Keep records from first table that do not appear in the second

SELECT Dataset1.Accountid, Dataset1.AssetClass
FROM Dataset1
LEFT JOIN Dataset2
	ON Dataset1.Accountid = Dataset2.Accountid
	WHERE Dataset2.Accountid IS NULL

