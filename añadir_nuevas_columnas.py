import pandas as pd

homelessness = pd.read_csv("homelessness.csv")

# Añade una columna a homelessness, denominada 'total', que contenga la suma de las columnas 'individuals' y 'family_members'

homelessness['total'] = homelessness['individuals'] + homelessness['family_members']

# Añade otra columna a homelessness denominada 'p_homeless', que contenga la proporcion de la poblacion de personas sin hogar total respecto a la poblacion total de cada estado 'state_pop'

homelessness['p_homeless'] = homelessness['total'] / homelessness['state_pop']

print(homelessness)