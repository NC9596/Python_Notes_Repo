print(r'''
             *****************************************
             *   ____        _   _                   *
             *  |  _ \ _   _| |_| |__   ___  _ __    *
             *  | |_) | | | | __| '_ \ / _ \| '_ \   *
             *  |  __/| |_| | |_| | | | (_) | | | |  *
             *  |_|    \__, |\__|_| |_|\___/|_| |_|  *
             *         |___/      Introduction       * 
             *                                       *
             *****************************************
''')

'''
> Python(1989) came way before Java(1995)
> Python is popular in the field of AIML because it is easy to learn

> Python supports Functional Programming, OOPs, Procedure Oriented Programming
               (pass Function to function)       (break project into modules)
                                                             
> Python versions => 1 ; 2 ; 3(latest) 
  Note: Python 3 is not backward compatible with older versions.
> Softwares needed: Python Interpreter (pip) ; an IDE(PyCharm, Spider, etc)
> * For single line execution we can use IDLE interactive console.
  * But for multiple lines of code, we should create a .py file
    To run this .py file => navigate to the folder where .py file exists
                         => run the code: python <FileName>.py
  * For projects use IDEs
> Note: In Python we do not use {} to specify a block of code
            Hence, we have to use indentation(space) to specify the block of code
'''

'''
Basic Math Operations:
    add: 2 + 3 = 5
    sub: 3 - 2 = 1
    mul: 2 * 3 = 6
    div: 3 / 2 = 1.5
 intDiv: 3 // 2 = 1
    pow: 2 ** 3 = 8 (same as 2*2*2)
    mod: 10 % 6 = 4
     _ : _ + 10 = 14 ( _ = result of previous operation)
     
    increment: x = 0
               x = x+1  ||  x += 1
    
    decrement: y = 2
               y = y-1  ||  y -=1
               
    Double Assignment: a,b=3,4
'''

'''
print function (to display values on the console):
    print('NC') => NC
    
    print('"NC"') => "NC"
    print("'NC'") => 'NC'
    print("\"'NC'\"") => "'NC'"
    
    print('NC\nc') => NC 
  (\n = next line)    c
    
    print(r'NC\nc') => NC\nc
    (r = raw string, i.e. will print the string as it is)
    
    print('NC ', end='') => NC [it will print NC and stays on the same line]
    print('1 ') => NC 1 
    
    print("A: {} and B: {}".format(a,b)) => For place holder in print function
    
    i = 9
    print("I: ", i) => To print the value of a variable
'''

'''
input function (to get input from the user):
    > [By default, input() function will ONLY take String values]
      [So, to do math functions we should cast it to the type we want]
      
    > [We can also print a message with the input("") function]
   
    >   x = int(input())
        y = int(input("Enter a value for x"))
        x = x + y
    
    > [We can limit the number of characters the input()[0] function can get]
      [input() function will take whole string, 
       but [0] will take only the first character]
      Ex: a = input("Enter a character")[0]

    > [Can evaluate the expression given by the user, use eval() function]
      Ex: result = eval(input("Enter an expression"))
      
    >> [Can also pass values from the command prompt, i.e. Arguments, use agrv]
       -> Should use the keyword argv, i.e. a LIST of STRING
       -> To access the values use the index number
           * [0] is for file name
       -> argv belongs to the sys module
       Ex: import sys
           x = int(sys.argv[1])
           y = int(sys.argv[2]) 
           print(x+y)
           
           Then go to cmd and run: python <FileName>.py 6 2
                           Output: 8
'''

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
                 *************      Modules      *************
    > Instead of writing one big project in one big file, we break into modules
    > All same features should be in one module, like math module, etc
    > Modules can have variables, functions or classes
    > One Module is One .py file
    
    > To get features of one module in another, then we should import it:
        -> import <moduleName>
        -> from <moduleName> import *
    
    > Advantages:
        -> Change in one module will not affect other modules
        -> We can reuse the modules in other projects
    
    Ex: ``demo.py                    | ``Calc.py
            import Calc              |                                     |
                                     |     def add(a,b):
            a,b=8,9                  |         return a+b
                                     |
            Calc.add(a,b)  ==> 17    |     def sub(a,b):
                                     |         return a-b
                                     |
                                     |     def mul(a,b):
                                     |         return a*b
                                     | 
                                     |     def div(a,b):
                                     |         return a/b
'''

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
                 *************      Math Module      *************
    > [Has some functions and Constants]
      [More on help("math")]
    
    > import math
      x = math.sqrt(25) = 5.0
      y = math.floor(2.9) = 2
      y = math.ceil(2.9) = 3
      z = math.pow(3,2) = 9.0
      math.pi = 3.14159....
      math.e = 2.718284....
    
    > [can also import a module as alias]
      import math as m
      x = m.sqrt(25) = 5.0
      
    > [can also import only the functions we need]
      from math import sqrt, pow
      pow(4,5) = 1024.0
'''

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
                 *************      NumberSystem      *************
    > To convert from decimal(base = 10) to binary(base = 2): bin({decimal number})
    > To convert from binary to decimal: 0b{binary number}
    > To convert from decimal to octal(base = 8): oct({decimal number})
    > To convert from octal to decimal: 0o{octal number}
    > To convert from decimal to hexa-decimal(base = 16): hex({decimal number})
    > To convert from hexa-decimal to decimal: 0x{hexa-decimal number}
'''

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
                 *************      Comments      *************
    > In Python we ONLY have Single Line Comments
        --> Use # for Single Line Comment
    > For MultiLine Comments, should use # in every line    
    
    > Triple Quotes(''' ''' OR """ """) ==> is used for documentation 
                                               NOT for Comments
            --> Parser will NOT ignore these lines 
            --> We can export these documentation in text/html format
            --> Use it ONLY for documentation                                 
'''

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
  *************      Python Compiled or Interpreted Language?      *************
    
    > Python is BOTH Compiled as well as Interpreted language
    
    > C and C++ are Compiled languages
        --> Compiler: Will convert high level language to machine level language
             [compiler can also convert from one high level language to another]
    
    > Python: 
        --> Python file will first gets compiled to get a Byte code
        --> Then, the Byte code will be interpreted in a Machine language
                                                [by a Special Vertual Machine]
                                                
       Python 
       Source  --> [Compiler] --> Byte Code --> [Interpreter] --> Machine Language
       Code                                (Python Virtual Machine)

        --> Interpreter: It has a set of instructions 
                         Interpreter will read line by line
                         
                         This is done to achieve Platform Independence
                                             (Write once Run Everywhere)
                                             
            PVM: use to run ONLY python codes
            JVM: use to run Java, Scala, etc
            
            NOTE: 
            1. Run code in JAVA:
                --> javac Demo.java  //to compile the code
                --> java Demo        //to run the file
                
            2. Run code in Python:
                --> python Demo.py   //will compile(gives byte code) and runs that
            
    > Python Implementations: 
      [For python language there are different implementations]
        
        1. cPython    :: implemented in C language [widely used]
                         i.e. internal working is happening with C language
        2. IronPython :: .NET implementation 
        3. Jython     :: java implementation
        4. PyPy       
'''