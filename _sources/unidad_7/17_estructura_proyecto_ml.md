# 🗂️ Unidad 7: Estructuración profesional de proyectos de Machine Learning

## 🎯 Propósito

Un proyecto MLOps no se sostiene solo con notebooks. Necesita una estructura clara que permita separar la exploración del código reutilizable, distinguir entradas de salidas y facilitar que cualquier integrante del equipo entienda dónde debe vivir cada componente:

* separar responsabilidades;
* ejecutar pasos de forma reproducible;
* colaborar en equipo;
* mantener el proyecto en el tiempo.

---

## ⚠️ Problema de una estructura improvisada

Una carpeta como esta suele crecer sin control:

```text
proyecto/
├── notebook_final.ipynb
├── notebook_final_2.ipynb
├── data.csv
├── modelo.pkl
├── pruebas.py
└── resultados.xlsx
```

Esta estructura puede parecer suficiente al inicio, pero rápidamente se vuelve difícil de mantener. Los principales problemas son:

* no se distingue exploración de código productivo;
* los datos y modelos quedan mezclados;
* no hay reglas claras para reproducir resultados;
* es difícil colaborar y revisar cambios.

---

## ✅ Estructura recomendada para el módulo

Una estructura mínima y profesional puede ser la siguiente. No es una plantilla rígida, pero sí una base razonable para que el proyecto tenga convenciones claras desde el inicio:

```text
mlops-session-duration/
├── data/
│   ├── raw/
│   ├── processed/
│   └── predictions/
├── models/
├── notebooks/
├── reports/
├── src/
│   └── session_duration/
│       ├── data.py
│       ├── features.py
│       ├── train.py
│       └── evaluate.py
├── tests/
├── dvc.yaml
├── pyproject.toml
├── poetry.lock
├── README.md
└── .gitignore
```

---

## 🧩 Rol de cada carpeta

| Carpeta o archivo | Propósito |
| --- | --- |
| `data/raw/` | Datos originales o simulados sin transformar |
| `data/processed/` | Datos listos para entrenamiento |
| `models/` | Modelos entrenados |
| `notebooks/` | Exploración, análisis y prototipos |
| `reports/` | Métricas, gráficos y reportes |
| `src/` | Código reutilizable del proyecto |
| `tests/` | Pruebas automatizadas |
| `dvc.yaml` | Definición del pipeline reproducible |
| `pyproject.toml` | Configuración del proyecto y dependencias |
| `README.md` | Instrucciones para ejecutar y reproducir |

---

## 🔄 De notebook a código reutilizable

El notebook es útil para explorar hipótesis, visualizar datos y probar ideas rápidamente. Pero cuando una lógica se vuelve importante para reproducir el resultado, debe moverse a código reutilizable para que pueda ejecutarse desde un pipeline, probarse y mantenerse.

Ejemplo:

| En notebook | En proyecto estructurado |
| --- | --- |
| Celdas de limpieza | `src/session_duration/data.py` |
| Transformaciones | `src/session_duration/features.py` |
| Entrenamiento | `src/session_duration/train.py` |
| Métricas | `src/session_duration/evaluate.py` |

---

## 🧠 Principios prácticos

* Un script debe tener una responsabilidad clara, de modo que sea fácil probarlo, depurarlo y reutilizarlo.
* Los notebooks no deberían ser la única forma de ejecutar el proyecto, porque eso dificulta automatizar el flujo.
* Los datos crudos no se modifican manualmente; cualquier transformación debe quedar expresada en código.
* Los outputs deben generarse por pipeline para evitar resultados manuales imposibles de rastrear.
* El README debe permitir que otra persona reproduzca el flujo sin depender de explicaciones externas.

---

## 🔗 Integración con herramientas

| Componente | Herramienta | Archivo esperado |
| --- | --- | --- |
| Código | Git | commits, ramas, Pull Requests |
| Entorno | Poetry | `pyproject.toml`, `poetry.lock` |
| Datos y pipeline | DVC | `.dvc`, `dvc.yaml`, `dvc.lock` |
| Experimentos | MLflow | runs, métricas, parámetros, artefactos |

---

## 🎯 Idea clave

> 💡 La estructura del proyecto no es decoración. Es una decisión técnica que facilita reproducibilidad, colaboración y mantenimiento.
