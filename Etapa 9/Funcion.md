# Explicación Detallada del Compresor de Texto Simple

Este documento explica en detalle cómo funciona el compresor de texto simple implementado en Python. El programa permite comprimir texto reemplazando palabras comunes con códigos numéricos más cortos.

## 1. Estructura del Diccionario (`crear_diccionario`)

La función `crear_diccionario()` es la base del sistema de compresión:

- Contiene una lista predefinida de palabras comunes en español
- Asigna un número único (convertido a string) a cada palabra
- Por ejemplo: "el" → "0", "sol" → "1", etc.
- Este diccionario se usa tanto para comprimir como para descomprimir

### Ejemplo de Diccionario:
```python
{
    "el": "0",
    "sol": "1",
    "brillaba": "2",
    ...
}
```

## 2. Proceso de Compresión (`comprimir_texto`)

La función `comprimir_texto(texto)` realiza la compresión siguiendo estos pasos:

1. **Preparación**:
   - Convierte todo el texto a minúsculas
   - Crea una lista vacía para el resultado
   - Inicializa una variable para ir construyendo palabras

2. **Procesamiento carácter por carácter**:
   - Si es una letra: la añade a la palabra actual
   - Si es otro carácter (espacio, puntuación):
     * Procesa la palabra acumulada (si existe)
     * Añade el carácter tal cual al resultado

3. **Procesamiento de palabras**:
   - Si la palabra está en el diccionario: usa su código
   - Si no está: mantiene la palabra original

### Ejemplo de Compresión:
```
Entrada: "El sol brillaba"
Proceso: "el" → "0", "sol" → "1", "brillaba" → "2"
Salida: "0 1 2"
```

## 3. Proceso de Descompresión (`descomprimir_texto`)

La función `descomprimir_texto(texto_comprimido)` revierte el proceso:

1. **Preparación**:
   - Crea un diccionario inverso (código → palabra)
   - Inicializa variables para el resultado y números temporales

2. **Procesamiento carácter por carácter**:
   - Si es un dígito: lo acumula
   - Si es otro carácter:
     * Procesa el número acumulado (si existe)
     * Añade el carácter tal cual

3. **Procesamiento de códigos**:
   - Si el código existe: usa la palabra original
   - Si no existe: mantiene el número

### Ejemplo de Descompresión:
```
Entrada: "0 1 2"
Proceso: "0" → "el", "1" → "sol", "2" → "brillaba"
Salida: "el sol brillaba"
```

## 4. Cálculo de Tamaño (`calcular_tamano`)

La función `calcular_tamano(texto)` mide el tamaño en bytes:
- Convierte el texto a UTF-8
- Cuenta los bytes resultantes
- Usado para calcular la eficiencia de la compresión

## 5. Función Principal (`main`)

La función `main()` coordina todo el proceso:

1. **Entrada**:
   - Pide el texto al usuario
   - Muestra el texto original y su tamaño

2. **Procesamiento**:
   - Comprime el texto
   - Descomprime el texto
   - Calcula estadísticas

3. **Salida**:
   - Muestra el texto comprimido y su tamaño
   - Muestra el texto descomprimido
   - Muestra el porcentaje de compresión

## Ejemplo Completo

```
Entrada: "El sol brillaba en el cielo azul"
Comprimido: "0 1 2 3 0 4 5"
Descomprimido: "el sol brillaba en el cielo azul"
```