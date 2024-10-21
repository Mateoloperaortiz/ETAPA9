class Diccionario:
    def __init__(self):
        self.palabra_a_codigo = {}
        self.codigo_a_palabra = {}
        self.frecuencias = {}
        self.codigo_actual = 0

    def agregar_palabra(self, palabra):
        if palabra not in self.palabra_a_codigo:
            codigo = str(self.codigo_actual)
            self.palabra_a_codigo[palabra] = codigo
            self.codigo_a_palabra[codigo] = palabra
            self.codigo_actual += 1

    def obtener_codigo(self, palabra):
        if palabra not in self.palabra_a_codigo:
            self.agregar_palabra(palabra)
        return self.palabra_a_codigo[palabra]

    def obtener_palabra(self, codigo):
        return self.codigo_a_palabra.get(codigo, codigo)

    def actualizar_frecuencias(self, texto):
        palabras = texto.lower().split()
        for palabra in palabras:
            if palabra in self.frecuencias:
                self.frecuencias[palabra] += 1
            else:
                self.frecuencias[palabra] = 1

    def optimizar_diccionario(self):
        palabras_comunes = sorted(self.frecuencias, key=self.frecuencias.get, reverse=True)[:1000]
        self.palabra_a_codigo = {}
        self.codigo_a_palabra = {}
        self.codigo_actual = 0
        for palabra in palabras_comunes:
            self.agregar_palabra(palabra)

diccionario_global = Diccionario()

def comprimir_texto(texto):
    diccionario_global.actualizar_frecuencias(texto)
    diccionario_global.optimizar_diccionario()

    resultado = []
    palabra_actual = ""
    for caracter in texto:
        if caracter.isalpha():
            palabra_actual += caracter
        else:
            if palabra_actual:
                if palabra_actual.lower() in diccionario_global.palabra_a_codigo:
                    codigo = diccionario_global.obtener_codigo(palabra_actual.lower())
                    if palabra_actual[0].isupper():
                        resultado.append(f"{codigo}^")  # Indicador para mayúscula
                    else:
                        resultado.append(codigo)
                else:
                    resultado.append(palabra_actual)
                palabra_actual = ""
            resultado.append(caracter)
    if palabra_actual:
        if palabra_actual.lower() in diccionario_global.palabra_a_codigo:
            codigo = diccionario_global.obtener_codigo(palabra_actual.lower())
            if palabra_actual[0].isupper():
                resultado.append(f"{codigo}^")
            else:
                resultado.append(codigo)
        else:
            resultado.append(palabra_actual)
    return "".join(resultado)

def descomprimir_texto(texto_comprimido):
    resultado = []
    numero = ""
    mayuscula = False
    for caracter in texto_comprimido:
        if caracter.isdigit():
            numero += caracter
        elif caracter == "^":
            mayuscula = True
        else:
            if numero:
                palabra = diccionario_global.obtener_palabra(numero)
                if mayuscula:
                    palabra = palabra.capitalize()
                    mayuscula = False
                resultado.append(palabra)
                numero = ""
            resultado.append(caracter)
    if numero:
        palabra = diccionario_global.obtener_palabra(numero)
        if mayuscula:
            palabra = palabra.capitalize()
        resultado.append(palabra)
    return "".join(resultado)

def calcular_tamano(texto):
    return len(texto.encode('utf-8'))

def main():
    print("Ingrese el texto a comprimir:")
    texto_original = input().strip()
    
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