def validarRango(numero):
  if numero >= 100 and numero <= 200 :
    print (f" {numero}, se encuentra dentro del rango")
  else:
    print (f" {numero}, no se encuentra dentro del rango")
      
def validarMultiplo3(numero):
  if numero % 3==0 :
    print (f" {numero} si es multiplo de 3")
  else:
    print(f" {numero} no es multiplo de 3")
      
def validarNumeros(numero):
  validarRango(numero)
  validarMultiplo3(numero)
      
