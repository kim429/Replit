A = int(input())
B = int(input())
C = int(input())
mul_ABC = str(A*B*C)
for i in range(10) :
  print(mul_ABC.count(str(i)))