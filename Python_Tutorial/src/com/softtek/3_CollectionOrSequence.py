print(r'''
             *****************************************
             *   ____        _   _                   *
             *  |  _ \ _   _| |_| |__   ___  _ __    *
             *  | |_) | | | | __| '_ \ / _ \| '_ \   *
             *  |  __/| |_| | |_| | | | (_) | | | |  *
             *  |_|    \__, |\__|_| |_|\___/|_| |_|  *
             *         |___/  Collection/Sequence    * 
             *                                       *
             *****************************************
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
      VALUES: can be anything, even another Dictionary
    > Dictionary can also be created using 2 Lists/Sets, use zip() and dict()
    
        Note: zip() function 
            --> zip() function is used to join 2 lists and save it in another var
            
            Ex: keys = [1,2,3]
                values = ['NC','DB','YC']
                
                | zipper = zip(keys,values)
                | print(zipper)         ==> will give only the address
                  
                | zipper = list(zip(keys,values))
                | print(zipper)         ==> will give in list format
                  
                | zipper = set(zip(keys,values))
                | print(zipper)         ==> will give in set format        
            
                | zipper = dict(zip(keys, values)) 
                | print(zipper)         ==> will give in dictionary format
                
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

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
        *************      Search Element in List      *************

    1. Linear Search:
        > Will search the one by one
        
        Ex: 
            def search(list, n):
                for i in range(0,len(list)):
                    if list[i] == n:
                        return True
                return False
            
            list = [5,8,4,6,9,2]
            n=9
            
            if search(list, n):
                print('Found')      ==> Found
            else:
                print('Not Found')

    2. Binary Search:
        > Values Must be sorted
        > Should specify the lower bound, upper bound and the mid index
        > Then the value to be searched will be compared with the mid index value
        > Then the upper bound, lower bound and mid index will be changed:
            --> If value to be searched < mid value 
                ==> Upper bound will be mid index
                ==> Lower bound will be the same
                ==> Mid index will be according to the new upper and lower bound
          
        Ex: def search(list, n):
                lowerBound = 0
                upperBound = len(list) - 1
                
                while(lowerBound <= upperBound):
                    mid = (lowerBound + upperBound)//2   ==> int division
                    
                    if list[mid] == n:
                        return True
                    
                    else:
                        if list[mid] < n:
                            lowerBound = mid + 1
                        else:
                            upperBound = mid - 1
                            
                return False
            
            list = [5,8,4,6,9,2]
            n=9
            
            if search(list, n):
                print('Found')      ==> Found
            else:
                print('Not Found')

'''

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
        *************      Sorting of Elements in List      *************
    
    1. Bubble Sort:
        > Compare the first 2 values => Then if 1st>2nd ==> Swap
        > Continue till 1st<2nd<3rd<....etc.
        
        Ex: def sort(nums):
        
                for i in range(len(nums)-1,0,-1):
                    for j in range(i):
                        if nums[j]>nums[j+1]:
                            temp = nums[j]
                            nums[j] = nums[j+1]
                            nums[j+1] = temp
                            
                        print(nums)
                            
            nums = [5,3,8,6,7,2]
            
            sort(nums)   
            print(nums)   ==>  [2,3,5,6,7,8]
            
    2. Selection Sort:
        > In bubble sort, in each iteration we swap numbers ==> takes time
        > In selection sort, we will find the min value from the list
        > Then, swap it with the first element 
            ==> we will have sorted and unsorted array
            ==> continue till we get the sorted array
        
        Ex: def sort(nums):
        
                for i in range(len(nums)-1):
                    minPosition = i
                    for j in range(i,len(nums)):
                        if nums[j]<nums[minPosition]:
                            minPosition = j
                            
                    temp = nums[i]
                    nums[i] = nums[minPosition]
                    nums[minPosition] = temp
                    print(nums)
                            
            nums = [5,3,8,6,7,2]
            
            sort(nums)   
            print(nums)   ==>  [2,3,5,6,7,8] 
'''