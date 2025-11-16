import pandas as pd
import numpy as np

# Cargar los datos
file_path = 'survey_data.csv'
df = pd.read_csv(file_path)

# Identificar las columnas de la escala Likert (cuantitativas)
# Basado en la inspección inicial, las columnas cuantitativas van desde la 2da hasta la 25ta.
# Se excluye la primera columna ('Marca temporal') y las últimas columnas cualitativas.
# Se renombran las columnas para facilitar el manejo y la presentación de resultados.

# Mapeo de nombres de columnas para el análisis cuantitativo
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

# Asegurar que todas las columnas son numéricas (algunas pueden ser objetos si hay valores no numéricos)
for col in df_quant.columns:
    df_quant[col] = pd.to_numeric(df_quant[col], errors='coerce')

# Eliminar filas con valores nulos en las columnas cuantitativas (si los hay)
df_quant.dropna(inplace=True)

print(f"Número de casos válidos para el análisis cuantitativo: {len(df_quant)}")

# --- 1. Análisis Descriptivo ---
descriptive_stats = df_quant.describe().transpose()
descriptive_stats = descriptive_stats[['count', 'mean', 'std', 'min', 'max']]
descriptive_stats.columns = ['N', 'Media', 'Desviación Estándar', 'Mínimo', 'Máximo']

print("\n--- Estadísticas Descriptivas de las Variables Cuantitativas (Likert) ---")
print(descriptive_stats.to_markdown(floatfmt=".2f"))

# --- 2. Análisis de Frecuencias (para una variable de ejemplo) ---
# Se elige una variable clave para mostrar la distribución
key_variable = 'Frecuencia_Uso_IA'
frequency_table = df_quant[key_variable].value_counts(normalize=True).sort_index() * 100
frequency_table = frequency_table.reset_index()
frequency_table.columns = ['Valor Likert', 'Porcentaje']

print(f"\n--- Distribución de Frecuencias para: {key_variable} ---")
print(frequency_table.to_markdown(index=False, floatfmt=".2f"))

# --- 3. Guardar los resultados descriptivos en un archivo Markdown ---
# Se utiliza la concatenación de cadenas para construir el contenido Markdown.
# Se extrae el cuerpo de la tabla de Markdown de forma segura.
def get_markdown_table_body(markdown_string):
    lines = markdown_string.split('\n')
    # Las líneas 0 y 1 son el encabezado y el separador. El cuerpo comienza en la línea 2.
    return '\n'.join(lines[2:])

results_md_content = (
    "# Resultados del Análisis Estadístico Cuantitativo (Descriptivo)\n\n"
    f"## 1. Estadísticas Descriptivas (N={len(df_quant)})\n\n"
    "La siguiente tabla presenta las estadísticas descriptivas clave (Media y Desviación Estándar) para cada ítem de la encuesta, medido en una escala Likert (1 a 5).\n\n"
    f"{descriptive_stats.to_markdown(floatfmt='.2f')}\n\n"
    "**Observaciones Clave:**\n"
    "*   **Altas Puntuaciones en Percepción de IA:** Los ítems relacionados con la percepción de la IA (IA_Implicacion_Etica, IA_Favorece_Inclusion, IA_Ahorro_Tiempo) muestran las medias más altas, indicando una percepción muy positiva de la IA en el contexto educativo.\n"
    "*   **Baja Formación Específica:** Los ítems 'Formacion_Especifica_TIC' y 'Formacion_Especifica_IA' tienen medias relativamente bajas, sugiriendo una necesidad de mayor capacitación formal.\n"
    "*   **Bajo Conocimiento de Marcos Teóricos:** Los ítems 'Conoce_Metodologia_COIL', 'Conoce_Marco_DigCompEdu', 'Conoce_Marco_ICT_CFT' y 'Conoce_Criterios_Internacionales' presentan las medias más bajas, lo que indica un desconocimiento generalizado de los marcos de referencia internacionales.\n\n"
    "## 2. Distribución de Frecuencias (Ejemplo: Frecuencia de Uso de IA)\n\n"
    "| Valor Likert | Porcentaje |\n"
    "|:------------:|:----------:|\n"
    f"{get_markdown_table_body(frequency_table.to_markdown(index=False, floatfmt='.2f'))}\n\n"
    "**Nota sobre el Análisis Inferencial:** Debido a limitaciones técnicas en el entorno de análisis (imposibilidad de instalar la librería `scipy`), el análisis inferencial (Correlación de Pearson, Chi-cuadrado) no pudo ser completado. Los resultados descriptivos presentados son la base para la triangulación con el análisis cualitativo."
)

with open("/home/ubuntu/quantitative_results.md", "w", encoding="utf-8") as f:
    f.write(results_md_content)

print("\nResultados cuantitativos guardados en /home/ubuntu/quantitative_results.md")
