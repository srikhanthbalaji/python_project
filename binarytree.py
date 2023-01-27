N=int(input("Enter the number of input "))
lt =[]
for i in range(0,N):
    lt.append(int(input("Enter next value ")))
try:
    print(lt.index(int(input("Enter to find value"))))
except ValueError:
    print("-1")