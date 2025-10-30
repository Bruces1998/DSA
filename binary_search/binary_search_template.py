'''
This is the most basic and generalized template
to solve the problems involving binary search 
algorithm.
https://leetcode.com/discuss/general-discussion/786126/python-powerful-ultimate-binary-search-template-solved-many-problems

'''
#some condition that needs to be checked each time
def some_condition(some_variables):
    pass

#basic template of the binary search
def binary_search(array):
    
    left = 0
    right = len(array) - 1

    while(left < right):
        
        mid = left + (right - left)//2 #make sure you get this right, most of the mistakes in binary 
                                       #search are made in this part of the code
        
        if some_condition(mid):
            right = mid
        
        else:
            left = mid+1


    return left

z