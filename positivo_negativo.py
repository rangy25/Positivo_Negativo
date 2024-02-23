#   Ejercicio no.5 programa para convertir si un numero es positivo o negativo

# input 
x= int(input( " digite el numero: "))
# processing 
if x > 0:
    rta="positivo"
elif x == 0:
    rta="su numero es neutro"
else:
    rta="negativo"
    
# output
print("el numero",x,"es",rta)