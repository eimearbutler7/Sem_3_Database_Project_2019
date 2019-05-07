#EIMEAR BUTLER G00364802
#QUESTIONS 4.1 for Applied DataBases Module May 2019



use world;

### 4.1.1 ###

DROP PROCEDURE IF EXISTS get_ppl_visited_country;

DELIMITER //
CREATE PROCEDURE get_ppl_visited_country(country_name varchar(52))
DETERMINISTIC
BEGIN
    SET @country_name = concat("%", country_name, "%");
    SELECT pn.personID, pn.personname, cy.Name, hy.dateArrived, co.Name
	FROM person pn
	INNER JOIN hasvisitedcity hy
	INNER JOIN city cy
	INNER JOIN country co 
	on pn.personID = hy.personID and hy.cityID = cy.ID and cy.CountryCode = co.Code
    
	WHERE co.Name LIKE @country_name;
	
END //

DELIMITER ; 
CALL get_ppl_visited_country('bra');

DELIMITER ;

### 4.1.2 ### FIRST INTERPRETATION (SIMPLE ANSWER) ###
#2 answers given as the question asks for a function however a function cannot modify a table to add a new column so a second procedure also added below to perform this

DROP FUNCTION IF EXISTS ren_continent;
DELIMITER //

CREATE FUNCTION ren_continent(input varchar(52))
RETURNS varchar(52)
DETERMINISTIC
BEGIN

	IF input LIKE "North America" or "South America" THEN 
		RETURN "Americas";
    ELSEIF input LIKE "Oceania"
		THEN RETURN "Australia";
	ELSEIF input LIKE "Antartica"
		THEN RETURN "Southpole";
	END IF;
END
//

DELIMITER ;
SELECT ren_continent('NORTH AMERICA');

### SECOND INTERPRETATION - PROCEDURE TO MODIFY TABLE ###

DROP PROCEDURE IF EXISTS ren_continent2;
DELIMITER //

CREATE PROCEDURE ren_continent2(input varchar(52))
DETERMINISTIC
BEGIN
ALTER TABLE country CHANGE Continent Continent enum('Asia','Europe','North America','Africa','Oceania','Antarctica','South America', "Americas", "Australia", "Southpole")DEFAULT NULL; #Source:https://dev.mysql.com/doc/refman/8.0/en/enum.html
ALTER TABLE country ADD COLUMN new_con_name VARCHAR(20) AFTER Continent; #source: http://www.mysqltutorial.org/mysql-add-column/

	IF input LIKE "North America" THEN
	UPDATE country SET new_con_name = "Americas" where continent like "North America";
	ELSEIF input LIKE "South America" THEN
	UPDATE country SET new_con_name = "Americas" where continent like "South America";	
    ELSEIF input LIKE "Oceania" THEN
    UPDATE country SET new_con_name = "Australia" where continent like "Oceania";
	ELSEIF input LIKE "Antartica" THEN
	UPDATE country SET new_con_name = "Southpole" where continent like "Antartica";
    END IF;
    SELECT * from Country;
END
//
DELIMITER ;

CALL ren_continent2('NORTH AMERICA');

### 4.1.3 ###

SELECT name, continent, population from country 
where population in (select max(population) as 'biggest_pop' from country WHERE population > 0 group by continent)
order by population desc;

    
### 4.1.4 ####

SELECT pn.personname, pn.age, cy.name, MIN(cy.population) AS min_pop
	FROM person pn
	INNER JOIN hasvisitedcity hy
	INNER JOIN city cy
	ON pn.personID = hy.personID AND hy.cityID = cy.ID
    WHERE pn.age = (SELECT MIN(age) FROM person); 
    
### 4.1.5 ###

UPDATE city
    SET population = IF(district='eastern cape', population+1000, population),
    population = IF(district='free state', population+2000, population),
    population = IF(district='western cape', population-10000, population);

SELECT * FROM city
WHERE district LIKE 'eastern cape' OR district LIKE 'western cape' OR district LIKE 'free state';


### 4.1.6 ### 


SELECT name, indepyear,
CASE 
    WHEN indepyear is Null THEN "N/A"
    WHEN indepyear between 2009 and 2019 and population <=100000000 THEN concat("New ", GovernmentForm) 
	WHEN indepyear between 2009 and 2019 and population >100000000 THEN concat("New Large ", GovernmentForm) 
    WHEN indepyear between 1970 and 2009 and population <=100000000 THEN concat("Modern ", GovernmentForm) 
	WHEN indepyear between 1970 and 2009 and population >100000000 THEN concat("Modern Large ", GovernmentForm) 
    WHEN indepyear between 1919 and 1970 and population <=100000000 THEN concat("Early ", GovernmentForm)
	WHEN indepyear between 1919 and 1970 and population >100000000 THEN concat("Early Large ", GovernmentForm) 
    WHEN indepyear < 1919 and population <=100000000 THEN concat("Old ", GovernmentForm)
    WHEN indepyear < 1919 and population >100000000 THEN concat("Old Large ", GovernmentForm) 
   
END  AS 'Desc'
from country;