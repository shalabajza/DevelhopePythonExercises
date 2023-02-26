def fibonacci(nr_elements):
    fib_nr = [0,1]
    for i in range(nr_elements-2):
        fib_nr.append(fib_nr[i+1] + fib_nr[i])
    return(fib_nr)

print(fibonacci(5))