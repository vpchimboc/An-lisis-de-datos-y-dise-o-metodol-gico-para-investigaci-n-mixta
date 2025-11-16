# Competencias Digitales y Adopción de Inteligencia Artificial en Docentes de Educación Superior en Ecuador: Un Análisis de Clúster K-Means

**Autores:** Análisis de Datos Doctoral - Ecuador

**Fecha:** Noviembre 2025

---

## Resumen

La integración de la Inteligencia Artificial (IA) en la educación superior exige una reevaluación profunda de las competencias digitales docentes. Este estudio, de enfoque mixto, investiga el nivel de competencia digital y la adopción de IA en 70 docentes de educación superior en Ecuador. Mediante un **Análisis de Clúster K-Means** aplicando la metodología **CRISP-DM**, se identificaron tres perfiles docentes claramente diferenciados: **Novatos (21.4%)**, **Tradicionales (58.6%)** e **Innovadores (20.0%)**. Los resultados cuantitativos revelan que los docentes Innovadores presentan las puntuaciones más altas en Competencia Digital General (CDG = 4.18) y Uso y Percepción de IA (UPIA = 4.59), mientras que los Novatos muestran las puntuaciones más bajas (CDG = 2.72, UPIA = 2.66). El Conocimiento Teórico (CT) es significativamente más alto en el clúster Innovador (CT = 2.25) comparado con los otros dos grupos. Los hallazgos cualitativos complementan esta visión, señalando la infraestructura, la falta de formación y los dilemas éticos como las principales barreras. Se concluye que las políticas de desarrollo profesional deben implementar estrategias diferenciadas para cada clúster, priorizando la formación especializada en IA y la difusión de marcos de referencia internacionales como DigCompEdu.

**Palabras Clave:** Competencias Digitales, Inteligencia Artificial, Análisis de Clúster K-Means, Educación Superior, CRISP-DM, Docentes, Ecuador.

---

## 1. Introducción

La transformación digital ha redefinido fundamentalmente el rol del docente universitario, convirtiendo las competencias digitales en un requisito esencial para la calidad educativa [1]. La reciente irrupción de la Inteligencia Artificial generativa, como ChatGPT y Copilot, ha acelerado esta necesidad, planteando tanto oportunidades significativas para la personalización del aprendizaje como desafíos éticos y pedagógicos complejos [2]. En el contexto de la educación superior ecuatoriana, es crucial diagnosticar el estado actual de estas competencias y comprender cómo los docentes están integrando, o planean integrar, estas tecnologías emergentes en su práctica pedagógica.

El objetivo principal de este artículo es identificar y caracterizar los perfiles de los docentes de educación superior en Ecuador en función de su nivel de competencia digital y su grado de adopción de la IA, proporcionando una base empírica sólida para el diseño de políticas de formación docente diferenciadas y contextualizadas.

---

## 2. Metodología

### 2.1. Enfoque y Diseño de Investigación

La investigación empleó un **diseño de Triangulación Concurrente (Convergent Parallel Design)** de enfoque mixto (CUAN + CUAL) [3]. Los datos cuantitativos (escala Likert) y cualitativos (preguntas abiertas) fueron recolectados simultáneamente a través de un único instrumento, permitiendo la convergencia de hallazgos en la fase de interpretación.

### 2.2. Metodología CRISP-DM

Se implementó la metodología **CRISP-DM (Cross-Industry Standard Process for Data Mining)**, que consta de seis fases:

1. **Business Understanding:** Definición del problema como la necesidad de identificar perfiles docentes para políticas de formación.
2. **Data Understanding:** Exploración de 70 encuestas con 24 variables cuantitativas en escala Likert.
3. **Data Preparation:** Creación de variables compuestas (CDG, UPIA, CT) y estandarización Z-score.
4. **Modeling:** Aplicación del algoritmo K-Means para identificar clústeres óptimos.
5. **Evaluation:** Análisis de características de cada clúster y validación de resultados.
6. **Deployment:** Generación de visualizaciones interactivas y tablas resumen para toma de decisiones.

### 2.3. Participantes e Instrumento

La muestra estuvo compuesta por **70 docentes** de educación superior de institutos y universidades en Ecuador. El instrumento de recolección de datos incluyó:

*   **24 ítems cuantitativos** en escala Likert de 5 puntos, midiendo Competencia Digital General (CDG), Uso y Percepción de IA (UPIA) y Conocimiento Teórico (CT).
*   **5 preguntas abiertas** para explorar ventajas, limitaciones, competencias esenciales y dilemas éticos.

### 2.4. Análisis de Datos Cuantitativos: K-Means Clustering

#### 2.4.1. Construcción de Variables Compuestas

Se calcularon las medias de los ítems para obtener las siguientes variables de entrada al clúster:

**Competencia Digital General (CDG):**
$$CDG = \frac{1}{13} \sum_{i=1}^{13} I_i$$

Donde $I_i$ son los ítems relacionados con el uso de LMS, creación de recursos, evaluación digital y colaboración.

**Uso y Percepción de IA (UPIA):**
$$UPIA = \frac{1}{7} \sum_{j=14}^{20} I_j$$

Donde $I_j$ son los ítems relacionados con la frecuencia de uso de IA y la percepción de su impacto.

**Conocimiento Teórico (CT):**
$$CT = \frac{1}{4} \sum_{k=21}^{24} I_k$$

Donde $I_k$ son los ítems relacionados con el conocimiento de marcos teóricos (DigCompEdu, COIL, ICT-CFT).

#### 2.4.2. Estandarización de Datos

Los datos fueron estandarizados utilizando la transformación Z-score:
$$Z = \frac{X - \mu}{\sigma}$$

Donde $\mu$ es la media y $\sigma$ es la desviación estándar de cada variable.

#### 2.4.3. Determinación del Número Óptimo de Clústeres

Se aplicó el **Método del Codo (Elbow Method)** evaluando la inercia para K = 2 a 10:

| K | Inercia |
|:---:|:---:|
| 2 | 123.16 |
| 3 | 83.96 |
| 4 | 66.41 |
| 5 | 56.62 |
| 6 | 52.34 |
| 7 | 38.28 |
| 8 | 35.08 |
| 9 | 29.72 |
| 10 | 32.63 |

El número óptimo de clústeres fue **K = 3**, determinado por el cambio significativo en la pendiente de la curva de inercia entre K=3 y K=4.

#### 2.4.4. Algoritmo K-Means

Se implementó el algoritmo K-Means con las siguientes características:

*   **Inicialización:** Aleatoria con seed=42 para reproducibilidad.
*   **Iteraciones:** Máximo 100 iteraciones hasta convergencia.
*   **Métrica de Distancia:** Distancia Euclidiana.
*   **Criterio de Convergencia:** Cambio menor a 1e-4 en la posición de centroides.

### 2.5. Análisis de Datos Cualitativos

Las respuestas a las preguntas abiertas fueron sometidas a un **Análisis de Contenido Temático** [4], utilizando codificación abierta para identificar categorías emergentes relacionadas con las barreras y los dilemas éticos de la IA.

---

## 3. Resultados

### 3.1. Perfiles Docentes: Análisis de Clúster K-Means

El análisis de clúster identificó tres perfiles docentes claramente diferenciados. La Tabla 1 presenta un resumen de las características principales de cada clúster.

| Clúster | Denominación | N | % Muestra | Media CDG | Media UPIA | Media CT | SD CDG | SD UPIA | SD CT |
|:-------:|:------------------|:--:|:----------:|:---------:|:----------:|:--------:|:-------:|:-------:|:-------:|
| 0 | Novatos | 15 | 21.4% | 2.72 | 2.66 | 1.05 | 0.66 | 0.70 | 0.14 |
| 1 | Tradicionales | 41 | 58.6% | 3.43 | 4.14 | 1.24 | 0.50 | 0.44 | 0.26 |
| 2 | Innovadores | 14 | 20.0% | 4.18 | 4.59 | 2.25 | 0.61 | 0.33 | 0.42 |

**Tabla 1. Caracterización de los Clústeres Docentes**

#### 3.1.1. Clúster 0: Docentes Novatos (21.4%, N=15)

Los docentes clasificados como Novatos presentan las puntuaciones más bajas en todas las dimensiones. Su Competencia Digital General (CDG = 2.72) indica un nivel de competencia digital básico, con variabilidad moderada (SD = 0.66). El Uso y Percepción de IA (UPIA = 2.66) es notablemente bajo, sugiriendo que este grupo tiene una experiencia limitada con tecnologías de IA. El Conocimiento Teórico (CT = 1.05) es el más bajo de todos los clústeres, indicando que estos docentes tienen escaso conocimiento de marcos teóricos formales como DigCompEdu o COIL.

**Implicaciones:** Este grupo requiere una intervención formativa fundamental, tanto en competencias digitales básicas (uso de LMS, herramientas de colaboración) como en la introducción estructurada a la IA y sus aplicaciones pedagógicas.

#### 3.1.2. Clúster 1: Docentes Tradicionales (58.6%, N=41)

Los docentes Tradicionales representan la mayoría de la muestra (58.6%). Presentan una Competencia Digital General moderada-alta (CDG = 3.43), indicando que son competentes en el uso de tecnologías educativas establecidas. Sin embargo, su Uso y Percepción de IA (UPIA = 4.14) es sorprendentemente alto, lo que sugiere que, aunque tienen experiencia limitada con IA, su percepción de su potencial es positiva. El Conocimiento Teórico (CT = 1.24) sigue siendo bajo, aunque ligeramente superior al de los Novatos.

**Hallazgo Clave:** Este clúster demuestra una paradoja interesante: los docentes tienen competencias digitales sólidas pero un conocimiento teórico limitado, lo que sugiere que su adopción de IA se basa más en la experiencia práctica que en un marco conceptual formal.

**Implicaciones:** Este grupo necesita formación especializada en IA que vincule su experiencia práctica con marcos teóricos, facilitando una integración más reflexiva y pedagógicamente fundamentada de la IA en su práctica docente.

#### 3.1.3. Clúster 2: Docentes Innovadores (20.0%, N=14)

Los docentes Innovadores lideran la muestra con las puntuaciones más altas en todas las dimensiones. Su Competencia Digital General (CDG = 4.18) indica un dominio avanzado de tecnologías digitales. El Uso y Percepción de IA (UPIA = 4.59) es el más alto, demostrando una integración activa y reflexiva de la IA en su enseñanza. El Conocimiento Teórico (CT = 2.25) es significativamente superior a los otros clústeres, sugiriendo que este grupo busca activamente marcos conceptuales para guiar su práctica.

**Implicaciones:** Este grupo actúa como agentes de cambio y puede desempeñar un rol crucial en la difusión de buenas prácticas y la mentoría de otros docentes. Su mayor conocimiento teórico sugiere que la adopción de IA está mediada por una comprensión más profunda de los marcos pedagógicos.

### 3.2. Visualizaciones del Análisis de Clúster

#### 3.2.1. Método del Codo (Elbow Plot)

La gráfica del Método del Codo muestra claramente el punto de inflexión en K=3, donde la reducción de inercia comienza a desacelerarse significativamente. Este es el criterio principal para seleccionar K=3 como el número óptimo de clústeres.

#### 3.2.2. Matriz de Puntuaciones Z-Score

La matriz de Z-scores por clúster revela patrones claros:

*   **Clúster 0 (Novatos):** Puntuaciones Z negativas en todas las variables, indicando que están por debajo del promedio general.
*   **Clúster 1 (Tradicionales):** Puntuaciones Z cercanas a cero en CDG (ligeramente positivas) y positivas en UPIA, indicando una posición intermedia en competencia digital pero una percepción de IA por encima del promedio.
*   **Clúster 2 (Innovadores):** Puntuaciones Z positivas en todas las variables, particularmente altas en CT, indicando que están significativamente por encima del promedio general.

#### 3.2.3. Visualización 2D con Centroides

La gráfica de dispersión 2D (CDG vs UPIA) con centroides marcados como estrellas negras muestra una separación clara entre los clústeres, validando la calidad de la segmentación. El tamaño de los puntos representa el Conocimiento Teórico (CT), evidenciando visualmente que el clúster Innovador tiene mayor CT.

#### 3.2.4. Gráfica de Barras de Medias

La comparación de medias por clúster confirma las diferencias significativas entre grupos, particularmente en CT, donde el clúster Innovador es claramente superior.

### 3.3. Hallazgos Cualitativos: Barreras y Dilemas Éticos

El análisis de contenido temático de las preguntas abiertas reveló que las principales barreras para la integración de las TIC y la IA se agrupan en tres categorías:

1. **Infraestructura y Conectividad (35% de menciones):** La limitación más recurrente, afectando la implementación de estrategias digitales. Los docentes reportan problemas de conexión a internet deficiente y falta de equipos actualizados tanto para ellos como para los estudiantes.

2. **Costo y Licenciamiento (25% de menciones):** La necesidad de herramientas de pago y la falta de licencias institucionales limita el acceso a plataformas especializadas de IA.

3. **Falta de Formación Específica (40% de menciones):** La demanda de capacitación continua, lo cual se alinea directamente con la baja media en 'Formacion_Especifica_IA' ($\bar{x} = 3.09$) del análisis descriptivo previo.

En cuanto a los dilemas éticos de la IA, los docentes expresaron preocupación por:

*   **Dependencia Tecnológica:** Riesgo de que los estudiantes se vuelvan excesivamente dependientes de las herramientas de IA.
*   **Sustitución del Pensamiento Crítico:** Preocupación de que la IA sustituya el análisis crítico y el criterio personal de los estudiantes.
*   **Plagio y Deshonestidad Académica:** Dilemas sobre cómo detectar y prevenir el uso no ético de IA en trabajos académicos.

---

## 4. Discusión

Los resultados del análisis de clúster K-Means confirman la heterogeneidad de los perfiles docentes en la educación superior ecuatoriana, un hallazgo consistente con estudios previos en contextos de rápida transformación digital [5]. La identificación de tres clústeres —Novatos, Tradicionales e Innovadores— proporciona una herramienta diagnóstica valiosa para la planificación estratégica institucional y el diseño de políticas de formación docente.

El **Clúster 2 (Innovadores)**, que representa el 20% de la muestra, demuestra que una porción significativa del profesorado ha logrado integrar un alto nivel de competencia digital con la adopción reflexiva de IA. Este grupo, además, presenta el mayor Conocimiento Teórico (CT = 2.25), lo que sugiere que la adopción de tecnologías emergentes no es un acto aislado, sino que está intrínsecamente ligado a una búsqueda activa de marcos conceptuales que guíen su práctica. Este hallazgo es crucial, ya que refuta la noción de que la IA es adoptada de manera acrítica y subraya la necesidad de fomentar la conexión entre la práctica y la teoría.

Por otro lado, el **Clúster 1 (Tradicionales)** (58.6% de la muestra) revela una brecha crítica: docentes con una sólida base en competencias digitales (CDG = 3.43) que, sin embargo, presentan una alta percepción de IA (UPIA = 4.14) pero un bajo conocimiento teórico (CT = 1.24). Este perfil es de particular interés para las políticas de formación, ya que su adopción de IA no se debe a una falta de habilidad tecnológica general, sino a una falta de comprensión teórica y pedagógica profunda. Estos docentes podrían beneficiarse enormemente de programas de formación que vinculen su experiencia práctica con marcos teóricos formales.

La baja puntuación en Conocimiento Teórico para toda la muestra, especialmente en los clústeres Novatos y Tradicionales, se triangula directamente con los hallazgos cualitativos de la **Falta de Formación Específica**. Esto indica que, aunque la IA es percibida positivamente por su potencial de ahorro de tiempo (media general UPIA = 3.91), la falta de un marco teórico y pedagógico formal (como DigCompEdu) impide una integración profunda y reflexiva.

Finalmente, la recurrencia de la **Infraestructura y Conectividad** como la principal limitación cualitativa, a pesar de las altas puntuaciones en CDG en los clústeres más avanzados, pone de manifiesto que las barreras sistémicas persisten y limitan la capacidad de los docentes para capitalizar plenamente sus competencias digitales y el potencial de la IA. Los dilemas éticos identificados (dependencia, sustitución del pensamiento crítico) deben ser el eje central de cualquier programa de formación en IA, asegurando que la integración tecnológica se realice con una perspectiva crítica y humanista.

---

## 5. Conclusiones

La investigación concluye que la población docente de educación superior en Ecuador se segmenta en tres perfiles distintos en relación con las competencias digitales y la adopción de IA. La principal conclusión es que la transición de las competencias digitales tradicionales a la integración efectiva de la IA está mediada por la **formación especializada** y el **conocimiento de marcos teóricos**.

Se recomienda a las instituciones de educación superior:

1. **Diseñar programas de formación diferenciados** basados en los perfiles de clúster, enfocando los esfuerzos en el Clúster 1 (Tradicionales) para superar la barrera del conocimiento teórico, y en el Clúster 0 (Novatos) para establecer las bases digitales fundamentales.

2. **Priorizar la inversión en infraestructura tecnológica** y el acceso a herramientas licenciadas para eliminar las barreras sistémicas que limitan la práctica docente.

3. **Integrar la ética de la IA** y el pensamiento crítico como componentes obligatorios en la formación, abordando los dilemas identificados por los propios docentes.

4. **Establecer comunidades de práctica** lideradas por el Clúster 2 (Innovadores) para facilitar la mentoría y la difusión de buenas prácticas.

5. **Implementar un sistema de seguimiento** que monitoree la evolución de los docentes entre clústeres, evaluando el impacto de las intervenciones de formación.

**Limitaciones:** El tamaño de la muestra (N=70) es relativamente pequeño y se limita a Ecuador. Futuras investigaciones deberían replicar este análisis con muestras más amplias y en contextos geográficos más diversos.

**Implicaciones Futuras:** Este estudio abre la puerta a investigaciones longitudinales que examinen cómo los docentes transicionan entre clústeres a lo largo del tiempo, así como estudios cualitativos más profundos sobre los factores que facilitan o impiden la adopción de IA en contextos específicos.

---

## 6. Referencias

[1] UNESCO. (2018). *Marco de Competencias de los Docentes en Materia de TIC*. UNESCO.

[2] Salloum, S. A., Dbouk, L., & Al-Emran, M. (2023). The role of artificial intelligence in higher education: A systematic review. *International Journal of Educational Technology in Higher Education*, 20(1), 1-28.

[3] Creswell, J. W., & Plano Clark, V. L. (2018). *Designing and Conducting Mixed Methods Research* (3rd ed.). SAGE Publications.

[4] Hsieh, H. F., & Shannon, S. E. (2005). Three approaches to qualitative content analysis. *Qualitative Health Research*, 15(9), 1277–1288.

[5] Tondeur, J., van Braak, J., Ertmer, P. A., & Ottenbreit-Leftwich, A. (2017). Understanding pre-service teachers' intentions to integrate technology in education: A cluster analysis. *Computers & Education*, 113, 128-137.

---

## Apéndice: Metodología CRISP-DM

La metodología CRISP-DM fue aplicada de manera integral en este estudio, proporcionando un marco estructurado para el análisis de datos:

*   **Fase 1 - Business Understanding:** Se definió el problema como la necesidad de identificar perfiles docentes para diseñar políticas de formación diferenciadas.
*   **Fase 2 - Data Understanding:** Se exploraron 70 encuestas con 24 variables cuantitativas, identificando distribuciones y correlaciones.
*   **Fase 3 - Data Preparation:** Se crearon variables compuestas y se estandarizaron los datos.
*   **Fase 4 - Modeling:** Se aplicó K-Means con K=3, determinado por el Método del Codo.
*   **Fase 5 - Evaluation:** Se caracterizaron los clústeres y se validaron los resultados.
*   **Fase 6 - Deployment:** Se generaron visualizaciones interactivas y tablas para la toma de decisiones.

---

**Fin del Artículo**
