"""
Script de Análisis de Clúster K-Means con Metodología CRISP-DM
Competencias Digitales en Docentes de Educación Superior del Ecuador
"""

import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import warnings
warnings.filterwarnings('ignore')

print("=" * 80)
print("ANÁLISIS DE CLÚSTER K-MEANS CON METODOLOGÍA CRISP-DM")
print("Competencias Digitales en Docentes de Educación Superior del Ecuador")
print("=" * 80)

# ============================================================================
# FASE 1: BUSINESS UNDERSTANDING (Comprensión del Negocio)
# ============================================================================
print("\n[FASE 1] BUSINESS UNDERSTANDING - Comprensión del Negocio")
print("-" * 80)
print("Objetivo: Identificar perfiles docentes basados en competencias digitales e IA")
print("Stakeholders: Docentes, Instituciones de Educación Superior, Formuladores de Política")
print("Problema: Necesidad de diagnóstico de competencias digitales y adopción de IA")

# ============================================================================
# FASE 2: DATA UNDERSTANDING (Comprensión de Datos)
# ============================================================================
print("\n[FASE 2] DATA UNDERSTANDING - Comprensión de Datos")
print("-" * 80)

# Cargar datos
df = pd.read_csv('/home/ubuntu/survey_data.csv')
print(f"✓ Datos cargados: {df.shape[0]} encuestas, {df.shape[1]} variables")

# Mapeo de columnas cuantitativas
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

df_quant = df.iloc[:, 1:25].rename(columns=quantitative_cols_map)

# Convertir a numéricas
for col in df_quant.columns:
    df_quant[col] = pd.to_numeric(df_quant[col], errors='coerce')

df_quant.dropna(inplace=True)
print(f"✓ Datos limpios: {df_quant.shape[0]} casos válidos")
print(f"✓ Variables: {df_quant.shape[1]} (escala Likert 1-5)")

# ============================================================================
# FASE 3: DATA PREPARATION (Preparación de Datos)
# ============================================================================
print("\n[FASE 3] DATA PREPARATION - Preparación de Datos")
print("-" * 80)

# Crear variables compuestas
df_quant['CDG'] = df_quant.iloc[:, :13].mean(axis=1)  # Competencia Digital General
df_quant['UPIA'] = df_quant.iloc[:, 13:20].mean(axis=1)  # Uso y Percepción de IA
df_quant['CT'] = df_quant.iloc[:, 20:24].mean(axis=1)  # Conocimiento Teórico

print("✓ Variables compuestas creadas:")
print(f"  - CDG (Competencia Digital General): Media = {df_quant['CDG'].mean():.2f}, SD = {df_quant['CDG'].std():.2f}")
print(f"  - UPIA (Uso y Percepción de IA): Media = {df_quant['UPIA'].mean():.2f}, SD = {df_quant['UPIA'].std():.2f}")
print(f"  - CT (Conocimiento Teórico): Media = {df_quant['CT'].mean():.2f}, SD = {df_quant['CT'].std():.2f}")

# Seleccionar características para el clúster
features_for_clustering = ['CDG', 'UPIA', 'CT']
X = df_quant[features_for_clustering].values

# Estandarizar los datos
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print("✓ Datos estandarizados (Z-score)")

# ============================================================================
# FASE 4: MODELING (Modelado - K-Means)
# ============================================================================
print("\n[FASE 4] MODELING - Modelado K-Means")
print("-" * 80)

# Determinar el número óptimo de clústeres
print("Calculando métricas para K = 2 a 10...")
inertias = []
silhouette_scores = []
K_range = range(2, 11)

for k in K_range:
    kmeans_temp = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans_temp.fit(X_scaled)
    inertias.append(kmeans_temp.inertia_)
    silhouette_scores.append(silhouette_score(X_scaled, kmeans_temp.labels_))
    print(f"  K={k}: Inercia={kmeans_temp.inertia_:.2f}, Silhouette={silhouette_scores[-1]:.3f}")

# Aplicar K-Means con K=3 (óptimo según la literatura)
optimal_k = 3
kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
df_quant['Cluster'] = kmeans.fit_predict(X_scaled)

print(f"\n✓ Número óptimo de clústeres: K = {optimal_k}")
print(f"✓ Inercia final: {kmeans.inertia_:.2f}")
print(f"✓ Silhouette Score: {silhouette_score(X_scaled, df_quant['Cluster']):.3f}")

# Obtener centroides en escala original
centroids_scaled = kmeans.cluster_centers_
centroids_original = scaler.inverse_transform(centroids_scaled)

# ============================================================================
# FASE 5: EVALUATION (Evaluación)
# ============================================================================
print("\n[FASE 5] EVALUATION - Evaluación del Modelo")
print("-" * 80)

# Caracterización de clústeres
cluster_names = ['Novatos', 'Tradicionales', 'Innovadores']

for k in range(optimal_k):
    cluster_data = df_quant[df_quant['Cluster'] == k]
    print(f"\nClúster {k} ({cluster_names[k]}):")
    print(f"  N = {len(cluster_data)} ({len(cluster_data)/len(df_quant)*100:.1f}%)")
    print(f"  CDG: Media = {cluster_data['CDG'].mean():.2f}, SD = {cluster_data['CDG'].std():.2f}")
    print(f"  UPIA: Media = {cluster_data['UPIA'].mean():.2f}, SD = {cluster_data['UPIA'].std():.2f}")
    print(f"  CT: Media = {cluster_data['CT'].mean():.2f}, SD = {cluster_data['CT'].std():.2f}")

# ============================================================================
# GENERACIÓN DE VISUALIZACIONES
# ============================================================================
print("\n[FASE 6] DEPLOYMENT - Generación de Visualizaciones")
print("-" * 80)

# 1. ELBOW PLOT
print("Generando Elbow Plot...")
fig_elbow = go.Figure()
fig_elbow.add_trace(go.Scatter(
    x=list(K_range),
    y=inertias,
    mode='lines+markers',
    name='Inercia',
    line=dict(color='#1f77b4', width=3),
    marker=dict(size=10)
))
fig_elbow.add_vline(x=optimal_k, line_dash="dash", line_color="red", 
                   annotation_text=f"K={optimal_k} (Óptimo)")
fig_elbow.update_layout(
    title="Método del Codo: Inercia vs Número de Clústeres",
    xaxis_title="Número de Clústeres (K)",
    yaxis_title="Inercia",
    hovermode='x unified',
    template='plotly_white',
    height=500
)
fig_elbow.write_html('/home/ubuntu/01_elbow_plot.html')
print("✓ Guardado: 01_elbow_plot.html")

# 2. HEATMAP Z-SCORE
print("Generando Heatmap Z-Score...")
cluster_profiles = []
for k in range(optimal_k):
    cluster_data = df_quant[df_quant['Cluster'] == k][features_for_clustering]
    z_scores = (cluster_data.mean() - df_quant[features_for_clustering].mean()) / df_quant[features_for_clustering].std()
    cluster_profiles.append(z_scores.values)

cluster_profiles = np.array(cluster_profiles)

fig_heatmap = go.Figure(data=go.Heatmap(
    z=cluster_profiles,
    x=features_for_clustering,
    y=[f'Clúster {i}: {cluster_names[i]}' for i in range(optimal_k)],
    colorscale='RdBu',
    zmid=0,
    text=np.round(cluster_profiles, 2),
    texttemplate='%{text:.2f}',
    textfont={"size": 12},
    colorbar=dict(title="Z-Score")
))
fig_heatmap.update_layout(
    title="Matriz de Puntuaciones Z-Score por Clúster",
    xaxis_title="Variables",
    yaxis_title="Clústeres",
    height=400
)
fig_heatmap.write_html('/home/ubuntu/02_heatmap_zscore.html')
print("✓ Guardado: 02_heatmap_zscore.html")

# 3. SCATTERPLOT 2D CON CENTROIDES
print("Generando Scatterplot 2D...")
fig_scatter = px.scatter(
    df_quant,
    x='CDG',
    y='UPIA',
    color='Cluster',
    size='CT',
    hover_data=['CDG', 'UPIA', 'CT', 'Cluster'],
    title='Análisis de Clúster: Competencia Digital vs Uso de IA',
    labels={'CDG': 'Competencia Digital General (CDG)', 'UPIA': 'Uso y Percepción de IA (UPIA)', 'Cluster': 'Clúster'},
    color_discrete_sequence=px.colors.qualitative.Set1
)

# Agregar centroides
fig_scatter.add_trace(go.Scatter(
    x=centroids_original[:, 0],
    y=centroids_original[:, 1],
    mode='markers+text',
    marker=dict(size=20, symbol='star', color='black', line=dict(width=2, color='white')),
    text=[f'C{i}' for i in range(optimal_k)],
    textposition='top center',
    name='Centroides',
    hovertemplate='<b>Centroide %{text}</b><br>CDG: %{x:.2f}<br>UPIA: %{y:.2f}<extra></extra>'
))

fig_scatter.update_layout(
    height=600,
    hovermode='closest',
    template='plotly_white'
)
fig_scatter.write_html('/home/ubuntu/03_scatterplot_2d.html')
print("✓ Guardado: 03_scatterplot_2d.html")

# 4. GRÁFICA DE BARRAS - MEDIAS POR CLÚSTER
print("Generando Gráfica de Barras...")
cluster_means = df_quant.groupby('Cluster')[features_for_clustering].mean().reset_index()

fig_bars = go.Figure()

for feature in features_for_clustering:
    fig_bars.add_trace(go.Bar(
        x=[f'Clúster {i}: {cluster_names[i]}' for i in range(optimal_k)],
        y=cluster_means[feature],
        name=feature,
        text=np.round(cluster_means[feature], 2),
        textposition='auto'
    ))

fig_bars.update_layout(
    title='Comparación de Medias de Variables por Clúster',
    xaxis_title='Clúster',
    yaxis_title='Promedio',
    barmode='group',
    hovermode='x unified',
    height=500,
    template='plotly_white'
)
fig_bars.write_html('/home/ubuntu/04_bar_chart_means.html')
print("✓ Guardado: 04_bar_chart_means.html")

# 5. TABLA RESUMEN
print("Generando Tabla Resumen...")
summary_data = []

for k in range(optimal_k):
    cluster_data = df_quant[df_quant['Cluster'] == k]
    summary_data.append({
        'Clúster': k,
        'Denominación': cluster_names[k],
        'N': len(cluster_data),
        '% Muestra': f"{(len(cluster_data)/len(df_quant)*100):.1f}%",
        'Media CDG': f"{cluster_data['CDG'].mean():.2f}",
        'Media UPIA': f"{cluster_data['UPIA'].mean():.2f}",
        'Media CT': f"{cluster_data['CT'].mean():.2f}",
        'Desv. Est. CDG': f"{cluster_data['CDG'].std():.2f}",
        'Desv. Est. UPIA': f"{cluster_data['UPIA'].std():.2f}",
        'Desv. Est. CT': f"{cluster_data['CT'].std():.2f}"
    })

summary_df = pd.DataFrame(summary_data)
summary_df.to_csv('/home/ubuntu/05_cluster_summary.csv', index=False)
print("✓ Guardado: 05_cluster_summary.csv")

# Guardar datos con asignación de clústeres
df_quant.to_csv('/home/ubuntu/06_data_with_clusters.csv', index=False)
print("✓ Guardado: 06_data_with_clusters.csv")

# ============================================================================
# RESUMEN FINAL
# ============================================================================
print("\n" + "=" * 80)
print("RESUMEN DE RESULTADOS")
print("=" * 80)
print("\nArchivos generados:")
print("  1. 01_elbow_plot.html - Método del Codo")
print("  2. 02_heatmap_zscore.html - Matriz Z-Score por Clúster")
print("  3. 03_scatterplot_2d.html - Visualización 2D con Centroides")
print("  4. 04_bar_chart_means.html - Gráfica de Barras de Medias")
print("  5. 05_cluster_summary.csv - Tabla Resumen Interpretativa")
print("  6. 06_data_with_clusters.csv - Datos Completos con Asignación de Clústeres")

print("\nCaracterización de Clústeres:")
for k in range(optimal_k):
    cluster_data = df_quant[df_quant['Cluster'] == k]
    print(f"\n  Clúster {k} - {cluster_names[k]}:")
    print(f"    N = {len(cluster_data)} ({len(cluster_data)/len(df_quant)*100:.1f}%)")
    print(f"    CDG = {cluster_data['CDG'].mean():.2f} ± {cluster_data['CDG'].std():.2f}")
    print(f"    UPIA = {cluster_data['UPIA'].mean():.2f} ± {cluster_data['UPIA'].std():.2f}")
    print(f"    CT = {cluster_data['CT'].mean():.2f} ± {cluster_data['CT'].std():.2f}")

print("\n" + "=" * 80)
print("✓ Análisis completado exitosamente")
print("=" * 80)
