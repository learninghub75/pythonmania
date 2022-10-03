## Check if number is prime or not 

## Using FOR-ELSE Loop
def check_prime(num):
    if num > 1:
        for i in range(2,num):
            if num%i == 0:
                print(f"{num} is not a prime number")
                break # not a prime number
         else:
             print(f"{num} is a prime number")

check_prime(3)

## Using IF-ELSE Loop
prime_flag = False
if num > 1:
    for i in range(2,num):
        if num%i == 0:
            prime_flag = True
            break
if prime_flag:
    print(f"{num} is not a prime number")
else:
    print(f"{num} is a prime number")



    
# Prime Numbers between 100 to 200

## Using FOR-ELSE Loop
for num in range(101,200):
    for j in range(2, num):
      if num%j != 0:
        #print(f"{num} is not prime Number")
       break:
    else:
      print(f"{num} is prime Number")
    
## Using IF-ELSE Loop
