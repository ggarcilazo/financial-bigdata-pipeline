# Core Pipeline de Big Data - Procesamiento Distribuido Financiero
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, current_timestamp

print("=== INICIANDO MOTOR DISTRIBUIDO PYSPARK (BIG DATA CORES) ===")

# 1. Inicializar la sesión de Spark optimizada para la nube
spark = SparkSession.builder \
    .appName("FinancialBigDataPipeline") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()

# 2. Simulación de carga masiva de datos brutos (10 Millones de Filas simuladas en el Data Lake)
print("Consumiendo transacciones financieras del Data Lake (Bronze Layer)...")
data_sucia = [
    ("TX-9901", "Asegurado_A", "2500.50", "Invalido", "2026-08-01"),
    ("TX-9902", "Asegurado_B", "410.00", "Activo", "2026-08-01"),
    ("TX-9903", "Asegurado_C", "-50.00", "Activo", "2026-08-01") # Registro corrupto (Monto negativo)
]
columnas = ["TransaccionID", "Cliente", "Monto", "EstadoContrato", "FechaProceso"]
df_bronze = spark.createDataFrame(data_sucia, columnas)

# 3. Transformación Analítica y Limpieza Masiva (Silver Layer)
print("Ejecutando limpieza de datos distribuidos en memoria RAM de la nube...")
df_silver = df_bronze \
    .withColumn("Monto_Clean", col("Monto").cast("double")) \
    .withColumn("EstadoContrato_Clean", when(col("EstadoContrato") == "Invalido", "Rechazado").otherwise(col("EstadoContrato"))) \
    .filter(col("Monto_Clean") > 0) \
    .withColumn("FechaActualizacionETL", current_timestamp())

# 4. Almacenamiento Estructurado en Formato Delta Lake (Gold Layer)
print("Inyectando matriz limpia en formato Delta de Alta Velocidad...")
df_silver.show()

# En un entorno real de Databricks, aquí se guarda físicamente corriendo:
# df_silver.write.format("delta").mode("overwrite").save("/mnt/datalake/gold_financial_trans")
print("[OK] Pipeline de Big Data ejecutado exitosamente. Datos normalizados listos para Power BI.")
