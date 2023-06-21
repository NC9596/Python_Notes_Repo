print(r'''
                 ____        _   _                 
                |  _ \ _   _| |_| |__   ___  _ __  
                | |_) | | | | __| '_ \ / _ \| '_ \ 
                |  __/| |_| | |_| | | | (_) | | | |
                |_|    \__, |\__|_| |_|\___/|_| |_|
                       |___/      Functions
''')

'''
        *************      Functions      *************
    > When we want to use same set of lines in multiple places => use functions
    > To break a big project into smaller parts[modularity] => use functions
    > Any changes will only affect the function, not other part of code
    > Steps to create a function:
        -> Function definition: def <functionName>(<parameters>):
                                    <block of code Or Suit>
                                    return <something>,<something>,etc.  #optional
        
        -> Function call: <functionName>(<parameters>)

        Ex: def add(x,y):  | def add(x,y):     | def add_sub(x,y):
                print(x+y) |     return(x+y)   |     c = x+y
                           |                   |     d = x-y
            add(5,4) => 9  | add(5,4) => 9     |     return c,d
                           |                   |
                           |                   | result1,result2=add_sub(3,2) =>5,1                                    
'''

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
            *************      Function Arguments      *************
    > Two types of passing Arguments
        -> Pass by value     => passes only the value, not the address
        -> Pass by reference => passes the address of the value, not the value
    > In Python, we do not have Pass by value OR Pass by reference
        * Everything in python is objects
        * Unless we change the value, both the variables point to the same 
        * When the value changes, only then the address changes
        
    Note: Mutable data type like list, will update both the list, 
          i.e. address will not change
     
        Ex: def update(x): 
                print(id(x)) => 3433466655   [i.e. address is same as variable a]
                x=8
                print(id(x)) => 5465657676   [address changed as the value changed]
                           
            a=10
            print(id(a))     => 3433466655
            update(a)
            print(id(a))     => 3433466655
            
        Ex: def update(list): 
                print(id(list)) => 3433466655  [i.e. address is same as variable a]
                list[1]=25
                print(id(list)) => 3433466655  [address remains same, cos mutable]
                print("in function: ",list) => in function: [10 25 30]
                           
            list=[10,20,30]
            print(id(list))     => 3433466655
            update(list)
            print(id(list))     => 3433466655
            print("out of function: ",list) => out of function: [10 25 30]
'''

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
            *************      Types of Arguments      *************
    > If arguments are present in function definition, then we need to pass the 
      arguments while calling the function
        -> Formal Arguments: While function definition
        -> Actual Arguments: While function calling
        
    > Actual Arguments has 4 types
        -> Position: Should follow the positions of Formal Arguments
                Ex: def person(name, age):
                        print(name)
                        print(age-5)
                        
                    person('NC',25) => NC
                                       20
                    
        -> Keyword: Should give the keyword specified in Formal Arguments
                Ex: def person(name, age):
                        print(name)
                        print(age-5)
                        
                    person(age=25, name='NC') => NC
                                                 20
                                       
        -> Default: To skip one of the Formal Arguments or give default values
                Ex: def person(name, age=18): #setting default value of age to 18
                        print(name)
                        print(age-5)
                        
                    person('NC') => NC   
                                    13
                                    
                    #if given a value, it will override the default value
                    person('NC',25) => NC
                                       20
                    
        -> Variable Length: When Number of functional arguments is not fixed
                Ex: def sum(*b):              #we will get b as a tuple
                        c= 0
                        for i in b:
                           c = c + i 
                        print(c)

                    sum(5,6,7,8) => 26
                    
        -> Keyword Variable Length: key value pair in variable length argument
                Ex: def person(name, **data): # will get data as dictionary/map
                        print(name)
                        print(data)
                        
                    person('NC',age=25,city='Bengaluru',phNo=88888888)
                            => NC
                               ['age':25, 'city':'Bengaluru', 'phNo':88888888]

'''

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
        *************      Scope of variable      *************
    > Variable declared outside a function is a Global Variable
        -> We can access a Global variable inside the Function
    > Variable declared inside a function is a Local Variable
        -> Local Variable is NOT accessible outside the function
    
    > Preference is given to the Local Variable if there is a conflict
    
    > To Change the value of a global variable inside a function:
        -> Should specify it by using global keyword
        
    > To get both Global and Local Variable inside a function:
        -> Should use globals() or globals()['<nameOfTheGlobalVariable>'] function
        -> To change the Global Variable without affecting the Local Variable
    
    Ex: a = 10               ==> Global Variable
        def somwFunction():
            a = 15           ==> Local Variable
            print(a) == 15
            
        print(a)     == 10    
            
    Ex: a = 10               ==> Global Variable
        def somwFunction():
            global a
            a = 15           ==> Global Variable
            print(a) == 15

        print(a)     == 15

    Ex: a = 10                   ==> Global Variable
        def somwFunction():
            a = 15               ==> Local Variable
            x = globals()['a']   ==> x Will point to the Global Variable
            x = 12               ==> Now it is no longer pointing to that 
            globals()['a'] = 12  ==> Global Variable 
                                     (This is to change the value of Global Var)
            print(a) == 15

        print(a)     == 12

'''

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
        *************      Recursion      *************
    > Calling the function inside the same function is called as Recursion
    > By default, the recursion limit is 1000 [sys.getrecursionlimit()]
        -> By Default, The function can call inside itself for 1000 times
        -> This limit can be changed [sys.setrecursionlimit(<newLimit>)]
        
    Ex: def factorial(n):
            if n==0:
                return 1
            
            return n * fact(n-1)
            
        print(fact(3))   ==> 6
'''

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
        *************      Lambdas OR Anonymous Functions      *************
    > Functions without name is called as Lamdas
    > When the function is to be used ONLY once and has ONLY one expression
      then Lamdas can be used
      
    > Syntax:
        
        <functionVariable> = lambda <argument1>,<argument2>,etc : <anExpression>
    
    > lambdas can have any number of arguments, but can have ONLY one expression
    
    > Uses: can be used in filter(), map(), reduce(), etc functions
    
    Note: Functions are also Objects in Python
    
    Ex: def square(a):                    f = lambda a : a*a
            return a*a
                                   OR     print(f(5)) => 25
        print(square(6))  => 36

    Ex: f = lambda a,b : a+b
        
        print(f(2,4))  => 6
        
    Ex: nums = [3,2,6,8,4,6,2,9]
        
        evens = list(filter(lambda n : n%2==0, nums))  => [2 6 8 4 6 2]
        
        doubles = list(map(lambda n : n*2, evens))   => [4 12 16 8 12 4]
        
        sum = reduce(lambda a,b : a+b, doubles)      => 56
    
'''

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
        *************      Decorators      *************
    > To add new features to the existing function without touching it
    > We can change the behavior of the existing function during the compile time
    > Syntax:
        
        def <newFunctionName>(oldFunction):
            def innerFunction(<arguments>):
                <blockOfCode>
            return oldFunction(<arguments>)
        return innerFunction
        
        oldFunction = <newFunctionName>(oldFunction)
        
    Ex: def div(a,b):
            print(a/b)
        
        div(2,4)  ===========>  0.5
        
        def smartDiv(func):
            def inner(a,b):
                if a<b:
                    a,b=b,a
            return func(a,b)
        return inner
        
        div = smartDiv(div)
        
        div(2,4)  ===========>  2
'''