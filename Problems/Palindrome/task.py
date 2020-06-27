str_input = input()
str_temp = ''
for x in str_input:
    str_temp = x + str_temp
if str_temp == str_input:
    print("Palindrome")
else:
    print("Not palindrome")