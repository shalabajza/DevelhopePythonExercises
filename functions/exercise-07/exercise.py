x = lambda a : a * a if a%2==0 else a

my_list = [*range(5)] 

newlist = [x(a) for a in my_list]

print(newlist)