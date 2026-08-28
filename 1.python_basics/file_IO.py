# #file read-  (r)

# f=open("test.txt","r")

# # data=f.readline()                   #prints line one by one
# # data=f.readlines()                  #prints line one by one in same line
# data=f.read()                         #print full data

# print(data)
# print(type(data))

# f.close()



#--------------------------------------------------------------------------------------------------------------------


# # file write (w)

# f=open("text.txt","w")

# data=f.write("hello world")

# print(data)
# f.close()



#--------------------------------------------------------------------------------------------------------------------




### Modes-
# r        ->        #reading [default]
# w        ->        #writing, truncates file first
# x        ->        #creates new & open for writing
# a        ->        #writing, appends at end
# b        ->        #binary mode
# t        ->        #text mode [default]
# +        ->        #opens disk file for update(r & w)



# # (a) -

# f=open("test.txt","a")
# data=f.write("\nalso i have done FULL STACK DEVELOPMENT")
# f.close()


#--------------------------------------------------------------------------------------------------------------------


# # (x) -

# f=open("sample1.txt","x")
# data=f.write("some random fact")
# f.close()

#--------------------------------------------------------------------------------------------------------------------

# # (r+)

# f=open("text.txt","r+")
# data=f.write("added to front\n")
# print(f.read())
# f.close()

#--------------------------------------------------------------------------------------------------------------------

# # (a+)

# f=open("text.txt","a+")
# data=f.write("\nadded to back")
# print(f.read())
# f.close()

#--------------------------------------------------------------------------------------------------------------------


# # (w+)

# f=open("text.txt","w+")
# data=f.write("\nthis is w+ mode")
# print(f.read())
# f.close()

#--------------------------------------------------------------------------------------------------------------------

# #with keyword!!
# with open("sample1.txt",'r') as f:
#     data=f.read()
#     print(data)
#     print(len(data))

#--------------------------------------------------------------------------------------------------------------------


# # delete operation in file 
# import os
# os.remove("sample1.txt")


#--------------------------------------------------------------------------------------------------------------------
# # practice Q


# data=True
# line=1
# word="priyanshu"

# with open("test.txt","r") as f:
#     flag=0
#     while(data):
#         data=f.readline()

#         if(word in data):
#             print(f" {word} found at line {line}")
#             flag=1
#             break
#         line+=1

#     if(flag==0):
#         print("not found")    




#--------------------------------------------------------------------------------------------------------------------
# # # exception handling!

# try:
#     x=int(input("enter a valid no. : "))
#     ans=10/x
# except ZeroDivisionError:
#     print("no. can not be divisible by 0")

# except ValueError:
#     print("invalid input please enter a integer")

# else:
#     print(f"ans : {ans}")

# finally:                                   #finally code irrespective of code executed or generate an error
#     print("end of code")



#--------------------------------------------------------------------------------------------------------------------

# # list comprehension

# n=int(input("enter a no. : "))

# square=[]
# for i in range(0,n+1):
#     square.append(i*i)

# print(square)

# sq=[i*i for i in range(n+1)]
# print(sq)

# sq_odd=[i*i for i in range(n+1) if i%2 !=0]
# print(sq_odd)





# nums=[-2,-4,3,5,2,-1]
# print(nums)
# nums=[0 if val<0 else val for val in nums]
# print(nums)


# words=["apple","mango","banana"]
# words=[i.upper() for i in words]
# print(words)




#--------------------------------------------------------------------------------------------------------------------

# import json

# json_str='{ "name":"priyanshu","age":20 }'
# print(type(json_str))

# py_obj=json.loads(json_str)          #python string to json
# print(type(py_obj),py_obj)



# python_obj= {
#     "subj":["pythonn","java","c++"],
#     "address":{
#         "city":"Ramnagar",
#         "Pin-code":244715
#     }
# }
# print(type(python_obj))

# json_string=json.dumps(python_obj)              #json to python string 
# print(type(json_string),json_string)




#--------------------------------------------------------------------------------------------------------------------



# json.load()                 #to read from json file
# json.dump()                 #to write from json file


import json

# with open("data.json","r") as f:
#     py_obj=json.load(f)
#     print(py_obj)

data={
    "course":"btech",
    "branch":"CSE AI & ML"
}

with open("data.json","w") as f:
    json.dump(data,f,indent=4,sort_keys=True)



