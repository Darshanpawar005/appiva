# Recursive Function for Fabonacci series
def Fabonacci_recursive(n):
  if n <= 0:
    return 1
  elif n == 1:
    return 0
  else:
    return Fabonacci_recursive(n-1) + Fabonacci_recursive(n-2)
  
# Non-recursive Function for Fabonacci series
def Fabonacci_nonrecursive(n):
  if n == 0:
    return 1
  elif n == 1:
    return 0
  else:
    a = 0
    b = 1
    for i in range(0, n):
      a, b = a+b, a
    return b

# User input
n = int(input("Enter number of fabonacci series : "))
print(f"The {n}th number of fabonacci series is {Fabonacci_recursive(n)}")
print(f"The {n}th number of fabonacci series is {Fabonacci_nonrecursive(n)}")