# ## string !
# word1 = "I love"
# word2 = "python"
# sentence = word1 + " " + word2

# #concatenate 
# print (sentence)

# print(word1[0])

# # word2[3]="k"                    error! strings are immutable
# for ch in word2:
#     print(ch,end="")



#------------------------------------------------------------------------------------------------

# # string slicing

# word="python"                       # str[st_idx,end_idx]    end_idx -> is not included
# print(word[2:4])

# sen="i study from apnacollege"
# print(sen[13:])
# print(sen[:len(sen)])

# print(sen[-7:-1])
# print(sen[-7:])



# #------------------------------------------------------------------------------------------------

# #string format

# a=10
# b=5
# sum=a+b

# print("sum of {} & {} is {}".format(a,b,sum))

# #index based formatting
# print("sum of {1} & {0} is {2}".format(a, b, sum))


# #value based formatting
# print("value of vars {a} & {b} is {c}".format(c=a+b, b=10, a=5,))


# #f-string
# print(f"avg of {a} & {b} is {(a+b)/2}")


#------------------------------------------------------------------------------------------------

# #list    []           -> list are mutable 
# marks=[99,89,100,65,92,"abc",20.6]

# marks[0]=0

# print(marks)
# print(len(marks))

# print(type(marks))

# #slicing in list 
# print(marks[:5])
# print(marks[:])
# print(marks[2:-2])


# #------------------------------------------------------------------------------------------------


# #Lists Methods
# # • l.append(val)          ->       add one element at the end
# # • l.insert(idx, val)     ->       insert element at idx
# # • l.sort()               ->       arranges in increasing order
# # • l.reverse()            ->       reverses order

# nums = [1, 2, 3]

# nums.append (4)
# print(nums)

# nums.insert(2,10)
# print(nums)

# nums.sort()
# print(nums)

# nums.sort(reverse=True)
# print(nums)

# nums.reverse()
# print(nums)

#------------------------------------------------------------------------------------------------

# loops in list

# nums=[1,2,3,4]
# for i in nums:
#     print(i)


# l=[1,2,3,4,5,6,7,8]
# x=4
# idx=0
# for i in l:
#     if(i==x):
#         print(f"{x} index found at idx : {idx}")
#         break
#     idx+=1




#--------------------------------------------------------------------------------------------------

# #tuples  ()              -> immmutable sequence of value

# tup=(1,2,3,4,5,"xyz",0.5)

# # tup[2]=15                          -> err because tuples are immutable

# print(tup)
# print(type(tup))
# print(len(tup))

# print(tup[0:3])
# print(tup[:])



# tup1=(1)
# print(type(tup1))

# tup2=(1,)
# print(type(tup2))


# # loops in tuples

# tup = (1, 2, 3, 4, 5)
# sum = 0
# for val in tup:
#     sum += val
# print (f"sum of vals is {sum}")


# #tuples method!!

# t=[1,2,3,2,3,4,2]
# val=3
# print(t.index(val))                 #index method
# print(t.count(2))                   #count method


#-----------------------------------------------------------------------------------------------


# #dictionary                mutable/unordered

# info={
#     "name":"priyanshu",
#     "age":20,
#     "course":"B.Tech",
#     3.14:"pi",
#     "cgpa":8.0
# }
# info["cgpa"]=9.0

# print(type(info))
# print(info["name"])
# print(info["cgpa"])

# print(info)


# #dictionary methods-

# # • d.keys()                          #returns all keys
# # • d.values()                        #returns all values
# # • d.items()                         #returns (key, val) pairs 
# # • d.get(val)                        #returns val acc. to key
# # • d.update(new_item)                #adds new item to dict

# print(info.keys())
# print(info.values())
# print(info.items())
# print(info.get("age"))

# info.update({
#     "branch":"AI & ML"
# })

# print(info.items())


#-----------------------------------------------------------------------------------------------


# #sets     {} -> collection of unique element!!     mutable /unordered

# s={1,2,2,2,2,3,3,5}
# s.add(10)

# print(s)
# print(len(s))
# print(type(s))



# #creating an empty set!! -

# # empty_set={}                        # 🙅🏻
# # print(type(empty_set))              #  ->dictionary will be created 

# empty_set=set()                       #constructor
# print(empty_set)
# print(len(empty_set))
# print(type(empty_set))




# #set methods-

# # • s.add(val)                                #adds a val
# # • s.remove(val)                             #removes a val
# # • s.clear()                                 #empties the set
# # • s.pop()                                   #removes a random val
# # • s.union(set2)                             #returns new union
# # • s.intersection(set2)                      #returns new intersection


# s2={4,5,6,7,8,9,10}
# print(s.union(s2))

# print(s.intersection(s2))

# s.remove(3)
# print(s)

# s.pop()
# print(s)

# s2.clear()
# print(s2)






#------------------------------------------------------------------------------------------------

# practice Q

info = [
    ("Alice", "Math"),
    ("Bob" ,"Science"),
    ("Alice", "Science"), 
    ("Charlie", "Math"), 
    ("Bob", "Math"), 
    ("Alice", "English"), 
    ("Charlie", "English")
]

#print all unique courses!
unique_couses=set()
for i in info:
    unique_couses.add(i[1])

print(unique_couses)


# print all student that have enrolled in english

for i in info:
    if(i[1]=="English"):
        print(i[0],end=" , ")

print()


#creat a dictionary with name of student & there course!

dict = {}
for name,sub in info:
    if(dict.get(name)==None):
        dict.update({name:set()})
        dict[name].add(sub)
    else:
        dict[name].add(sub)

print(dict)

