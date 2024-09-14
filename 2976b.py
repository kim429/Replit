str_DKSH = str(input())
count = 0
for i in range(0,len(str_DKSH)):
  if i < len(str_DKSH)-3 and str_DKSH[i] == 'D' and str_DKSH[i+1] == 'K' and str_DKSH[i+2] == 'S' and str_DKSH[i+3] == 'H':
    count += 1

print(count)