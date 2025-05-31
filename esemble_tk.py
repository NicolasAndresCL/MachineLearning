import pandas as pd
from sklearn.ensemble import VotingRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
import tkinter as tk
from tkinter import messagebox, ttk

# Cargar datos
data = pd.read_csv('niños.csv')
X = data[['peso', 'sexo', 'altura']]
y = data['talla']

# Modelo ensemble
model = VotingRegressor([
    ('dt', DecisionTreeRegressor()),
    ('lr', LinearRegression()),
    ('knn', KNeighborsRegressor(n_neighbors=5))
])
model.fit(X, y)

def predecir():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        sexo = sexo_var.get()
    except Exception:
        messagebox.showerror("Error", "Ingrese valores válidos.")
        return
    talla_predicha = model.predict([[peso, sexo, altura]])[0]
    sexo_texto = "Masculino" if sexo == 1 else "Femenino"
    resultado.set(f"Sexo: {sexo_texto}\nTalla predicha: {talla_predicha:.2f} cm")

# Interfaz
root = tk.Tk()
root.title("Predicción de Talla")
root.geometry("320x250")
root.resizable(False, False)
root.configure(bg="#f0f4f8")

frame = ttk.Frame(root, padding=20)
frame.pack(expand=True)

ttk.Label(frame, text="Peso (kg):").grid(row=0, column=0, sticky="w", pady=5)
entry_peso = ttk.Entry(frame, width=15)
entry_peso.grid(row=0, column=1, pady=5)

ttk.Label(frame, text="Altura (cm):").grid(row=1, column=0, sticky="w", pady=5)
entry_altura = ttk.Entry(frame, width=15)
entry_altura.grid(row=1, column=1, pady=5)

ttk.Label(frame, text="Sexo:").grid(row=2, column=0, sticky="w", pady=5)
sexo_var = tk.IntVar(value=0)
sexo_frame = ttk.Frame(frame)
sexo_frame.grid(row=2, column=1, pady=5)
ttk.Radiobutton(sexo_frame, text="Femenino", variable=sexo_var, value=0).pack(side="left")
ttk.Radiobutton(sexo_frame, text="Masculino", variable=sexo_var, value=1).pack(side="left")

ttk.Button(frame, text="Predecir", command=predecir).grid(row=3, column=0, columnspan=2, pady=15)

resultado = tk.StringVar()
ttk.Label(frame, textvariable=resultado, foreground="#1565c0", font=("Segoe UI", 11, "bold")).grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
