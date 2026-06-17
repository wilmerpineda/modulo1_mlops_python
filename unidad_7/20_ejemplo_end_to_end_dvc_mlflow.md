# Unidad 7: Ejemplo end-to-end con DVC y MLflow

## Propósito

Esta guía muestra cómo reproducir el ejemplo completo ubicado en la carpeta `example/`.

El objetivo no es solo ejecutar comandos. La idea es entender cómo se conectan las piezas de un flujo MLOps mínimo:

* Poetry prepara un ambiente reproducible;
* DVC genera, versiona y reproduce datos y artefactos;
* MLflow registra experimentos, métricas, modelos y resultados.

El caso sigue la temática del módulo: un problema de regresión para predecir `session_minutes`, es decir, el tiempo de permanencia de un usuario en una plataforma digital.

---

## 1. Mapa general del flujo

```{mermaid}
flowchart LR
    A[params.yaml] --> B[Generar datos mock]
    B --> C[data/raw/session_data.csv]
    C --> D[Preparar train/test]
    D --> E[data/processed]
    E --> F[Entrenar modelo]
    F --> G[reports/metrics.json]
    F --> H[models/regression_model.joblib]
    F --> I[MLflow]
    G --> J[DVC]
    H --> J
```

La lectura importante es esta:

* `params.yaml` controla los parámetros del ejercicio;
* `dvc.yaml` define las etapas reproducibles;
* `dvc.lock` registra qué versión exacta de entradas y salidas produjo el resultado;
* MLflow guarda la historia de experimentos para comparar ejecuciones.

---

## 2. Estructura del ejemplo

```text
example/
├── README.md
├── pyproject.toml
├── poetry.lock
├── poetry.toml
├── params.yaml
├── dvc.yaml
├── dvc.lock
├── data/
│   ├── raw/
│   └── processed/
├── models/
├── reports/
├── src/
│   └── session_duration/
│       ├── generate_data.py
│       ├── prepare_data.py
│       └── train.py
└── tests/
```

Cada carpeta cumple un rol:

| Carpeta o archivo | Propósito |
| --- | --- |
| `pyproject.toml` | Declara dependencias del proyecto |
| `poetry.lock` | Fija versiones exactas del ambiente |
| `poetry.toml` | Hace que el ambiente `.venv/` viva dentro de `example/` |
| `params.yaml` | Centraliza parámetros de datos, split, modelo y MLflow |
| `dvc.yaml` | Define el pipeline reproducible |
| `dvc.lock` | Registra hashes de entradas y salidas |
| `src/` | Contiene el código ejecutable |
| `data/` | Guarda datos crudos y procesados generados por el pipeline |
| `models/` | Guarda el modelo serializado |
| `reports/` | Guarda métricas, predicciones y gráficos |

---

## 3. Preparar el ambiente con Poetry

Desde la raíz del repositorio:

```bash
cd example
```

Verifica Poetry:

```bash
python -m poetry --version
```

Instala el ambiente:

```bash
python -m poetry install
```

En este ejemplo el ambiente queda dentro de:

```text
example/.venv/
```

Esto ocurre porque `poetry.toml` define:

```toml
[virtualenvs]
in-project = true
```

Esta decisión ayuda a los estudiantes porque todo lo necesario para ejecutar el ejemplo queda contenido en la carpeta `example/`.

---

## 4. Generar datos mock

El primer script crea un dataset simulado:

```bash
python -m poetry run python -m session_duration.generate_data --params params.yaml
```

Salida esperada:

```text
data/raw/session_data.csv
```

El dataset contiene variables como:

| Variable | Descripción |
| --- | --- |
| `segment` | Tipo de usuario |
| `historical_avg_session_minutes` | Promedio histórico de duración |
| `historical_sessions_last_7d` | Sesiones recientes |
| `days_since_last_session` | Días desde la última sesión |
| `hour_of_day` | Hora de la sesión |
| `entry_point` | Punto de entrada a la plataforma |
| `push_received_last_24h` | Si recibió notificación reciente |
| `session_minutes` | Variable objetivo |

La variable objetivo es:

```text
session_minutes
```

---

## 5. Cómo usa DVC este ejemplo

DVC puede usarse de dos maneras principales:

1. versionar archivos estáticos con `dvc add`;
2. declarar pipelines reproducibles con `dvc.yaml`.

En este ejemplo usamos principalmente la segunda forma, porque los datos mock se generan mediante código.

### Pipeline declarado

El archivo `dvc.yaml` define tres etapas:

```text
generate_data -> prepare_data -> train_model
```

Cada etapa declara:

* comando a ejecutar;
* dependencias;
* parámetros;
* salidas.

Ejemplo conceptual:

```yaml
stages:
  generate_data:
    cmd: python -m session_duration.generate_data --params params.yaml
    deps:
      - src/session_duration/generate_data.py
      - params.yaml
    outs:
      - data/raw/session_data.csv
```

DVC sabe que si cambia `params.yaml` o `generate_data.py`, debe volver a generar el dataset.

---

## 6. Ejecutar el pipeline completo

Ejecuta:

```bash
python -m poetry run dvc repro
```

DVC revisa dependencias y ejecuta solo lo necesario.

Si todo corre correctamente, se generan:

```text
data/raw/session_data.csv
data/processed/train.csv
data/processed/test.csv
models/regression_model.joblib
reports/metrics.json
reports/predictions.csv
reports/predicted_vs_actual.png
mlflow.db
mlruns/
```

Después de ejecutar, revisa el estado:

```bash
python -m poetry run dvc status
```

Resultado esperado:

```text
Data and pipelines are up to date.
```

---

## 7. Qué registra DVC

DVC registra la relación entre:

* código;
* parámetros;
* datos;
* modelos;
* reportes.

El archivo clave es:

```text
dvc.lock
```

Este archivo permite responder:

* ¿qué datos se usaron?;
* ¿qué código produjo el modelo?;
* ¿qué parámetros estaban activos?;
* ¿qué salidas generó el pipeline?

En proyectos reales, `dvc.lock` debe versionarse con Git.

---

## 8. Remoto local de DVC

Para practicar sin nube ni credenciales, el ejemplo usa un remoto local:

```bash
python -m poetry run dvc remote add -d localremote ./dvc_remote
python -m poetry run dvc push
```

Esto crea una carpeta:

```text
example/dvc_remote/
```

Esa carpeta simula un almacenamiento externo. En una empresa podría ser S3, Azure Blob Storage, Google Cloud Storage o Google Drive.

Para recuperar artefactos versionados desde el remoto:

```bash
python -m poetry run dvc pull
```

---

## 9. Cómo usa MLflow este ejemplo

La etapa `train_model` registra el experimento en MLflow.

El código hace cuatro cosas:

* define el experimento;
* entrena el modelo;
* registra parámetros y métricas;
* guarda artefactos y el modelo.

Ejemplo conceptual:

```python
mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("session_minutes_regression")

with mlflow.start_run(run_name=params["model"]["type"]):
    mlflow.log_params(...)
    mlflow.log_metrics(...)
    mlflow.log_artifact("reports/metrics.json")
    mlflow.sklearn.log_model(...)
```

En este ejemplo se usa SQLite como backend local:

```text
sqlite:///mlflow.db
```

Esto es compatible con MLflow 3.x y mantiene los resultados dentro de la carpeta `example/`.

---

## 10. Abrir la interfaz de MLflow

Ejecuta:

```bash
python -m poetry run mlflow ui --backend-store-uri sqlite:///mlflow.db
```

Abre en el navegador:

```text
http://127.0.0.1:5000
```

Dentro de MLflow puedes revisar:

| Sección | Qué muestra |
| --- | --- |
| Experiments | Lista de experimentos |
| Runs | Ejecuciones individuales |
| Parameters | Configuración del experimento |
| Metrics | Resultados cuantitativos |
| Artifacts | Archivos asociados al run |
| Models | Modelo registrado como artefacto |

---

## 11. Métricas registradas

El ejemplo registra tres métricas de regresión:

| Métrica | Interpretación |
| --- | --- |
| `mae` | Error absoluto promedio |
| `rmse` | Penaliza más los errores grandes |
| `r2` | Proporción de variabilidad explicada |

Ejemplo de salida:

```json
{
  "mae": 4.153789407341469,
  "rmse": 5.074841679560861,
  "r2": 0.6564498742147427
}
```

Para este problema, un mejor modelo debería tender a:

* menor `mae`;
* menor `rmse`;
* mayor `r2`.

---

## 12. Modelos usados

El ejemplo permite comparar dos tipos de modelo.

### `linear_regression`

Modelo lineal base.

Útil para:

* tener una línea de referencia;
* explicar relaciones simples;
* comparar contra modelos más flexibles.

Configuración:

```yaml
model:
  type: linear_regression
  random_state: 42
  n_estimators: 120
  max_depth: 8
```

En este caso `n_estimators` y `max_depth` no afectan a la regresión lineal, pero se mantienen en `params.yaml` para que el archivo conserve una estructura simple.

### `random_forest`

Modelo basado en árboles.

Útil para:

* capturar relaciones no lineales;
* manejar interacciones entre variables;
* obtener un modelo más fuerte como baseline práctico.

Configuración:

```yaml
model:
  type: random_forest
  random_state: 42
  n_estimators: 120
  max_depth: 8
```

Después de cambiar el modelo, ejecuta:

```bash
python -m poetry run dvc repro
```

Luego abre MLflow y compara los runs.

---

## 13. Qué debe observar el estudiante

Después de ejecutar el flujo, el estudiante debería poder responder:

* ¿qué etapa genera los datos mock?;
* ¿qué archivo define el pipeline?;
* ¿qué archivo registra el estado exacto del pipeline?;
* ¿qué parámetros afectan al modelo?;
* ¿dónde se guardan las métricas?;
* ¿cómo se comparan dos ejecuciones en MLflow?;
* ¿qué archivos deben ir a Git y cuáles no?

---

## 14. Qué debe entregar el estudiante

Para un ejercicio aplicado, una entrega mínima debería incluir:

* `pyproject.toml` y `poetry.lock`;
* `params.yaml`;
* `dvc.yaml` y `dvc.lock`;
* scripts en `src/`;
* evidencia de ejecución de `dvc repro`;
* captura o resumen de runs en MLflow;
* comparación de al menos dos ejecuciones;
* explicación de qué modelo seleccionaría y por qué.

La comparación debe incluir al menos:

| Run | Modelo | MAE | RMSE | R2 | Comentario |
| --- | --- | --- | --- | --- | --- |
| 1 | `linear_regression` | valor | valor | valor | baseline |
| 2 | `random_forest` | valor | valor | valor | modelo alternativo |

---

## 15. Errores comunes

### Usar `dvc add` sobre una salida del pipeline

No uses:

```bash
dvc add data/raw/session_data.csv
```

en este ejemplo, porque `session_data.csv` ya está declarado como salida de `generate_data` en `dvc.yaml`.

Usa `dvc add` para datasets externos que no son generados por el pipeline.

### No versionar `dvc.lock`

Si no se versiona `dvc.lock`, se pierde parte de la trazabilidad del pipeline.

### Registrar métricas sin parámetros

Una métrica sola no explica cómo se obtuvo el resultado. MLflow debe registrar también parámetros como:

* tipo de modelo;
* `random_state`;
* tamaño del dataset;
* proporción de test;
* hiperparámetros.

### Comparar modelos con datos distintos sin control

Si cambia el dataset, la comparación puede dejar de ser justa. Por eso DVC y MLflow deben usarse juntos:

* DVC controla datos y outputs;
* MLflow controla experimentos.

---

## Idea clave

> Un flujo reproducible no depende de recordar qué se ejecutó. Depende de dejar explícitos el ambiente, los datos, el pipeline, los parámetros y los experimentos.

