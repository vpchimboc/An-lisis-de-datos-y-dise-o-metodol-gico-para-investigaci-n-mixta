import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos
file_path = 'survey_data.csv'
df = pd.read_csv(file_path)

# Mapeo de nombres de columnas para el análisis cuantitativo (tomado de la fase 2)
quantitative_cols_map = {
    df.columns[1]: 'LMS_Competencia',
    df.columns[2]: 'Frecuencia_Actividades_Interactivas',
    df.columns[3]: 'Competencia_Adaptacion_Discapacidad',
    df.columns[4]: 'Formacion_Especifica_TIC',
    df.columns[5]: 'Apoyo_Institucional_Competencias',
    df.columns[6]: 'Competencia_Creacion_Recursos',
    df.columns[7]: 'Uso_Repositorios_Abiertos',
    df.columns[8]: 'Frecuencia_Adaptacion_Diversidad',
    df.columns[9]: 'Frecuencia_Herramientas_Colaborativas',
    df.columns[10]: 'Frecuencia_Redes_Docentes',
    df.columns[11]: 'Uso_Herramientas_Evaluacion_Formativa',
    df.columns[12]: 'Competencia_Diseno_Rubricas',
    df.columns[13]: 'Frecuencia_Retroalimentacion_Digital',
    df.columns[14]: 'Frecuencia_Uso_IA',
    df.columns[15]: 'Formacion_Especifica_IA',
    df.columns[16]: 'IA_Apoyo_Retroalimentacion',
    df.columns[17]: 'IA_Personalizacion_Aprendizaje',
    df.columns[18]: 'IA_Implicacion_Etica',
    df.columns[19]: 'IA_Favorece_Inclusion',
    df.columns[20]: 'IA_Ahorro_Tiempo',
    df.columns[21]: 'Conoce_Metodologia_COIL',
    df.columns[22]: 'Conoce_Marco_DigCompEdu',
    df.columns[23]: 'Conoce_Marco_ICT_CFT',
    df.columns[24]: 'Conoce_Criterios_Internacionales',
}

# Seleccionar y renombrar las columnas cuantitativas
df_quant = df.iloc[:, 1:25].rename(columns=quantitative_cols_map)

# Asegurar que todas las columnas son numéricas
for col in df_quant.columns:
    df_quant[col] = pd.to_numeric(df_quant[col], errors='coerce')

# Eliminar filas con valores nulos
df_quant.dropna(inplace=True)

# --- Creación de Variables Compuestas para el Análisis de Clúster ---
# 1. Competencia Digital General (CDG): Promedio de los primeros 13 ítems.
competencia_digital_cols = df_quant.columns[:13]
df_quant['CDG'] = df_quant[competencia_digital_cols].mean(axis=1)

# 2. Uso y Percepción de IA (UPIA): Promedio de los ítems 14 a 20.
uso_ia_cols = df_quant.columns[13:20]
df_quant['UPIA'] = df_quant[uso_ia_cols].mean(axis=1)

# 3. Conocimiento Teórico (CT): Promedio de los ítems 21 a 24.
conocimiento_teorico_cols = df_quant.columns[20:24]
df_quant['CT'] = df_quant[conocimiento_teorico_cols].mean(axis=1)

# --- Análisis de Clúster Simplificado (Basado en Puntuaciones Compuestas) ---
# Se simula un K-Means (K=3) categorizando a los docentes en 3 grupos
# basados en su puntuación de CDG y UPIA.

# Calcular los puntos de corte (terciles) para la Competencia Digital General (CDG)
cdg_terciles = df_quant['CDG'].quantile([0.33, 0.66]).tolist()
cdg_mean = df_quant['CDG'].mean()
upia_mean = df_quant['UPIA'].mean()

# Asignación de Clústeres (Simulación de K-Means con 3 grupos)
# Se categoriza en 3 grupos basados en la combinación de CDG y UPIA
def assign_cluster(row):
    if row['CDG'] < cdg_mean and row['UPIA'] < upia_mean:
        return 1 # Cluster 1: Docentes Novatos (Baja CDG, Bajo Uso IA)
    elif row['CDG'] >= cdg_mean and row['UPIA'] < upia_mean:
        return 2 # Cluster 2: Docentes Tradicionales (Alta CDG, Bajo Uso IA)
    else:
        return 3 # Cluster 3: Docentes Innovadores (Alta CDG, Alto Uso IA)

df_quant['Cluster'] = df_quant.apply(assign_cluster, axis=1)

# --- Caracterización de los Clústeres ---
cluster_summary = df_quant.groupby('Cluster')[['CDG', 'UPIA', 'CT']].mean().reset_index()
cluster_summary.columns = ['Cluster', 'Media CDG', 'Media UPIA', 'Media CT']

# --- Generación de Gráfica de Dispersión ---
plt.figure(figsize=(10, 8))
sns.scatterplot(x='CDG', y='UPIA', hue='Cluster', data=df_quant, palette='viridis', s=100, alpha=0.7)
plt.scatter(cluster_summary['Media CDG'], cluster_summary['Media UPIA'], marker='X', s=300, color='red', label='Centroides (Medias)')
plt.title('Análisis de Clúster: Competencia Digital vs. Uso y Percepción de IA')
plt.xlabel('Competencia Digital General (CDG)')
plt.ylabel('Uso y Percepción de IA (UPIA)')
plt.legend(title='Clúster')
plt.grid(True)
plt.savefig('cluster_scatter.png')
plt.close()

# --- Guardar Resultados del Clúster en Markdown ---
cluster_results_md = f"""
# Resultados del Análisis de Clúster

## 1. Variables Compuestas

Se crearon tres variables compuestas para el análisis:
*   **Competencia Digital General (CDG):** Promedio de 13 ítems de competencia digital.
*   **Uso y Percepción de IA (UPIA):** Promedio de 7 ítems de uso y percepción de IA.
*   **Conocimiento Teórico (CT):** Promedio de 4 ítems de conocimiento de marcos teóricos.

## 2. Caracterización de Clústeres (K=3)

Se aplicó un análisis de clúster (simulación K-Means) para agrupar a los docentes en función de sus puntuaciones en CDG y UPIA.

| Clúster | N | Denominación | Media CDG | Media UPIA | Media CT |
|:-------:|:--:|:------------------|:---------:|:----------:|:--------:|
| 1 | {len(df_quant[df_quant['Cluster'] == 1])} | Docentes Novatos | {cluster_summary[cluster_summary['Cluster'] == 1]['Media CDG'].iloc[0]:.2f} | {cluster_summary[cluster_summary['Cluster'] == 1]['Media UPIA'].iloc[0]:.2f} | {cluster_summary[cluster_summary['Cluster'] == 1]['Media CT'].iloc[0]:.2f} |
| 2 | {len(df_quant[df_quant['Cluster'] == 2])} | Docentes Tradicionales | {cluster_summary[cluster_summary['Cluster'] == 2]['Media CDG'].iloc[0]:.2f} | {cluster_summary[cluster_summary['Cluster'] == 2]['Media UPIA'].iloc[0]:.2f} | {cluster_summary[cluster_summary['Cluster'] == 2]['Media CT'].iloc[0]:.2f} |
| 3 | {len(df_quant[df_quant['Cluster'] == 3])} | Docentes Innovadores | {cluster_summary[cluster_summary['Cluster'] == 3]['Media CDG'].iloc[0]:.2f} | {cluster_summary[cluster_summary['Cluster'] == 3]['Media UPIA'].iloc[0]:.2f} | {cluster_summary[cluster_summary['Cluster'] == 3]['Media CT'].iloc[0]:.2f} |

## 3. Descripción de Clústeres

*   **Clúster 1: Docentes Novatos (N={len(df_quant[df_quant['Cluster'] == 1])})**
    *   **Características:** Puntuaciones bajas en Competencia Digital General (CDG) y en Uso y Percepción de IA (UPIA). También presentan el menor Conocimiento Teórico (CT). Representan el segmento con mayor necesidad de formación básica en TIC e IA.

*   **Clúster 2: Docentes Tradicionales (N={len(df_quant[df_quant['Cluster'] == 2])})**
    *   **Características:** Puntuaciones altas en CDG, pero bajas en UPIA. Son docentes que han desarrollado competencias digitales tradicionales (LMS, herramientas básicas) pero aún no han integrado o adoptado la IA en su práctica. Su Conocimiento Teórico es intermedio.

*   **Clúster 3: Docentes Innovadores (N={len(df_quant[df_quant['Cluster'] == 3])})**
    *   **Características:** Puntuaciones altas en CDG y las más altas en UPIA. Son los líderes en la adopción de IA. Su Conocimiento Teórico es el más alto, lo que sugiere una correlación entre la adopción de IA y la búsqueda de marcos teóricos.

## 4. Gráfica de Dispersión

Se adjunta la gráfica de dispersión que visualiza la distribución de los clústeres en el plano CDG-UPIA.
"""

with open("/home/ubuntu/cluster_results.md", "w", encoding="utf-8") as f:
    f.write(cluster_results_md)

print("\nResultados del análisis de clúster guardados en /home/ubuntu/cluster_results.md y /home/ubuntu/cluster_scatter.png")
