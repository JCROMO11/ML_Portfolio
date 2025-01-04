# Word Count Pipeline

Este proyecto tiene como objetivo procesar archivos de texto ubicados en un directorio de entrada, limpiar y contar las palabras que contienen, y guardar los resultados en un archivo de salida. Utiliza Python y la librería Pandas para manejar y procesar los datos de manera eficiente.

## Requisitos

- Python 3.x
- Pandas (se puede instalar con `pip install pandas`)

## Descripción de las Funciones

1. **`load_input(input_directory)`**: 
   - Carga todos los archivos de texto en el directorio `input_directory/` y los almacena en un DataFrame de Pandas.
   - Cada línea de texto de los archivos se convierte en una fila en el DataFrame.

2. **`clean_text(dataframe)`**: 
   - Limpia el texto eliminando puntuaciones y convirtiéndolo a minúsculas.
   
3. **`count_words(dataframe)`**: 
   - Cuenta las palabras en los textos y devuelve un DataFrame con el número total de ocurrencias de cada palabra.
   
4. **`count_words2(dataframe)`**: 
   - Alternativa a `count_words`, utiliza el método `value_counts` de Pandas para contar las palabras y devuelve el conteo de palabras de forma más compacta.

5. **`save_output(dataframe, output_filename)`**: 
   - Guarda el DataFrame resultante en un archivo de salida con formato `.txt` (tab-separated).

6. **`run(input_directory, output_filename)`**: 
   - Orquesta todas las funciones anteriores: carga los archivos, limpia el texto, cuenta las palabras y guarda el resultado.
