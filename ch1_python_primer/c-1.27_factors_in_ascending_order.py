"""
C-1.27 In Section 1.8, we provided three different implementations of a generator that computes
factors of a given integer. The third of those implementations, from page 41, was the most
efficient, but we noted that it did not yield the factors in increasing order.
Modify the generator so that it reports factors in increasing order, while maintaining its general performance advantages.


# Implementation ver1:
def factors(n):                     # traditional function that computes factors
    results = []                    # store factors in a new list
    for k in range(1,n+1):
        if n % k == 0:              # divides evenly, thus k is a factor
            results.append(k)       # add k to the list of factors
    return results                  # return the entire list

# Implementation ver2:
def factors(n):                 # generator that computes factors
    for k in range(1,n+1):      # divides evenly, thus k is a factor
       if n % k == 0:
           yield k              # yield this factor as next result

# Implementation ver3:
def factors(n):             # generator that computes factors
    k = 1
    while k * k < n:        # while k < sqrt(n)
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k == n:          # special case if n is perfect square
        yield k


Reference: https://stackoverflow.com/questions/20444751/python-generator-yield-factors-in-increasing-order-beginner
"""

def factors(n):             # generator that computes factors
    k = 1
    larger_factors = []
    while k * k < n:        # while k < sqrt(n)
        if n % k == 0:
            yield k
            # yield n // k
            larger_factors.append(n // k) # temporarily append larger factors to a list
        k += 1
    if k * k == n:          # special case if n is perfect square
        yield k
    for factor in reversed(larger_factors):
        yield factor        # yield larger factors at the end

fac_num = 1000
factors = factors(fac_num)
for factor in factors:
    print(factor)

"""
output: 
1
2
4
5
8
10
20
25
40
50
100
125
200
250
500
1000
"""
