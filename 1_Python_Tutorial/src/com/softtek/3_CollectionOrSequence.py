print(r'''
                 ____        _   _                 
                |  _ \ _   _| |_| |__   ___  _ __  
                | |_) | | | | __| '_ \ / _ \| '_ \ 
                |  __/| |_| | |_| | | | (_) | | | |
                |_|    \__, |\__|_| |_|\___/|_| |_|
                       |___/  Collection/Sequence
''')

'''
                 *************      List      *************
    > List is a collection of values/elements
    > [] : used to define a List
    > Values can be of same data type or different
    > List is mutable(i.e. values can be changed)
    > List can contain other lists
    > List has many useful methods/functions [run help() method to know more]
      Ex: insert()
          remove()
          pop()
          extend()
'''

'''
> numbers = [1,2,3,4,5]

  numbers[0] = 1
  numbers[-5] = 1
  
> values = [1, 'nandi', 99.9]
> complexList = [numbers, values]

'''

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
                 *************      Tuple      *************
    > Similar to List, but Tuple is immutable
    > () : used to define Tuple
    > Tuple has 2 methods: count() and index()
    > Usecase: Iteration in Tuple is faster than List
'''

'''
> numbers = (1,2,3,4,5)
'''

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
                 *************      Set      *************
    > Similar to List, but only contains UNIQUE elements and no sequence
    > {} : used to define Set
    > Set is mutable
    > Set will NOT follow a sequence, it will just store the values, not the order      
'''

'''
> set = {1,8,7,0,9,5}
'''

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
                 *************      Dictionary      *************
    > Like Map, to store KEY-VALUE pair
    > KEY: should be of immutable type(like string, int, etc.)
    > VALUES: can be anything, even another Dictionary
    > Dictionary can also be created using 2 Lists/Sets, use zip() and dict()
    > Dictionary has many useful methods/functions [run help() method to know more]
      Ex: get()
'''

'''
> data = {1:'NC',2:'DB',3:'YC'}
  data[3] = YC
  data.get(1) = NC
  
  for i,j in data.items():
        print(i,j)            => 1 NC
                                 2 DB
                                 3 YC

> keys = [1,2,3]
  values = ['NC','DB','YC']
  data = dict(zip(keys, values)) 
'''

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
                 *************      Range      *************
    > When we iterate through the values, use Range
    > Range will give the values present in the given range of numbers
    > Can also take 3 parameters, to specify the difference b/t the numbers
'''

'''
> range(10)
    range(0,10)
> list(range(10)) = [0,1,2,3,4,5,6,7,8,9] // to convert from range to list
> list(range(3,10,2)) = [3,5,7,9]
> list(range(10,3,-2)) = [10,8,6,4]
'''
