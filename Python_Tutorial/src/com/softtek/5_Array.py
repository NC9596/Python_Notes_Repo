print(r'''
             *****************************************
             *   ____        _   _                   *
             *  |  _ \ _   _| |_| |__   ___  _ __    *
             *  | |_) | | | | __| '_ \ / _ \| '_ \   *
             *  |  __/| |_| | |_| | | | (_) | | | |  *
             *  |_|    \__, |\__|_| |_|\___/|_| |_|  *
             *         |___/    Array and Numpy      * 
             *                                       *
             *****************************************
''')

'''
        *************      array Module      *************

    > Array is similar to List, but all the values should be of same type
    > Array in Python do not have a fixed size, i.e. it can be shrunk or expanded  
    > To use array() we should import array module
    > To create an array we need to specify 2 things, type and values
    > Types of array: 1D Array, 2D Array[Ex: Matrix], etc
      To work with multidimensional array we should use numpy module(3rd party)
    
    > TypeCode     C Type       Pyton Type    Min. size in bytes
          b      signed char      int                  1
          B     unsigned char     int                  1
          u      Py_unicode    Unicode char            2
          h     signed short      int                  2
          H    unsigned short     int                  2
          i      signed int       int                  2
          I     unsigned int      int                  2 
          l      signed long      int                  4
          L     unsigned long     int                  4
          f         float        float                 4
          d        double       double                 8
    
    > Note: unsigned => does not consider negative values
              signed => will consider negative values
    
    > Syntax: import array
              array.array('<typeCode>',[<ListOfValues>])
    
      Ex: import array   
          a = array.array('i',[5,9,8,5,4])
    
    > More info on help('array')
'''

'''
    > important functions:
        * buffer-info(): gets a tuple with address and the size
        * append(): to add values 
        * remove(): to remove values
        * reverse(): will reverse an existing array
        * index(<value>): will give an index of the value
    
    > To copy an array into another array:
      Ex: import array   
          vals = array.array('i',[5,9,8,5,4])
          newArray = array.array(vals.typecode,(a for a in vals))
    
    > To copy an array into another array and square the values:
      Ex: import array   
          vals = array.array('i',[5,9,8,5,4])
          newArray = array.array(vals.typecode,(a*a for a in vals))
          
    > Can create an empty array:
      Ex: import array   
          vals = array.array('i',[])
'''

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
        *************      numpy Module      *************
    > pip3 install numpy
    > To work with multidimensional array
    > To declare an array with numpy module, typeCode is not necessary/optional
    
    > Syntax: import numpy                   import numpy
              numpy.array([<values>])  or    numpy.array([<values>], type) 

'''

'''
    > Ways to create array using numpy:
     1. array(): 
            import numpy
            arr = numpy.array([1,2,3,4,5])
            arr => [1,2,3,4,5]
                
        Note: The type of array is dynamic, i.e. if defined arr = array([1,2,'n'])
                then the type of this array will be changed to string 
                
     2. linspace():
            import numpy
            arr = numpy.linspace(0,5,6) [takes 0 1 2 3 4 5 and divides into 6 parts] 
            arr => [0. 1. 2. 3. 4. 5.]
        Note: linspace(<start>,<stop>,<numberOfParts>)
              <stop> and <start> is both included
              <numberOfParts> by default is 50
              
     3. logspace(): The spacing depends on the log of a value
            import numpy
            arr = numpy.logspace(0,5,6)
            arr => [1.e+00 1.e+01 1.e+02 1.e+03 1.e+04 1.e+05]
        Note: logspace(<start>,<stop>,<numberOfParts>)
              <stop> and <start> is both included
              <numberOfParts> by default is 50    
        

    4. arange(): same as range()
            import numpy
            arr = numpy.arange(1,15,2)
            arr => [1,3,5,7,9,11,13] 
        Note: arange(<start>,<stop>,<numberOfSteps>)
              <stop> is not included
              <numberOfSteps> will skip the values
              
     5. zeros(): will create an array with 0 as values
            import numpy
            arr = numpy.zeros(5)
            arr => [0. 0. 0. 0. 0.]
            
        Note: Will get float values
              To get in integer should sprcify the type, i.e. zeros(<size>,int)

     6. ones(): 
            import numpy
            arr = numpy.ones(5)
            arr => [1. 1. 1. 1. 1.]
            
        Note: Will get float values
              To get in integer should sprcify the type, i.e. ones(<size>,int)
'''

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
        *************      Array Math Operations      *************

    > We can do math operation to an array
        Ex: arr = numpy.array([1,2,3,4,5])
            arr = arr + 10
            
            arr => [11 12 13 14 15]
            
    > We can add 2 arrays and can concatenate the two arrays
        Ex: arr1 = numpy.array([1,2,3,4,5])
            arr2 = numpy.array([1,2,3,4,5])
            arr3 = arr1 + arr2
            arr3 => [2 4 6 8 10]
            
            concatenate(arr1,arr2)


    > We can do some operations on an array
        Ex: arr = numpy.array([1,2,3,4,5])
            max(arr)
            min(arr)
            log(arr)
            sum(arr)
            etc.
'''

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
        *************      Array Copying      *************

    > Cannot copy array using = operator, cos it will do Aliasing(same address)
        Ex: arr1 = numpy.array([1,2,3,4,5])
            arr2 = arr1
            => both arr1 and arr2 will point to the same address
            
    > To create an array(with different address) use view() function
        Ex: arr1 = numpy.array([1,2,3,4,5])
            arr2 = arr1.view()
            => But this will do a shallow copy, i.e. still dependent 
            
            arr1[1]=7 [Will also change the value of arr2]
            
    > To create a deep copy(i.e. 2 different arrays) use copy() function
        Ex: arr1 = numpy.array([1,2,3,4,5])
            arr2 = arr1.copy()
'''

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
        *************      Multidimensional Array      *************
    > Array inside an array is called a Multidimensional Array
    > We should import numpy module to work with Multidimensional Array
    > Important functions in numpy module: 
        -> dtype == Will give the type of data we are working with
        -> ndim  == Will give the number of dimensions/rank we have
        -> shape == Will give a tuple (<noOfRows>,<noOfColumns>)
        -> size  == Will give the size of the entire block
        -> flatten() == Will convert from Multidimensional Array to 1D array
        -> reshape(<noOfRows>,<noOfColumns>) == 1D array to 2D array
           reshape(<noOf_2D_Arrays>,<noOf_1D_Arrays>,<noOfvalues>) == 1D to 3D
        -> matrix(<array>) == Will convert a 2D array to a matrix
        Ex: arr1 = array([
                            [1,2,3],
                            [4,5,6]
                        ])
            
            arr1.dtype => int32
            arr1.ndim  => 2
            arr1.shape => (2,3)
            arr1.size  => 6
            arr2 = arr1.flatten() => [1 2 3 4 5 6]
            arr3 = arr2.reshape(2,3) => [[1 2 3]
                                         [4 5 6]]
            arr4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
            arr4 = arr2.reshape(2,2,3) => [[1 2 3]
                                           [4 5 6]
                                           
                                           [7 8 9]
                                           [10 11 12]]   
            m = matrix(arr3) => [[1 2 3]
                                 [4 5 6]]
              

'''

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
        *************      Matrix      *************
    > Matrix has lot of useful functions    
    > matrix(<array>) or matrix('<valuesInRow1>;<valuesInRow2>;<valuesInRow3'>;etc.)
      Ex: m = matrix('1 2 3; 4 5 6; 7 8 9') => [[1 2 3]
                                                [4 5 6]
                                                [7 8 9]]
    > Important functions:
        -> diagonal(<matrix>) == Will give all the diagonal elements
        -> max() == Will give the max value
        -> min() == Will give the min value
        -> Can also do Matrix Calculations: 
                m1 + m2
                m1 - m2
                m1 * m2
'''
