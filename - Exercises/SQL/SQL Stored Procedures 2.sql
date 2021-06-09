-- Create Sample Data

Create Table People 
(id int, 
FirstName varchar(50), 
LastName varchar(50), 
)

Insert into People VALUES
(1, 'Tim', 'Corey'),
(2, 'Jon', 'Corey'),
(3, 'Chris', 'Corey'),
(4, 'Bill', 'Smith'),
(5, 'Jane', 'Smith'),
(6, 'Jamie', 'Smith'),
(7, 'Maggy', 'Corey'),
(8, 'Sue', 'Storm')

SELECT * FROM People

-- Create Procedure

CREATE PROCEDURE dbo.spPeople_GetAll
AS
BEGIN
	SELECT id, FirstName, LastName
	FROM dbo.People
END

EXEC dbo.spPeople_GetAll


-- Alter Procedure to set no count on

ALTER PROCEDURE dbo.spPeople_GetAll
AS
BEGIN
	SET NOCOUNT ON;
	SELECT id, FirstName, LastName
	FROM dbo.People
END

EXEC dbo.spPeople_GetAll


-- Add a variable/Parameter

CREATE PROCEDURE dbo.spPeople_GetByLastName
	@Lastname nvarchar(50)
AS
BEGIN
	SELECT id, FirstName, LastName
	FROM dbo.People
	WHERE LastName = @LastName;
END

EXEC dbo.spPeople_GetByLastName @LastName = 'Corey'


-- Alter to add a second variable/Parameter
ALTER PROCEDURE dbo.spPeople_GetByLastName
	@LastName nvarchar(50),
	@FirstName nvarchar(50)
AS
BEGIN
	SELECT id, FirstName, LastName
	FROM dbo.People
	WHERE LastName = @LastName AND FirstName = @FirstName;
END


EXEC dbo.spPeople_GetByLastName @LastName = 'Corey', @FirstName = 'Tim'