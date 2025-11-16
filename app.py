import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import warnings
warnings.filterwarnings('ignore')

# Configuración de la página
st.set_page_config(
    page_title="Análisis de Clúster K-Means",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos personalizados
st.markdown("""
    <style>
        .main {
            padding: 2rem;
        }
        .metric-card {
            background-color: #f0f2f6;
            padding: 1rem;
            border-radius: 0.5rem;
            margin: 0.5rem 0;
        }
    </style>
    """, unsafe_allow_html=True)

# ============================================================================
# FASE 1: BUSINESS UNDERSTANDING (Comprensión del Negocio)
# ============================================================================
st.sidebar.header("📋 CRISP-DM Metodología")
st.sidebar.markdown("""
**Fases del Proyecto:**
1. **Business Understanding** ✓
2. **Data Understanding** 
3. **Data Preparation**
4. **Modeling**
5. **Evaluation**
6. **Deployment**
""")

# ============================================================================
# FASE 2: DATA UNDERSTANDING (Comprensión de Datos)
# ============================================================================

@st.cache_data
def load_data():
    """Cargar y preparar los datos para el análisis."""
    df = pd.read_csv('survey_data.csv')
    
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
    
    return df_quant

# Cargar datos
df_quant = load_data()

# ============================================================================
# FASE 3: DATA PREPARATION (Preparación de Datos)
# ============================================================================

# Crear variables compuestas
df_quant['CDG'] = df_quant.iloc[:, :13].mean(axis=1)  # Competencia Digital General
df_quant['UPIA'] = df_quant.iloc[:, 13:20].mean(axis=1)  # Uso y Percepción de IA
df_quant['CT'] = df_quant.iloc[:, 20:24].mean(axis=1)  # Conocimiento Teórico

# Seleccionar características para el clúster
features_for_clustering = ['CDG', 'UPIA', 'CT']
X = df_quant[features_for_clustering].values

# Estandarizar los datos
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ============================================================================
# INTERFAZ PRINCIPAL
# ============================================================================

st.title("📊 Análisis de Clúster K-Means")
st.markdown("**Competencias Digitales en Docentes de Educación Superior del Ecuador**")
st.markdown("---")

# Tabs para organizar el contenido
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["📈 Elbow Plot", "🔥 Heatmap Z-Score", "🎯 Scatterplot 2D", "📊 Barras Medias", "📋 Tabla Resumen"]
)

# ============================================================================
# FASE 4: MODELING (Modelado - K-Means)
# ============================================================================

# Determinar el número óptimo de clústeres
@st.cache_data
def compute_kmeans_metrics():
    """Calcular métricas para diferentes números de clústeres."""
    inertias = []
    silhouette_scores = []
    K_range = range(2, 11)
    
    for k in K_range:
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        kmeans.fit(X_scaled)
        inertias.append(kmeans.inertia_)
        silhouette_scores.append(silhouette_score(X_scaled, kmeans.labels_))
    
    return list(K_range), inertias, silhouette_scores

K_range, inertias, silhouette_scores = compute_kmeans_metrics()

# Aplicar K-Means con K=3 (óptimo según la literatura)
optimal_k = 3
kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
df_quant['Cluster'] = kmeans.fit_predict(X_scaled)

# Obtener centroides en escala original
centroids_scaled = kmeans.cluster_centers_
centroids_original = scaler.inverse_transform(centroids_scaled)

# ============================================================================
# TAB 1: ELBOW PLOT
# ============================================================================

with tab1:
    st.subheader("Método del Codo para Determinar el Número Óptimo de Clústeres")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Elbow Plot
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
            title="Elbow Plot: Inercia vs Número de Clústeres",
            xaxis_title="Número de Clústeres (K)",
            yaxis_title="Inercia",
            hovermode='x unified',
            template='plotly_white'
        )
        st.plotly_chart(fig_elbow, use_container_width=True)
    
    with col2:
        # Silhouette Score
        fig_silhouette = go.Figure()
        fig_silhouette.add_trace(go.Scatter(
            x=list(K_range),
            y=silhouette_scores,
            mode='lines+markers',
            name='Silhouette Score',
            line=dict(color='#ff7f0e', width=3),
            marker=dict(size=10)
        ))
        fig_silhouette.add_vline(x=optimal_k, line_dash="dash", line_color="red",
                                annotation_text=f"K={optimal_k} (Óptimo)")
        fig_silhouette.update_layout(
            title="Silhouette Score vs Número de Clústeres",
            xaxis_title="Número de Clústeres (K)",
            yaxis_title="Silhouette Score",
            hovermode='x unified',
            template='plotly_white'
        )
        st.plotly_chart(fig_silhouette, use_container_width=True)
    
    st.info(f"✓ **Número óptimo de clústeres seleccionado: K = {optimal_k}**")

# ============================================================================
# TAB 2: HEATMAP Z-SCORE
# ============================================================================

with tab2:
    st.subheader("Matriz de Puntuaciones Z-Score por Clúster")
    
    # Calcular Z-scores por clúster
    cluster_profiles = []
    for k in range(optimal_k):
        cluster_data = df_quant[df_quant['Cluster'] == k][features_for_clustering]
        z_scores = (cluster_data.mean() - df_quant[features_for_clustering].mean()) / df_quant[features_for_clustering].std()
        cluster_profiles.append(z_scores.values)
    
    cluster_profiles = np.array(cluster_profiles)
    
    # Crear heatmap
    fig_heatmap = go.Figure(data=go.Heatmap(
        z=cluster_profiles,
        x=features_for_clustering,
        y=[f'Clúster {i}' for i in range(optimal_k)],
        colorscale='RdBu',
        zmid=0,
        text=np.round(cluster_profiles, 2),
        texttemplate='%{text:.2f}',
        textfont={"size": 12},
        colorbar=dict(title="Z-Score")
    ))
    fig_heatmap.update_layout(
        title="Heatmap: Puntuaciones Z-Score por Clúster",
        xaxis_title="Variables",
        yaxis_title="Clústeres",
        height=400
    )
    st.plotly_chart(fig_heatmap, use_container_width=True)
    
    st.markdown("""
    **Interpretación:**
    - **Valores positivos (rojo):** La variable está por encima del promedio general para ese clúster.
    - **Valores negativos (azul):** La variable está por debajo del promedio general para ese clúster.
    - **Valores cercanos a 0 (blanco):** La variable está cerca del promedio general.
    """)

# ============================================================================
# TAB 3: SCATTERPLOT 2D CON CENTROIDES
# ============================================================================

with tab3:
    st.subheader("Visualización 2D: CDG vs UPIA con Centroides")
    
    # Crear scatterplot
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
    st.plotly_chart(fig_scatter, use_container_width=True)

# ============================================================================
# TAB 4: GRÁFICA DE BARRAS - MEDIAS POR CLÚSTER
# ============================================================================

with tab4:
    st.subheader("Comparación de Medias de Variables por Clúster")
    
    # Calcular medias por clúster
    cluster_means = df_quant.groupby('Cluster')[features_for_clustering].mean().reset_index()
    
    # Crear gráfica de barras agrupadas
    fig_bars = go.Figure()
    
    for feature in features_for_clustering:
        fig_bars.add_trace(go.Bar(
            x=[f'Clúster {i}' for i in range(optimal_k)],
            y=cluster_means[feature],
            name=feature,
            text=np.round(cluster_means[feature], 2),
            textposition='auto'
        ))
    
    fig_bars.update_layout(
        title='Medias de Variables por Clúster',
        xaxis_title='Clúster',
        yaxis_title='Promedio',
        barmode='group',
        hovermode='x unified',
        height=500,
        template='plotly_white'
    )
    st.plotly_chart(fig_bars, use_container_width=True)

# ============================================================================
# TAB 5: TABLA RESUMEN INTERPRETATIVA
# ============================================================================

with tab5:
    st.subheader("Tabla Resumen: Caracterización de Clústeres")
    
    # Crear tabla resumen
    summary_data = []
    cluster_names = ['Novatos', 'Tradicionales', 'Innovadores']
    
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
    st.dataframe(summary_df, use_container_width=True)
    
    st.markdown("---")
    st.subheader("Interpretación de Clústeres")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 🔴 Clúster 0: Novatos
        - **Características:** Puntuaciones bajas en CDG y UPIA
        - **Perfil:** Docentes con competencias digitales limitadas y bajo uso de IA
        - **Necesidad:** Formación básica en TIC e introducción a IA
        """)
    
    with col2:
        st.markdown("""
        ### 🟡 Clúster 1: Tradicionales
        - **Características:** CDG alta, UPIA baja
        - **Perfil:** Competentes en tecnologías establecidas pero reacios a IA
        - **Necesidad:** Formación especializada en IA y cambio de mentalidad
        """)
    
    with col3:
        st.markdown("""
        ### 🟢 Clúster 2: Innovadores
        - **Características:** CDG y UPIA altas, CT más alto
        - **Perfil:** Líderes en adopción de IA con conocimiento teórico
        - **Necesidad:** Rol de agentes de cambio y mentores
        """)

# ============================================================================
# FASE 5: EVALUATION (Evaluación)
# ============================================================================

st.markdown("---")
st.subheader("📊 Métricas de Evaluación del Modelo")

col1, col2, col3, col4 = st.columns(4)

with col1:
    silhouette_avg = silhouette_score(X_scaled, df_quant['Cluster'])
    st.metric("Silhouette Score", f"{silhouette_avg:.3f}", 
              "Rango: -1 a 1 (Mayor es mejor)")

with col2:
    inertia_final = kmeans.inertia_
    st.metric("Inercia Final", f"{inertia_final:.2f}", 
              "Suma de distancias al centroide")

with col3:
    st.metric("Número de Clústeres", optimal_k, 
              "Determinado por Elbow Method")

with col4:
    st.metric("Muestras Totales", len(df_quant), 
              "Docentes encuestados")

# ============================================================================
# FASE 6: DEPLOYMENT (Despliegue)
# ============================================================================

st.markdown("---")
st.subheader("💾 Exportar Resultados")

# Botón para descargar tabla resumen
csv = summary_df.to_csv(index=False)
st.download_button(
    label="📥 Descargar Tabla Resumen (CSV)",
    data=csv,
    file_name="cluster_summary.csv",
    mime="text/csv"
)

# Guardar datos con asignación de clústeres
df_with_clusters = df_quant.copy()
st.download_button(
    label="📥 Descargar Datos Completos con Clústeres (CSV)",
    data=df_with_clusters.to_csv(index=False),
    file_name="data_with_clusters.csv",
    mime="text/csv"
)

st.success("✓ Análisis completado exitosamente. Todos los datos están listos para exportar.")
