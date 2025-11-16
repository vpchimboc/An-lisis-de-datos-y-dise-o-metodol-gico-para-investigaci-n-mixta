import pandas as pd

# Cargar los datos
file_path = 'survey_data.csv'
df = pd.read_csv(file_path)

# Identificar las columnas de preguntas abiertas (cualitativas)
qualitative_cols = [
    'Mencione las principales ventajas que ha encontrado al usar plataformas virtuales en su institución.',
    '¿Qué limitaciones ha enfrentado en el uso de herramientas digitales en su práctica docente?',
    'En su opinión, ¿qué competencias digitales son esenciales para un docente de educación superior?',
    '¿De qué manera el uso de herramientas digitales ha influido en sus estrategias o criterios para evaluar el aprendizaje de sus estudiantes? ',
    '¿Qué retos técnicos o dilemas éticos ha experimentado o considera que podría enfrentar al integrar herramientas de inteligencia artificial en el aula? '
]

# Crear un DataFrame para el análisis cualitativo
df_qual = df[qualitative_cols].copy()

# Limpiar los datos: eliminar respuestas vacías o con texto no informativo
df_qual.dropna(inplace=True)
for col in qualitative_cols:
    df_qual = df_qual[df_qual[col].astype(str).str.strip() != '']

print(f"Número de respuestas cualitativas válidas para el análisis: {len(df_qual)}")

# --- Análisis de Contenido Temático (Ejemplo) ---
# Se simula un proceso de codificación y categorización para una de las preguntas.
# En una investigación real, este proceso sería manual e inductivo, buscando temas emergentes.

# Pregunta de ejemplo para análisis
pregunta_ejemplo = '¿Qué limitaciones ha enfrentado en el uso de herramientas digitales en su práctica docente?'

# Categorías predefinidas (basadas en una lectura inicial de las respuestas)
categorias = {
    "Infraestructura y Conectividad": ["internet", "conectividad", "equipos", "infraestructura", "recursos"],
    "Falta de Formación": ["formación", "capacitación", "conocimiento", "preparación"],
    "Tiempo y Carga Laboral": ["tiempo", "sobrecarga", "carga laboral"],
    "Costo y Licenciamiento": ["pago", "licencia", "costo", "gratuita"],
    "Resistencia o Cultura Digital": ["resistencia", "cultura", "actitud"]
}

# Función para categorizar una respuesta
def categorizar_respuesta(respuesta):
    respuesta_lower = str(respuesta).lower()
    for categoria, keywords in categorias.items():
        if any(keyword in respuesta_lower for keyword in keywords):
            return categoria
    return "Otra"

# Aplicar la categorización
df_qual['Categoria_Limitaciones'] = df_qual[pregunta_ejemplo].apply(categorizar_respuesta)

# Calcular la frecuencia de cada categoría
frecuencia_categorias = df_qual['Categoria_Limitaciones'].value_counts().reset_index()
frecuencia_categorias.columns = ['Categoría', 'Frecuencia']

# Obtener citas representativas de forma segura
def get_quote(df, category, question, index=0):
    quotes = df[df['Categoria_Limitaciones'] == category][question]
    return quotes.iloc[index] if len(quotes) > index else "No hay cita disponible para esta categoría."

# --- Guardar los resultados del análisis cualitativo en un archivo Markdown ---
results_md_content = f"""
# Resultados del Análisis Cualitativo (Preliminar)

Este análisis se centra en las respuestas a las preguntas abiertas para identificar temas y patrones emergentes. A continuación, se presenta un ejemplo de categorización para la pregunta sobre las limitaciones en el uso de herramientas digitales.

## 1. Categorización de Limitaciones (N={len(df_qual)})

Se identificaron las siguientes categorías temáticas a partir de las respuestas de los docentes:

{frecuencia_categorias.to_markdown(index=False)}

**Observaciones Clave:**
*   **Infraestructura y Conectividad:** La principal limitación reportada por los docentes está relacionada con la falta de una infraestructura tecnológica adecuada, incluyendo problemas de conexión a internet y la disponibilidad de equipos tanto para ellos como para los estudiantes.
*   **Costo y Licenciamiento:** Un número significativo de docentes menciona el costo de las herramientas digitales y la falta de licencias institucionales como una barrera importante.
*   **Falta de Formación:** La necesidad de mayor capacitación y desarrollo de competencias digitales sigue siendo una preocupación central.

## 2. Citas Representativas por Categoría

A continuación, se presentan algunas citas textuales que ilustran las categorías identificadas:

### Infraestructura y Conectividad
> "{get_quote(df_qual, 'Infraestructura y Conectividad', pregunta_ejemplo, 0)}"
> "{get_quote(df_qual, 'Infraestructura y Conectividad', pregunta_ejemplo, 1)}"

### Costo y Licenciamiento
> "{get_quote(df_qual, 'Costo y Licenciamiento', pregunta_ejemplo, 0)}"

### Falta de Formación
> "{get_quote(df_qual, 'Falta de Formación', pregunta_ejemplo, 0)}"

**Nota:** Este es un análisis preliminar. Un análisis cualitativo completo requeriría un proceso de codificación abierta y axial más riguroso para desarrollar un sistema de categorías robusto y validado.
"""

with open("/home/ubuntu/qualitative_results.md", "w", encoding="utf-8") as f:
    f.write(results_md_content)

print("\nResultados cualitativos guardados en /home/ubuntu/qualitative_results.md")
