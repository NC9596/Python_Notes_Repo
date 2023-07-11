print(r'''
             *****************************************
             *   ____        _   _                   *
             *  |  _ \ _   _| |_| |__   ___  _ __    *
             *  | |_) | | | | __| '_ \ / _ \| '_ \   *
             *  |  __/| |_| | |_| | | | (_) | | | |  *
             *  |_|    \__, |\__|_| |_|\___/|_| |_|  *
             *         |___/  Statements and Loops   * 
             *                                       *
             *****************************************
''')

'''
                 *************      If Statement      *************
    > Syntax: if ____:
                <block of code>
             
                    OR
             
              if (___):
                <block of code>    
    
    > Note: In python we do not use {} to specify a block of code
            Hence, we have to use indentation(space) to specify the block of code
    
    > Note: We can have if inside an if (nested IF)
        
'''

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
                 *************      If else Statement      *************
    > Syntax: if ____:
                <block of code>
              else:
                <block of code>
'''

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
                 *************      If else if Statement      *************
    > Syntax: if ____:
                <block of code>
              elif ____:
                <block of code>
              else:
                <block of code>
    
    
'''

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
                 *************      While Loop      *************
    > While loop is a condition check loop, i.e. condition must be specified
    > For a while loop we need a counter. 
                                                 increment
                  initialization -> condition ->    or
                                                 decrement
    > Syntax: counter initialization                                                 
              while ____:                                               
                <block of code>
                counter increment/decrement
    
    > Note: we can have while loop inside a while loop(nested WHILE)

'''

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
                 *************      For Loop      *************
    > For loop works with Sequence (tuple, list, string, set, etc.)
    > counter will be initialized and incremented internally
    > Syntax: for <variableName> in <sequence>:
                <block of code>
                
      Ex: x = ['Nc', 2, 2.9]            for i in ['Nc', 2, 2.9]:
          for i in x:            or       print(i)
            print(i)

    > Can we print first 9 digits using for loop? => use range() function
      Ex: for i in range(1,10):
            print(i)
            
    > We can have if statement inside for loop and for inside for (nested FOR)
    
    > Pattern Ex: for i in range(4):                          *
                    for j in range(i+1):        Output::      **
                      print('* ',end="")                      ***
                    print()                                   ****
'''

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
                 *************      For Else Loop      *************
    > If there is a for loop which has a condition statement along with break,
      then we can use else statement for the for-loop
    > Note: break statement is compulsory for this to work 
    
    Ex: numList = [12,13,14,16,18]
        for num in NumList:
          if num%5 == 0:
            print(num)
            break
        else:
          print("not found")
          
    Ex: num = 7
        for i in range(2,num):
          if num % i == 0
            print("Not Prime")
            break
        else:
          print("Prime")
]'''

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
                 *************      Break Continue Pass      *************
    > break: * It is a statement
             * It will get the execution out of the loop
    
    > continue: * It is a statement
                * It will skip the current iteration and continues with the next one
    
    > pass: * It is a statement
            * To specify an empty block we use pass
            * As {} is not used in Python to specify a block of code, we use pass
'''