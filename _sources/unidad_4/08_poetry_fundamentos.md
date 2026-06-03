# 📦 Unidad 4: Fundamentos de gestión de entornos con Poetry

## 🌍 El problema de los entornos en Machine Learning

En proyectos de Machine Learning, no solo importa el código. También importan las condiciones bajo las cuales ese código se ejecuta, porque pequeñas diferencias en librerías o versiones pueden cambiar resultados, generar errores o impedir que otra persona reproduzca el experimento:

- las versiones de librerías;
- las dependencias instaladas;
- la configuración del entorno.

Un mismo código puede comportarse de manera diferente dependiendo del entorno donde se ejecute. Por eso la gestión del entorno debe tratarse como parte del proyecto, no como una configuración informal de cada computador.

---

## ⚠️ El clásico problema

Seguramente has visto (o vivido) algo como:

> ❗ “en mi computador funciona perfectamente”  
> ❗ “en el tuyo da error”

Esto ocurre porque:

- versiones de librerías son distintas;
- dependencias no están sincronizadas;
- el entorno no es reproducible.

---

## 🧠 ¿Qué es un entorno?

Un entorno es el conjunto de componentes que hacen posible ejecutar el proyecto de forma consistente:

- versión de Python;
- librerías instaladas;
- dependencias del proyecto.

---

## 🔄 ¿Por qué es un problema en MLOps?

En MLOps necesitamos controlar el entorno porque los experimentos, pipelines y despliegues deben poder repetirse en distintos contextos:

- reproducibilidad;
- consistencia;
- colaboración entre equipos;
- despliegue en distintos entornos (local, staging, producción).

Sin control de entornos:

- no se pueden replicar experimentos;
- aparecen errores inesperados;
- se pierde confianza en los resultados.

---

## 🧰 Soluciones tradicionales

### 📄 `requirements.txt`

Un archivo `requirements.txt` lista dependencias de forma sencilla:

```text
pandas==2.0.0
scikit-learn==1.3.0
numpy==1.24.0
```

👉 Problemas:
- no maneja bien dependencias indirectas;
- no asegura consistencia total;
- difícil de mantener en proyectos grandes.

---

### 🐍 Conda

Conda permite crear entornos virtuales y manejar paquetes de distintos ecosistemas. Es una alternativa muy usada en ciencia de datos, aunque en este módulo nos enfocamos en Poetry por su integración con `pyproject.toml` y su manejo explícito de lock files.

👉 Problemas:
- más pesado;
- menos enfocado en proyectos reproducibles modernos;
- gestión compleja en equipos grandes.

---

## 🚀 ¿Qué es Poetry?

Poetry es una herramienta moderna para gestionar proyectos Python de forma reproducible. Su valor no está solo en instalar librerías, sino en mantener una definición clara del proyecto y un archivo de bloqueo con versiones resueltas:

- gestión de dependencias;
- control de entornos virtuales;
- empaquetado de proyectos Python.

---

## 🎯 ¿Qué resuelve Poetry?

Poetry permite convertir la instalación del entorno en un proceso documentado y repetible:

- definir dependencias de forma clara;
- asegurar versiones consistentes;
- reproducir entornos fácilmente;
- integrar el proyecto como paquete Python.

---

## 🧩 Componentes clave

### 📄 `pyproject.toml`

`pyproject.toml` es el archivo principal del proyecto. Define:

- nombre del proyecto;
- versión;
- dependencias;
- configuración.

---

### 🔒 `poetry.lock`

`poetry.lock` es un archivo generado automáticamente después de resolver dependencias. Contiene:

- versiones exactas de dependencias;
- dependencias indirectas;
- información para reproducibilidad.

---

## 🔄 Flujo básico con Poetry

```{mermaid}
flowchart LR
    A[Definir dependencias] --> B[poetry add]
    B --> C[Actualizar pyproject.toml]
    C --> D[Generar poetry.lock]
    D --> E[Entorno reproducible]
```

---

## 🧪 Ejemplo conceptual

```bash
poetry init
poetry add pandas scikit-learn numpy
poetry install
```

---

## ⚠️ Diferencia clave con pip

| Aspecto | pip | Poetry |
|--------|-----|--------|
| Gestión de dependencias | Básica | Avanzada |
| Reproducibilidad | Limitada | Alta |
| Entorno virtual | Externo | Integrado |
| Lock file | No siempre | Sí (`poetry.lock`) |

---

## 🔗 Conexión con MLOps

Poetry permite:

- reproducir experimentos;
- compartir entornos entre equipos;
- garantizar consistencia entre desarrollo y producción;
- integrarse con pipelines automatizados.

---

## 🧠 Ejemplo en este curso

En el proyecto del módulo:

- el código estará versionado con Git;
- los datos con DVC;
- los experimentos con MLflow;
- y el entorno con Poetry.

👉 Es decir, cada componente resuelve un problema distinto.

---

## 🎯 Idea clave

> 💡 No basta con versionar código.  
> También debemos versionar el entorno en el que ese código se ejecuta.

---

## 📚 Lecturas recomendadas

* [Poetry documentation](https://python-poetry.org/docs/)
* [Poetry documentation - Managing dependencies](https://python-poetry.org/docs/managing-dependencies/)
* [Python Packaging User Guide - pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)

---

## 🚀 Lo que sigue

👉 Cheat sheet práctico de Poetry
