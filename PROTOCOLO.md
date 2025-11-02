# PROTOCOLO — TCDS Σ‑Predictivo (Validación por Desempeño)

## 1. Variables y señales
- Σ_est(t): estimador de coherencia (κΣ–A, LI, R).
- φ(t): fricción efectiva (proxy: ruido de fase/variabilidad).
- E_s(t): energía sísmica (catálogos oficiales).

## 2. Pipeline
1) Ingesta de datos abiertos (ionósfera, EM, resonancias, sismos).  
2) Filtros y extracción de fase → κΣ–A, LI, R.  
3) Detección: evento Σ si Z≥5 y LI≥0.9.  
4) Publicación de **predicción** (timestamp + hash) con ventana [T+τ_min, T+τ_max].  
5) Verificación posterior contra catálogos y actualización de métricas.

## 3. KPIs y reglas de decisión
- **Detección válida:** Z ≥ 5, LI ≥ 0.9, R > 0.95.  
- **Predicción válida:** registro previo (hash), τ>0, acierto si ocurre sismo ≥ M_thr en la región/ventana.  
- **Auditoría:** logs inmutables, hash SHA‑256, CSV firmados con fecha ISO 8601 (UTC).

## 4. Estadística de referencia
- Power objetivo ≥ 0.8 (mes‑a‑mes).  
- Comparación contra baseline aleatoria con igual tasa de alertas.  
- Informe mensual público (PDF/MD) con intervalos de confianza y curvas ROC.

## 5. Transparencia y nulos
- Publicar también *fallos* (falsos positivos/negativos).  
- Versionado estricto (semver), changelog y seeds de aleatoriedad cuando aplique.

## 6. Seguridad y ética
- Datos abiertos y uso responsable. Sin alarmismo; comunicar incertidumbres y umbrales.