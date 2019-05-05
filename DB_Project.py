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

	
##DISPLAY MENU SECTION##

def display_menu():
	print("--------")
	print("World DB")
	print("--------")
	print("MENU")
	print("====")
	print("1- View 15 Cities ")
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
			view_city_15(15)
			print()
			del choice
			main()
		if choice == "2":
			symbol = str(input("Enter < > or = :"))
#			if symbol == "<":
#				pass
#			if symbol == ">":
#				pass
#			if symbol == "=":
#				pass
#			else:
#				print("You entered", symbol, "***Only < > or = permitted, please enter again:***")
#				main()
			
			pop = input("Enter Population:")
			
#			if pop == int(pop):
			pop = int(pop)
			view_city_pop(symbol, pop)	
#			else:
#				print("***only integers are permitted, please enter again:***")
#				pop 			
			
			print()
			del choice
			main()
		if choice == "3":
			name = input("Enter Name of City:")
			ccode = input("Enter Country Code for City:")
			district = input("Enter District of City:")
			population = int(input("Enter Population of City:"))
#		if population == int(population):
#			population = int(population)
			
			add_city(name, ccode, district, population)
			
			
			print()
			del choice
			main()
		if choice == "4":
			find_car_enginesize()
			print()
			del choice
			main()
		if choice == "5":
			add_car()
			print()
			del choice
			main()
		if choice == "6":
			view_country_name()
			print()
			del choice
			main()
		if choice == "7":
			view_country_pop()
			print()
			del choice
			main()
		if choice == "x":
			return	
		if choice == "X":
			return	
		if choice != "1" or "2" or "3"or "4"or "5"or "6"or "7"or"x"or"X": 	
			print()
			print("***", choice, "is an invalid choice, try again ***")
			print()
			del choice
			main()

##ACTION	
def view_city_15(s):
	if(not conn):
		connect();
	
	query = "SELECT * FROM city limit %s"
	
	with conn:
		cursor = conn.cursor()
		cursor.execute(query, (s))
		y = cursor.fetchall()
		print()
		print("------------------------ OUTPUT --------------------------")
		for row in y:
			print('{:>15}'.format(row["Name"]), "｜", row["CountryCode"], "｜", '{:>15}'.format(row["District"]), "｜", row["Population"])

		

def view_city_pop(a, b):
	if(not conn):
		connect();
	
	query = "SELECT * FROM city WHERE Population %s %d" % (a,b) 
	
	with conn:
		cursor = conn.cursor()
		cursor.execute(query)
		y = cursor.fetchall()
		print()
		print("-------------------- OUTPUT ----------------------")
		for row in y:
			print('{:>5}'.format(row["ID"]), '{:>20}'.format(row["Name"]), "｜", row["CountryCode"], "｜", '{:>20}'.format(row["District"]), "｜", row["Population"])
	

def add_city(c, d, e, f):
	if(not conn):
		connect();
	
	query = "INSERT INTO City (Name, CountryCode, District, Population) VALUES (%s, %s, %s, %d)" % (c, d, e, f) 
	
	with conn:
		cursor = conn.cursor()
		cursor.execute(query)
		y = cursor.fetchall()
		print()
		print("-------------------- OUTPUT ----------------------")
		for row in y:
			print('{:>5}'.format(row["ID"]), '{:>20}'.format(row["Name"]), "｜", row["CountryCode"], "｜", '{:>20}'.format(row["District"]), "｜", row["Population"])
	
	
##def find_car_enginesize

##def add_car():
	
##def view_country_name():
	
##def view_country_pop():
	
	



if __name__ == "__main__": 
    main()