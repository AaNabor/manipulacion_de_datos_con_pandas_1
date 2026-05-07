import pandas as pd

homelessness = pd.read_csv('homelessness.csv')

# Filtra homelessness para los casos en los que el censo de EE.UU 'state' aparece en la lista de estados de Mojave, canu, asignandolos a 'mojave_homelessness'

canu = ["California", "Arizona", "Nevada", "Utah"]

mojave_homelessness = homelessness[homelessness['state'].isin(canu)]

print(mojave_homelessness)
