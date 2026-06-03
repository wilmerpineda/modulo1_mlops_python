# 🧰 Unidad 7: Ecosistema de herramientas MLOps

## 🎯 Propósito

MLOps es un ecosistema. No existe una única herramienta que resuelva todo el ciclo de vida de un modelo.

En este módulo usamos un conjunto mínimo:

* Git/GitHub;
* Poetry;
* DVC;
* MLflow.

Pero en proyectos reales aparecen otras herramientas según la escala, el equipo y el tipo de despliegue.

---

## 🗺️ Mapa general

```{mermaid}
flowchart LR
    A[Codigo] --> B[Git/GitHub]
    C[Entorno] --> D[Poetry]
    E[Datos] --> F[DVC]
    G[Experimentos] --> H[MLflow]
    I[Pipelines programados] --> J[Airflow]
    K[Contenedores] --> L[Docker]
    M[Operacion a escala] --> N[Kubernetes]
```

---

## 🔧 Herramientas del módulo

| Herramienta | Pregunta que responde |
| --- | --- |
| Git | ¿Qué cambió en el código? |
| GitHub | ¿Cómo colaboramos, revisamos y publicamos cambios? |
| Poetry | ¿Cómo reproducimos el entorno? |
| DVC | ¿Qué datos y outputs corresponden a cada versión? |
| MLflow | ¿Qué experimento produjo qué resultado? |

---

## 🚀 Herramientas complementarias

### Airflow

Airflow permite definir y programar flujos de trabajo mediante DAGs.

En MLOps puede usarse para:

* ejecutar entrenamientos programados;
* coordinar procesos de datos;
* activar tareas de validación;
* automatizar pipelines batch.

---

### Docker

Docker permite empaquetar una aplicación con sus dependencias en una imagen portable.

En MLOps puede usarse para:

* ejecutar el mismo servicio en distintos entornos;
* reducir diferencias entre desarrollo y producción;
* desplegar APIs de predicción;
* integrar pipelines de CI/CD.

---

### Kubernetes

Kubernetes permite operar aplicaciones contenerizadas a escala.

En MLOps puede usarse para:

* desplegar servicios de predicción;
* escalar cargas de entrenamiento o inferencia;
* gestionar recursos;
* mantener disponibilidad de servicios.

---

## ⚖️ Cómo elegir herramientas

Antes de incorporar una herramienta, conviene preguntar:

* ¿Qué problema concreto resuelve?
* ¿El equipo tiene capacidad para mantenerla?
* ¿Reduce trabajo manual o agrega complejidad?
* ¿Se integra con el flujo actual?
* ¿Es necesaria para la escala del proyecto?

Una herramienta útil en una empresa grande puede ser innecesaria en un proyecto pequeño. MLOps no consiste en usar todas las herramientas, sino en construir un flujo confiable.

---

## 📚 Referencias oficiales

* [Apache Airflow documentation](https://airflow.apache.org/docs/)
* [Docker documentation](https://docs.docker.com/)
* [Kubernetes documentation](https://kubernetes.io/docs/)
* [MLflow Tracking documentation](https://www.mlflow.org/docs/latest/ml/tracking)
* [DVC documentation](https://dvc.org/doc/)
* [Poetry documentation](https://python-poetry.org/docs/)
* [GitHub Docs - Pull requests](https://docs.github.com/articles/using-pull-requests)

---

## 🎯 Idea clave

> 💡 La herramienta correcta depende del problema operativo que necesitas resolver, no de una lista fija de tecnologías.
