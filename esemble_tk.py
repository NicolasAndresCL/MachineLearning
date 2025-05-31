import pandas as pd
from sklearn.ensemble import VotingRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
import tkinter as tk
from tkinter import messagebox

# Carga el archivo CSV como un DataFrame de Pandas
data = pd.read_csv('niños.csv')
X = data[['peso', 'sexo', 'altura']]
y = data['talla']

# Modelos
models = [
    ('decision_tree', DecisionTreeRegressor()),
    ('linear_regression', LinearRegression()),
    ('k_neighbors', KNeighborsRegressor(n_neighbors=5))
]
model = VotingRegressor(models)
model.fit(X, y)

def interpretar_sexo(sexo):
    if sexo == 1:
        return "masculino"
    elif sexo == 0:
        return "femenino"
    else:
        return "valor no válido"

def predecir():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        sexo = int(entry_sexo.get())
        if sexo not in (0, 1):
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos.\nSexo: 0=femenino, 1=masculino")
        return

    sexo_texto = interpretar_sexo(sexo)
    talla_predicha = model.predict([[peso, sexo, altura]])[0]
    resultado.set(f"Sexo: {sexo_texto}\nTalla predicha: {talla_predicha:.2f} cm")

# Interfaz Tkinter
root = tk.Tk()
root.title("Predicción de Talla")

tk.Label(root, text="Peso (kg):").grid(row=0, column=0, padx=5, pady=5)
entry_peso = tk.Entry(root)
entry_peso.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Altura (cm):").grid(row=1, column=0, padx=5, pady=5)
entry_altura = tk.Entry(root)
entry_altura.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Sexo (0=femenino, 1=masculino):").grid(row=2, column=0, padx=5, pady=5)
entry_sexo = tk.Entry(root)
entry_sexo.grid(row=2, column=1, padx=5, pady=5)

tk.Button(root, text="Predecir", command=predecir).grid(row=3, column=0, columnspan=2, pady=10)

resultado = tk.StringVar()
tk.Label(root, textvariable=resultado, fg="blue").grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()