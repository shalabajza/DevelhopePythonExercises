list1 = ["lion", "monkey", "dog","fish"]
tuple1 = ("lion", "monkey", "dog","fish")
set1 = {"lion", "monkey", "dog","fish"}
dict1 = {"lion":"land", "monkey":"land", "dog":"land","fish":"water"}

for item in list1:
    print(item)

for item in tuple1:
    print(item)

for item in set1:
    print(item)

for item in dict1:
    print(item,' lives in ',dict1[item])