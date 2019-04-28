use world;

#describe country;
#SELECT Name, continent from country;
delimiter ;

DROP FUNCTION IF EXISTS ren_continent;

delimiter //

ALTER TABLE country CHANGE Continent Continent enum('Asia','Europe','North America','Africa','Oceania','Antarctica','South America', "Americas", "Australia", "Southpole")DEFAULT NULL //

CREATE FUNCTION ren_continent(input varchar(52))
RETURNS ENUM('text') 
DETERMINISTIC
BEGIN
	IF input like "North America" THEN 
		UPDATE country
		SET continent = "Americas"
		WHERE continent LIKE "North America" or continent LIKE "South America";
    ELSEIF input like "Oceania"
		THEN UPDATE country
		SET continent = "Australia"
        WHERE continent = "Australia";
	ELSEIF input like "Antartica"
		THEN UPDATE country
		SET continent = "Southpole"
        WHERE continent = "Southpole";
	END IF;
RETURN country;
END //

Delimiter ;

SELECT ren_continent('NORTH AMERICA');
#SELECT continent FROM country;

#Describe country;

Select * from country;

Select DISTINCT continent
	FROM country;

SELECT  continent, max(population) as 'biggst_pop', name 
	FROM country
	WHERE population > 0
    GROUP BY continent
    Order by population DESC;

SELECT * from country
	where population = 1277558000;
    
SELECT * from country
	where Continent like 'Antartica';

SELECT * from country
	where Name like 'Argentina';

 
SELECT * FROM person
  where age = 22;

SET @MINAGE = min(age) FROM person;

SET @age = (SELECT min(age) FROM person); 
SELECT pn.personname, pn.age, cy.name, min(cy.population)
	FROM person pn
	INNER JOIN hasvisitedcity hy
	INNER JOIN city cy
	on pn.personID = hy.personID and hy.cityID = cy.ID
    WHERE pn.age = @age; 
    
Select * from hasvisitedcity
where personid = 3;

Select * from hasvisitedcity
where personid = 5;

Select * from person
where personname = 'Jane';

SELECT * from city
where ID = 23;
#119811
SELECT * from city
where ID = 2113;
#164880
SELECT * from city
where ID = 3793;
#8008278



Select * from city
where district like 'eastern cape' or district like 'western cape' or district like 'free state';
Select * from city
where district like ;
Select * from city
where district like ;



UPDATE city
    SET population = if(district='eastern cape', population+1000, population),
    population = if(district='free state', population+2000, population),
    population = if(district='western cape', population-10000, population);

SELECT * from country;    
SELECT name, indepyear from country
case
where indepyear=
case
;	

update ;
UPDATE country
SET col as 'DESC'
WHERE indepyear = null;;;


SELECT * ,
CASE
	WHEN indepyear=null then return 'N.A' as 'DESC'

END
FROM country;


delimiter //

CREATE FUNCTION run(input varchar(3))
RETURNS 
DETERMINISTIC
BEGIN 
 IF indepyear='null' then return 'N.A' as 'DESC'; 
END//
Delimiter ;
// ;

#https://stackoverflow.com/questions/26510998/if-else-statement-and-insert-a-new-column;

SELECT name, indepyear, IFNULL(indepyear, 'N/A') AS 'DESC',
CASE indepyear
	WHEN indepyear >= 2009 THEN 'NEW'  
	WHEN indepyear >2009 and >= 1970 THEN 'Modern'
	WHEN indepyear >1970 and >= 1919 THEN 'Early' 
	WHEN indepyear >1919 THEN 'Old'
END  AS 'DESC'
from country;