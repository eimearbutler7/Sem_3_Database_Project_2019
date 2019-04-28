# 4.1.1 ##### 

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

delimiter ; 
CALL get_ppl_visited_country('bra');

delimiter ;

# 4.1.2 #### FINISH QUESTION 4.2 to add new column....??


DROP FUNCTION IF EXISTS ren_continent;


delimiter //


CREATE FUNCTION ren_continent(input varchar(52))
RETURNS varchar(52)
DETERMINISTIC
BEGIN
ALTER TABLE country CHANGE Continent Continent enum('Asia','Europe','North America','Africa','Oceania','Antarctica','South America', "Americas", "Australia", "Southpole")DEFAULT NULL;

	IF input like "North America" or "South America" THEN 
		RETURN "Americas";
    ELSEIF input like "Oceania"
		THEN RETURN "Australia";
	ELSEIF input like "Antartica"
		THEN RETURN "Southpole";
	END IF;
END
//

Delimiter ;

SELECT ren_continent('NORTH AMERICA');

# 4.1.3 #####FIX NAME COLUMN LATER

SELECT  continent, max(population) as 'biggst_pop', name 
	FROM country
	WHERE population > 0
    GROUP BY continent
    Order by population DESC;
    
# 4.1.4 ######

SELECT pn.personname, pn.age, cy.name, min(cy.population) as min_pop
	FROM person pn
	INNER JOIN hasvisitedcity hy
	INNER JOIN city cy
	on pn.personID = hy.personID and hy.cityID = cy.ID
    WHERE pn.age = (SELECT min(age) FROM person); 
    
    
# 4.1.5 ##########     

UPDATE city
    SET population = if(district='eastern cape', population+1000, population),
    population = if(district='free state', population+2000, population),
    population = if(district='western cape', population-10000, population);

Select * from city
where district like 'eastern cape' or district like 'western cape' or district like 'free state';


# 4.1.6 ##########UNSURE WHAT THE CONFLICT IS#   ;


SELECT name, indepyear, IFNULL(indepyear, 'N/A') AS 'DESC', 
CASE indepyear
	WHEN indepyear >= 2009 THEN 'NEW'  
	WHEN indepyear >2009 and >= 1970 THEN 'Modern'
	WHEN indepyear >1970 and >= 1919 THEN 'Early' 
	ELSE 'Old'
END  AS 'DESC'
from country;

#https://stackoverflow.com/questions/26510998/if-else-statement-and-insert-a-new-column;
