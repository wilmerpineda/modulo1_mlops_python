# 📊 Unidad 6: Fundamentos de tracking de experimentos con MLflow

## 🎯 Propósito

En las unidades anteriores controlamos tres piezas fundamentales del flujo MLOps:

* el código con Git;
* el entorno con Poetry;
* los datos y pipelines con DVC.

Ahora necesitamos controlar una cuarta pieza: **los experimentos**. Esta pieza es crítica porque la mayor parte del trabajo de modelado consiste en probar alternativas, comparar resultados y justificar por qué una configuración es mejor que otra para el problema de negocio.

En Machine Learning, un experimento no es solo ejecutar un modelo. Es una combinación específica de:

* versión de datos;
* versión de código;
* parámetros;
* algoritmo;
* métricas;
* artefactos generados.

---

## ⚠️ El problema sin tracking

En un flujo manual, es común registrar resultados en hojas de cálculo, archivos sueltos o nombres de carpetas como:

```text
modelo_final.pkl
modelo_final_v2.pkl
modelo_final_ahora_si.pkl
```

Este enfoque falla rápidamente porque:

* no permite comparar experimentos con rigor;
* se pierden parámetros importantes;
* no queda claro qué artefacto corresponde a cada resultado;
* no existe una auditoría confiable del proceso.

---

## 🚀 ¿Qué es MLflow Tracking?

MLflow Tracking es un componente de MLflow que permite registrar y consultar ejecuciones de experimentos. En lugar de depender de notas manuales, MLflow crea un historial consultable donde cada ejecución queda asociada con sus parámetros, métricas y archivos generados.

Una ejecución o **run** puede guardar:

* parámetros, por ejemplo `alpha`, `max_depth` o `random_state`;
* métricas, por ejemplo `mae`, `rmse` o `r2`;
* artefactos, por ejemplo modelos, gráficos o reportes;
* etiquetas y metadatos útiles para auditoría.

---

## 🧩 Conceptos clave

### Experimento

Un experimento es una agrupación lógica de ejecuciones relacionadas. En el caso de este módulo, podemos usar un experimento para reunir todos los modelos que intentan predecir `session_minutes`, aunque cada ejecución use parámetros o algoritmos distintos.

Ejemplo:

```text
session_minutes_regression
```

---

### Run

Un **run** es una ejecución concreta del código de entrenamiento. Cada run representa una combinación puntual de datos, código, parámetros y resultados, por lo que funciona como una unidad básica de auditoría.

Ejemplo:

```text
LinearRegression con dataset v1 y split 80/20
```

---

### Parámetros

Los parámetros son valores de configuración elegidos antes o durante el entrenamiento. Registrarlos permite entender qué decisiones produjeron un resultado, especialmente cuando se comparan modelos con distintos algoritmos o hiperparámetros.

```python
mlflow.log_param("model_type", "linear_regression")
mlflow.log_param("test_size", 0.2)
```

---

### Métricas

Las métricas son resultados numéricos usados para evaluar el desempeño. En un problema de regresión como el del curso, métricas como `mae`, `rmse` y `r2` ayudan a comparar modelos desde perspectivas complementarias.

```python
mlflow.log_metric("mae", mae)
mlflow.log_metric("rmse", rmse)
mlflow.log_metric("r2", r2)
```

---

### Artefactos

Los artefactos son archivos producidos por el experimento. Guardarlos junto con el run permite revisar evidencia adicional, como gráficos de residuales, reportes de evaluación o el modelo serializado.

Ejemplos:

* modelo entrenado;
* matriz de errores;
* gráfico de residuales;
* archivo de predicciones;
* reporte de evaluación.

---

## 🔄 Flujo conceptual

```{mermaid}
flowchart LR
    A[Entrenar modelo] --> B[Registrar parámetros]
    B --> C[Registrar métricas]
    C --> D[Guardar artefactos]
    D --> E[Comparar runs]
    E --> F[Seleccionar modelo]
```

---

## 🧪 Ejemplo mínimo

```python
import mlflow

mlflow.set_experiment("session_minutes_regression")

with mlflow.start_run():
    mlflow.log_param("model_type", "linear_regression")
    mlflow.log_param("test_size", 0.2)

    mlflow.log_metric("mae", mae)
    mlflow.log_metric("rmse", rmse)
    mlflow.log_metric("r2", r2)
```

Este fragmento no reemplaza el entrenamiento; lo envuelve para dejar evidencia de lo que ocurrió. La idea es que el código siga entrenando y evaluando el modelo, pero que además registre la información necesaria para comparar y auditar el resultado.

---

## 🖥️ Interfaz de MLflow

Después de registrar ejecuciones, se puede abrir la interfaz local con:

```bash
mlflow ui
```

Desde allí es posible:

* comparar runs;
* ordenar por métricas;
* revisar parámetros;
* descargar artefactos;
* identificar el mejor experimento.

---

## ⚖️ MLflow, Weights & Biases y Neptune.ai

| Herramienta | Enfoque principal | Comentario |
| --- | --- | --- |
| MLflow | Tracking, modelos, registro y despliegue | Muy usado en flujos locales y empresariales |
| Weights & Biases | Seguimiento colaborativo y visualización avanzada | Popular en deep learning y equipos de investigación |
| Neptune.ai | Tracking a gran escala y organización de experimentos | Útil cuando hay muchos runs, métricas y usuarios |

En este módulo usaremos MLflow porque permite trabajar localmente, se integra bien con Python y cubre los conceptos esenciales de tracking.

---

## 🔗 Conexión con Git, Poetry y DVC

MLflow no reemplaza a Git, Poetry ni DVC. Los complementa.

| Pregunta | Herramienta |
| --- | --- |
| ¿Qué código se ejecutó? | Git |
| ¿Qué entorno se usó? | Poetry |
| ¿Qué datos alimentaron el experimento? | DVC |
| ¿Qué parámetros, métricas y artefactos produjo? | MLflow |

---

## 🎯 Idea clave

> 💡 Un experimento que no queda registrado es difícil de comparar, auditar y reproducir.

---

## 📚 Lecturas recomendadas

* [MLflow Tracking documentation](https://www.mlflow.org/docs/latest/ml/tracking)
* [Weights & Biases documentation](https://docs.wandb.ai/)
* [Neptune.ai documentation - Runs](https://docs.neptune.ai/experiments/)
