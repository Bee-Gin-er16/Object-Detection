# multiline comments = ctrl + /

# GET DATE AND TIME
# ---------------------------------------->
# import datetime
# now = datetime.datetime.now()
# print("Current date and time: ")
# print(now.strftime("%Y-%m-%d %H:%M:%S"))
# ---------------------------------------->

# GET AREA OF A CIRCLE USING GIVEN RADIUS
# ---------------------------------------->
# from math import pi
# r = float(input("Input the radius of the circle:"))
# print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))
# ---------------------------------------->

# GET AND REVERSE FIRST NAME AND LAST NAME
# ---------------------------------------->
# first = str(input("Enter first name: "))
# last = str(input("Enter last name: "))
# full_name = last+ " " +first
# print(full_name)
# ---------------------------------------->

# ACCEPT A SEQUENCE OF COMMA-SEPARATED NUMBERS & GENERATE LIST & TUPLES
# ---------------------------------------->
# nums = "3,5,7,23" # example string
# li = nums.split(',')
# tp = tuple(li)
# print(li)
# print(tp)
# ---------------------------------------->

# ACCEPT A FILENAME FROM USER & PRINT IT'S EXTENSION
# ---------------------------------------->
# filename = input("Input the Filename: ")
# f_extns = filename.split(".")
# print ("The extension of the file is : " + repr(f_extns[-1]))
# ---------------------------------------->

# DISPLAY FIRST TAND LAST COLORS FROM FOLLOWING ARRAY
# ---------------------------------------->
# color_list = ["Red","Green","White" ,"Black"]
# print("First color is: ", color_list[0])
# print("Last color is: ", color_list[-1])
# ---------------------------------------->

# DISPLAY EXAM SCHEDULE
# ---------------------------------------->
# exam_st_date = (11, 12, 2014)
# print( "The examination will start from : %i / %i / %i"%exam_st_date)
# ---------------------------------------->

# ACCEPT INTEGER AND GET SUM OF N+NN+NNN
# ---------------------------------------->
# a = int(input("Input an integer : "))
# n1 = int( "%s" % a )
# n2 = int( "%s%s" % (a,a) )
# n3 = int( "%s%s%s" % (a,a,a) )
# print (n1+n2+n3)
# ---------------------------------------->

# PRINT DOCUMENTS OF PYTHON BUILT-IN FXN
# ---------------------------------------->
# print(abs.__doc__) # absolute as a example fxn
# ---------------------------------------->

# PRINT CALENDAR OF GIVEN MONTH AND YEAR
# ---------------------------------------->
# import calendar
# y = int(input("Input the year : "))
# m = int(input("Input the month : "))
# print(calendar.month(y, m))
# ---------------------------------------->

# CALCULATE DAYS BETWEEN TWO DATES
# ---------------------------------------->
# from datetime import date
# f_date = date(2014, 7, 2)
# l_date = date(2014, 7, 11)
# delta = l_date - f_date
# print(delta.days)
# ---------------------------------------->

# VOLUME OF A SPHERE
# ---------------------------------------->
# pi = 3.1415926535897931
# r= 6.0
# V= 4.0/3.0*pi* r**3
# print('The volume of the sphere is: ',V)
# ---------------------------------------->

# DIFF BETWEEN GIVEN NUMBER & 17. IF N>17, RETURN DOUBLE ABSOLUTE DIFFERENCE
# ---------------------------------------->
# def difference(n):
#     if n <= 17:
#         return 17 - n
#     else:
#         return (n - 17) * 2 

# print(difference(22))
# print(difference(14))
# ---------------------------------------->

# TEST WHETHER NUM IS WITHIN 100, 1000, 2000
# ---------------------------------------->
# def near_thousand(n):
#       return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
# print(near_thousand(1000))
# print(near_thousand(900))
# print(near_thousand(800))   
# print(near_thousand(2200))
# ---------------------------------------->

# SUM OF 3 GIVEN NOS.IF VALUES ARE EQUAL, RETURN 3 TIMES OF THEIR SUM
# ---------------------------------------->
# def sum_thrice(x, y, z):

#      sum = x + y + z
  
#      if x == y == z:
#       sum = sum * 3
#      return sum

# print(sum_thrice(1, 2, 3))
# print(sum_thrice(3, 3, 3))
# ---------------------------------------->

# GET A NEW STRING FROM A GIVEN STRING WHERE 'IS' IS ADDED AT BEGGINING
# IF STRING STARTS WITH 'IS', PRINT AS IS
# ---------------------------------------->
# def new_string(str):
#   if len(str) >= 2 and str[:2] == "Is":
#     return str
#   return "Is" + str

# print(new_string("Array"))
# print(new_string("IsEmpty"))
# ---------------------------------------->

# GET A STRING WHICH IS N(NOT NEGATIVE INTEGER) COPIES OF GIVEN STRING
# ---------------------------------------->
# def larger_string(str, n):
#    result = ""
#    for i in range(n):
#       result = result + str
#    return result

# print(larger_string('abc', 2))
# print(larger_string('.py', 3))
# ---------------------------------------->