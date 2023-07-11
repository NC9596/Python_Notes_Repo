print(r'''
             *****************************************
             *   ____        _   _                   *
             *  |  _ \ _   _| |_| |__   ___  _ __    *
             *  | |_) | | | | __| '_ \ / _ \| '_ \   *
             *  |  __/| |_| | |_| | | | (_) | | | |  *
             *  |_|    \__, |\__|_| |_|\___/|_| |_|  *
             *         |___/          OOPs           * 
             *                                       *
             *****************************************                                           
''')

'''
        *************      OOPs      *************
    > Objects will have 2 things:
        -> Attributes: data like name, phNum, etc.  ==> Variables
        -> Behavior: actions like move(), etc.      ==> Methods
    > Functions in OOPs is called as Methods
    > Concepts of OOP
        -> Object         : Instance of a Class
        -> Class          : Blueprint/Design of an Object
        -> Encapsulation
        -> Abstraction
        -> Polymorphism
'''

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
            *************      Class and Object      *************
    > To define a Class use class keyword
    > To get an instance of the class, use the constructor
    
    > Objects will have 2 things:
        -> Attributes: data like name, phNum, etc.  ==> Variables
        -> Behavior: actions like move(), etc.      ==> Methods
    
    > In Python, __init__(self) is like the Constructor
        -> It is a special method
        -> It will initialize the variables
        -> It will be called automatically for every object
    
    > To call the method of the class:
        -> Passing Object as an argument: 
           <objectName> = <className>()
           <className>.<methodName>(<objectName>)
        
        -> Calling method using the object
           <objectName> = <className>()
           <objectName>.<methodName>()  //it will send the object as argument
      
    Note: Do not use the inbuilt class names for your Class
    
    Ex: class Computer:
            def __init__(self,cpu,ram):
                self.cpu = cpu
                self.ram = ram
            
            def config(self):
                print('Config is ', self.cpu, self.ram)
                
        comp1 = Computer('i9', 32)
        comp2 = Computer('i5', 16)
        
        print(type(comp1))  ==>  __main__.Computer

        comp1.config()      ==> Config is i9 32
'''

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
            *************      Constructor and Self      *************
    > Constructor, i.e. <className>() is called to create the object of a class
    > Size of the object is dependent on the number of variables/attributes
        -> Constructor is responsible to allocate the memory to an object
        -> Every time we create an object, it is allocated to new space(address)
    > Constructor will internally call the __init__() method
    Note: Objects will be stored in Heap Memory
    
    > To define variables:>
        -> using __init__() method:>
        
            class <className>:
                def __init__(self):
                    self.<variable1> = <variable1Value>
                    self.<variable2> = <variable2Value>
                    etc..
            
            Note: In this way, all objects will have the same value for variables
                  To assign a new value. use <objectName>.<variable1>=<updatedVal>  
    
            Ex: class Computer:
                    def __init__(self):
                        self.name = "Nc"
                        self.age = 23
                        
                c1 = Computer()
                c2 = Computer()
                
                print(c1.name)       ==> Nc
                
                c1.name = "Nandish"
                
                print(c1.name)       ==> Nandish
    
    > self, is a pointer that directs the method to an object that is used to call 
            the method
        -> We can compare two objects, we should create a compare() method
            Ex: class Computer:
                    def __init__(self):
                        self.name = "Nc"
                        self.age = 23
                        
                    def update(self):
                        self.age = 18
                        
                    def compare(self, other):
                        if self.age == other.age:
                            return True
                        else: 
                            return False
                        
                c1 = Computer()
                c2 = Computer()
                
                print(c1.name)       ==> Nc
                
                c1.update()          ==> Will call the update method and points
                                         the self to object c1
                                         
                c1.name = "Nandish"
                
                print(c1.name)       ==> Nandish
                
                if c1.compare(c2):
                    print("They are same")
                else:
                    print("They are different")
'''

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
            *************      Types of Variable in OOPs      *************
    > Two types: 
        -> Instance Variable: 
            * Defined in __init__() method
            * Different for different Objects
            * Belong to Instance Namespace (i.e. different for each object)
        -> Class/Static Variable:   
            * Defined outside of __init__() method but inside the class
            * Common for all the Objects
            * Belong to Class Namespace (i.e. common for all objects)
            
    Ex: class Car:
            
            wheels = 4
            
            def __init__(self):
                self.mil = 10
                self.com = "BMW"
                
        c1 = Car()
        c2 = Car()
        
        c1.mil = 8        // Will change the value of mil for c1 only
        
        Car.wheels = 5    // Will change the value of wheels for all the objects
        
        print(c1.mil, c1.wheels)    ==>  8  5    
        print(c2.mil, c2.wheels)    ==> 10  5       
''' 

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
            *************      Types of Methods in OOPs      *************
    > Three types:
        -> Instance Methods: 
            * Works with the Objects (i.e. instance variables 
                                    work with instance methods)
            * If working with instance variable, use self
            * Two types of Instance Methods:
                --> Accessor Methods: 
                    * Methods that ONLY fetch the values of instance Variables
                    * Similar to Getter methods in java
                --> Mutator Methods: 
                    * Methods that ONLY change the values of instance Variables
                    * Similar to Setter methods in java
        -> Class Methods:
            * If working with class variable, use cls 
            * To create a class method, we should use a decorator(@classmethod)
        -> Static Methods:
            * This method is not concerned about instance nor class variables
              (used when there is some extra things to be done in the class)
            * To create a static method, we should use a decorator(@staticmethod)
            
    Ex: class Student:
        
            school = "NC's School"
    
            def __init__(self, m1, m2, m3):
                self.m1 = m1
                self.m2 = m2
                self.m3 = m3
                
            def average(self):
                return (self.m1+self.m2+self.m3)/3
                
            def get_m1(self):         //Accessor method or Getter method
                return self.m1
                
            def set_m1(self, value):  //Mutator method or Setter method
                self.m1 = value
            
            @classmethod
            def getSchool(cls):       //Class Method
                return cls.school
                
            @staticmethod    
            def info():               //Static Method
                print("This is Student class...")
                
        s1 = Student(34, 67, 32)    
        s2 = Student(89, 32, 12) 
        
        print(s1.average())   
''' 

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
            *************      Inner Class      *************
    > Class inside a class is an inner class
    > Used when the inner class is ONLY used by the outer class
    > Object of inner class can be created in two ways:
        -> Inside the outer class, 
                in the __init__() method of the outer class
        -> Outside the outer class,
                use <outerClassName>.<innerClassName>() constructor
    Ex: class Student:
            
            def __init__(self, name, rollNo):
                self.name = name
                self.rollNo = rollNo
                self.lap = self.Laptop()      //inner class object created 
                
            def show(self):
                print(self.name, self.rollNo)
                self.lap.show()
                
            class Laptop:
                
                def __init__(self):
                    self.brand = "HP"
                    self.cpu = 'i5'
                    self.ram = 8
                    
                def show(self):
                print(self.brand, self.cpu, self.ram)
                    
        s1 = Student('NC', 2)
        lap1 = Student.Laptop()   //inner class Object created outside the class
        s1.show()             ==> NC 2
                                  HP i5 8  
        print(s1.lap.brand)   ==> HP
'''

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
            *************      Inheritance      *************
    > Class inherits another class is the Child/Sub class
    > class <class2>(<class1>) ==> class2 inherits class1
        -> Here class1 is the Parent class/Super class
        -> And class2 is the Child class/Sub class
    
    > Sub class can access all  the features of Super class
      But, Super class can NOT access any features of a Sub class
      
    > Types of Inheritance:
        1. Single Level Inheritance: a class inherits a Parent class
        2. Multi Level Inheritance: a class inherits a Sub/Child class
        3. Multiple Inheritance: a class inherits two or more classes
    
    Ex: class A:
            def feature1(self):
                print('Feature 1 working')
                
            def feature2(self):
                print('Feature 2 working')
                
        class B(A):                        // Single Level Inheritance
            def feature3(self):
                print('Feature 3 working')
                
            def feature4(self):
                print('Feature 4 working')
                
        class C(B):                        // Multi Lever Inheritance
            def feature5(self):
                print('Feature 5 working')
                
        class X:
            def feature6(self):
                print('Feature 6 working')
        
        class Y(A,X):                     // Multiple Inheritance
            def feature7(self):
                print('Feature 7 working')       
        
        b1 = B()
        b1.feature1()

'''

'''
            *************      Constructor in Inheritance      *************
    > When an object of Child class is created, 
        then first the __init__() of Child/Sub class will be called, if exists
        else, the __init__() of Super/Parent class is called 
    
    > If we want to specifically call __init__() method of Parent/Super class:
        then should use the super().__init__() in the __init__() of Sub class
    
    Ex: class A:
            
            def __init__(self):
                print('in A init')
    
            def feature1(self):
                print('Feature 1 working')
                
            def feature2(self):
                print('Feature 2 working')
                
        class B(A):
            
            | def __init__(self):   |
            |    super().__init__() |
            |    print('in B init') |
        
            def feature3(self):
                print('Feature 3 working')
                
            def feature4(self):
                print('Feature 4 working')
                
        b1 = B()  ==> in A init (if __init__() of B class is not defined)
        
                      in B init (if __init__() of B class is present)
                      
                      in A init (if super().__init__() is present in
                      in B init       __init__() of B class)

'''  

'''
            *************      Method Resolution Order      *************
    > MRO, is the concept to overcome the Diamond problem
    > It is a concept related to Multiple inheritance
    > MRO: The Multiple inheritance will start from the Left to Right
            Ex: class C(A,B) ==> super().__init__() will prefer class A first
                class C(B,A) ==> super().__init__() will prefer class B first    
    > We can use super() method to call other methods, not only __init__() 
        
    Ex: class A:
            
            def __init__(self):
                print('in A init')
    
            def feature1(self):
                print('Feature 1 A working')
                
        class B:
            
            def __init__(self):   
                print('in B init') 
        
            def feature1(self):
                print('Feature 1 B working')
                
            def feature2(self):
                print('Feature 2 working')
                
        class C(A,B):
            
            def __init__(self):
                super().__init__()
                print('in C init') 
                
            def feature(self):
                super().feature1()
        
        c1 = C()       ==> in A init
                           in C init
                        
        c1.feature1()  ==> Feature 1 A working
        c1.feature     ==> Feature 2 working
'''

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
            *************      Polymorphism      *************
    > Objects have multiple forms is called Polymorphism
    > Uses: Loose Coupling, Dependency Injection, Interface, etc.
    > Four ways to implement Polymorphism:
    
        1. Duck Typing:
            -> Behavior of the bird that matches that of Duck, is a Duck
            -> The method we use of a class is important, not the class itself
               i.e. the same method can also be used from other class, if present
               i.e. the Behavior is important
               
            -> Similar to Interface in java, i.e. say class A and class B 
               implements an interface X, 
               then the method can be taken from either of the class
               
            Ex: 
                class PyCharm:
                    def execute(self):
                        print("Compiling and Running")
                
                class MyEditor:
                    def execute(self):
                        print("Spell Check, Compiling and Running")
                
                class Laptop:
                    def code(self, ide):
                        ide.execute()
                        
                ide1 = PyCharm()
                ide2 = MyEditor()
                lap1 = Laptop()
                lap1.code(ide1)    ==> Compiling and Running
                lapq.code(ide2)    ==> Spell Check, Compiling and Running
                
                // execute() method can come from PyCharm or MyEditor
            
        2. Operator Overloading:
            -> Using the same operator for different datatype objects
                Ex: 4 + 5               ==> 9
                    'Hi, ' + 'Welcome'  ==> Hi, Welcome
                
                Behind the scene, int.__add__(4,5)               ==> 9
                                  str.__add__('Hi, ', 'Welcome') ==> Hi, Welcome
                                  
            -> Hence, if we use + operator it calls __add__() method
                      if we use - operator it calls __sub__() method                         
                      if we use * operator it calls __mul__() method
                      if we use > operator it calls __gt__() method
                      etc.
                      [those methods are called as Magic Methods]
                      
            Ex: class Student:
                    def __init__(self, m1, m2):
                        self.m1 = m1
                        self.m2 = m2
                    
                    def __add__(self, other):
                        m1 = self.m1 + other.m1
                        m2 = self.m2 + other.m2
                        return Student(m1, m2)
                        
                    def __gt__(self, other):
                        r1 = self.m1 + self.m2
                        r1 = other.m1 + other.m2
                        if r1 > r2:
                            return True
                        else:
                            return False
                            
                    def __str__(self):
                        return '{} {}'.format(self.m1, self.m2)
                        
                s1 = Student(58,69)        
                s2 = Student(69,65)  
                
                s3 = s1 + s2         
                print(s3.m1)          ==> 118 (i.e. 58 + 60)   
                
                if s1 > s2:
                    print('s1 wins')
                else: 
                    print('s2 wins')  ==> s2 wins
                    
                //same as print(s2.__str__())    
                print(s2)             ==> 69 65        
            
        3. Method Overloading:
            > Method Overloading is not there in Python
                i.e. cannot create two methods with the same name in one class
            > Same method with the same name with different number of parameters
            > To achieve Method Overloading, we can use
              Variable length argument  OR  Default arguments
               (line 107 in Functions)   (line 95 in Functions)
            
            Ex: class Student:
                    def __init__(self):
                        self.m1 = m1
                        self.m2 = m2
                        
                    def sum(self, a=None, b=None, c=None):
                        if a!=None and b!=None and c!=None:
                            return a + b + c
                        elif a!=None and b!=None:
                            return a + b
                        else:
                            return a
                        
                s1 = Student()
                
                print(s1.sum(2))      ==> 2
                print(s1.sum(5,9))    ==> 14
                print(s1.sum(1,2,3))  ==> 6
        
        4. Method Overriding:
            > Same method name and same number of parameters, in different class
            > If a method is called by a Sub class Object, 
              then that method will be searched in the Sub/Child class first,
              if not found, then it will be searched in Parent/Super class
            
            Ex: class A:
                    def show(self):
                        print('in A show')
                        
                | class B(A):               |
                |    def show(self):        |
                |        print('in B show') |
                
                b = B()
                b.show()   ==> in A show (if show() is not present in class B)
                               in B show (if show() is present in class B)
''' 

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
            *************      Abstraction      *************
    > Abstract Method:
        -> A method without a body is called a Abstract method
           i.e. Method which has only declaration and NOT definition
    > Abstract Class: 
        -> A class which has at least one Abstract Method is called Abstract Class
        -> Not supported by Python 
        -> But to achieve Abstract class, that class should inherit ABC class
           i.e. Abstract Base Class(ABC), should import abc module
        -> Cannot create an Object of an Abstract Class
           It is like Interface in java
        -> Syntax: from abc import ABC, abstractmethod
                   
                   class <className>(ABC):      //should be a sub class of ABC 
                       @abstractmethod          //should add this decorator 
                       def <methodName>(self):
                           pass                 //should not have a  body
    
    Note: A Sub class of an Abstract class, should Define/Implement 
                                            ALL the Abstract Methods
                                      present in the parent abstract class
    
    Ex: from abc import ABC, abstractmethod
        
        class Computer(ABC):
            def process(self):
                pass
                
        class Laptop(Computer):
            def process(self):
                print("It's Working")
                
        class Whiteboard:
            def write(self):
                print("It's Writing")
                
        class Programmer:
            def work(self, com)       //com can be anything
                print('Solving Bugs')
                com.process()
    
        com1 = Laptop()
        whi1 = Whiteboard()
        com1.process()        ==> It's Working 
        
        prog1 = Programmer()
        prog1.work(com1)      ==> Solving Bugs
                                  It's Working
                                  
        prog1.work(whi1)      ==> ERROR, cos process() not found in Whiteboard        
'''