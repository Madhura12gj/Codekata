lst=[]
n=int(input())
k=int(input())
for i in range (n):
  numbers=int(input())
  lst.append(numbers)
  
a=lst[ :k]
print(sum(a))
