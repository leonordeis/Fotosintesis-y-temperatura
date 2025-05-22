import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def fotosintesis_neta(temp, temp_opt=25, max_fotosintesis=10, ancho=10):
    """
    Modelo simplificado de fotosíntesis neta como función de temperatura.
    temp: temperatura actual (°C)
    temp_opt: temperatura óptima para fotosíntesis (°C)
    max_fotosintesis: valor máximo de fotosíntesis neta
    ancho: controla la dispersión de la curva
    """
    return max_fotosintesis * np.exp(-((temp - temp_opt) ** 2) / (2 * ancho ** 2))

st.title("Simulación de Fotosíntesis Neta vs Temperatura")

# Slider para que el usuario seleccione la temperatura actual
temp_actual = st.slider("Selecciona la temperatura actual (°C):", 0.0, 50.0, 25.0, 0.5)

# Generar datos para la curva
temperaturas = np.linspace(0, 50, 500)
fotosintesis = fotosintesis_neta(temperaturas)

# Crear la gráfica
fig, ax = plt.subplots()
ax.plot(temperaturas, fotosintesis, label="Curva fotosíntesis neta")
ax.axvline(temp_actual, color="red", linestyle="--", label=f"Temperatura actual: {temp_actual} °C")
ax.scatter([temp_actual], [fotosintesis_neta(temp_actual)], color="red")
ax.set_xlabel("Temperatura (°C)")
ax.set_ylabel("Fotosíntesis neta (unidades arbitrarias)")
ax.set_title("Simulación de Fotosíntesis Neta vs Temperatura")
ax.legend()
ax.grid(True)

# Mostrar la gráfica en Streamlit
st.pyplot(fig)