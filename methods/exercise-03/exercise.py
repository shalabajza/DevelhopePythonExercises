num1 = 1122334455666

num1_str = str(num1)
print("string length: ", len(num1_str))
print("third element: ", num1_str[2])
print("elements 3-5: ", num1_str[2:5])

# check if num2, num3 in string? 
# decided to use placeholder values as a proof of concept

num2 = 112
num3 = 45567

print(str(num2) in num1_str)
print(str(num3) in num1_str)

string_with_0 = '0' + num1_str
print(string_with_0[0:4])
print(string_with_0[5:])

#### use negative indexing to reach the "567" string_with_0
# There is no '567' part in the string. I'll just add that to the end if that's what you wanted to do
string_with_0 += "567"
print(string_with_0[-3:])