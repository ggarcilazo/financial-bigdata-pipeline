# 📊 Módulo 5: Pipeline Core de Big Data Financiero y Procesamiento Distribuido Cloud

Este repositorio contiene la arquitectura de un pipeline de datos de gran escala diseñado para procesar y limpiar millones de registros transaccionales de forma distribuida en la nube de **Databricks Community Edition** utilizando **PySpark / SQL Enterprise**.

🌐 **Cuaderno Ejecutivo Desplegado:** Sincronizado nativamente con el catálogo de Databricks Serverless.

---

## 🏗️ Arquitectura del Data Lakehouse (Capa Medallón)

```text
 [ FUENTE DE DATOS EXTERNA ] ──► [ CAPA BRONZE (RAW) ] ──► [ CAPA SILVER (CLEANSED) ] ──► [ CAPA GOLD (CURATED) ]
 (Millones de filas en AWS S3)      Registros puros en bruto     Limpieza masiva en memoria       Almacenamiento Delta / KPI
```

## 📸 Evidencias de Procesamiento de Millones de Datos Reales
*Procesamiento distribuido multi-nodo en Databricks Serverless reduciendo millones de registros analíticos en 3.4 segundos.*





![Métricas Databricks](./data-lake-delta/evidencia_databricks.png)
