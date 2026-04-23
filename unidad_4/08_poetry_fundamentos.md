# 📦 Unidad 4: Fundamentos de gestión de entornos con Poetry

## 🌍 El problema de los entornos en Machine Learning

En proyectos de Machine Learning, no solo importa el código.

También importan:

- las versiones de librerías;
- las dependencias instaladas;
- la configuración del entorno.

Un mismo código puede comportarse de manera diferente dependiendo del entorno donde se ejecute.

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

Un entorno es el conjunto de:

- versión de Python;
- librerías instaladas;
- dependencias del proyecto.

---

## 🔄 ¿Por qué es un problema en MLOps?

En MLOps necesitamos:

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

Lista de dependencias:

```txt
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

Permite crear entornos virtuales.

👉 Problemas:
- más pesado;
- menos enfocado en proyectos reproducibles modernos;
- gestión compleja en equipos grandes.

---

## 🚀 ¿Qué es Poetry?

Poetry es una herramienta moderna para:

- gestión de dependencias;
- control de entornos virtuales;
- empaquetado de proyectos Python.

---

## 🎯 ¿Qué resuelve Poetry?

Poetry permite:

- definir dependencias de forma clara;
- asegurar versiones consistentes;
- reproducir entornos fácilmente;
- integrar el proyecto como paquete Python.

---

## 🧩 Componentes clave

### 📄 `pyproject.toml`

Archivo principal del proyecto.

Define:

- nombre del proyecto;
- versión;
- dependencias;
- configuración.

---

### 🔒 `poetry.lock`

Archivo generado automáticamente.

Contiene:

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

## 🚀 Lo que sigue

👉 Cheat sheet práctico de Poetry
