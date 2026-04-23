# 🔧 Unidad 3: Fundamentos de Git y GitHub

## 🌍 ¿Por qué necesitamos control de versiones?

En proyectos de Machine Learning, el código evoluciona constantemente:

- se prueban nuevas variables;
- se ajustan modelos;
- se corrigen errores;
- se integran cambios de distintos miembros del equipo.

Sin un sistema de control de versiones, esto genera problemas como:

- pérdida de código;
- sobrescritura de cambios;
- dificultad para identificar qué versión funciona;
- imposibilidad de colaborar de forma organizada.

> ❗ En este contexto, Git no es una herramienta opcional.  
> 👉 Es un componente esencial de cualquier flujo MLOps.

---

## 🧠 ¿Qué es Git?

Git es un sistema de control de versiones distribuido que permite:

- registrar cambios en el código;
- mantener historial de versiones;
- trabajar en paralelo mediante ramas;
- colaborar sin sobrescribir el trabajo de otros.

---

## 🧩 Conceptos fundamentales

### 📁 Repositorio

Es el contenedor del proyecto.

Incluye:

- código fuente;
- historial de cambios;
- estructura del proyecto.

---

### 📝 Commit

Un commit representa un punto en el tiempo del proyecto.

Incluye:

- cambios realizados;
- autor;
- mensaje descriptivo.

> 💡 Un commit debe responder:  
> 👉 ¿Qué cambié y por qué?

---

### 📌 Área de staging

Es un espacio intermedio donde se preparan los cambios antes de confirmarlos.

Flujo típico:

```{mermaid}
flowchart LR
    A[Archivo modificado] --> B[Staging Area]
    B --> C[Commit]
```

---

### 🌿 Ramas (branches)

Permiten trabajar en diferentes versiones del proyecto en paralelo.

```{mermaid}
flowchart LR
    A[main] --> B[feature/model]
    A --> C[feature/data]
```

---

### 🔀 Merge

Proceso de integrar cambios de una rama a otra.

```{mermaid}
flowchart LR
    A[feature branch] --> B[merge]
    B --> C[main]
```

---

## ⚠️ Problema sin Git

Imagina el siguiente escenario:

- dos personas editan el mismo archivo;
- ambas guardan cambios;
- una sobrescribe a la otra.

Resultado:

- pérdida de trabajo;
- errores difíciles de rastrear.

---

## 🚀 ¿Qué es GitHub?

GitHub es una plataforma que permite:

- alojar repositorios Git en la nube;
- colaborar con otros desarrolladores;
- gestionar cambios mediante Pull Requests;
- documentar proyectos.

---

## 🔄 Flujo básico de trabajo

```{mermaid}
flowchart LR
    A[Modificar archivos] --> B[git add]
    B --> C[git commit]
    C --> D[git push]
    D --> E[Repositorio en GitHub]
```

---

## 🤝 Trabajo colaborativo

```{mermaid}
flowchart LR
    A[Crear rama] --> B[Desarrollar cambios]
    B --> C[Commit]
    C --> D[Push]
    D --> E[Pull Request]
    E --> F[Revisión]
    F --> G[Merge a main]
```

---

## 🧠 Buenas prácticas esenciales

### 🔹 No trabajar directamente en `main`
### 🔹 Usar ramas descriptivas
### 🔹 Escribir buenos commits
### 🔹 Hacer commits pequeños y frecuentes
### 🔹 Usar Pull Requests

---

## 🔗 Conexión con MLOps

Git es la base de:

- reproducibilidad del código;
- colaboración entre equipos;
- trazabilidad de cambios;
- integración con pipelines automatizados.

---

## 🎯 Idea clave

> 💡 Git no es solo una herramienta para guardar código,  
> es un sistema para gestionar la evolución de un proyecto.

---

## 🚀 Lo que sigue

👉 Cheat sheet práctico de Git
