# 🧾 Unidad 4: Poetry Cheat Sheet

## 🎯 Propósito

Este documento resume los comandos más importantes de Poetry, explicando:

- qué hace cada comando,
- cuándo usarlo,
- errores comunes.

---

## 🚀 Inicializar proyecto

### `poetry init`

Crea un proyecto interactivo.

```bash
poetry init
```

👉 Cuándo usarlo:
- iniciar un proyecto desde cero.

---

### `poetry new`

Crea estructura completa de proyecto.

```bash
poetry new nombre_proyecto
```

---

## 📦 Gestión de dependencias

### `poetry add`

Instala una librería y la registra.

```bash
poetry add pandas
poetry add scikit-learn
```

👉 También puedes fijar versiones:

```bash
poetry add numpy==1.24.0
```

---

### `poetry remove`

Elimina dependencias.

```bash
poetry remove pandas
```

---

## 🔧 Instalación del entorno

### `poetry install`

Instala todas las dependencias del proyecto.

```bash
poetry install
```

👉 Cuándo usarlo:
- al clonar un repositorio.

---

## 🐍 Entorno virtual

### `poetry shell`

Activa el entorno virtual.

```bash
poetry shell
```

---

### `poetry env info`

Muestra información del entorno.

```bash
poetry env info
```

---

## ▶️ Ejecutar comandos

### `poetry run`

Ejecuta comandos dentro del entorno.

```bash
poetry run python script.py
```

---

## 🔄 Actualización

### `poetry update`

Actualiza dependencias.

```bash
poetry update
```

⚠️ Puede romper compatibilidad si no se controla.

---

## 📄 Archivos clave

### `pyproject.toml`
Define dependencias y configuración.

### `poetry.lock`
Asegura versiones exactas.

---

## ⚠️ Errores comunes

### ❌ No usar `poetry install`
👉 El entorno no se crea correctamente.

---

### ❌ Mezclar pip con poetry
👉 Rompe consistencia.

---

### ❌ No subir `poetry.lock`
👉 Otros no podrán reproducir entorno.

---

### ❌ Actualizar sin control
👉 Puede romper el proyecto.

---

## 🧠 Buenas prácticas

- usar siempre `poetry add`;
- versionar `poetry.lock`;
- no mezclar herramientas;
- documentar dependencias.

---

## 🎯 Idea clave

> Poetry no solo instala librerías,  
> garantiza que todos trabajen en el mismo entorno.

---

## 🚀 Lo que sigue

👉 Entornos reproducibles en proyectos reales
