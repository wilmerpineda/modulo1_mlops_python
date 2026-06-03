# 📦 Unidad 5: Fundamentos de versionamiento de datos con DVC

## 🌍 El problema que Git no resuelve

En la unidad anterior vimos cómo Git permite versionar código. Sin embargo, en proyectos de Machine Learning el código no es el único elemento crítico, porque los resultados dependen también de archivos que suelen ser grandes, cambiantes y difíciles de almacenar dentro del historial de Git:

- datasets;
- archivos intermedios;
- modelos entrenados;
- resultados de experimentos.

---

## ⚠️ ¿Por qué no usar Git para datos?

Podríamos pensar que Git puede resolverlo todo:

> “si Git versiona código, también puede versionar datos”

Pero esto genera problemas importantes:

- archivos grandes (GB o más);
- repositorios lentos;
- historial difícil de manejar;
- costos de almacenamiento elevados.

---

## 🧠 El problema real

En Machine Learning, los resultados dependen directamente de los datos. Si no versionamos los datos, una métrica puede cambiar sin que sepamos si la causa fue el código, el dataset, el preprocesamiento o una combinación de todos esos factores:

- no sabemos con qué dataset se entrenó el modelo;
- no podemos reproducir resultados;
- no podemos comparar experimentos de forma confiable.

---

## 🔄 Relación entre datos y modelo

```{mermaid}
flowchart LR
    A[Datos] --> B[Modelo]
    B --> C[Predicciones]
```

👉 Si cambian los datos, cambia el modelo.

---

## 🚀 ¿Qué es DVC?

DVC (*Data Version Control*) es una herramienta que permite conectar el versionamiento de datos con el flujo de Git. Su objetivo es mantener el repositorio liviano, pero conservar la trazabilidad necesaria para reproducir experimentos:

- versionar datos sin almacenarlos directamente en Git;
- rastrear cambios en datasets;
- construir pipelines reproducibles;
- integrar datos con código.

---

## 🎯 ¿Qué resuelve DVC?

DVC permite que el equipo trabaje con datos y artefactos grandes sin perder control sobre qué versión se usó en cada experimento:

- asociar datasets a commits de Git;
- reproducir pipelines completos;
- almacenar datos en remoto (S3, Drive, etc.);
- mantener repositorios livianos.

---

## 🧩 ¿Cómo funciona DVC?

DVC no guarda los datos directamente en Git. En su lugar, separa los archivos pesados de los metadatos que describen su ubicación y contenido:

- crea archivos `.dvc` que actúan como punteros;
- los datos se almacenan en un sistema externo;
- Git versiona solo los metadatos.

---

## 🔄 Flujo conceptual con DVC

```{mermaid}
flowchart LR
    A[Dataset] --> B[dvc add]
    B --> C[Archivo .dvc]
    C --> D[Git]
    B --> E[Almacenamiento remoto]
```

---

## 📄 Archivos clave

### 🔹 `.dvc`

Un archivo `.dvc` referencia un dataset o artefacto concreto. Git versiona este archivo pequeño, mientras DVC se encarga del contenido real.

Ejemplo conceptual:

```yaml
outs:
  - md5: abc123
    path: data/raw/data.csv
```

---

### 🔹 `dvc.yaml`

`dvc.yaml` define pipelines y permite estructurar etapas encadenadas. Cada etapa puede declarar dependencias, comandos y salidas:

- procesamiento;
- entrenamiento;
- evaluación.

---

### 🔹 `dvc.lock`

Registra versiones exactas de dependencias del pipeline.

---

## 🔗 Integración con Git

DVC funciona sobre Git:

- Git versiona código y archivos `.dvc`;
- DVC versiona datos.

---

## 🧪 Ejemplo conceptual

```bash
dvc init
dvc add data/raw/dataset.csv
git add data/raw/dataset.csv.dvc .gitignore
git commit -m "add dataset"
```

👉 El dataset queda versionado sin estar en Git.

---

## ⚠️ Problemas sin DVC

```{mermaid}
flowchart LR
    A[Dataset v1] --> B[Modelo v1]
    A2[Dataset v2] --> B2[Modelo v2]
    B --> C[Resultados]
    B2 --> C2[Resultados distintos]
```

👉 Sin control de datos:
- no hay trazabilidad;
- no hay reproducibilidad.

---

## 🔄 DVC como pipeline

```{mermaid}
flowchart LR
    A[Raw Data] --> B[Processing]
    B --> C[Training]
    C --> D[Evaluation]
```

Cada etapa puede:

- depender de archivos previos;
- generar outputs;
- ser reproducida automáticamente.

---

## 🧠 Conexión con MLOps

DVC se integra con:

| Componente | Herramienta |
|-----------|------------|
| Código | Git |
| Entorno | Poetry |
| Datos | DVC |
| Experimentos | MLflow |

---

## 🧪 Aplicación al proyecto del curso

En este módulo:

- versionaremos el dataset generado;
- construiremos un pipeline reproducible;
- separaremos etapas del modelo;
- conectaremos datos con código.

---

## 🎯 Idea clave

> 💡 En Machine Learning, versionar código no es suficiente.  
> También debemos versionar los datos.

---

## 📚 Lecturas recomendadas

* [DVC documentation - Get started](https://dvc.org/doc/start)
* [DVC documentation - Data pipelines](https://dvc.org/doc/start/data-pipelines/data-pipelines)
* [DVC documentation - Defining pipelines](https://dvc.org/doc/user-guide/pipelines/defining-pipelines)

---

## 🚀 Lo que sigue

👉 Cheat sheet práctico de DVC
