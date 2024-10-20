def crear_diccionario():
    palabras = [
        # Palabras del ejemplo
        "el", "sol", "brillaba", "en", "cielo", "azul", "sin", 
        "nubes", "radiante", "y", "sereno",
        
        # Artículos y determinantes
        "la", "los", "las", "un", "una", "unos", "unas",
        
        # Verbos comunes
        "es", "está", "era", "fue", "ser", "estar", "hacer",
        "tiene", "va", "dice", "hacer", "ver", "dar", "saber",
        
        # Sustantivos comunes
        "día", "tiempo", "año", "vida", "mundo", "casa", "agua",
        "tierra", "aire", "fuego", "mar", "montaña", "río",
        
        # Adjetivos comunes
        "grande", "pequeño", "bueno", "malo", "alto", "bajo",
        "feliz", "triste", "hermoso", "feo", "claro", "oscuro",
        
        # Preposiciones y conjunciones
        "de", "a", "con", "por", "para", "entre", "sobre",
        "pero", "mas", "aunque", "sino", "porque", "pues",
        
        # Adverbios
        "muy", "bien", "mal", "así", "ahora", "después",
        "antes", "cerca", "lejos", "siempre", "nunca",
        
        # Pronombres
        "yo", "tú", "él", "ella", "nosotros", "vosotros",
        "ellos", "ellas", "me", "te", "se", "nos", "os"
    ]
    
    diccionario = {}
    for i, palabra in enumerate(palabras):
        diccionario[palabra] = str(i)
    return diccionario

def comprimir_texto(texto):

    diccionario = crear_diccionario()

    texto = texto.lower()

    resultado = []
    palabra_actual = ""
    
    for caracter in texto:
        if caracter.isalpha():
            palabra_actual += caracter
        else:
            if palabra_actual:
                if palabra_actual in diccionario:
                    resultado.append(diccionario[palabra_actual])
                else:
                    resultado.append(palabra_actual)
                palabra_actual = ""
            resultado.append(caracter)

    if palabra_actual:
        if palabra_actual in diccionario:
            resultado.append(diccionario[palabra_actual])
        else:
            resultado.append(palabra_actual)
    
    return "".join(resultado)

def descomprimir_texto(texto_comprimido):

    diccionario = crear_diccionario()
    diccionario_inverso = {}
    for palabra, codigo in diccionario.items():
        diccionario_inverso[codigo] = palabra

    resultado = []
    numero = ""
    
    for caracter in texto_comprimido:
        if caracter.isdigit():
            numero += caracter
        else:
            if numero:
                if numero in diccionario_inverso:
                    resultado.append(diccionario_inverso[numero])
                else:
                    resultado.append(numero)
                numero = ""
            resultado.append(caracter)

    if numero:
        if numero in diccionario_inverso:
            resultado.append(diccionario_inverso[numero])
        else:
            resultado.append(numero)
    
    return "".join(resultado)

def calcular_tamano(texto):
    return len(texto.encode('utf-8'))

def main():
    print("Ingrese el texto a comprimir:")
    texto_original = input()

    texto_comprimido = comprimir_texto(texto_original)

    print("\nResultados:")
    print(f"Texto original ({calcular_tamano(texto_original)} bytes):")
    print(texto_original)
    print(f"\nTexto comprimido ({calcular_tamano(texto_comprimido)} bytes):")
    print(texto_comprimido)

    texto_descomprimido = descomprimir_texto(texto_comprimido)
    print("\nTexto descomprimido:")
    print(texto_descomprimido)

    bytes_original = calcular_tamano(texto_original)
    bytes_comprimido = calcular_tamano(texto_comprimido)
    porcentaje = ((bytes_original - bytes_comprimido) / bytes_original) * 100
    print(f"\nPorcentaje de compresión: {porcentaje:.1f}%")

if __name__ == "__main__":
    main()