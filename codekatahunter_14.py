from itertools import permutations
m=input("")
a=permutations(m)
for i in list(a):
  print("".join(i))
