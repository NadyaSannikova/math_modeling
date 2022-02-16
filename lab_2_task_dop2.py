a,b,c=map(int,input().split())
if a<=b+c or b<=c+a or c<=a+b:
  print("Такой треугольник есть.")
  if a==b==c:
    print("Равносторонний")
  elif a!=b and b!=c and a!=c:
    print("Разносторонний")
  else:
    print("Равнобедренный")