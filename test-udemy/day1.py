respuesta_1 = input("¿Cuál ha sido la cerveza con mejor gusto que has probado?: ").split()
while len(respuesta_1) > 2:
    print("Por favor ingresa máximo dos palabras.")
    respuesta_1 = input("¿Cuál ha sido la cerveza con mejor gusto que has probado?: ").split()
print("Tu mejor cerveza es: " + ' '.join(respuesta_1))
respuesta_2 = input("¿Dónde sería el mejor lugar para compartir una?: ").split()
while len(respuesta_2) > 2:         
    print("Por favor ingresa máximo dos palabras.")
    respuesta_2 = input("¿Dónde sería el mejor lugar para compartir una?: ").split()
print("Que gran lugar es "  + ' '.join(respuesta_2))
input("Por último... ¿Cuál es el nombre que le pondrías a tu propia cerveza?: ")
print("¡Felicitaciones por responder estas preguntas de mierda! 😎")






