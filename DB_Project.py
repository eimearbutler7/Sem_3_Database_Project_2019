##CONNECTION SET UP SECTION##

import pymysql

conn = None

def connect():
	global conn
	conn = pymysql.connect(host="localhost",user="root", password="Rmprwq*5", db="world", cursorclass=pymysql.cursors.DictCursor)

##REFERENCE FUNCTIONS SECTION##
import operator 

def get_operator_fn(op):
    return {
        '>' : operator.gt,
        '<' : operator.lt,
        '=' : operator.eq,
        }[op]
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
		display_menu()
		choice = None
		choice = input("Choice:")

		if choice == "1":
			print()
			print("<---------- View 15 Cities ---------->")
			print()
			view_city_15(15)
			print()
			del choice
			main()
		
		if choice == "2":
			print()
			print("<---------- View Cities by Population ---------->")
			print()
			symbol = str(input("Enter < > or = :"))
			pop = input("Enter Population:")
			pop = int(pop)
			view_city_pop(symbol, pop)	
			print()
			del choice
			main()
		
		if choice == "3":
			print()
			print("<---------- Add New City ---------->")
			print()
			name1 = str(input("Enter Name of City:"))
			name = ('"' + name1 + '"')
			ccode1 = str(input("Enter Country Code for City:"))
			ccode = ('"' + ccode1 + '"')
#opportunity to check if CCode is compliant
			district1 = str(input("Enter District of City:"))
			district = ('"' + district1 + '"')
			population = int(input("Enter Population of City:"))
			add_city(name, ccode, district, population)
			add_city_show(name)
			
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
			if co_nameg == []:
				cname = input("Counry name Search:")
				co_name = view_country_name(cname)
				co_name
			else:
				print()
				print("-------------------------- LIST IS UNCHANGED ----------------------------")
				print()
				print('{:>23.23}'.format("Name"), "｜", '{:>13.13}'.format("Continent"), "｜", '{:>8}'.format("Pop."),  "｜", '{:>25.25}'.format("Head of State"))
				print()
				for row in co_nameg:
					print('{:>23.23}'.format(row["Name"]), "｜", '{:>13.13}'.format(row["Continent"]), "｜", '{:>8}'.format(row["Population"]), "｜", '{:>25.25}'.format(row["HeadOfState"])) 
			print()
			del choice
			main()
		
		if choice == "7":
			print()
			print("<---------- View Countries by Population ---------->")
			print()
			if co_popg == []:
				csymbol = str(input("Enter < > or = :"))
				cpop = int(input("Enter Population:"))
				co_pop = view_country_pop(csymbol,cpop)
				co_pop
			else:
				print()
				print("-------------------------- LIST IS UNCHANGED ----------------------------")
				print()
				print('{:>4.4}'.format("Code"),'{:>23.23}'.format("Name"), "｜", '{:>13.13}'.format("Continent"), "｜", '{:>15}'.format("Population"))
				print()
				for row in co_popg:
					print('{:>4.4}'.format(row["Code"]), '{:>23.23}'.format(row["Name"]), "｜", '{:>13.13}'.format(row["Continent"]), "｜", '{:>15}'.format(row["Population"])) 
				print('{:>4.4}'.format("Code"),'{:>23.23}'.format("Name"), "｜", '{:>13.13}'.format("Continent"), "｜", '{:>8}'.format("Pop."))
			print()
			del choice
			main()
				
		if choice == "x":
			return	
		if choice == "X":
			return	
		
		if choice != "1" or "2" or "3"or "4"or "5"or "6"or "7"or"x"or"X": 	
			print()
			print("***", choice, "is an invalid choice, please try again ***")
			print()
			del choice
			main()


##CORRESPONDING "ACTION" FUNCTIONS FOR EACH SELECTION##	

def view_city_15(s):
	if(not conn):
		connect();
	
	query = "SELECT * FROM city limit %s"
	
	with conn:
		cursor = conn.cursor()
		cursor.execute(query, (s))
		y = cursor.fetchall()
		print()
		print("------------------------  UPDATED --------------------------")
		print()
		print('{:>15}'.format("Name"), "｜", '{:>7}'.format("Co.Code"), "｜", '{:>20}'.format("District"), "｜", "Pop.")
		print()
		for row in y:
			print('{:>15}'.format(row["Name"]), "｜", '{:>7}'.format(row["CountryCode"]), "｜", '{:>20}'.format(row["District"]), "｜", row["Population"])
		

def view_city_pop(a, b):
	if(not conn):
		connect();
	
	query = "SELECT * FROM city WHERE Population %s %d ORDER BY Population desc" % (a,b) 
	
	try:
	
		with conn:
			cursor = conn.cursor()
			cursor.execute(query)
			y = cursor.fetchall()
			print()
			print("-------------------- OUTPUT ----------------------")
			print()
			print('{:>5}'.format("ID"), '{:>20.20}'.format("Name"), "｜", '{:>7}'.format("Co.Code"), "｜", '{:>20}'.format("District"), "｜", "Pop.")
			print()
			for row in y:
				print('{:>5}'.format(row["ID"]), '{:>20.20}'.format(row["Name"]), "｜", '{:>7}'.format(row["CountryCode"]), "｜", '{:>20}'.format(row["District"]), "｜", row["Population"])

	except pymysql.err.IntegrityError as e:
		print(e)
	except pymysql.err.ProgrammingError as e:
		print(e)
	except Exception as e:
		print(e)


def add_city(c, d, e, f):
	if(not conn):
		connect();
	
	query = "INSERT INTO city (Name, CountryCode, District, Population) VALUES (%s, %s, %s, %d);" % (c, d, e, f) 
	
	##if name not in db vs if it is
	try:
		with conn:
			cursor = conn.cursor()
			cursor.execute(query)
			y = cursor.fetchall()
			print()
			print("-------------------- DB UPDATED ----------------------")
			print()
	except:
		print("This request was not accepted, please try again!")
		
def add_city_show(c):
	if(not conn):
		connect();
	
	query = "SELECT * FROM city WHERE Name LIKE %s" % (c) 
	
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
	
	query = "SELECT * FROM country WHERE Name LIKE %s%s%s" % ('"%',t,'%"') 
	
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
			for row in co_name:
				co_nameg.append(row)

	except pymysql.err.IntegrityError as e:
		print(e)
	except pymysql.err.ProgrammingError as e:
		print(e)
	except Exception as e:
		print(e)


			
def view_country_pop(a, b):
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