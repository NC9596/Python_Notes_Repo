print(r'''
                 ____        _   _                 
                |  _ \ _   _| |_| |__   ___  _ __  
                | |_) | | | | __| '_ \ / _ \| '_ \ 
                |  __/| |_| | |_| | | | (_) | | | |
                |_|    \__, |\__|_| |_|\___/|_| |_|
                       |___/ Variable And Operators
''')

'''
> Variables = whose value can be changed
> No need to define the type of variable in Python, because as soon as 
  we give the value Python will automatically detect the type.
> To get the address of a variable, use id() method
> To get the datatype of a variable, use type() method
> If created multiple variables with same value, then both variables will point to
  the same value, i.e. address of both variable will be same
  [Hence, Python is memory efficient]
  [i.e. Python allocates memory based on value, not the variable]
> As soon as the value of a variable changes, the address also changes  
> if a value is not referred by any variable, it goes to garbage collection

Note: 
 * Cannot create a constant variable in Python

'''

'''
> name = 'Nandish'

  name[0] = N
  name[-7] = N
  name[0:5] = Nandi (exclusive of the end index, i.e. 5)
  name[3:] = dish 
  name[:5] = Nandi
  len(name) = 7
  
  id(name) = 12345678
  
  Note => String is immutable, i.e. the value cannot be changed
  Ex: name[0] = F (to change the value at index 0)
      Will give an error 
  
> a = 10
  b = 10
  id(a) = 143563775
  id(b) = 143563775
  
  a = 9
  id(a) = 145678988
  id(b) = 143563775
'''
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
                 *************      DataType      *************
 None       (like null) 
 Numeric    int[1,3,etc.] | float[1.5,4.9,etc] | complex[2+3j,etc.] | bool[True,etc.]
 Sequence   List | Tuple | Set | String | Range
 Dictionary (like Map)
'''

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
                 *************      Operators      *************
    Arithmetic Operator       +   -   *   / 
    Assignment Operator   =   +=   -=   *=   /=     Note: a,b=5,6 is possible
    Unary Operator                 -               Ex: n = -n
    Relational Operator   ==   <=   >=   !=
    Logical Operator         and   or   not        Ex: a<5 and b<5; not a; etc.
    Bitwise Operator         ~         &     |     ^         <<              >>
    (More at line 67)  [Complement]  [And]  [Or] [XOR]  [Left Shift]   [Right Shift]
'''

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
                 *************      Bitwise Operator      *************
    > Complement Operator (~ tilde operator):
        Ex: ~12 = -13
        -> [Complement of a number is the reverse of the binary format]
                [i.e. ~1 = 0  and  ~0 = 1]
        -> [2's Complement: (To store negative numbers)]
                2's complement = 1's complement + 1
                Ex: 13 in binary format: 00001101
                         1's complement: 11110010
                         2,s complement: 11110010
                                                +
                                                1
                                         11110011 => -13 in binary format
                    12 in binary format: 00001100
                        12's complement: 11110011 => Same as -13 in binary
                                                     [Hence, ~12 = 13] 
                                                     
    > Bitwise And (& ampersand operator):                              x  y  x&y  
        Ex: 12 & 13 = 12                                             | 0  0   0  |
        -> [If both are 1 => 1]                                      | 1  0   0  |
        -> 12 in binary format: 00001100                             | 0  1   0  |
           13 in binary format: 00001101                             | 1  1   1  |
                       12 & 13: 00001100 => Same as 12 in binary     -------------
                                            [Hence 12 & 13 = 12]
                                             
    > Bitwise Or (| pipe operator):                                    x  y  x|y 
        Ex: 12 | 13 = 13                                             | 0  0   0  |       
        -> [If any one is 1 => 1]                                    | 1  0   1  |
        -> 12 in binary format: 00001100                             | 0  1   1  |
           13 in binary format: 00001101                             | 1  1   1  |
                       12 | 13: 00001101 => Same as 13 in binary
                                            [Hence 12 | 13 = 13]
                                            
    > Bitwise XOR (^ cap operator):                                    x  y  x^y
        Ex: 12 ^ 13 = 1                                              | 0  0   0  |
        -> [If odd numbers' of 1 => 1]                               | 1  0   1  |
        -> 12 in binary format: 00001100                             | 0  1   1  |
           13 in binary format: 00001101                             | 1  1   0  |
                       12 ^ 13: 00000001 => Same as 1 in binary
                                             [Hence 12^13 = 1]
                                             
    > Left Shift (<<):
        Ex: 10 << 2 = 40
        -> [Shift the bit to the left side of the .]
           [We gain bits in left shift]
        -> 10 in binary format: 00001010.0000
                       10 << 2: 0000101000.00 => 00101000 in decimal is 40
                                                   [Hence 10 << 2 = 40]
                                                   
    > Right Shift (>>):
        Ex: 10 << 2 = 40
        -> [Shift the bit to the right side of the .]
           [We lose bits in right shift]
        -> 10 in binary format: 00001010.0000
                       10 << 2: 000010.000000 => 00000010 in decimal is 2
                                                   [Hence 10 << 2 = 2]
'''

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
                 *************      Number Swap      *************
    > Use third variable: a=1
                          b=2
                          temp=1
                          a=b [i.e. 2]
                          b=temp [i.e. 1]
    
    > Use an operator: a=1
                       b=2
                       a=a+b [i.e. 3]
                       b=a-b [i.e. 1]
                       a=a-b [i.e. 2]
                       
    > Use XOR operator(to save memory): a=1
                                        b=2
                                        a=a^b [i.e. 3]
                                        b=a^b [i.e. 1]
                                        a=a^b [i.e. 2]
    
    > Two Rotation (Python Exclusive): a=1
                                       b=2
                                       a,b=b,a [Python will solve right side first]
                                               [It will store it in Stack]
'''

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
                 *************      Special Variable      *************
    > __name__ is a special variable
    > If a module is run alone, then                  __name__ = "__main__"
    > If the module is imported in another module the __name__ = "<moduleName>"
    
    Ex: 
        Case1 :: When both modules are run individually
        ``demo.py                                  ``Calc.py
          
          print("In Demo") ==>  In Demo      or      print("In Calc") ==> In Calc
          print(__name__)  ==>  __main__             print(__name__)  ==> __main__
          
          
        Case2 :: When one is imported in the other
        ``demo.py                              |    ``Calc.py
          import Calc                          |
                                               |  
          print("In Demo: ",__name__)          |     print("In Calc: ", __name__)     
        
        -> When demo.py is run ==> In Calc: Calc
                                   In Demo: __main__ 
                                   
        Case3 :: When one is imported in the other and to customize the main                   
        ``demo.py                              |    ``Calc.py
          import Calc                          |
                                               |
          def main():                          |      print("In Calc: ", __name__)
              print("In Demo: ",__name__)      |          
                                               |
          if __name__== "__main__":            |      if __name__== "__main__":             | 
              main()                           |          main()
            
         
        -> When demo.py is run ==> In Demo: __main__  
'''