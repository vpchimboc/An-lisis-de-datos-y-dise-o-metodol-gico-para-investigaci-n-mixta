import pandas as pd

# Definir la ruta del archivo
file_path = 'INSTRUMENTODERECOLECCIÓNDEDATOS(respuestas)(1).xlsx'

# Cargar el archivo Excel
try:
    df = pd.read_excel(file_path)
except Exception as e:
    print(f"Error al cargar el archivo: {e}")
    exit()

# Mostrar información general del DataFrame
print("--- Información del DataFrame ---")
df.info()

# Mostrar las primeras 5 filas para inspección
print("\n--- Primeras 5 filas ---")
#print(df.head().to_markdown(index=False))

# Guardar el DataFrame en un archivo CSV para un manejo más sencillo
csv_path = 'survey_data.csv'
df.to_csv(csv_path, index=False, encoding='utf-8')
print(f"\nDatos guardados en: {csv_path}")

# Identificar y mostrar las columnas de preguntas abiertas (cualitativas)
# Basado en la inspección inicial, las columnas cualitativas son las últimas.
# Se asume que las columnas con nombres largos y que no son de selección múltiple son las abiertas.
qualitative_cols = [
    'Mencione las principales ventajas que ha encontrado al usar plataformas virtuales en su institución.',
    '¿Qué limitaciones ha enfrentado en el uso de herramientas digitales en su práctica docente?',
    'En su opinión, ¿qué competencias digitales son esenciales para un docente de educación superior?',
    '¿De qué manera el uso de herramientas digitales ha influido en sus estrategias o criterios para evaluar el aprendizaje de sus estudiantes? ',
    '¿Qué retos técnicos o dilemas éticos ha experimentado o considera que podría enfrentar al integrar herramientas de inteligencia artificial en el aula? ',
    'INSTITUCIÓN DE EDUCACIÓN SUPERIOR' # Aunque es categórica, puede ser útil para el contexto cualitativo.
]

print("\n--- Columnas Cualitativas Identificadas ---")
for col in qualitative_cols:
    if col in df.columns:
        print(f"- {col}")
    else:
        print(f"- ¡Advertencia! Columna no encontrada: {col}")

# Contar el número de encuestados
print(f"\nNúmero total de encuestados (filas): {len(df)}")
