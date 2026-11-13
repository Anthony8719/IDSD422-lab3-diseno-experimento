# Plantilla de protocolo — Experimento de ubicación de producto

**Fecha:** 27/10/2026  
**Caso de estudio:** RetailAndina S.A.  
**Asignatura:** Estadística y Programación para Ciencia de Datos I

---

## 1. Pregunta e hipótesis

**Pregunta de investigación:** ¿Colocar el producto estrella en el pasillo principal aumenta sus ventas semanales promedio en comparación con su ubicación habitual durante cuatro semanas?

**Hipótesis nula (H0):** La venta semanal promedio del producto en el pasillo principal no es mayor que en su ubicación habitual.

**Hipótesis alternativa (H1):** La venta semanal promedio del producto en el pasillo principal es mayor que en su ubicación habitual.

Se busca determinar si la ubicación del producto influye en sus ventas, manteniendo condiciones de medición comparables entre las tiendas participantes.

## 2. Unidad experimental

**Unidad experimental:** tienda-semana, entendida como una semana durante la cual una tienda mantiene el producto en una ubicación asignada.

**Número de unidades:** 10 tiendas × 4 semanas = 40 observaciones tienda-semana.

Se seleccionaron diez tiendas para participar durante cuatro semanas. Cada establecimiento recibe ambas condiciones: dos semanas con el producto en el pasillo principal y dos semanas en su ubicación habitual.

Este diseño permite comparar las ventas dentro de una misma tienda y reducir la influencia de características propias del establecimiento. Sin embargo, las 40 observaciones no son independientes, ya que varias pertenecen a la misma tienda.

## 3. Factor, niveles y tratamiento

**Factor:** ubicación del producto estrella dentro de la tienda.

**Niveles del factor:**
- Pasillo principal.
- Ubicación habitual.

**Tratamiento:** colocar el producto en el pasillo principal durante las semanas asignadas.

**Condición de control:** mantener el producto en su ubicación habitual.

Se utiliza un diseño cruzado en el que cada tienda alterna ambas ubicaciones durante cuatro semanas. De esta forma, cada establecimiento funciona como su propia referencia para comparar los resultados.

## 4. Grupo de control

El control corresponde a las semanas en las que el producto permanece en su ubicación habitual dentro de la misma tienda.

Su función es proporcionar una referencia para comparar las ventas obtenidas durante las semanas de tratamiento. Esta estrategia reduce la influencia de diferencias permanentes entre establecimientos, aunque no elimina los cambios temporales, las promociones ni otros factores externos.

## 5. Aleatorización

Para asignar las condiciones se utilizó un generador de números aleatorios de NumPy con la semilla `1234597`, permitiendo reproducir la misma asignación.

**Código utilizado en Python:**

`rng = np.random.default_rng(1234597)`

`primera = rng.choice(["pasillo_principal", "habitual"], size=len(tiendas))`

A cada tienda se le asignó aleatoriamente una ubicación inicial. Durante las cuatro semanas se alternaron las condiciones, garantizando que cada establecimiento tuviera dos semanas en tratamiento y dos en control.

**Resultado de la corrida:**

| Tienda | Ubicación inicial | Secuencia durante las cuatro semanas |
|---|---|---|
| Quito Norte | Habitual | H – P – H – P |
| Quito Sur | Pasillo principal | P – H – P – H |
| Guayaquil Centro | Habitual | H – P – H – P |
| Guayaquil Norte | Pasillo principal | P – H – P – H |
| Cuenca Centro | Pasillo principal | P – H – P – H |
| Cuenca Sur | Habitual | H – P – H – P |
| Ambato Centro | Habitual | H – P – H – P |
| Manta | Habitual | H – P – H – P |
| Loja | Habitual | H – P – H – P |
| Machala | Pasillo principal | P – H – P – H |

**H:** habitual. **P:** pasillo principal.

El sorteo produjo seis tiendas que comenzaron en la ubicación habitual y cuatro en el pasillo principal. Esto no representa un error, porque el procedimiento original no exigía una distribución inicial exactamente equilibrada.

La aleatorización busca evitar que las características de las tiendas determinen sistemáticamente la condición inicial. No garantiza eliminar todos los factores de confusión, pero ayuda a reducir el sesgo de asignación.

## 6. Respuesta y medición

**Variable respuesta:** ventas semanales del producto estrella, expresadas en dólares estadounidenses (USD).

**Período de medición:** cuatro semanas consecutivas.

**Responsable del registro:** sistema de punto de venta (POS) de cada establecimiento, con supervisión del equipo encargado del análisis.

Las ventas se registrarán al finalizar cada semana, utilizando los mismos criterios de medición para todas las tiendas.

**Cegamiento:** el personal de tienda puede identificar la ubicación del producto, por lo que no es posible garantizar un cegamiento completo. Sin embargo, el procesamiento de las ventas puede realizarse mediante procedimientos estandarizados para reducir errores y decisiones subjetivas.

## 7. Factores a controlar

| Factor a controlar | Cómo se controla o registra |
|---|---|
| Clima | Registrar condiciones meteorológicas que puedan modificar la afluencia de clientes. |
| Eventos locales | Documentar feriados, festividades y eventos especiales durante las semanas del experimento. |
| Surtido y stock | Mantener disponibilidad suficiente del producto y registrar posibles faltantes. |
| Cambios en el personal | Registrar cambios de turnos y personal que puedan afectar las ventas. |
| Promociones simultáneas | Evitar promociones diferentes entre condiciones o documentarlas para considerar su influencia. |
| Precio del producto | Mantener un precio estable durante el experimento o registrar cualquier modificación. |

Estos controles son importantes porque las ventas podrían cambiar por motivos distintos de la ubicación. Por ejemplo, una promoción puede aumentar las ventas incluso cuando el producto permanece en el lugar habitual.

## 8. Limitaciones del diseño

El experimento puede verse afectado por promociones simultáneas, falta de stock, cambios de personal, eventos locales y diferencias de demanda entre semanas. Si estos factores no se controlan, podrían confundirse con el efecto de la ubicación.

También puede existir un efecto de arrastre: los clientes podrían recordar dónde se encontraba anteriormente el producto. Además, el cambio de ubicación podría desplazar ventas de otros productos, generando canibalización sin un incremento equivalente en las ventas totales de la tienda.

El experimento dura únicamente cuatro semanas, por lo que sus resultados no permitirían asegurar que el efecto se mantiene durante todo el año.

Finalmente, las observaciones de una misma tienda están relacionadas. Por tanto, el análisis debe considerar esta dependencia y evitar tratarlas como 40 establecimientos independientes.

## 9. Comparación en código (Python/R)

### 9.1. Análisis de los cuatro registros originales

Se utilizó `plantillas/registro_experimento.csv` para calcular las ventas promedio por ubicación mediante Python y R.

| Ubicación | Registros | Venta promedio |
|---|---:|---:|
| Habitual | 2 | 1.040 USD |
| Pasillo principal | 2 | 1.335 USD |

**¿Qué grupo muestra mayor venta promedio en la plantilla?**

El pasillo principal muestra una venta promedio de 1.335 USD frente a los 1.040 USD de la ubicación habitual. La diferencia descriptiva es de 295 USD a favor del pasillo principal.

**¿Por qué con cuatro filas no se puede concluir que la ubicación causó el aumento?**

Los datos son insuficientes para demostrar una relación causal, porque solamente se tienen cuatro observaciones, no existe una asignación aleatoria documentada y una de las tiendas registra una promoción simultánea. Además, no se dispone de mediciones repetidas ni de información suficiente sobre otros factores que pudieron influir en las ventas.

**Si se ejecutara el experimento con el protocolo propuesto, ¿qué faltaría para realizar una comparación justa?**

Sería necesario aplicar la asignación aleatoria, registrar las ventas de las diez tiendas durante cuatro semanas, verificar el cumplimiento de las ubicaciones y controlar factores externos. Posteriormente, se deberían comparar las ventas dentro de cada tienda, considerando las diferencias entre semanas y las posibles promociones.

### 9.2. Simulación complementaria de 40 observaciones

Como complemento, se generó una simulación reproducible con diez tiendas y cuatro semanas, guardada en `plantillas/resultado_simulacion.csv`.

Los resultados fueron analizados mediante Python y R, obteniendo los mismos valores estadísticos.

| Estadístico | Resultado |
|---|---:|
| Número de tiendas | 10 |
| Observaciones simuladas | 40 |
| Promedio en ubicación habitual | 1.107,20 USD |
| Promedio en pasillo principal | 1.346,90 USD |
| Diferencia media pareada | 239,70 USD |
| Desviación estándar de las diferencias | 102,39 USD |
| Intervalo de confianza del 95 % | [166,45; 312,95] USD |
| Valor p (prueba t pareada bilateral) | 0,00004092 |

La simulación muestra una diferencia promedio positiva a favor del pasillo principal. El intervalo de confianza calculado no incluye cero y el valor p es inferior a 0,05.

Sin embargo, estos resultados corresponden a datos generados artificialmente y no constituyen evidencia de un efecto real en RetailAndina. Además, la simulación incluye una promoción simultánea y el análisis pareado simplificado no controla explícitamente todos los posibles efectos de semana y arrastre.

La utilidad de esta simulación es comprobar el funcionamiento del procedimiento estadístico y practicar la interpretación de resultados experimentales.

---

## Conclusión del protocolo

El diseño propuesto permite evaluar la influencia de la ubicación del producto mediante comparaciones dentro de diez tiendas durante cuatro semanas. La aleatorización contribuye a reducir sesgos de asignación, mientras que el registro de factores externos permite interpretar mejor las diferencias observadas.

Los cuatro registros originales no son suficientes para establecer conclusiones causales. Por su parte, la simulación demuestra cómo analizar datos experimentales reproducibles, pero no reemplaza la ejecución real del experimento.
