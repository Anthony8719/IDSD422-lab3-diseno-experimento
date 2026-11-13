
# comparacion_experimento.py — Laboratorio 3
# Comparación de grupos y simulación de un experimento

from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

# Rutas del repositorio
RAIZ = Path(__file__).resolve().parent.parent
CARPETA_DATOS = RAIZ / "plantillas"

# -----------------------------------------------------------
# 1. Cargar los datos originales
# -----------------------------------------------------------

# TODO 1: Cargar registro_experimento.csv
df = pd.read_csv(CARPETA_DATOS / "registro_experimento.csv")

print("=== DATOS ORIGINALES ===")
print(df.to_string(index=False))

# TODO 2: Calcular el promedio por ubicación

print("\n--- PROMEDIO DE VENTAS POR UBICACIÓN ---")
promedios = df.groupby("ubicacion")["ventas_producto"].mean()
print(promedios)

# TODO 3: Número de registros por grupo

print("\n--- REGISTROS POR GRUPO ---")
registros = df["ubicacion"].value_counts()
print(registros)

# TODO 4: Interpretación de los resultados

print("\n--- INTERPRETACIÓN ---")
print(
    "El pasillo principal presenta un promedio de ventas mayor "
    "que la ubicación habitual."
)
print(
    "Sin embargo, con solo cuatro registros no se puede demostrar "
    "que la ubicación sea la causa de la diferencia."
)
print(
    "Se requiere una asignación aleatoria, más observaciones "
    "y controlar factores como promociones y temporadas."
)

# -----------------------------------------------------------
# 2. Diseño experimental: 10 tiendas durante 4 semanas
# -----------------------------------------------------------

tiendas = [
    "Quito Norte",
    "Quito Sur",
    "Guayaquil Centro",
    "Guayaquil Norte",
    "Cuenca Centro",
    "Cuenca Sur",
    "Ambato Centro",
    "Manta",
    "Loja",
    "Machala"
]

semanas = [1, 2, 3, 4]


# Asignación aleatoria 
rng = np.random.default_rng(1234597)

primera = rng.choice(
    ["pasillo_principal", "habitual"],
    size=len(tiendas)
)

filas = []

for tienda, condicion in zip(tiendas, primera):

    otra = (
        "habitual"
        if condicion == "pasillo_principal"
        else "pasillo_principal"
    )

    for semana in semanas:

        ubicacion = (
            condicion
            if semana % 2 == 1
            else otra
        )

        filas.append({
            "tienda": tienda,
            "semana": semana,
            "ubicacion": ubicacion
        })

diseno = pd.DataFrame(filas)

print("\n=== ASIGNACIÓN EXPERIMENTAL ===")
print(diseno.to_string(index=False))

print("\nTotal de observaciones:", len(diseno))

print("\nDistribución por ubicación:")
print(diseno["ubicacion"].value_counts())

# -----------------------------------------------------------
# 3. Simulación del experimento
# -----------------------------------------------------------

rng = np.random.default_rng(1234598)

# Diferencias iniciales entre tiendas
efecto_tienda = dict(
    zip(
        tiendas,
        rng.normal(1100, 120, len(tiendas))
    )
)

# Variación por semana
efecto_semana = {
    1: 0,
    2: 30,
    3: 60,
    4: 90
}

# Ventas simuladas
diseno["ventas_producto"] = (
    diseno["tienda"].map(efecto_tienda)
    + diseno["semana"].map(efecto_semana)
    + (
        diseno["ubicacion"] == "pasillo_principal"
    ) * 220
    + rng.normal(0, 90, len(diseno))
).round(0).astype(int)

# Registrar promoción simultánea
diseno["promocion_simultanea"] = "no"

condicion_promocion = (
    (diseno["tienda"] == "Guayaquil Centro")
    & (diseno["semana"] == 1)
)

diseno.loc[
    condicion_promocion,
    "promocion_simultanea"
] = "si"

diseno.loc[
    condicion_promocion,
    "ventas_producto"
] += 180

# Guardar los datos simulados
ruta_salida = CARPETA_DATOS / "resultado_simulacion.csv"

diseno.to_csv(
    ruta_salida,
    index=False
)

print("\n=== SIMULACIÓN GENERADA ===")
print(diseno.to_string(index=False))

print("\nArchivo guardado en:")
print(ruta_salida)

# -----------------------------------------------------------
# 4. Comparación de ventas simuladas
# -----------------------------------------------------------

print("\n=== PROMEDIOS DE LA SIMULACIÓN ===")

promedios_simulados = diseno.groupby(
    "ubicacion"
)["ventas_producto"].mean()

print(promedios_simulados)

# Comparación pareada por tienda
piv = diseno.groupby(
    ["tienda", "ubicacion"]
)["ventas_producto"].mean().unstack()

piv["diferencia"] = (
    piv["pasillo_principal"]
    - piv["habitual"]
)

print("\n=== COMPARACIÓN POR TIENDA ===")
print(piv)

# -----------------------------------------------------------
# 5. Estadísticas de la simulación
# -----------------------------------------------------------

media = piv["diferencia"].mean()
dev = piv["diferencia"].std(ddof=1)
n = len(piv)

# Intervalo de confianza del 95 %
t_crit = stats.t.ppf(
    0.975,
    df=n - 1
)

margen_error = t_crit * dev / np.sqrt(n)

ic_inf = media - margen_error
ic_sup = media + margen_error

# Prueba t pareada
prueba = stats.ttest_rel(
    piv["pasillo_principal"],
    piv["habitual"]
)

print("\n=== RESULTADOS ESTADÍSTICOS ===")

print(f"Número de tiendas: {n}")
print(f"Diferencia media: {media:.2f} USD")
print(f"Desviación estándar: {dev:.2f} USD")

print(
    f"Intervalo de confianza 95 %: "
    f"[{ic_inf:.2f}, {ic_sup:.2f}] USD"
)

print(f"p-value: {prueba.pvalue:.8f}")

# -----------------------------------------------------------
# 6. Interpretación final
# -----------------------------------------------------------

print("\n=== INTERPRETACIÓN FINAL ===")

print(
    "Se compararon las ventas promedio de las dos ubicaciones "
    "dentro de cada una de las diez tiendas."
)

print(
    "La prueba t pareada permite analizar las diferencias "
    "entre las condiciones utilizando los promedios por tienda."
)

print(
    "Los resultados corresponden a una simulación y no "
    "demuestran un efecto real en las ventas de RetailAndina."
)

print(
    "La simulación incluye una promoción que podría influir "
    "en los resultados y debe considerarse al interpretarlos."
)
