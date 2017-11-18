def DeterminarLaSuma(num1, num2, num3):
  if(num1 == num2 + num3):
    print("la suma de los numeros es ", num1)
  elif(num2 == num1 + num3):
    print("la suma de los numeros es ", num2)
  elif(num3 == num2 + num1):
    print("la suma de los numeros es ", num3)
  else:
    print("no hay numero que de suma de los otros")
    
DeterminarLaSuma(4, 8, 4)