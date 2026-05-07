import pandas as pd

homelessness = pd.read_csv('homelessness.csv')

# Uso de métodos y atributos para revisar los valores de un dataframe

# Métodos: Describe una propiedad

homelessness.head() # Devuelve las primeras filas, el encabezado del df

homelessness.info() # Muestra información sobre cada una de las columnas, como el tipo de datos y el número de valores que faltan

homelessness.describe() # Calcula unas cuantas estadisticas sumarias para cada columna

# Atributos: Realiza una operacion

homelessness.shape # Devuelve el número de filas y columnas del df

homelessness.values # Matriz de NumPy bidimensional de valores

homelessness.columns # Indice de columnas, con nombres de columnas

homelessness.index # Indice de filas, con los números o nombres de las filas