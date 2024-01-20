{{config(materialized='table')}}

SELECT provincia, pantalla, butacas, espacio_INCAA, COUNT(1)
FROM raw_cine
GROUP BY 1,2,3,4