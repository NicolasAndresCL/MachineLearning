import pandas as pd
from sklearn.ensemble import VotingRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
# Carga el archivo CSV como un DataFrame de Pandas
data = pd.read_csv('niños.csv')
# Divide el DataFrame en características y etiquetas
X = data[['peso', 'sexo', 'altura']]
y = data['talla']
# Crea una lista de modelos
models = [
    ('decision_tree', DecisionTreeRegressor()),
    ('linear_regression', LinearRegression()),
    ('k_neighbors', KNeighborsRegressor(n_neighbors=5))
]
# Crea un modelo de ensamble con los modelos anteriores
model = VotingRegressor(models)
# Entrena el modelo con los datos
model.fit(X, y)
# Función para interpretar el sexo
def interpretar_sexo(sexo):
    """
    Convierte un valor numérico del sexo a su representación en texto.

    Parámetros:
    - valor (int): 1 para masculino, 0 para femenino.

    Retorna:
    - str: 'masculino' o 'femenino' según corresponda.
    """
    if sexo == 1:
        return "masculino"
    elif sexo == 0:
        return "femenino"
    else:
        return "valor no válido"
# Hace una predicción con el modelo
peso = 25
sexo = 0 # 1 representa chico
altura = 130

# Interpretar el sexo    
sexo_texto = interpretar_sexo(sexo)
print(f'El sexo es: {sexo_texto}')

talla_predicha = model.predict([[peso, sexo, altura]])
print(f'Para un peso de {peso} kg, una altura de {altura} cm y un sexo {sexo_texto}, se predice una talla de {talla_predicha[0]:.2f} cm.')