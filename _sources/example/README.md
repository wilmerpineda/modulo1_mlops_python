# Ejemplo end-to-end: Poetry, DVC y MLflow

Esta carpeta contiene un proyecto pequeno de regresion para practicar un flujo MLOps reproducible. El objetivo es predecir `session_minutes`, el tiempo de permanencia de un usuario en una plataforma digital.

El ejemplo conecta tres ideas:

- Poetry controla el ambiente de Python.
- DVC versiona datos y ejecuta el pipeline.
- MLflow registra parametros, metricas, modelos y artefactos.

## 1. Requisitos

Ejecuta todos los comandos desde esta carpeta:

```bash
cd example
```

Verifica que Poetry este disponible:

```bash
python -m poetry --version
```

Si `poetry --version` falla por un launcher roto, usa `python -m poetry` en todos los comandos. En Windows esto suele evitar problemas cuando Poetry fue instalado con otra version de Python.

El proyecto esta ajustado para Python `>=3.14,<3.15`. Las dependencias usan versiones compatibles con ese rango; en particular, `pandas` se mantiene en `>=2.3,<3.0` porque MLflow 3.x todavia declara `pandas <3`.

Si tienes varias versiones instaladas, selecciona Python 3.14 antes de instalar:

```bash
python -m poetry env use 3.14
```

El archivo `poetry.toml` deja configurado que el entorno virtual se cree dentro de esta carpeta como `.venv/`.

## 2. Crear el ambiente con Poetry

Instala las dependencias declaradas en `pyproject.toml`:

```bash
python -m poetry install
```

Si `poetry.lock` aun no existe, Poetry lo generara al resolver dependencias. Tambien puedes crearlo explicitamente con:

```bash
python -m poetry lock
```

Opcionalmente, crea el entorno virtual dentro del proyecto:

```bash
python -m poetry config virtualenvs.in-project true --local
python -m poetry install
```

Comprueba que el paquete local se puede importar:

```bash
python -m poetry run python -c "import session_duration; print('ok')"
```

## 3. Inicializar DVC dentro de `example`

Este repositorio ya tiene Git en la raiz del material del curso. Por eso el ejemplo usa DVC como subproyecto:

```bash
python -m poetry run dvc init --subdir
```

Esto crea la carpeta `.dvc/` dentro de `example/`. Git debe versionar la configuracion de DVC, pero no el cache interno.

## 4. Generar datos mock manualmente

El dataset se genera con parametros de `params.yaml`:

```bash
python -m poetry run python -m session_duration.generate_data --params params.yaml
```

Salida esperada:

```text
data/raw/session_data.csv
```

El archivo contiene variables como `segment`, `historical_avg_session_minutes`, `hour_of_day`, `entry_point` y la variable objetivo `session_minutes`.

## 5. Asociar los datos al repositorio con DVC

En este ejemplo los datos mock son una salida declarada del pipeline:

```yaml
stages:
  generate_data:
    outs:
      - data/raw/session_data.csv
```

Eso significa que DVC asociara el archivo al repositorio cuando ejecutes:

```bash
python -m poetry run dvc repro
```

Despues de la primera ejecucion, DVC creara o actualizara `dvc.lock`. Ese archivo registra la version exacta de los datos, dependencias y salidas del pipeline.

Git debe versionar:

```bash
git add example/dvc.yaml example/dvc.lock example/params.yaml
git add example/src example/tests example/README.md example/pyproject.toml
```

La regla practica es:

- Git versiona codigo, configuracion y metadatos.
- DVC versiona el contenido de los datos y artefactos declarados como salidas.

### Alternativa: asociar un dataset estatico con `dvc add`

Si recibes un CSV externo que no sera generado por el pipeline, puedes asociarlo con `dvc add`:

```bash
python -m poetry run dvc add data/raw/dataset_externo.csv
```

DVC crea un archivo pequeno:

```text
data/raw/dataset_externo.csv.dvc
```

Ese archivo es el puntero que Git debe versionar:

```bash
git add example/data/raw/dataset_externo.csv.dvc example/data/raw/.gitignore
```

No uses `dvc add` sobre `data/raw/session_data.csv` en este proyecto, porque ese archivo ya pertenece a la etapa `generate_data` de `dvc.yaml`.

## 6. Configurar un remoto local de DVC

Para practicar `dvc push` y `dvc pull` sin credenciales de nube:

```bash
python -m poetry run dvc remote add -d localremote ./dvc_remote
python -m poetry run dvc push
```

`dvc_remote/` simula un almacenamiento externo. En un proyecto real podria reemplazarse por S3, Azure Blob Storage, Google Drive u otro backend.

Para recuperar datos versionados:

```bash
python -m poetry run dvc pull
```

## 7. Ejecutar el pipeline completo con DVC

El pipeline esta definido en `dvc.yaml` y tiene tres etapas:

- `generate_data`: crea `data/raw/session_data.csv`.
- `prepare_data`: separa train y test en `data/processed/`.
- `train_model`: entrena el modelo, guarda metricas y registra el experimento en MLflow.

Ejecuta todo:

```bash
python -m poetry run dvc repro
```

Archivos generados:

```text
data/raw/session_data.csv
data/processed/train.csv
data/processed/test.csv
models/regression_model.joblib
reports/metrics.json
reports/predictions.csv
reports/predicted_vs_actual.png
mlruns/
mlflow.db
```

Si cambias `params.yaml`, DVC detecta que etapas deben repetirse:

```bash
python -m poetry run dvc status
python -m poetry run dvc repro
```

## 8. Ejecutar scripts manualmente

Tambien puedes correr cada paso sin DVC para entender el flujo:

```bash
python -m poetry run python -m session_duration.generate_data --params params.yaml
python -m poetry run python -m session_duration.prepare_data --params params.yaml
python -m poetry run python -m session_duration.train --params params.yaml
```

Este modo sirve para depurar. Para reproducibilidad, usa `dvc repro`.

## 9. Revisar resultados con MLflow

Abre la interfaz local:

```bash
python -m poetry run mlflow ui --backend-store-uri sqlite:///mlflow.db
```

Luego visita:

```text
http://127.0.0.1:5000
```

En MLflow podras revisar:

- parametros del modelo y del dataset;
- metricas `mae`, `rmse` y `r2`;
- artefactos como `metrics.json`, predicciones, grafico y modelo serializado;
- comparacion entre ejecuciones.

Para comparar modelos, cambia en `params.yaml`:

```yaml
model:
  type: linear_regression
```

Despues ejecuta:

```bash
python -m poetry run dvc repro
```

Vuelve a MLflow y compara el nuevo run contra el anterior.

## 10. Pruebas

Ejecuta las pruebas basicas:

```bash
python -m poetry run pytest
```

Las pruebas validan contratos minimos del ejemplo:

- el dataset mock contiene las columnas esperadas;
- existe la variable objetivo `session_minutes`;
- las metricas de regresion conservan nombres esperados.

## 11. Que debe quedar versionado

Versiona en Git:

```text
README.md
pyproject.toml
poetry.lock
params.yaml
dvc.yaml
dvc.lock
.dvc/config
src/
tests/
```

No versiones en Git:

```text
data/raw/session_data.csv
data/processed/
models/
reports/
mlruns/
mlflow.db
dvc_remote/
.venv/
```

DVC y MLflow se encargan de conectar esos artefactos con una ejecucion reproducible.
