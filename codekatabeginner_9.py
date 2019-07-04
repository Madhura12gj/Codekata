lst=[]
n=int(input())
a=int(input())
for i in range (n):
  numbers=int(input())
  lst.append(numbers)
  
k=lst[ :a]
print(sum(k))
