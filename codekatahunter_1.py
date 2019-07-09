nint=int(input())
empli=list(map(int,input().split()[:nint]))
count=0
li=[]

for i in range (0,nint+1):
  if(empli.count(i)>1):
    li.append(i)
    
if(len(li)==0):
  print("unique")

sortli=sorted(li)
print(' '.join(map(str,sortli)))
