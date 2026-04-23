# 🧾 Unidad 3: Git Cheat Sheet

## 🎯 Propósito

Este documento resume los comandos más importantes de Git, explicando:

- qué hace cada comando,
- cuándo usarlo,
- y errores comunes.

---

## 🚀 Inicialización de repositorio

### `git init`

Inicializa un repositorio Git en la carpeta actual.

```bash
git init
```

👉 Cuándo usarlo:
- al iniciar un proyecto nuevo.

⚠️ Error común:
- ejecutarlo en una carpeta incorrecta.

---

## 📥 Estado del repositorio

### `git status`

Muestra el estado actual de los archivos.

```bash
git status
```

👉 Permite ver:
- archivos modificados;
- archivos en staging;
- archivos no rastreados.

---

## ➕ Agregar cambios

### `git add`

Agrega archivos al área de staging.

```bash
git add archivo.py
git add .
```

👉 Cuándo usarlo:
- antes de hacer commit.

⚠️ Error común:
- usar `git add .` sin revisar cambios.

---

## 💾 Guardar cambios

### `git commit`

Guarda cambios en el historial.

```bash
git commit -m "add preprocessing step"
```

👉 Buenas prácticas:
- mensajes claros y específicos.

❌ Malo:
```bash
git commit -m "cambios"
```

---

## 🌿 Ramas

### `git branch`

Lista ramas existentes.

```bash
git branch
```

### `git checkout -b`

Crea y cambia a una nueva rama.

```bash
git checkout -b feature/model
```

👉 Cuándo usarlo:
- para desarrollar nuevas funcionalidades.

---

## 🔄 Cambiar de rama

```bash
git checkout main
```

---

## 🔀 Merge

Integra cambios de una rama a otra.

```bash
git merge feature/model
```

⚠️ Puede generar conflictos.

---

## 🌍 Trabajo con GitHub

### `git remote add`

Conecta repositorio local con remoto.

```bash
git remote add origin https://github.com/user/repo.git
```

---

### `git push`

Envía cambios al repositorio remoto.

```bash
git push origin main
```

---

### `git pull`

Trae cambios del repositorio remoto.

```bash
git pull origin main
```

---

## 🔁 Flujo típico

```bash
git checkout -b feature/data
git add .
git commit -m "add dataset generation"
git push origin feature/data
```

Luego:
- crear Pull Request en GitHub;
- revisión;
- merge a `main`.

---

## ⚠️ Errores comunes

### 1. Trabajar en `main`
👉 Evítalo siempre.

### 2. No hacer pull antes de trabajar
👉 Puede generar conflictos.

### 3. Commits gigantes
👉 Difíciles de revisar.

### 4. Mensajes poco claros
👉 Pierden trazabilidad.

---

## 🎯 Idea clave

> Git no es memorizar comandos.  
> Es entender el flujo de trabajo.

---

## 🚀 Lo que sigue

👉 Flujo colaborativo con GitHub (notebook práctico)
