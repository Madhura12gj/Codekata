l,u =input().split()
l= int(l)  
u= int(u)  
for num in range(l+1,u):  
  if num > 1:
    for i in range(2,num):
       if (num % i) == 0:
         break
    else:
      print(num) 
