# 🔍 Unidad 6: Reproducibilidad y auditoría del proceso experimental

## 🌍 ¿Por qué auditar experimentos?

En un proyecto académico puede bastar con mostrar una métrica final.

En un proyecto profesional, esa métrica debe poder explicarse:

* de dónde salió;
* con qué datos se obtuvo;
* con qué código se generó;
* qué configuración se usó;
* qué modelo fue seleccionado y por qué.

La auditoría experimental consiste en conservar evidencia suficiente para reconstruir y justificar el proceso.

---

## 🧩 Evidencia mínima de un experimento

Un experimento reproducible debería dejar registro de:

| Elemento | Ejemplo | Herramienta |
| --- | --- | --- |
| Código | commit de Git | Git |
| Datos | versión del dataset | DVC |
| Entorno | `poetry.lock` | Poetry |
| Parámetros | `test_size`, `random_state`, hiperparámetros | MLflow |
| Métricas | `mae`, `rmse`, `r2` | MLflow |
| Artefactos | modelo, reportes, gráficos | MLflow / DVC |

---

## 🔄 Flujo recomendado

```{mermaid}
flowchart LR
    A[Actualizar código] --> B[Versionar cambios con Git]
    B --> C[Validar entorno con Poetry]
    C --> D[Ejecutar pipeline con DVC]
    D --> E[Registrar experimento con MLflow]
    E --> F[Comparar resultados]
    F --> G[Documentar decisión]
```

---

## 🧪 Ejemplo de preguntas de auditoría

Antes de seleccionar un modelo, el equipo debería poder responder:

* ¿Qué métrica usamos para decidir?
* ¿Por qué esa métrica es adecuada para el caso?
* ¿Qué versión de datos produjo el resultado?
* ¿El resultado se puede reproducir desde cero?
* ¿Qué limitaciones tiene el modelo seleccionado?
* ¿Qué evidencia queda disponible para revisión?

---

## ⚠️ Reproducible no significa idéntico siempre

En Machine Learning pueden existir pequeñas variaciones por:

* inicialización aleatoria;
* paralelismo;
* diferencias de hardware;
* librerías con operaciones no deterministas.

Por eso se recomienda:

* fijar semillas cuando sea posible;
* registrar versiones de dependencias;
* evitar procesos manuales no documentados;
* comparar resultados dentro de tolerancias razonables.

---

## 🧠 Selección responsable del modelo

El mejor modelo no siempre es el que tiene la métrica más alta.

También deben considerarse:

* estabilidad del resultado;
* interpretabilidad;
* costo de ejecución;
* facilidad de despliegue;
* mantenimiento;
* riesgos de sesgo o degradación.

---

## ✅ Checklist de auditoría

Antes de cerrar un experimento, verifica:

* el código está en una rama o commit identificable;
* el entorno se instala con `poetry install`;
* los datos están trazados con DVC;
* el pipeline se puede ejecutar con `dvc repro`;
* MLflow registra parámetros, métricas y artefactos;
* la decisión del modelo queda documentada;
* otra persona puede seguir las instrucciones sin depender de tu computador.

---

## 🎯 Idea clave

> 💡 La reproducibilidad permite repetir el resultado. La auditoría permite confiar en el proceso que produjo ese resultado.
