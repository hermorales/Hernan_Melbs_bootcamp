def add_one(n):
    result = n + 1
    return result
    
#print add_one(10)

# recursive solution
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

#print factorial(1)

# while loop solution
def factorial(n):
    total = 1
    while n > 1:
        total *= n
        n -= 1
    return total
    
#print factorial(1)

# for loop solution
def factorial(n):
    total = 1
    for i in range(1,n+1):
        total *= i
    return total

#print factorial(1)

#Fibonacci functions
def fibonacci(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a+b
        n -= 1
    return a

    # returns the number of times base X occurs
    # in the sequence
def base_count(S,B):
        return S.count(B)
def gc_content(S):
    return (base_count(S, 'G') + 
            base_count(S, 'C')) / float(len(S))
sequence = 'GTCAGC'
print base_count(sequence, 'G')
print gc_content(sequence)



