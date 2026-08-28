# # 1st program

# print('hello \n world')
# print('apna college')



# # variable
# name="priyanshu"
# age=20
# pi=3.14
# flag=True

# isPrime=None

# print("my name is: ",name,"my age is ",age)


#-------------------------------------------------------------------------------------------------------


# # data type

# print(type(name))
# print(type(age))
# print(type(pi))
# print(type(flag))
# print(type(isPrime))

# '''
# this 
# is
# a
# multiline 
# commment
# '''


# a=5
# b=10
# sum=(a+b)
# print(sum)



#-------------------------------------------------------------------------------------------------------



# '''
# # Operators
#     • Arithmetic           [+,-,/,*,//,**,%]
#     • Relational / Comparison
#     • Assignment
#     • Logical
# '''


# # • Arithmetic           [+,-,/,*,//,**,%]
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a**b)
# print(a%b)


# # • Relational / Comparison         [>,<,<=,>=,==,!=]
# print(a>b)
# print(a<b)
# print(a<=b)
# print(a>=b)
# print(a==b)
# print(a!=b)



# # • Assignment                      [=,+=,-=,/=,*=,%=,**=]

# c=10
# c-=5
# print(c)



# # • Logical                           [not,and ,or]

# isPrime=False

# print(not(isPrime))

# print((3>1) and (5>2))
# print((3>1) and (5<2))

# print((3<1) or (5>2))
# print((3>1) or (5<2))


#-------------------------------------------------------------------------------------------------------


# '''        type conversion
#                  |
#                  |
#     - - - - - - - - - - - - - - -
#     |                           |
# type conversion              type casting
# (implicit by python) 

# '''
# # type conversion
# x=10
# y=5
# print(type(x/y))



# # type casting
# x1=int(x+y)
# print(type(x1))

# var=bool(10)
# print(type(x1),var)


#-------------------------------------------------------------------------------------------------------

# # input in python

# username = input ("enter your name: ")
# print("welcome", username)


# #sum of 2 nums
# a = float(input("enter a: "))
# b = float(input("enter b: "))
# sum = a + b
# print (sum)



# #calculate avg of 2 nums
# a = float(input("enter 1st num: "))
# b= float(input("enter 2nd num: "))
# avg = (a+b) /2
# print ("avg of 2 nums =", avg)



#-------------------------------------------------------------------------------------------------------

# # conditional statement
# age = int(input("enter age: "))
# if age >= 18:
#     print ("you can vote") 
#     print ("you can drive")
# else:
#     print ("you can't vote")




# color = input("enter color: ")
# if color == "red":
#     print("stop")
# elif color == "green":
#     print ("go")
# elif color == "yellow":
#     print("Look")
# else:
#     print("wrong color")





# age = int(input ("enter age: "))
# if age < 13 :
#     print("child")
# elif (age >= 13 and age < 18): #13-18
#     print("teenager")
# else:
#     print("adult")



# username = input ("enter username: ")
# password = input ("enter password: ")
# if (username == "admin" and password == "pass"):
#     print("LOGIN Successful!")
# elif (username != "admin"):
#     print("Wrong Username")
# else: 
#     print("Wrong Password")





# n = int(input("enter num: "))
# if (n % 5 == 0):
#     print("multiple of 5")
# else:
#     print("not multiple of 5")



# n = int(input("enter num: "))
# if (n % 2 == 0):
#     print ("EVEN")
# else:
#     print ("ODD") 




# username = input ("enter username: ")
# password = input("enter password: ")

# if(username == "admin" and password == "pass"):
#     print ("success")
# else:
#     if (username != "admin"):
#         print("wrong username")
#     else:
#         print ("wrong password")


#-------------------------------------------------------------------------------------------------------
# math case alterantive for if else elif!!

# color = input("enter color: ")
# match color:
#     case "Green":
#         print ("Go")
#     case "Yellow":
#         print ("Look")
#     case "Red":
#         print ("Stop")
#     case _:
#         print ("Wrong color!")




#-------------------------------------------------------------------------------------------------------
#LOOPS-

# while--

#infinite loop
# while True:
#     print("hello world")



# #finite Loop = 10x
# count = 1
# while (count <= 10):
#     print ("hello world", count)
#     count += 1

# print ("after loop, count=", count) #11


# # forward print 1 to 5
# i = 1 #iterator
# while (i <= 5):
#     print (i)
#     i += 1


# # backward print 1 to 5
# i = 5
# while (i >= 1):
#     print (i)
#     i=i-1



# #multiplication table of any num

# n= int(input("enter num:"))
# i = 1
# while (i <= 10): 
#     print (n * i)
#     i += 1



# i = 1
# while (i <=10):
#     if(i%6 == 0):
#         break
#     print(i)
#     i += 1
# print("outside loop now....")





# i = 1
# while (i <10):
#     if (i % 3 == 0):
#         i+=1
#         continue
#     print (i)
#     i += 1

# print("outside loop......")




# #odd nums
# i = 1
# while (i <= 10):
#     print (i)
#     i += 2



#-------------------------------------------------------------------------------------------------------


# for--

# string = "hello" #o
# if 'o' in string:
#     print ("o exists in string")
# if 'x' in string:
#     print ("o exists in string")




# string = "hello"
# #in => membership operator
# for var in string: 
#     print (var)


# for i in range(5):
#     print(i)


# for i in range(5):
#     print(i+1)




# #count the number off i's: = 5
# word = "artificial intelligence"
# count = 0
# for ch in word:
#     if(ch == "i"):
#         count += 1
# print ("count of i = ", count)                #count of i =  5



# # count vowel
# word = "artificial"
# count = 0
# for ch in word:
#     if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
#         count += 1
# print("ans =", count)


#-------------------------------------------------------------------------------------------------------



# #range fxn-

# # range(st,end,step)      -> end is compulsary

# for i in range(5):
#     print(i,end=" ")
# print("\n")

# for i in range(2,10):
#     print(i,end=" ")
# print("\n")

# for i in range(2,11,2):
#     print(i,end=" ")
# print("\n")


#-------------------------------------------------------------------------------------------------------


# # sum of n no.

# n = int(input("enter number: "))       # n*(n+1) / 2
# sum = 0
# for i in range (1, n+1):
#     sum += i
# print("sum =", sum)

#-------------------------------------------------------------------------------------------------------


# #fxn-

# def hello(): 
#     print("hello") 
#     print("from python")
# hello()



# #function definition def sum(a, b): #parameters
# def sum(a,b):
#     s=a + b 
#     return s

# #function call
# ans = sum (3, 4)
# print (ans)



#-------------------------------------------------------------------------------------------------------

#lambda fxn-

# sum =lambda a,b:a+b
# print(sum(4,5))



#-------------------------------------------------------------------------------------------------------

#WAF to find factorial-

def calc_factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i

    return fact

n=int(input("enter a no: " ))
print(calc_factorial(n))



