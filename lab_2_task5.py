a,b=map(int,input().split())
if a%b==0:
  print("a делится на b")
  print("Частное: ",a//b)
else:
  print("a не делится на b")
  print("Остаток: ",a%b)
  print("Частное: ",a//b)