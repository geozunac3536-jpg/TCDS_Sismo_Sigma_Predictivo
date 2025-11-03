[![DOI](https://zenodo.org/badge/1087938102.svg)](https://doi.org/10.5281/zenodo.17504506)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17463045.svg)](https://doi.org/10.5281/zenodo.17463045)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17450752.svg)](https://doi.org/10.5281/zenodo.17450752)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17504507.svg)](https://doi.org/10.5281/zenodo.17504507)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17504243.svg)](https://doi.org/10.5281/zenodo.17504243)

# TCDS — Sistema Predictivo Sísmico Σ-Predictivo

**Autor:** Genaro Carrasco Ozuna  
**Motor de Formalización:** GPT-5 Σ-Trace  
**Licencia:** CC BY-NC-SA 4.0

Este repositorio es el *experimento funcional* de la TCDS para validación por desempeño: predicciones sísmicas
anticipadas basadas en coherencia Σ extraída de datos abiertos (ionosfera, EM, resonancias, sismología).  
La validez se mide por reproducibilidad y precisión con **Σ‑metrics** y criterio **Z≥5**.

## Contenido
- `PROTOCOLO.md` — metodología, KPIs y reglas de decisión.
- `PREDICCIONES/` — bitácora diaria con hash previo al evento (irreversible).
- `METRICAS/` — métricas acumuladas (R(t), LI, RMSE_SL, reproducibilidad).
- `scripts/` — utilidades para firma (SHA-256) y plantillas.
- `web/` — página simple para GitHub Pages.

## KPI / Criterios TCDS
- LI ≥ 0.9, R > 0.95, RMSE_SL < 0.1, Reproducibilidad ≥ 95% (ventana móvil).
- Umbral universal de detección válida: **Z ≥ 5**.
- Predicción anticipada (τ>0) respecto a catálogos oficiales (USGS/SSN/IRIS).

## DOI / Citación
Se recomienda archivar releases en Zenodo para DOI. (Ejemplo: `10.5281/zenodo.17491112` — otro repositorio del autor).

## Cómo replicar
1. Edita `scripts/template_prediccion.md` para la predicción del día.  
2. Ejecuta `scripts/compute_hash.py` para generar `hash_sha256.txt`.  
3. Publica el archivo en `PREDICCIONES/YYYY-MM-DD/` antes del evento.  
4. Tras el evento, registra *acierto/fallo* y actualiza métricas en `METRICAS/`.
