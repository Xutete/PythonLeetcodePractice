# import heapq to implent heap queue in python
import heapq

# initializing list
li = [5, 7, 9, 1, 3]

# using heapify to convert list into heap 堆
heapq.heapify(li)


# printing created heap
print ("The created heap is: ", (list(li)))


# using heappush() to push elements into heap
# pushes 4
heapq.heappush(li, 4)

# print the modified heap
print(list(li))


# using heappop() to pop smallest element
print("The popped and smallest element is: ", end = "" )
print(heapq.heappop(li))




#
li1 = [5, 1, 9, 4, 3]
li2 = [5, 7, 9, 4, 3]


heapq.heapify(li1)
heapq.heapify(li2)

# using heappushpop() to push and pop items simultaneously
# pops 2
print("The popped item using heappushpop() is: ", end = "")
print(heapq.heappushpop(li1, 2))

# using heapreplace() to push and pop items simultaneously
# pops 3
print("The popped item using heapreplace() is :", end = "")
print(heapq.heapreplace(li2, 2))



# heapq.nlargest() & heapq.nsmallest()

li3 = [6, 7, 9, 4, 3, 5, 8, 10, 1]

# using heapify() to convert list into heap
heapq.heapify(li3)

# using nlargest to print 3 largest numbers
print("The 3 largest numbers in list are: ", end = "")
print(heapq.nlargest(3, li3))

# using nsmallest to print 3 smallest numbers
print("The 3 smallest numbers in list are: ", end = "")
print(heapq.nsmallest(3, li3))





