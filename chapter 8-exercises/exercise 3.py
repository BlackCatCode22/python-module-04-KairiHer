The potential issue in the previous program is with this part of the code:

if len(lst) > 1:
    del lst[0]   
    del lst[-1]  
elif len(lst) == 1:
    lst.clear()  

How to break the program?
Try passing an empty list ([]) to chop():

nums = []
chop(nums) 

Fixed Version of chop()
Modify chop() to check for an empty list before attempting to remove elements:
def chop(lst):
    """Safely removes the first and last elements from the list."""
    if len(lst) < 2:
        return  
    del lst[0]  
    del lst[-1]  
