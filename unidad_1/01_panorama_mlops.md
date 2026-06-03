# 🧭 Unidad 1: Panorama de MLOps

## 🔍 ¿Qué es MLOps?

MLOps (Machine Learning Operations) es un conjunto de prácticas que busca integrar tres perspectivas que tradicionalmente se trabajan por separado:

* **Ciencia de datos**
* **Ingeniería de software**
* **DevOps**

El objetivo de esa integración es construir sistemas de Machine Learning que no solo produzcan buenas métricas en una etapa experimental, sino que también puedan sostenerse cuando el proyecto crece:

* reproducibles,
* escalables,
* mantenibles,
* y colaborativos.

---

## ⚠️ El problema tradicional

En muchos proyectos de ciencia de datos, el flujo típico es el siguiente:

```{mermaid}
flowchart LR
    A[Datos] --> B[Notebook]
    B --> C[Modelo]
    C --> D[Resultados]
```

Este enfoque funciona en etapas exploratorias, pero presenta limitaciones críticas:

* el código no está estructurado;
* los datos no están versionados;
* los experimentos no son trazables;
* los resultados no son reproducibles;
* no hay colaboración organizada.

👉 En resumen: **el modelo funciona, pero el proceso no.**

---

## 🧱 ¿Qué cambia al pasar de Data Science a MLOps?

En ciencia de datos exploratoria, el objetivo principal suele ser encontrar una señal útil en los datos: probar variables, entrenar modelos y comparar métricas. Esa etapa es valiosa porque ayuda a descubrir si el problema tiene potencial predictivo, pero todavía no garantiza que el resultado pueda operar de forma confiable.

En MLOps, ese objetivo se amplía. Además de obtener un buen modelo, el equipo debe poder responder preguntas operativas:

* ¿Quién cambió el código y por qué?
* ¿Qué versión del dataset se usó?
* ¿Qué dependencias tenía el entorno?
* ¿Qué parámetros produjo el mejor resultado?
* ¿Cómo se repite el entrenamiento?
* ¿Cómo se detecta que el modelo dejó de funcionar bien?

Por eso MLOps no reemplaza la ciencia de datos. La complementa con prácticas de ingeniería que hacen que los resultados sean reutilizables, auditables y mantenibles.

---

## 🚨 Cuando intentamos escalar

Cuando este modelo se intenta llevar a producción, el flujo se rompe porque aparecen exigencias que no estaban presentes durante la exploración individual:

```{mermaid}
flowchart LR
    A[Datos iniciales] --> B[Notebook]
    B --> C[Modelo entrenado]
    C --> D[Resultados prometedores]
    D --> E[Intento de reproducción]
    E --> F[Resultados inconsistentes]
```

Esto ocurre porque:

* no sabemos qué versión de los datos se usó;
* no conocemos los parámetros exactos;
* el entorno no es replicable;
* no existe un pipeline definido.

---

## 🧠 El cambio de mentalidad

MLOps propone un cambio fundamental en la forma de entender el trabajo:

> ❗ Pasar de construir modelos a construir sistemas.

Esto implica pensar en el modelo como una pieza dentro de un proceso más amplio, donde importan tanto las predicciones como la capacidad de repetir, revisar y mejorar el flujo:

* flujos de trabajo completos;
* control de versiones;
* trazabilidad;
* automatización;
* colaboración.

---

## 🔄 Flujo MLOps (visión general)

Un flujo típico de MLOps se ve así:

```{mermaid}
flowchart LR
    A[Datos] --> B[Preprocesamiento]
    B --> C[Entrenamiento]
    C --> D[Evaluación]
    D --> E[Registro de Experimentos]
    E --> F[Modelo Seleccionado]
    F --> G[Despliegue]
    G --> H[Monitoreo]
    H --> A
```

Este flujo introduce elementos clave que no suelen estar presentes en un notebook aislado:

* ciclo continuo;
* retroalimentación;
* control en cada etapa.

---

## 🧩 Componentes clave de MLOps

### 🔹 1. Versionamiento de código

Permite:

* rastrear cambios;
* colaborar en equipo;
* evitar sobrescrituras.

👉 Herramienta: **Git / GitHub**

---

### 🔹 2. Gestión de entornos

Permite:

* reproducir ejecuciones;
* evitar conflictos de dependencias;
* garantizar consistencia.

👉 Herramienta: **Poetry**

---

### 🔹 3. Versionamiento de datos

Permite:

* saber qué datos se usaron;
* reproducir experimentos;
* manejar datasets grandes.

👉 Herramienta: **DVC**

---

### 🔹 4. Tracking de experimentos

Permite:

* comparar modelos;
* registrar métricas;
* guardar artefactos.

👉 Herramienta: **MLflow**

---

## 🚧 Retos frecuentes en proyectos reales

### Reproducibilidad

Un resultado es reproducible cuando otro integrante del equipo puede obtenerlo nuevamente usando el mismo código, los mismos datos y un entorno equivalente.

Sin reproducibilidad:

* las métricas pierden credibilidad;
* los errores son difíciles de diagnosticar;
* la comparación entre modelos se vuelve subjetiva.

---

### Escalabilidad

Un flujo escala cuando puede crecer en volumen de datos, número de experimentos, usuarios, modelos y miembros del equipo sin volverse inmanejable.

En MLOps, escalar no significa solo usar más infraestructura. También significa tener procesos claros para:

* automatizar ejecuciones;
* separar responsabilidades;
* reutilizar componentes;
* evitar trabajo manual repetitivo.

---

### Mantenimiento

Un modelo en producción requiere mantenimiento continuo porque los datos, el comportamiento de los usuarios y las condiciones del negocio cambian.

Algunos riesgos comunes son:

* degradación del desempeño;
* cambios en la distribución de variables;
* dependencias obsoletas;
* falta de documentación;
* pérdida de conocimiento cuando cambia el equipo.

---

## 🧰 Ecosistema de herramientas

MLOps no depende de una única herramienta. Normalmente se combinan varias piezas, cada una enfocada en un problema específico.

| Necesidad | Herramientas frecuentes | Rol en el flujo |
| --- | --- | --- |
| Versionar código | Git, GitHub | Historial, ramas, colaboración y Pull Requests |
| Gestionar entornos | Poetry, Conda, pip-tools | Dependencias reproducibles |
| Versionar datos y modelos | DVC, Git LFS, LakeFS | Trazabilidad de datasets y artefactos grandes |
| Ejecutar pipelines | DVC, Airflow, Prefect | Automatización de etapas |
| Registrar experimentos | MLflow, Weights & Biases, Neptune.ai | Métricas, parámetros, artefactos y comparación |
| Empaquetar aplicaciones | Docker | Contenedores portables |
| Orquestar despliegues | Kubernetes | Escalamiento y operación de servicios |

En este módulo trabajaremos con Git/GitHub, Poetry, DVC y MLflow. Airflow, Docker y Kubernetes aparecen como parte del ecosistema porque suelen usarse en módulos posteriores o en entornos productivos más avanzados.

---

## ⚖️ Data Science vs MLOps

| Aspecto          | Enfoque tradicional      | Enfoque MLOps           |
| ---------------- | ------------------------ | ----------------------- |
| Código           | Notebooks aislados       | Proyectos estructurados |
| Datos            | Sin control de versiones | Versionados             |
| Experimentos     | Manuales                 | Registrados             |
| Reproducibilidad | Baja                     | Alta                    |
| Colaboración     | Limitada                 | Estructurada            |
| Escalabilidad    | Difícil                  | Natural                 |

---

## 🧪 Ejemplo conceptual

### 🔴 Enfoque tradicional

Un científico de datos:

* carga datos localmente;
* entrena un modelo;
* guarda resultados manualmente.

Problemas:

* nadie más puede reproducirlo;
* si cambia el dataset, no hay trazabilidad;
* si el modelo mejora, no hay historial.

---

### 🟢 Enfoque MLOps

El equipo:

* versiona el código;
* versiona los datos;
* define pipelines;
* registra experimentos;
* documenta el proceso.

Resultado:

* cualquier persona puede replicar el flujo;
* los resultados son auditables;
* el sistema puede escalar.

---

## 🔗 Conexión con este módulo

En este módulo aprenderás a implementar este flujo usando:

* Git → control de versiones
* Poetry → entornos reproducibles
* DVC → datos y pipelines
* MLflow → experimentos

Pero más importante aún:

> 💡 aprenderás a integrarlos en un sistema coherente.

---

## 🚀 Lo que viene a continuación

En la siguiente sección profundizaremos en:

👉 el **ciclo de vida completo de un modelo de Machine Learning**

y cómo cada etapa se conecta con prácticas de MLOps.

---

## 🎯 Idea clave para llevar

> ❗ Un modelo no es el final del proceso.
> 👉 Es solo una pieza dentro de un sistema mucho más grande.

---

## 📚 Lecturas recomendadas

* [Google Cloud - MLOps: continuous delivery and automation pipelines in machine learning](https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning)
* [Git documentation - Reference](https://git.github.io/git-reference/)
* [DVC documentation - Data pipelines](https://dvc.org/doc/start/data-pipelines/data-pipelines)
* [MLflow documentation - Tracking](https://www.mlflow.org/docs/latest/ml/tracking)
* [Poetry documentation](https://python-poetry.org/docs/)
