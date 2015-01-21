def  maxXor( l,  r):
  max = 0
  for j in range (l, r+1):
    for k in range(l, r+1):
        xor = j ^ k
        if xor > max:
            max = xor
  return max


_l = int(raw_input());


_r = int(raw_input());

res = maxXor(_l, _r);
print(res)