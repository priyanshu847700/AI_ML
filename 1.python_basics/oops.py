# classes & objects


# class student:
#     subject="python",                         #class attributes
#     course="btech"

#     def __init__(self,name,cgpa):              # default constuctor
#         print("constructor was called...... ")

#     def __init__(self,name,cgpa):              # parameterised constructor #instance attribute
#         self.name=name
#         self.cgpa=cgpa

#     def get_cgpa(self):
#         return self.cgpa
    
# stu1=student("priyanshu",9.1)         # constructor was called......
# stu2=student("archana",9.2)                          
# stu3=student("shakshi",9.3)                          

# print(stu1.name,stu1.cgpa)             # priyanshu 9.1
# print(stu2.name,stu2.cgpa)             # archana 9.2
# print(stu3.name,stu3.cgpa)             # shakshi 9.3

# print(stu1.get_cgpa())                  #9.1


# print(stu1)                             # <__main__.student object at 0x102b484f0>
# print(stu1.subject , stu1.course)       # ('python',) btech
# print(type(stu1))                       # <class '__main__.student'>




#------------------------------------------------------------------------------------------------



# class student:
#     college_name="ABES"
#     PI=3.14

#     def __init__(self,name,cgpa):
#         self.name=name
#         self.cgpa=cgpa
#         self.PI=3.1

# stu1=student("priyanshu",9.8)

# print(stu1.name)
# print(stu1.cgpa)

# print(stu1.college_name)
# print(student.college_name)
# print(stu1.PI)
# print(student.PI)





#------------------------------------------------------------------------------------------------

# # instance class & static method

# class laptop:
#     storage_type="ssd"

#     def __init__(self,ram,storage):
#         self.ram=ram
#         self.storage=storage

#     def get_info(self):    #instance method
#         print(f"laptop has ram : {self.ram} storage : {self.storage} storage_type : {self.storage_type}")

#     @classmethod
#     def get_storage_type(cls):
#         print(f"laptop storage type is : {cls.storage_type}")

#     @staticmethod
#     def discount(price,discount):
#         final_price=price - ((price/100)*discount)
#         print(f"final price = {final_price}")

# l1=laptop(4,64)
# l2=laptop(8,512)
# l3=laptop(16,256)

# l1.get_info()

# l1.get_storage_type()

# l1.discount(100,10)





#------------------------------------------------------------------------------------------------





# # practice Q

# class product:
#     count=0

#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#         product.count+=1

#     def get_info(self):
#         print(f"Price of {self.name} is {self.price} ruppes")

#     @classmethod
#     def no_of_product(cls):
#         print(cls.count)

#     @staticmethod
#     def discount(price,discount):
#         print(f"discounted price : {price - ((price/100)*discount)}")

    
# p1=product("bottel",450)

# p1.get_info()
# product.no_of_product()

# p1.discount(450,10)




#-----------------------------------------------------------------------------------------------------------------


# #encapsulaion         -> wrapping data & function into single unit
# #abstraction
# #inheritance
# #polymorphism


# class bankaccount:
#     def __init__(self,name,balance):
#         self.name=name         #public
#         self._balance=balance  #protected

#     def get_balance(self):              #getter fxn 
#         return self._balance

#     def set_balance(self,newbalance):   #setter fxn
#             self._balance=newbalance
    
# acc1=bankaccount("priyanshu rawat",2_00_000)

# acc1.set_balance(4000000)

# print(acc1.get_balance())



#-----------------------------------------------------------------------------------------------------------------

# # single level inheritance

# class employee:
#     start_time="10 am"
#     end_time="5 pm"


# class teacher(employee):
#     def __init__(self,subject):
#         self.subject=subject   

#     def change_start_time(self,new_start_time):
#         self.start_time=new_start_time


# t1=teacher("english")

# t1.change_start_time("11 am")
# print(t1.subject ,t1.end_time ,t1.start_time)





# # multilevel inheritance
# class employee:
#     start_time="10 am"
#     end_time="5 am"

# class adminstaff(employee):
#     def __init__(self,role):
#         self.role=role

# class accountant(adminstaff):
#     def __init__(self,salary,role):
#             super().__init__(role)
#             self.salary=salary

# acc1=accountant(20000,"CA")

# print(acc1.salary,acc1.role,acc1.start_time,acc1.end_time)





# ##multiple inheritance

# class teacher:
#      def __init__(self,salary):
#           self.salary=salary

# class student:
#      def __init__(self,cgpa):
#         self.cgpa=cgpa

# class TA(teacher,student):
#      def __init__(self,salary,cgpa,name):
#         super().__init__(salary)
#         student.__init__(self,cgpa) 
#         self.name=name

# ta1=TA(200000,8.5,"priyanshu")
# print(ta1.name ,ta1.salary ,ta1.cgpa )




#-----------------------------------------------------------------------------------------------------------------



# ##abstraction!
# #abstract classes

# from abc import ABC ,abstractmethod          #abstraction based classes

# class animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass

# class lion(animal):
#     def make_sound(self):
#         print("roar....")

# class cat(animal):
#     def make_sound(self):
#         print("meow....")

# class cow(animal):
#     def make_sound(self):
#         print("mooo....")


# l=lion()
# l.make_sound()

# c=cat()
# c.make_sound()


##-------------------------------------------------------------------------------------------------------------------



##polymophism

# function overriding

class employee:
    def get_degination(self):
        print("designation = employee")

class teacher(employee):
    def get_degination(self):
        print("designation = teacher")

t1=teacher()
t1.get_degination()


#duck typing -
    
e1=employee()
e1.get_degination()