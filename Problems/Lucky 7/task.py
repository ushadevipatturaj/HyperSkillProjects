num = int(input())
x = []
for _ in range(num):
    x.append(int(input()))
for i in x:
    if i % 7 == 0:
        print(i ** 2)
