N = int(input())
for T in range(0,N) :
  r,e,c = map(int,input().split())
  if r < e-c :
    print("advertise")
  elif r == e-c :
    print("does not matter")
  else :
    print("do not advertise")
