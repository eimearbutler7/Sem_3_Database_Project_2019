#EIMEAR BUTLER G00364802
#QUESTIONS 4.4 for Applied DataBases Module May 2019


##CONNECTION SET UP SECTION##

import pymysql 	#import the functionality to connect python to mysql

conn = None #set variable

def connect(): #establish function to connect to the mysql database
	global conn	
	conn = pymysql.connect(host="localhost",user="root", password="Rmprwq*5", db="world", cursorclass=pymysql.cursors.DictCursor)

import pymongo	#import the functionality to connect python to mongodb

myclient = None #set variable

def connect_m(): #establish function to connect to the mongo database
	myclient = pymongo.MongoClient()
	myclient.admin.command('ismaster')
	
#def mongo example():
#	mydb = myclient["projectbd"]
#	docs = mydb["docs"]
#	query = {'':''}
#	people = docs.find(query)
#	for p in people:
#		print(p)

##REFERENCE FUNCTIONS & GLOBAL VARIABLES SECTION##
import operator #import operator functionality 

def get_operator_fn(op): #define function to change a string paraeter into equivalent matheatical operator to enable other functions
    return {
        '>' : operator.gt,
        '<' : operator.lt,
        '=' : operator.eq,
        }[op]
		
country_codeg = [] #define global variables that will be referenced further on to enable mysql results (output) to be appended to these empty lists
country_nameg = []
co_nameg = [] 
co_popg = []

##DISPLAY MENU SECTION##

def display_menu():
	print("--------")
	print("World DB")
	print("--------")
	print("MENU")
	print("====")
	print("1- View 15 Cities")
	print("2- View Cities by Population")
	print("3- Add New City")
	print("4- Find Car by Engine Size")
	print("5- Add New Car")
	print("6- View Countries by Name")
	print("7- View Countries by Population")
	print("x- Exit Application") 
	
##MAIN FUNCTION SECTION##

def main():
	
	while True:
		display_menu() #while called, display the menu function as defined above
		choice = None		#ensure the "choice" variable is "none" to begin with and is reset each time before more choices are made, this shouldn't be an issue as choice is a local variable but as I am calling functions within functions I did have some trouble during testing, this fixed the bugs
		choice = input("Choice:") #accept choice input as a string, testing compliance of input performed below

		if choice == "1": #if statements direct from the display menu depending on the input
			print()
			print("<---------- View 15 Cities ---------->") #confirm choice
			print()
			view_city_15(15) #run function connected to this choice, details of associated action below
			print()
			del choice #REPEATED FOR ALL CHOICES: again choice is deleted after the function is run to ensure it is reset for the next time the function is called
			main() #REPEATED FOR ALL CHOICES: return to call main function again 
		
		if choice == "2":
			print()
			print("<---------- View Cities by Population ---------->")
			print()
			symbol = str(input("Enter < > or = :")) #accept input and ensure it is a string - non string will lead to function error
			pop = int(input("Enter Population:")) #accept input and ensure it is an integer - non string will lead to function error
			view_city_pop(symbol, pop)	#run function connected to this choice, details of associated action below
			print()
			del choice
			main()
		
		if choice == "3":
			print()
			print("<---------- Add New City ---------->")
			print()
			##NAME INPUT##
			name1 = str(input("Enter Name of City:")) #accept input and ensure it is a string
			country_name()
			if name1 in country_nameg:
				print("This city name already exists in the Database, please try again.") #if a duplicate exists, print error & return to main
				main() 
			if name1.isalpha() and len(name1) < 35: #test input to ensure it meets schema requirements before trying to update the DB #source: https://stackoverflow.com/questions/20890618/isalpha-python-function-wont-consider-spaces
					name2 = ('"' + name1 + '"') #add string quotes to allow mysql to accept the input request
			else: 
				print("Entries must be alphabetic and contain between 1 and 35 characters. Try again.") #if non-compliant, print error & return to main
				main() 
			##COUNTRY CODE INPUT##
			ccode1 = input("Enter Country Code for City:") 
			country_code() #Function to extract list of country codes from DB and make accessible within python program as global variable
			if ccode1 in country_codeg: #if statement test input to ensure it matches existing list of Codes before trying to update the DB
				ccode2 = ('"' + ccode1 + '"')		#if accepted, add string quotes to allow mysql to accept the input request		
			else:	
				print("***ERROR*** Country Code", ccode1," does not exist. Try again!") #if non-compliant, print error & return to main
				main()
			##DISTRICT INPUT##
			district1 = str(input("Enter District of City:"))  #accept input and ensure it is a string
			if district1.isalpha() and len(district1) < 20: #test input to ensure it meets schema requirements before trying to update the DB #source: https://stackoverflow.com/questions/20890618/isalpha-python-function-wont-consider-spaces
				district2 = ('"' + district1 + '"')  #add string quotes to allow mysql to accept the input request
			else: 
				print("Entries must be alphabetic and contain between 1 and 20 characters. Try again.") #if non-compliant, print error & return to main
				main()
			##POPULATION INPUT##
			population2 = int(input("Enter Population of City:")) #accept input and ensure it is an integer
			##FUNCTIONS##
			add_city(name2, ccode2, district2, population2) #run function connected to this choice, details of associated action below
			add_city_show(name2) #run additional function to then show the results of the first			
			print()
			del choice
			main()
		
		if choice == "4":
			print()
			print("=<--------- Find Car by Engine Size ---------->")
			print()
			find_car_enginesize()
			print()
			del choice
			main()
		
		if choice == "5":
			print()
			print("<---------- Add New Car ---------->")
			print()
			add_car()
			print()
			del choice
			main()
		
		if choice == "6":
			print()
			print("<---------- View Countries by Name ---------->")
			print()
			if co_nameg == []:  #if global variable is empty (note: it will be filled the first time this function is run and therefore this statement is only true the first timme the function is runused once)
				cname = str(input("Counry name Search:")) #accept input and ensure it is a string
				view_country_name(cname) #run function connected to this choice, details of associated action below
			
			else: #this will run every time except the first time to produce same result from output stored in global variable co_nameg
				print()
				print("-------------------------- LIST IS UNCHANGED ----------------------------")
				print() #the below code just provides the titles again and...
				print('{:>23.23}'.format("Name"), "｜", '{:>13.13}'.format("Continent"), "｜", '{:>8}'.format("Pop."),  "｜", '{:>25.25}'.format("Head of State"))
				print()     
				for row in co_nameg:    #...prints and formats the data again from the global variable co_nameg
					print('{:>23.23}'.format(row["Name"]), "｜", '{:>13.13}'.format(row["Continent"]), "｜", '{:>8}'.format(row["Population"]), "｜", '{:>25.25}'.format(row["HeadOfState"])) 
			print()
			del choice
			main()
		
		if choice == "7":
			print()
			print("<---------- View Countries by Population ---------->")
			print()
			if co_popg == []: 	#if global variable is empty (note: it will be filled the first time this function is run and therefore this statement is only true the first timme the function is runused once)
				csymbol = str(input("Enter < > or = :")) #accept input and ensure it is an string 
				cpop = int(input("Enter Population:")) #accept input and ensure it is an integer
				view_country_pop(csymbol,cpop) #run function connected to this choice, details of associated action below 
				
			else: #this will run every time except the first time to produce same result from output stored in global variable co_popg
				print()
				print("-------------------------- LIST IS UNCHANGED ----------------------------")
				print() #the below code just provides the titles again and...
				print('{:>4.4}'.format("Code"),'{:>23.23}'.format("Name"), "｜", '{:>13.13}'.format("Continent"), "｜", '{:>15}'.format("Population"))
				print() #...prints and formats the data again from the global variable co_popg
				for row in co_popg:
					print('{:>4.4}'.format(row["Code"]), '{:>23.23}'.format(row["Name"]), "｜", '{:>13.13}'.format(row["Continent"]), "｜", '{:>15}'.format(row["Population"])) 
				print('{:>4.4}'.format("Code"),'{:>23.23}'.format("Name"), "｜", '{:>13.13}'.format("Continent"), "｜", '{:>8}'.format("Pop."))
			print()
			del choice
			main()
				
		if choice == "x": #both large and small x cancels the program
			return	
		if choice == "X":
			return	
		
		if choice != "1" or "2" or "3"or "4"or "5"or "6"or "7"or"x"or"X": 	 #all other entries return the user to the display menu to try again
			print()
			print("***", choice, "is an invalid choice, please try again ***")
			print()
			del choice
			main()


##CORRESPONDING "ACTION" FUNCTIONS FOR EACH SELECTION##	

def view_city_15(s):
	if(not conn):	#REPEATED FOR ALL FUNCTIONS: if not connected to DB, connect
		connect();
	
	query = "SELECT * FROM city limit %s" #QUERY for mysql where s is preselected to limit the list results to 15
	
	with conn:
		cursor = conn.cursor() #REPEATED FOR ALL FUNCTIONS: activatecursor to execute query in mysql and retuern results as local variable
		cursor.execute(query, (s))
		y = cursor.fetchall()
		print()   #REPEATED FOR ALL FUNCTIONS: confirm update and print results in suitable format
		print("------------------------  UPDATED --------------------------") 
		print()
		print('{:>15}'.format("Name"), "｜", '{:>7}'.format("Co.Code"), "｜", '{:>20}'.format("District"), "｜", "Pop.")
		print()
		for row in y:
			print('{:>15}'.format(row["Name"]), "｜", '{:>7}'.format(row["CountryCode"]), "｜", '{:>20}'.format(row["District"]), "｜", row["Population"])
		

def view_city_pop(a, b):
	if(not conn):
		connect();
	
	query = "SELECT * FROM city WHERE Population %s %d ORDER BY Population desc" % (a,b) #QUERY for mysql where input is given by user for a&b
	
	try:
	
		with conn:
			cursor = conn.cursor()
			cursor.execute(query)
			y = cursor.fetchall()
			print()
			print("-------------------- OUTPUT ----------------------")
			print()
			print('{:>5}'.format("ID"), "｜", '{:>20.20}'.format("Name"), "｜", '{:>7}'.format("Co.Code"), "｜", '{:>20}'.format("District"), "｜", "Pop.")
			print()
			for row in y:
				print('{:>5}'.format(row["ID"]), "｜", '{:>20.20}'.format(row["Name"]), "｜", '{:>7}'.format(row["CountryCode"]), "｜", '{:>20}'.format(row["District"]), "｜", row["Population"])

	except pymysql.err.IntegrityError as e:  #REPEATED FOR ALL FUNCTIONS: included some established error exceptions to better format feedback to user
		print(e)
	except pymysql.err.ProgrammingError as e:
		print(e)
	except Exception as e:
		print(e)


def add_city(c, d, e, f):
	if(not conn):
		connect();
	          #QUERY for mysql where input is given by user for c, d, e & f
	query = "INSERT INTO city (Name, CountryCode, District, Population) VALUES (%s, %s, %s, %d);" % (c, d, e, f) 
	
	try:
		with conn:
			cursor = conn.cursor()
			cursor.execute(query)
			y = cursor.fetchall()
			print()  #where query is accepted the following confirmation is given 
			print("-------------------- DB UPDATED ----------------------")
			print()
	except: #where query fails, the following warning is given 
		print("This request was not accepted, please try again!")

def country_code(): #Inspired by: http://www.mysqltutorial.org/mysql-delete-duplicate-rows/
	if(not conn):
		connect();
	
	query = "SELECT CountryCode FROM city GROUP BY CountryCode;" #query run to get 1 list of CountryCodes from DB
	
	with conn:
		cursor = conn.cursor()
		cursor.execute(query) 
		y = cursor.fetchall()
		for row in y: #query results are then appended to global variable to store and use again
			country_codeg.append(row["CountryCode"]) #source: https://stackoverflow.com/questions/10195139/how-to-retrieve-sql-result-column-value-using-column-name-in-python
		
def country_name(): #same function run except for country name this time
	if(not conn):
		connect();
	
	query = "SELECT Name FROM city GROUP BY Name;"
	
	with conn:
		cursor = conn.cursor()
		cursor.execute(query)
		y = cursor.fetchall()
		for row in y:
			country_nameg.append(row["CountryCode"]) #source: https://stackoverflow.com/questions/10195139/how-to-retrieve-sql-result-column-value-using-column-name-in-python



def add_city_show(c):
	if(not conn):
		connect();
	
	query = "SELECT * FROM city WHERE Name LIKE %s" % (c) # query to show record for new entry is it has been accepted. 
	
	with conn:
		cursor = conn.cursor()
		rows_count = cursor.execute(query)
		rows_count
		y = cursor.fetchall()
		print()
		print("Records Affected:")
		print()
		print('{:>5}'.format("ID"), '{:>20}'.format("Name"), "｜", '{:>7}'.format("Co.Code"), "｜", '{:>20}'.format("District"), "｜", "Pop.")
		print()
		for row in y:
			print('{:>5}'.format(row["ID"]), '{:>20}'.format(row["Name"]), "｜", '{:>7}'.format(row["CountryCode"]), "｜", '{:>20}'.format(row["District"]), "｜", row["Population"])
			
	
##def find_car_enginesize

##def add_car():

def view_country_name(t):
	if(not conn):
		connect();
	
	query = "SELECT * FROM country WHERE Name LIKE %s%s%s" % ('"%',t,'%"') # query to search DB 
	
	try:
		with conn:
			cursor = conn.cursor()
			cursor.execute(query)
			co_name = cursor.fetchall()
			print()
			print("------------------------------ OUTPUT ----------------------")
			print()
			print('{:>23.23}'.format("Name"), "｜", '{:>13.13}'.format("Continent"), "｜", '{:>8}'.format("Pop."),  "｜", '{:>25.25}'.format("Head of State"))
			print()
			for row in co_name:
				print('{:>23.23}'.format(row["Name"]), "｜", '{:>13.13}'.format(row["Continent"]), "｜", '{:>8}'.format(row["Population"]), "｜", '{:>25.25}'.format(row["HeadOfState"])) 
			for row in co_name: #again results added to global variable to ensure they can be retrieved within the python program again
				co_nameg.append(row)

	except pymysql.err.IntegrityError as e:
		print(e)
	except pymysql.err.ProgrammingError as e:
		print(e)
	except Exception as e:
		print(e)


			
def view_country_pop(a, b): #same approach as per function view_country_name
	if(not conn):
		connect();
	
	query = "SELECT * FROM country WHERE Population %s %d ORDER BY Population desc" % (a,b) 
	
	try:
		with conn:
			cursor = conn.cursor()
			cursor.execute(query)
			co_pop = cursor.fetchall()
			print()
			print("------------------------------ OUTPUT ----------------------")
			print()
			print('{:>4.4}'.format("Code"),'{:>23.23}'.format("Name"), "｜", '{:>13.13}'.format("Continent"), "｜", '{:>15}'.format("Population"))
			print()
			for row in co_pop:
				print('{:>4.4}'.format(row["Code"]), '{:>23.23}'.format(row["Name"]), "｜", '{:>13.13}'.format(row["Continent"]), "｜", '{:>15}'.format(row["Population"])) 
			for row in co_pop:
				co_popg.append(row)

	except pymysql.err.IntegrityError as e:
		print(e)
	except pymysql.err.ProgrammingError as e:
		print(e)
	except Exception as e:
		print(e)
				
	


##PYTHON CODE TO ACTIVATE THE PROGRAM WHEN RUN IN COMMAND LINE##
if __name__ == "__main__": 
    main()