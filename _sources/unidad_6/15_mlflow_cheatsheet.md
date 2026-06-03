# 🧾 Unidad 6: MLflow Cheat Sheet

## 🎯 Propósito

Este documento resume los comandos y funciones más importantes para registrar experimentos con MLflow.

---

## 📦 Instalación

```bash
poetry add mlflow
```

O, si el proyecto aún no usa Poetry:

```bash
pip install mlflow
```

---

## 🧪 Crear o seleccionar experimento

```python
import mlflow

mlflow.set_experiment("session_minutes_regression")
```

👉 Úsalo para agrupar ejecuciones relacionadas con el mismo problema.

---

## ▶️ Iniciar una ejecución

```python
with mlflow.start_run():
    ...
```

👉 Todo lo que se registre dentro del bloque queda asociado a la misma ejecución.

---

## ⚙️ Registrar parámetros

```python
mlflow.log_param("model_type", "linear_regression")
mlflow.log_param("test_size", 0.2)
mlflow.log_param("random_state", 42)
```

👉 Los parámetros explican cómo se configuró el experimento.

---

## 📏 Registrar métricas

```python
mlflow.log_metric("mae", mae)
mlflow.log_metric("rmse", rmse)
mlflow.log_metric("r2", r2)
```

👉 Las métricas permiten comparar experimentos.

---

## 📁 Registrar artefactos

```python
mlflow.log_artifact("reports/metrics.json")
mlflow.log_artifact("reports/residuals.png")
```

👉 Los artefactos son archivos generados por el experimento.

---

## 🤖 Registrar modelo

```python
import mlflow.sklearn

mlflow.sklearn.log_model(model, "model")
```

👉 Útil para guardar el modelo entrenado junto con el run.

---

## 🖥️ Abrir la interfaz local

```bash
mlflow ui
```

Por defecto, la interfaz queda disponible en:

```text
http://127.0.0.1:5000
```

---

## 🧠 Buenas prácticas

* usar nombres de experimentos descriptivos;
* registrar siempre parámetros y métricas principales;
* guardar artefactos relevantes, no todos los archivos del proyecto;
* registrar el `random_state` cuando aplique;
* documentar qué métrica define el mejor modelo;
* conectar cada run con la versión de código y datos usada.

---

## ⚠️ Errores comunes

### ❌ Registrar solo métricas

Sin parámetros, no sabemos qué configuración produjo el resultado.

---

### ❌ No guardar artefactos

Sin artefactos, se pierde evidencia como gráficos, reportes o modelos.

---

### ❌ Comparar modelos con datos distintos sin trazabilidad

Si cambia el dataset y no queda registrado, la comparación puede ser injusta.

---

## 🎯 Idea clave

> MLflow no mejora el modelo por sí solo. Mejora la trazabilidad del proceso experimental.
