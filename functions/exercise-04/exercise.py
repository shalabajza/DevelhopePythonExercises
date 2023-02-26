namelist = [['John','Doe'],['Tristram','Mcbride'],['Baldwin','Preston'],['Wally','Collins']]

def hello(name = 'John', surname = 'Doe'):
    print('Hello', name, surname)

for i in range(len(namelist)):
    hello(namelist[i][0], namelist[i][1])
