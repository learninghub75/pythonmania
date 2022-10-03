# Prime Numbers between 100 to 200
# Hint: for loop

for num in range(101,200):
    for j in range(2, num):
      if num%j != 0:
        #print(f"{num} is not prime Number")
       break:
    else:
      print(f"{num} is prime Number")
