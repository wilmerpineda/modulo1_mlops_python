# ✅ Unidad 7: Checklist integrador del módulo

## 🎯 Propósito

Este checklist resume lo que un proyecto final del módulo debería evidenciar.

Úsalo como guía de autoevaluación antes de entregar la actividad integradora.

---

## 1. Repositorio y colaboración

El proyecto debería tener:

* repositorio Git inicializado;
* historial de commits claro;
* ramas para trabajo colaborativo;
* Pull Requests o evidencia equivalente de revisión;
* `.gitignore` adecuado;
* README con instrucciones de ejecución.

---

## 2. Estructura del proyecto

El proyecto debería separar:

* notebooks exploratorios;
* código reutilizable;
* datos crudos;
* datos procesados;
* modelos;
* reportes;
* configuración.

---

## 3. Entorno reproducible

Debe existir:

* `pyproject.toml`;
* `poetry.lock`;
* instrucciones para instalar dependencias;
* comandos ejecutables con `poetry run`;
* ausencia de dependencias instaladas manualmente sin registrar.

---

## 4. Datos y pipeline

Debe existir evidencia de:

* datos versionados o trazados con DVC;
* etapas definidas en `dvc.yaml`;
* `dvc.lock` generado;
* pipeline reproducible con `dvc repro`;
* separación entre datos crudos y procesados.

---

## 5. Experimentación

Los experimentos deberían registrar:

* nombre del experimento;
* parámetros;
* métricas;
* artefactos relevantes;
* modelo entrenado cuando aplique;
* criterio de selección del mejor modelo.

---

## 6. Reproducibilidad mínima esperada

Otra persona debería poder ejecutar:

```bash
git clone <repo>
cd <repo>
poetry install
dvc pull
dvc repro
mlflow ui
```

Y entender:

* qué problema resuelve el modelo;
* cómo se generan los datos;
* cómo se entrena;
* cómo se evalúa;
* qué experimento fue seleccionado.

---

## 7. Documentación

El README o reporte final debe incluir:

* descripción del problema;
* estructura del proyecto;
* instrucciones de instalación;
* instrucciones de ejecución;
* métricas principales;
* limitaciones;
* próximos pasos.

---

## 🎓 Cierre del módulo

Al completar este módulo, el objetivo no es solo conocer comandos.

El objetivo es poder construir un flujo de Machine Learning donde:

* el código sea trazable;
* los datos sean reproducibles;
* el entorno sea consistente;
* los experimentos sean comparables;
* las decisiones técnicas queden justificadas.

---

## 🎯 Idea clave

> 💡 MLOps empieza cuando dejamos de depender de ejecuciones manuales y comenzamos a construir sistemas reproducibles.
