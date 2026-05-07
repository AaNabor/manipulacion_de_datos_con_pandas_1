import pandas as pd

homelessness = pd.read_csv('homelessness.csv')

# Ordena el data frame 'homelessness' por el número de personas sin hogar de la columna 'individuals', de menor a mayor y guardarlo como 'homeless_ind'. Imprime el encabezado del dataframe ordenado.

homelessness_ind = homelessness.sort_values('individuals')

print(homelessness_ind.head())

# Ordena 'homelessness' por el número de 'family_members' sin hogar en orden descendente y guardarlo como 'homelessness_fam'

homelessness_fam = homelessness.sort_values('family_members', ascending= False)

print(homelessness_fam.head())

# Ordena 'homelessness' primero por 'region' (ascendente) y luego por número de miembros de familia (descendente), guardarlo como 'homelessness_reg_fam

homelessness_reg_fam = homelessness.sort_values(['region', 'family_members'], ascending=[True, False])

print(homelessness_reg_fam.head())