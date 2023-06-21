print(r'''
                 ____        _   _                 
                |  _ \ _   _| |_| |__   ___  _ __  
                | |_) | | | | __| '_ \ / _ \| '_ \ 
                |  __/| |_| | |_| | | | (_) | | | |
                |_|    \__, |\__|_| |_|\___/|_| |_|
                       |___/          OOPs
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