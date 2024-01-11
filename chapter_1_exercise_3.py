# Exercise 3 :  Recursive function
def sum_integers(n):
    if n == 1:
        return 1
    else:
        return n + sum_integers(n - 1)

n = 5
result = sum_integers(n)
print(f"The somme of integers from 1 to  {n} est {result}.")
