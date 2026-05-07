# 🐍 Manipulación de Datos con Pandas 1 🐼

<p>En este repositorio se documentan conceptos básicos para comenzar a manipular datos con pandas 🐼. <br>
Los ejercicios y dataset usados son parte del bootcamp de analista de datos con python 🐍. <br>
Trabajé con un dataset que contiene información sobre la población de Estados Unidos que no tiene acceso a la vivienda 🏠</p>

## Contenido 📖

1. #### Transformación de DataFrames  <br>
<p> Uso de <strong>.head(), .info(), .shape, .describe()</strong></p>

2. #### Ordenar filas <br>
<p> Uso de <strong>.sort_values()</strong></p>

3. #### Subconjunto de columnas <br>
<p> Selección de columnas <strong>df["col_a], df[["col_a", "col_b"]]</strong></p>

4. #### Subconjunto de filas <br>
<p> Selección de filas <strong>df[df["row_a"]], operador & (AND)</strong></p>

5. #### Subconjuntos de filas por variables categóricas <br>
<p> Uso del <strong>operador | (OR), .isin()</strong></p>

6. #### Añadir filas <br>
<p> Añadir nuevas columnas a partir operaciones con otras columnas <strong>df["new_col"] = df["col_a"] + df["col_b"]</strong></p>

7. #### Analisis: ¿Qué estado tiene el mayor número de personas sin hogar por cada 10mil habitantes? <br>
<p>El análisis revela que, al normalizar la métrica poblacional, el Distrito de Columbia presenta la mayor tasa de incidencia con 53.73 personas sin hogar por cada 10,000 habitantes. Como siguiente paso, se sugiere cruzar esta información con datos de costo de vivienda estatal para evaluar posibles correlaciones.</p>
