def chop(lst):
    """Removes the first and last elements from the list, if possible."""
    if len(lst) < 2:  # If the list has 0 or 1 elements, return immediately
        return
    del lst[0]
    del lst[-1]

What changed?
Instead of:

if len(lst) > 1:
    del lst[0]
    del lst[-1]
elif len(lst) == 1:
    lst.clear()

We now use:

if len(lst) < 2:
    return
