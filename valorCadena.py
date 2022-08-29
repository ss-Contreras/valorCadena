print("======================================================")
tamanoletra = input("Digite una palabra: ")

def cadena(tamanoletra):
    tamano = 0
    for i in tamanoletra:
        if i == " ":
            continue
        tamano = tamano + 1
    return tamano
    
tamano = cadena(tamanoletra)

print(f"El tamaño de la cadena de caracteres es de {tamano}")
print("======================================================")