def chop(lst):
    """Removes the first and last elements from the list and returns None."""
    if len(lst) > 1:
        del lst[0]   
        del lst[-1]  
    elif len(lst) == 1:
        lst.clear()  

def middle(lst):
    """Returns a new list containing all but the first and last elements."""
    return lst[1:-1]  
  

nums = [1, 2, 3, 4, 5]

print("Original list:", nums)
chop(nums)
print("After chop:", nums) 

nums2 = [1, 2, 3, 4, 5]
print("Middle:", middle(nums2)) 
