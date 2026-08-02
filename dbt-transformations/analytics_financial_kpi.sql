-- Modelo dbt: Transformación Analítica para Reportes Financieros
{{ config(materialized='table') }}

WITH transacciones_limpias AS (
    SELECT 
        TransaccionID,
        Cliente,
        Monto_Clean AS monto,
        EstadoContrato_Clean AS estado,
        CAST(FechaProceso AS DATE) AS fecha_proceso
    FROM {{ ref('df_silver') }} -- Referencia dinámica al paso anterior del pipeline
)

SELECT 
    fecha_proceso,
    estado,
    COUNT(TransaccionID) AS total_transacciones_procesadas,
    SUM(monto) AS volumen_financiero_consolidado,
    AVG(monto) AS ticket_promedio_seguro
FROM transacciones_limpias
GROUP BY fecha_proceso, estado
ORDER BY volumen_financiero_consolidado DESC
