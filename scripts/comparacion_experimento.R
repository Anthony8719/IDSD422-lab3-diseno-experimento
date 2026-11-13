
# comparacion_experimento.R — Laboratorio 3
# Comparación de grupos y análisis del experimento

# -----------------------------------------------------------
# 1. Cargar los datos originales
# -----------------------------------------------------------

df <- read.csv(
  "plantillas/registro_experimento.csv",
  stringsAsFactors = FALSE
)

cat("=== DATOS ORIGINALES ===\n")
print(df)

# TODO 1: Cargar registro_experimento.csv
# TODO 2: Calcular el promedio por ubicación

cat("\n--- PROMEDIO DE VENTAS POR UBICACIÓN ---\n")

promedios <- aggregate(
  ventas_producto ~ ubicacion,
  data = df,
  FUN = mean
)

print(promedios)

# TODO 3: Contar los registros por grupo

cat("\n--- REGISTROS POR GRUPO ---\n")

registros <- table(df$ubicacion)
print(registros)

# TODO 4: Interpretación de los resultados

cat("\n--- INTERPRETACIÓN ---\n")

cat(
  "El pasillo principal presenta un promedio de ventas mayor ",
  "que la ubicación habitual.\n",
  sep = ""
)

cat(
  "Sin embargo, cuatro registros no permiten demostrar ",
  "que la ubicación sea la causa de la diferencia.\n",
  sep = ""
)

cat(
  "Se necesita una asignación aleatoria, más observaciones ",
  "y controlar promociones y otros factores externos.\n",
  sep = ""
)

# -----------------------------------------------------------
# 2. Cargar los resultados de la simulación
# -----------------------------------------------------------

ruta_simulacion <- "plantillas/resultado_simulacion.csv"

if (!file.exists(ruta_simulacion)) {
  stop(
    "No se encontró resultado_simulacion.csv. ",
    "Ejecuta primero comparacion_experimento.py."
  )
}

simulacion <- read.csv(
  ruta_simulacion,
  stringsAsFactors = FALSE
)

cat("\n=== DATOS SIMULADOS ===\n")
print(simulacion)

cat(
  "\nTotal de observaciones:",
  nrow(simulacion),
  "\n"
)

# -----------------------------------------------------------
# 3. Comparación de ventas simuladas
# -----------------------------------------------------------

cat("\n=== PROMEDIOS POR UBICACIÓN ===\n")

promedios_simulados <- aggregate(
  ventas_producto ~ ubicacion,
  data = simulacion,
  FUN = mean
)

print(promedios_simulados)

cat("\n=== REGISTROS POR UBICACIÓN ===\n")
print(table(simulacion$ubicacion))

# -----------------------------------------------------------
# 4. Comparación pareada por tienda
# -----------------------------------------------------------

media_tienda <- tapply(
  simulacion$ventas_producto,
  list(
    simulacion$tienda,
    simulacion$ubicacion
  ),
  mean
)

cat("\n=== PROMEDIOS POR TIENDA ===\n")
print(round(media_tienda, 2))

# Diferencia entre las dos ubicaciones
diferencias <- (
  media_tienda[, "pasillo_principal"]
  - media_tienda[, "habitual"]
)

cat("\n=== DIFERENCIAS POR TIENDA ===\n")
print(diferencias)

# -----------------------------------------------------------
# 5. Estadísticas de la simulación
# -----------------------------------------------------------

media <- mean(diferencias)
dev <- sd(diferencias)
n <- length(diferencias)

cat("\n=== ESTADÍSTICAS ===\n")

cat(sprintf(
  "Número de tiendas: %d\n",
  n
))

cat(sprintf(
  "Diferencia media: %.2f USD\n",
  media
))

cat(sprintf(
  "Desviación estándar: %.2f USD\n",
  dev
))

# Prueba t pareada
prueba <- t.test(
  media_tienda[, "pasillo_principal"],
  media_tienda[, "habitual"],
  paired = TRUE
)

# Intervalo de confianza del 95 %
cat(sprintf(
  "Intervalo de confianza 95 %%: [%.2f, %.2f] USD\n",
  prueba$conf.int[1],
  prueba$conf.int[2]
))

cat(sprintf(
  "p-value: %.8f\n",
  prueba$p.value
))

# -----------------------------------------------------------
# 6. Interpretación final
# -----------------------------------------------------------

cat("\n=== INTERPRETACIÓN FINAL ===\n")

cat(
  "Se compararon las ventas promedio de ambas ubicaciones ",
  "dentro de cada una de las diez tiendas.\n",
  sep = ""
)

cat(
  "La prueba t pareada permite estudiar las diferencias ",
  "entre condiciones utilizando los promedios por tienda.\n",
  sep = ""
)

cat(
  "Los resultados provienen de datos simulados, ",
  "por lo que no demuestran un efecto real ",
  "en las ventas de RetailAndina.\n",
  sep = ""
)

cat(
  "La promoción simultánea puede influir en la comparación ",
  "y debe considerarse al interpretar los resultados.\n",
  sep = ""
)
