# 📁 Diseño de Almacenamiento: Delta Lake Open-Format

Para este ecosistema de Big Data, se implementó una arquitectura de **Lakehouse** dividida en tres capas analíticas:

1. **Capa Bronze (Raw):** Datos brutos en formato JSON/CSV extraídos directamente de los cores de seguros.
2. **Capa Silver (Cleansed):** Tablas limpias procesadas mediante PySpark, con tipos de datos corregidos y registros corruptos eliminados.
3. **Capa Gold (Curated):** Datos almacenados en formato **Delta (Parquet optimizado)** con soporte de transacciones ACID y versionado de datos para auditorías financieras.
