# 🧩 Caso de Estudio: Predicción del Tiempo de Permanencia de Usuarios

## 🌐 Contexto empresarial

Una plataforma digital de comercio electrónico y contenido busca mejorar la experiencia de sus usuarios a través de estrategias de personalización y optimización del engagement.

Uno de los indicadores clave para el negocio es el **tiempo de permanencia en la aplicación** (*session duration*), ya que está directamente relacionado con:

* la probabilidad de conversión,
* la exposición a contenido relevante,
* la interacción con productos y servicios,
* y el valor generado por usuario.

Actualmente, la compañía cuenta con grandes volúmenes de datos históricos sobre el comportamiento de los usuarios, pero enfrenta dificultades para transformar esa información en decisiones operativas consistentes.

---

## 🚨 Problema a resolver

El equipo de analítica ha sido encargado de responder la siguiente pregunta:

> ❓ ¿Podemos predecir cuánto tiempo permanecerá un usuario en la plataforma durante una sesión?

Responder esta pregunta permitiría:

* priorizar contenidos en tiempo real;
* ajustar estrategias de recomendación;
* optimizar campañas de engagement;
* y mejorar la asignación de recursos en la plataforma.

---

## 🎯 Objetivo del modelo

Construir un modelo de **regresión** que permita estimar:

> ⏱️ `session_minutes`: tiempo de permanencia (en minutos) de un usuario en una sesión.

A partir de variables como:

* características del usuario;
* comportamiento histórico;
* contexto temporal;
* tipo de acceso a la plataforma.

---

## 📊 Variables del problema (visión conceptual)

A continuación se presentan ejemplos de variables que podrían estar disponibles:

### 🔹 Variables del usuario

* `segment`: tipo de usuario (nuevo, activo, en riesgo, churn)
* `historical_avg_session_minutes`
* `historical_sessions_last_7d`
* `days_since_last_session`

### 🔹 Variables contextuales

* `hour_of_day`
* `day_of_week`
* `device_os`
* `site`

### 🔹 Variables de interacción

* `entry_point` (home, búsqueda, recomendación, notificación)
* `push_received_last_24h`

### 🔹 Variable objetivo

* `session_minutes`

---

## ⚠️ Desafíos del problema

Aunque el problema parece directo, en la práctica presenta múltiples retos:

### 1. Variabilidad del comportamiento

El tiempo de sesión puede variar significativamente entre usuarios y momentos del día.

### 2. Sesgos en los datos

Usuarios más activos generan más datos, lo que puede sesgar el modelo.

### 3. Datos dinámicos

El comportamiento del usuario cambia con el tiempo (concept drift).

### 4. Reproducibilidad

Diferentes versiones del dataset pueden producir resultados distintos.

### 5. Escalabilidad

El modelo debe integrarse en un entorno donde múltiples equipos trabajan simultáneamente.

---

## 🧠 Más allá del modelo

Un error común es pensar que el objetivo es simplemente entrenar un modelo que prediga `session_minutes`.

Sin embargo, en un entorno real, el desafío es mucho más amplio:

> ❗ No se trata solo de construir un modelo, sino de construir un sistema que lo haga confiable, reproducible y útil en producción.

Esto implica responder preguntas como:

* ¿Qué versión de los datos se utilizó?
* ¿Qué parámetros se emplearon?
* ¿Cómo se comparan diferentes modelos?
* ¿Cómo se garantiza que otro equipo pueda replicar los resultados?

---

## 🔄 Conexión con MLOps

Este caso de estudio será el hilo conductor del módulo y permitirá introducir progresivamente los componentes de MLOps:

* **Git / GitHub** → colaboración y versionamiento de código
* **Poetry** → gestión de entornos reproducibles
* **DVC** → versionamiento de datos y pipelines
* **MLflow** → seguimiento de experimentos

A lo largo del módulo, este problema evolucionará desde:

👉 un notebook exploratorio
hasta
👉 un sistema estructurado y reproducible

---

## 🧪 Enfoque del módulo

Durante el desarrollo del curso:

1. Se construirá un dataset simulado basado en este contexto.
2. Se desarrollará un modelo base de regresión.
3. Se estructurará el proyecto siguiendo buenas prácticas.
4. Se integrarán herramientas de MLOps.
5. Se evaluará el sistema completo desde una perspectiva aplicada.

---

## 🎯 Idea clave

> 💡 El valor no está solo en predecir el tiempo de sesión,
> sino en construir un sistema que permita hacerlo de forma consistente, reproducible y escalable.

---

## 🚀 Lo que sigue

En la siguiente sección comenzaremos a analizar:

👉 cómo un flujo típico basado en notebooks evoluciona hacia un sistema estructurado

y por qué este cambio es fundamental en entornos reales.
