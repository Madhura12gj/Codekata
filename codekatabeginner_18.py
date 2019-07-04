l=int(input())
u=int(input())

for num in range(l, u + 1):
  ord = len(str(num))
  sum = 0 
  tmp = num
  while tmp > 0:
    dg = tmp % 10
    sum += dg ** ord
    tmp //= 10
  if num == sum:
    print(num)
