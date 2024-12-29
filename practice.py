#PYTHON PRACTICE CODE:

# name = "Sujal saraswat"     (we can commnt out in python using # and ''')
# age = 20
# hobby = "coding,watching"
# address = "Berasia, (Bhopal)"
# print("name:",name)
# print("Age:",age)
# print("Hobby:",hobby)
# print("Address:",address)



# print(5*2)
# print(2+3)
# print(4%2)
# print(2-3)
# print(34/17)
# print(9**3)



#TO FIND SOMETHING IN A STRING WE CAN ALSO US 'in' OPERATOR:
#name = "sujal saraswat"
#print('w' in name)



'''HOW TO TAKE INPUT FROM THE USER:'''
# name = input("PLEASE ENTER YOUR NAME:")
# print(name)
# age = int(input("PLEASE ENTER YOUR AGE:"))
# print(age)
# email = input("PLEASE ENTER YOUR MAIL ID:")
# print(email)
# roll_number = int(input("PLEASE ENTER YOUR ENROLLMENT NUMBER:"))
# print(roll_number)



#PROGRAM TO ADD TWO NUMBERS:
# a = int(input("PLEASE ENTER YOUR FIRST NUMBER:"))
# b = int(input("PLEASE ENTER YOUR SECOND NUMBER:"))
# c = a + b
# print("Your sum is:",c)




# name = input("PLEASE ENTER YOUR NAME:")
# surName = input("PLEASE ENTER YOUR SURNAME:")
# fullName = name +" "+surName
# print("YOUR FULLNAME IS:",fullName)



# a = int(input("PLEASE ENTER YOUR FIRST VALUE:"))
# b = int(input("PLEASE ENTER YOUR SECOND VALUE:"))
# c = a/b
# print("YOUR DIVISION IS:",c)




# a = input("What is your name? , please enter here:")
# print("Hello, I am",a)
# b = input("Please enter your age here:")
# print("I am",b,"years old")
# c = input("Where do you study?")
# print("I'm studying in",c,"and its a very nice institute!")
# d = input("What degree you are persuing from there?")
# print("I am persuing",d,"in computer science and engineering!")
# e = input("Where do you live?")
# print("I lives in",e)




# a = float(input("Please enter first value:"))
# b = float(input("Please enter second value:"))
# c = a / b
# print("Your answer is:",c)



#name = "sujal saraswat"
#print(name.upper()) '''To convert string to uppercase'''
#print(name.lower()) '''to convert string to lower case'''
#print(len(name))    '''to calculate length of string'''
#print(name.find('w')) '''to find something in string'''
#print(name.replace('sujal','adi'))  '''to replace something in string'''





# age = int(input("Please eneter your age: "));
# print("Your age is",age);
# if age>=18:
#     print("You can vote!")
# else:
#     print("Sorry, you can't vote!")





# age = int(input("Please enter your age:"))
# if age<=5:
#     print("You are a very small child💕");
# elif age<10:
#     print("You are a small child!");
# elif age<15:
#     print("Your are a teenagerr!");
# elif age<=17:
#     print("You are going to vote!!!!")
# elif age<60:
#     print("You can vote!");
# else:
#     print("you are a senior citizen!");




'''TO MAKE A CALCULATOR:'''
# a = int(input('Please enter the first value:'));
# operator = input("Please enter the operation you want to perform +,-,/,*,%,**:");
# b = int(input("Please enter the second value:"));

# if operator=='+':
#     print("The sum between both the numbers",a , "and" , b, "is:");
#     print(a+b);
# elif operator == "-":
#     print("The subtraction between both the numbers",a,"and",b,"is:");
#     print(b-a);
# elif operator == "/":
#     print("The division between both the numbers",a,"and",b,"is:");
#     print(a/b);
# elif operator == "*":
#     print("The product of both the numbers",a,"and",b,"is:");
#     print(a*b);
# elif operator == "%":
#     print("The remainder of both the numbers",a, "and",b,"is:");
#     print(a%b);
# elif operator == "**":
#     print("The answer of both the values",a, "and",b,"is:");
#     print(a**b);
# else:
#     print("Error, no operation performed!");




# a = range(100)
# print(a)


'''they are module functions ans they provide us special modules in python.'''
# import math
# print(dir(math))


'''to import square root function from amth module:'''
# from math import sqrt
# print(sqrt(256))


'''to import all the functions from math module:'''
# from math import *
# print(sqrt(225))



'''HOW TO WRITE FUNCTIONS IN PYTHON:'''   #def=definition of function!
# def sum():
#     a = 23;
#     b = 23;
#     c = a + b;
#     print(c);
# sum();



# def minus(a,b):
#     print("Your sum is:",a+b)
# minus(23,23);



# def sum():
#     a = int(input("enter the first value:"))
#     b = int(input("enter the second value:"))
#     c = a+b
#     print("Your answer is:",c)
# sum()




# print(12)
# print(50,end=" ")  '''end is used to print 2nd and 3rd statement in sma line'''
# print(100)




# a = input("PLEASE ENTER YOUR NAME:")
# b = input("PLEASE ENTER YOUR EMAIL:")
# c = int(input("PLEASE ENTER YOUR MOBILE NUMBER:"))
# d = input("Please enter the name of your college:")
# e = input("Please enter the course you are persuing:")
# print("Your name is:",a.upper())
# print("Your e-mail is:",b)
# print("Your mobile number is:",c)
# print("The name of my college is:",d.upper())
# print("The name of my course is:",e.upper())




'''string slicing and list slicing are defined as the type of technique of extracting elements from a string or a list by giving index numbers and in this end index is not included. exa- [1,4]'''



'''Lists in python:'''
# marks = ("karan",34,13,"bhopal")
# print(marks)
# student = ["karan sharma",90.2,19,"bhopal"]
# print(student)
# student = ["karan",67,90,"sujal"]
# print(student[2])

'''string slicing'''
# marks = [34,67,89,90,98,87,65]
# print(marks[1:3])

# student = ["sujal saraswat",97,20,"bhopal","jai narain college of technology"]
# print(student[1:3])



'''lists and tuples are same but the main difference is that lists are mutable(changes can be made in elements of list after making it) while tuples are immutable(no changes can be made in elements of tuple after making it)'''




# a = "sujal saraswat"
# b = "My age is 20"
# c = "I am currently persuing my degree from jai narain college of technology"
# d = "I want to be a software engineer"
# print(a,"\n",b,"\n",c,"\n",d)



# a = int(input("Please enter the first number:"))
# op = input("Please enter the operation to perform +,-,/,*,%,**,//:")
# c = int(input("Please enter the second number:"))
# d = a + c
# e = a - c
# f = a / c
# g = a * c
# h = a % c
# i = a // c
# j = a ** c
# if op == "+":
#     print("The sum of both the values is:",d)
# elif op == "-":
#     print("The difference between both the numbers is:",e)    
# elif op == "/":
#     print("The division between both the numbers is:",f)
# elif op == "*":
#     print("The product of both the numbers is:",g)
# elif op == "%":
#     print("The remainder of both the product is:",h)
# elif op == "//":
#     print("The double divide is:",i)
# else:
#     print("The power of a is:",j)


   

# def details():
#     a = int(input("Pleae enter your phone number:"))
#     b = input("Please enter your name:")
#     c = int(input("Please enter your adhaar number:"))
#     print(a)
#     print(b)
#     print(c)
# details()




# a = ["sujal",89,90,91,"virat",101,"@"]     """list"""
# b = (56,6777,67.6,"sujal","amijetomar",90)   """tuple"""
# a[2] = "rohit"
# print(a)
# print(type(a))
# print(b)
# print(type(b))



# a = int(input())
# b = int(input())
# def sum(a,b):
#     print(a+b)
# sum(a,b)



# city = ["Bhopal","bombay","delhi","gurgaon","bengaluru","pune","noida"]
# fruits = ["banana","apple","watermelon","papaya","grapes"]

# def lists(list):
#     print(list)
#     print(len(list))
#     print(type(list))
#     print(city[2],end=" ")
#     print(city[3],end=" ")
#     print(fruits[0],end=" ")
#     print(fruits[1],end=" ")
#     print(fruits[2])

# lists(city)
# lists(fruits)



# hero = {
#     "ironman", fff
#     "superman",
#     "batman",
#     "spiderman",
#     "hulk"
# }
# print(hero)



'''usd to inr converter'''
# usd = int(input("Please enter the money in USD:"))
# inr = 84.95
# res = usd*inr
# print("your total expenditure in indan rupees is:",res,"Rs.")



'''CURRENCY CONVERTER'''
# USD = 84.95
# euro = 88.35
# yen = 0.54
# argentinePeso = 0.083
# swissFranc = 94.85
# gbp = 106.83
# australianDollar = 52.97

# val = int(input("Please enter the amount:"))
# curr = input("Please choose the currency: USD,euro,yen,argentinePeso,swissFranc,gbp,australianDollar")

# if curr == USD:
#     print("The value of USD to INR is:",val*USD)
# elif curr == euro:
#     print("The value of EURO to INR is:",val*euro)
# elif curr == yen:
#     print("The value of JAPANESE YEN to INR is:",val*yen)
# elif curr == argentinePeso:
#     print("The value of argentinePeso to INR is:",val*argentinePeso)
# elif curr == swissFranc:
#     print("The value of swissFranc to INR is:",val*swissFranc)
# elif curr == gbp:
#     print("The value of GBP to INR is:",val*gbp)
# elif curr == australianDollar:
#     print("The value of australianDollar to INR is:",val*australianDollar)


#print "Hello" infintely:
#while True:
#print("Hello")



# while Loop
# i = 1             '''Initialisation'''
# while i<=10:      '''Termination'''
#     print("Hellojii")
#     i = i+1       '''Updation'''



# fn = ["Sujal","saraswat","raj",90,98,87,76]
# i = 10
# while i<=50:    '''The process of running a loop is known as iteration'''
#     print(fn)
#     i = i+1



# name = input()
# i = 1                            
# while i <= 10:
#     print("My name is",name)
#     i = i+1  or   i += 1



# i = 1
# print("The numbers from 1 to 100 are:")
# while i <= 100:
#     print(i)
#     i+=1



# arr = [1,4,9,16,25,36,49,64,81,100]
# i = 0
# while i<= 9:
#     print(arr[i])
#     i = i+1



# i = 100
# while i>=1:
#     print(i)
#     i=i-1



#To print table of a integer:
# i = 1;
# while i<=10:
#     print(4*i)
#     i=i+1




# print("Please enter your desired number:")
# user = int(input())
# i = 1
# print("The table of your desired number",user,"is:")
# while i<=10:
#     print(user*i)
#     i=i+1



# fruits = ["mango","apple","grapes","banana","watermelon","cherry","Strawberry"]
# i = 0
# while i<=6:
#     print(fruits[i])
#     i=i+1



# arr = [0,1,2,3,4,5,6,7,8,9]
# i=0
# while i<=len(arr):
#     print(arr[i])
#     i=i+1



# arr = [1,23,34,45,56,67,78,89,90,988,76,45]
# print("Enter your desired number:")
# x = int(input())
# i = 0
# while i<len(arr):
#     if (arr[i]==x):
#         print("X found on index",i)
#     i = i+1



#for loop:
# fruits = ["apple","banana","strwaberry","Lichi","mango","papaya","Melon","Cherry"]
# for val in fruits:
#     print(val)


# num = [1,2,3,4,5,6,7,8]
# for val in num:
#     print(val)



# mail = "saraswatsujal@gmail.com"
# for val in mail:
#     print(val)



# to print a table of value input by the user:
# num = (1,2,3,4,5,6,7,8,9,10)
# el = int(input())
# for val in num:
#     print(el*val)



'''OOPS IN PYTHON:'''

'''Attributes store information about the class or object, like a person's name, age, or a company's name.'''

'''ek class ke andar k andar k attribute ko bolte h class attribute and agar kisi object k andar attribute banate h to use bolte h object attribute'''

# class Student:
#     name="sujal"
#     rollNo=1202
# s1 = Student()
# print(s1.rollNo)
# print(s1.name)



# class employee:
#     name="sujal"
#     name1="rohit"
#     name2="Virat"
#     name3="shami"
# em1 = employee()
# print(em1.name)
# print(em1.name1)
# print(em1.name2)
# print(em1.name3)



# class car:
#     color = "Red"
#     model = "ferrari b68"
#     Number = "MP04BE8274"
#     Place = "Bhopal"
#     ownerName = "sujal saraswat"
# car1 = car()
# print("This is car1:")
# print(car1.ownerName)
# car2 = car()
# print("this is car 2")
# print(car2.color)
# print(car2.Number)
# car3 = car()
# print("This is car 3:")
# print(car3.model)
# print(car3.Place)


# class marks:
#     p = 90
#     c = 98
#     m = 85
# student = marks()
# print(student.p,student.c,student.m)



# class marks:
#     s1 = 98
#     s2 = 90
#     s3 = 97
#     s4 = 89
#     s5 = 84
#     s6 = 79
#     s7 = 77
#     s8 = 91

# student1 = marks()
# print("Kuldeep got",student1.s1,"percent")
# print("Suraj got",student1.s2,"percent")
# print("Golu got",student1.s3,"percent")
# print("Sujal got",student1.s4,"percent")
# print("Rohit got",student1.s5,"percent")
# print("Akash got",student1.s6,"percent")
# print("Akku got",student1.s7,"percent")
# print("Mahi got",student1.s8,"percent")

