a,b,c=map(float,input().split())

d=b**2-(4*a*c)
if d>0:
  x1=(-b+(d**0.5))/(2*a)
  x2=(-b-(d**0.5))/(2*a)
  print(x1,x2)
elif d==0:
  print(-b/(2*a))
else:
  print("Корней нет")