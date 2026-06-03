# 🧾 Unidad 5: DVC Cheat Sheet

## 🎯 Propósito

Este documento resume los comandos más importantes de DVC, explicando:

- qué hace cada comando,
- cuándo usarlo,
- errores comunes.

---

## 🚀 Inicialización

### `dvc init`

Inicializa DVC en el repositorio.

```bash
dvc init
```

👉 Cuándo usarlo:
- después de inicializar Git.

---

## 📦 Versionar datos

### `dvc add`

Versiona un archivo o dataset.

```bash
dvc add data/raw/dataset.csv
```

👉 Qué hace:
- crea archivo `.dvc`;
- actualiza `.gitignore`.

---

## 📤 Subir datos

### `dvc push`

Envía datos al almacenamiento remoto.

```bash
dvc push
```

---

## 📥 Descargar datos

### `dvc pull`

Descarga datos desde remoto.

```bash
dvc pull
```

---

## 🔗 Conectar almacenamiento remoto

### `dvc remote add`

```bash
dvc remote add -d myremote <url>
```

---

## 🔄 Pipeline

### `dvc repro`

Ejecuta el pipeline completo.

```bash
dvc repro
```

👉 Clave en MLOps:
- ejecuta solo lo necesario.

---

## 📄 Archivos importantes

- `dvc.yaml` → define pipeline
- `dvc.lock` → versiones exactas
- `.dvc` → referencia datasets

---

## ⚠️ Errores comunes

### ❌ No hacer `git add` de archivos `.dvc`
👉 Se pierde trazabilidad

---

### ❌ Olvidar `dvc push`
👉 Otros no pueden acceder a datos

---

### ❌ Modificar datos manualmente
👉 Rompe el pipeline

---

## 🧠 Buenas prácticas

- usar DVC desde el inicio;
- versionar datasets clave;
- usar pipelines (`dvc.yaml`);
- mantener sincronizado con Git.

---

## 🎯 Idea clave

> DVC permite versionar datos y reproducir pipelines,  
> no solo almacenar archivos.

---

## 🚀 Lo que sigue

👉 Pipeline completo con DVC
