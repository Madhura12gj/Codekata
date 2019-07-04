urstri = input()
print(''.join([ urstri[x:x+2][::-1] for x in range(0, len(urstri), 2) ]))
