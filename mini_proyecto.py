import pandas as pd

homelessness = pd.read_csv("homelessness.csv")

# ¿Qué estado tiene el mayor numero de personas sin hogar por cada 10 mil habitantes?

# Añade una columna a homelessness, 'ind_per_10k' que contenga el numero de personas sin hogar por cada 10 mil personas en cada estado, utilizando 'state_pop' para la poblacion del estado

homelessness['ind_per_10k'] = 10000 * homelessness['individuals'] / homelessness['state_pop']

# Subconjunta las filas en las que 'ind_per_10k' sea superior a 20, asignandolas a 'high_homelessness'

high_homelessness = homelessness[homelessness['ind_per_10k'] > 20]

# Ordena 'high_homelessness' aplicando el orden descendente a 'ind_per_10k' y asignandolo a 'high_homelessness_srt'

high_homelessness_srt = high_homelessness.sort_values('ind_per_10k', ascending= False)

# Selecciona las columnas 'state' e 'ind_per_10k' de 'high_homelessness_srt' y guardalas como 'result'

result = high_homelessness_srt[['state', 'ind_per_10k']]

print(result)

# El análisis revela que, al normalizar la métrica poblacional, el Distrito de Columbia presenta la mayor tasa de incidencia con 53.73 personas sin hogar por cada 10,000 habitantes. Como siguiente paso, se sugiere cruzar esta información con datos de costo de vivienda estatal para evaluar posibles correlaciones.