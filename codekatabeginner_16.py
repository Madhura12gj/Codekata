m,a =input().split()
m= int(m)  
a= int(a)  
for num in range(m+1,a):  
  if num > 1:
    for i in range(2,num):
       if (num % i) == 0:
         break
    else:
      print(num, end=" ") 
