n=int(input())
l1=list(map(str,input().split()))
for i in l1:
  if l1.count(i)>1:
    print(i)
    break
else:
  print("unique")
