number = int(input())
start = 2
while start <= number:
    if number % start != 0:
        start += 1
        continue
    if number % start == 0 and start == number:
        print("This number is prime")
        break
    if number % start == 0:
        print("This number is not prime")
        break
else:
    print("This number is not prime")
