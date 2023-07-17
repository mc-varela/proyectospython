#Define una variable de cada tipo de primitivo
nombre = "Cristina Varela"
edad = 31
peso = 162.50
estatura = 1.58
toma = False



#¿Cuál es el límite de int en Python?
#Los números se dividen en tres tipos de datos de Python: int / Integer: Int puede almacenar todos
# los valores enteros. Este tipo de datopuede ser de cualquier tamaño. No hay límite de tamaño

#"Una solución simple para restringir los flotantes a dos puntos decimales
#es usar la función integrada round(x[, n]) . devuelve numero x redondeado a n precisión
#de dígitos después del punto decimal.

sumar = 0
numero = 1

while numero !=0:
    numero = int(input("Por favor ingrese un numero:"))
    if numero != 0:
        if numero % 2 == 0:
            sumar = sumar +numero


print('Nombre',nombre)
print("Edad", edad)
print("Peso", peso, "Lbs")
print("Estatura", estatura,"m")
print("Toma", toma)
print("La suma de los numeros enteros son:", sumar)





