# 🔧 Unidad 3: Fundamentos de Git y GitHub

## 🌍 ¿Por qué necesitamos control de versiones?

En proyectos de Machine Learning, el código evoluciona constantemente porque el equipo prueba hipótesis, corrige errores y ajusta decisiones a medida que entiende mejor los datos:

- se prueban nuevas variables;
- se ajustan modelos;
- se corrigen errores;
- se integran cambios de distintos miembros del equipo.

Sin un sistema de control de versiones, esos cambios quedan dispersos y se vuelve difícil saber qué versión produjo un resultado específico. Esto genera problemas como:

- pérdida de código;
- sobrescritura de cambios;
- dificultad para identificar qué versión funciona;
- imposibilidad de colaborar de forma organizada.

> ❗ En este contexto, Git no es una herramienta opcional.  
> 👉 Es un componente esencial de cualquier flujo MLOps.

---

## 🧠 ¿Qué es Git?

Git es un sistema de control de versiones distribuido que permite registrar la evolución del proyecto y trabajar de forma colaborativa sin depender de una única copia central:

- registrar cambios en el código;
- mantener historial de versiones;
- trabajar en paralelo mediante ramas;
- colaborar sin sobrescribir el trabajo de otros.

---

## 🧩 Conceptos fundamentales

### 📁 Repositorio

Un repositorio es el contenedor del proyecto y de su historial. Incluye:

- código fuente;
- historial de cambios;
- estructura del proyecto.

---

### 📝 Commit

Un commit representa un punto en el tiempo del proyecto. En lugar de guardar archivos sueltos, Git guarda una fotografía lógica de los cambios preparados, junto con información que permite reconstruir el historial:

- cambios realizados;
- autor;
- mensaje descriptivo.

> 💡 Un commit debe responder:  
> 👉 ¿Qué cambié y por qué?

---

### 📌 Área de staging

El área de staging es un espacio intermedio donde se preparan los cambios antes de confirmarlos. Esta separación permite construir commits más limpios, seleccionando solo los archivos o fragmentos que pertenecen a una misma intención de cambio.

Flujo típico:

```{mermaid}
flowchart LR
    A[Archivo modificado] --> B[Staging Area]
    B --> C[Commit]
```

---

### 🌿 Ramas (branches)

Las ramas permiten trabajar en diferentes versiones del proyecto en paralelo. En un equipo de MLOps, esto es clave para que una persona pueda mejorar el pipeline de datos mientras otra ajusta el modelo sin bloquearse mutuamente.

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

Estas prácticas reducen errores de colaboración y hacen que el historial del proyecto sea más fácil de revisar:

* no trabajar directamente en `main`, porque esa rama debe representar una versión estable;
* usar ramas descriptivas, por ejemplo `feature/data-pipeline` o `fix/model-metrics`;
* escribir commits claros que expliquen qué cambió y por qué;
* hacer commits pequeños y frecuentes para facilitar la revisión;
* usar Pull Requests para discutir, validar e integrar cambios antes del merge.

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

## 📚 Lecturas recomendadas

* [Git documentation - Reference](https://git.github.io/git-reference/)
* [Pro Git Book](https://git-scm.com/book/en/v2)
* [GitHub Docs - About pull requests](https://docs.github.com/articles/using-pull-requests)

---

## 🚀 Lo que sigue

👉 Cheat sheet práctico de Git
