# Designer Door Mat

x = input().split( )
n = int(x[0])
m = int(x[1])
l = int((n-1)/2)
for i in range(1,l+1):
  print((".|."*(2*i-1)).center(m,'-'))
  
print("WELCOME".center(m,'-'))

for i in range(l,0,-1):
  print((".|."*(2*i-1)).center(m,'-'))
