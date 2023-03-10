from collections import deque

#  Deque is preferred over a list in the cases where we need quicker append and pop operations from both the ends of the container
queue = deque(['name', 'age', 'DOB'])
print(queue)

# initializing deque
de = deque([1, 2, 3])
print("deque: ", de)

# using append() to insert element at right end
# inserts 4 at the end of deque
de.append(4)

# printing modified deque
print("\nThe deque after appending at right is : ")
print(de)

# using appendleft() to insert element at left end
# inserts 6 at the beginning of deque
de.appendleft(6)

# printing modified deque
print("\nThe deque after appending at left is : ")
print(de)

"""pop():- This function is used to delete an argument from the right end of the deque.
popleft():- This function is used to delete an argument from the left end of the deque."""

de2 = deque([1, 2, 3, 3, 4, 2, 4])
print ("The number 4 first occurs at a position : ")
print (de.index(4,2,5)) # index(ele, beg, end):- This function returns the first index of the value mentioned in arguments, starting searching from beg till end index.

"""
insert(i, a) :- This function inserts the value mentioned in arguments(a) at index(i) specified in arguments.
remove():- This function removes the first occurrence of the value mentioned in arguments.
count():- This function counts the number of occurrences of value mentioned in arguments."""

