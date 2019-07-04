lst=[]
n=int(input())
k=int(input())
for i in range (n):
  numbers=int(input())
  lst.append(numbers)
  
w=lst[ :k]
print(sum(w))
