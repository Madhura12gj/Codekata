nm=int(input())
sum=0
t=nm
while t>0:
  digit=t%10
  sum+=digit**3
  t//=10
if nm==sum:
  print("yes")
else:
  print("no")
