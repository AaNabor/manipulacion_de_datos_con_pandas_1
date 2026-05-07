import pandas as pd

homelessness = pd.read_csv('homelessness.csv')

# Crea una serie llamada 'individuals' que contenga solo la columna 'individuals' de 'homelessness'

individuals = homelessness['individuals']

print(individuals.head())

# Crea un DataFrame llamado 'state_fam' que contenga solo las columnas 'state' y 'family_members' de 'homelessness' en ese orden

state_fam = homelessness[['state', 'family_members']]

print(state_fam.head())

# Crea un DataFrame llamado 'ind_state' que contenga las columnas 'individuals' y 'state' de 'homelessness' en ese orden

ind_state = homelessness[['individuals', 'state']]

print(ind_state.head())