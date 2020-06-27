str_input = input()
str_temp = ''
for i in str_input:
    if i.isupper():
        str_temp += "_" + i.lower()
    else:
        str_temp += i
print(str_temp)