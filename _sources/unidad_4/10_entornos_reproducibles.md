# 🔁 Unidad 4: Entornos reproducibles en proyectos de Machine Learning

## 🌍 ¿Qué significa reproducibilidad?

En Machine Learning, la reproducibilidad implica que un experimento pueda ejecutarse nuevamente bajo las mismas condiciones y producir resultados consistentes.

Esto requiere controlar:

- el código,
- los datos,
- y el entorno de ejecución.

> ❗ Si no puedes reproducir un resultado, no puedes confiar plenamente en él.

---

## ⚠️ El problema real

En equipos de trabajo es común observar:

- diferentes versiones de librerías;
- conflictos entre dependencias;
- resultados inconsistentes entre máquinas;
- fallas al desplegar en producción.

Ejemplo típico:

> “El modelo funcionaba en desarrollo, pero falla en producción.”

---

## 🧠 Componentes de la reproducibilidad

```{mermaid}
flowchart LR
    A[Código] --> D[Reproducibilidad]
    B[Datos] --> D
    C[Entorno] --> D
```

Para lograr reproducibilidad, los tres deben estar controlados.

---

## 📦 Rol de Poetry

Poetry permite controlar el entorno mediante:

- definición explícita de dependencias;
- versiones exactas en `poetry.lock`;
- creación automática de entornos virtuales.

---

## 🔄 Flujo reproducible con Poetry

```{mermaid}
flowchart LR
    A[Clonar repositorio] --> B[poetry install]
    B --> C[Entorno consistente]
    C --> D[Ejecutar código]
    D --> E[Mismos resultados]
```

---

## 🧪 Ejemplo práctico

Supongamos que un equipo trabaja en un modelo de regresión.

### Paso 1: un integrante crea el entorno

```bash
poetry init
poetry add pandas scikit-learn numpy
```

### Paso 2: se generan archivos clave

- `pyproject.toml`
- `poetry.lock`

### Paso 3: otro integrante clona el proyecto

```bash
git clone repo.git
cd repo
poetry install
```

👉 Resultado: mismo entorno, sin conflictos.

---

## ⚠️ ¿Qué pasa sin Poetry?

```{mermaid}
flowchart LR
    A[Instalar manualmente] --> B[Versiones distintas]
    B --> C[Errores]
    C --> D[Resultados inconsistentes]
```

---

## 🔗 Integración con MLOps

Un flujo completo incluye:

| Componente | Herramienta |
|-----------|------------|
| Código | Git |
| Datos | DVC |
| Experimentos | MLflow |
| Entorno | Poetry |

---

## 🧠 Buenas prácticas

- siempre incluir `poetry.lock` en el repositorio;
- no mezclar pip con Poetry;
- documentar cómo instalar el entorno;
- usar `poetry install` como paso inicial.

---

## 🧪 Aplicación al proyecto del curso

En este módulo:

- el entorno será gestionado con Poetry;
- el código estará versionado con Git;
- el pipeline evolucionará hacia DVC;
- los experimentos se integrarán con MLflow.

👉 Esto permite construir un sistema reproducible.

---

## 🎯 Idea clave

> 💡 La reproducibilidad no es opcional en MLOps.  
> Es la base para construir sistemas confiables.

---

## 🚀 Lo que sigue

En la siguiente unidad comenzaremos con:

👉 versionamiento de datos con DVC
