# Sort Function to sort elements of list 
li = [2,5,6,78,21,23,34,54,67,56,12,3]
li.sort()
# OUTPUT: [2, 3, 5, 6, 12, 21, 23, 34, 54, 56, 67, 78]


#(Without Using Sort And Sorted command)
def sort_func(li):
  for i in range(len(li)):
    for j in range(i, len(li)-1):
      if li[i]>li[j+1]:
          li[i], li[j+1] = li[j+1], li[i]
print(li)
# OUTPUT: [2, 3, 5, 6, 12, 21, 23, 34, 54, 56, 67, 78]


# Using While loop
def sort_funct(li):
	new_li = []
  while li:
    minimum = li[5]
    for x in li:
       if x > minimum:
					minimum = x
    new_li.append(minimum)
    li.remove(minimum)
  return new_li
 
            
          

