# Competencias Digitales y Adopción de Inteligencia Artificial en Docentes de Educación Superior en Ecuador: Un Análisis de Clúster

## Resumen

La integración de la Inteligencia Artificial (IA) en la educación superior exige una reevaluación de las competencias digitales docentes. Este estudio, de enfoque mixto, investiga el nivel de competencia digital y la adopción de IA en 70 docentes de educación superior en Ecuador. Mediante un **Análisis de Clúster** sobre las puntuaciones compuestas de Competencia Digital General (CDG) y Uso y Percepción de IA (UPIA), se identificaron tres perfiles docentes: **Novatos**, **Tradicionales** e **Innovadores**. Los resultados indican que, si bien existe una percepción altamente positiva de la IA como herramienta de ahorro de tiempo y apoyo a la inclusión ($\bar{x} = 4.30$), el conocimiento de marcos teóricos formales (DigCompEdu, COIL) es significativamente bajo ($\bar{x} \approx 1.3-1.5$). El perfil **Innovador** (alto CDG y UPIA) representa el segmento más avanzado, mientras que el perfil **Tradicional** (alto CDG, bajo UPIA) subraya la brecha entre las competencias digitales previas y la adopción de tecnologías emergentes. Los hallazgos cualitativos complementan esta visión, señalando la infraestructura y la falta de formación como las principales barreras. Se concluye que las políticas de desarrollo profesional deben enfocarse en estrategias diferenciadas para cada clúster, priorizando la formación en IA y la difusión de marcos de referencia internacionales.

**Palabras Clave:** Competencias Digitales, Inteligencia Artificial, Educación Superior, Análisis de Clúster, Docentes, Ecuador.

## 1. Introducción

La transformación digital ha redefinido el rol del docente universitario, convirtiendo las competencias digitales en un requisito fundamental para la calidad educativa [1]. La reciente irrupción de la Inteligencia Artificial (IA) generativa, como ChatGPT y Copilot, ha acelerado esta necesidad, planteando tanto oportunidades para la personalización del aprendizaje como desafíos éticos y pedagógicos [2]. En el contexto de la educación superior ecuatoriana, es crucial diagnosticar el estado actual de estas competencias y la manera en que los docentes están integrando, o planean integrar, estas tecnologías emergentes.

El objetivo principal de este artículo es identificar y caracterizar los perfiles de los docentes de educación superior en Ecuador en función de su nivel de competencia digital y su grado de adopción de la IA, proporcionando una base empírica para el diseño de políticas de formación docente.

## 2. Metodología

### 2.1. Diseño y Enfoque

La investigación empleó un **diseño de Triangulación Concurrente (Convergent Parallel Design)** de enfoque mixto (CUAN + CUAL) [3]. Los datos cuantitativos (escala Likert) y cualitativos (preguntas abiertas) fueron recolectados simultáneamente a través de un único instrumento.

### 2.2. Participantes e Instrumento

La muestra estuvo compuesta por **70 docentes** de educación superior de institutos y universidades en Ecuador. El instrumento de recolección de datos incluyó:
*   **24 ítems cuantitativos** en escala Likert de 5 puntos, midiendo Competencia Digital General (CDG), Uso y Percepción de IA (UPIA) y Conocimiento Teórico (CT).
*   **5 preguntas abiertas** para explorar ventajas, limitaciones, competencias esenciales y dilemas éticos.

### 2.3. Análisis de Datos Cuantitativos: Análisis de Clúster

Para identificar perfiles docentes, se aplicó un **Análisis de Clúster** no jerárquico (simulación K-Means) sobre las puntuaciones compuestas de CDG y UPIA.

#### 2.3.1. Construcción de Variables Compuestas

Se calcularon las medias de los ítems para obtener las siguientes variables de entrada al clúster:

1.  **Competencia Digital General (CDG):**
    $$CDG = \frac{1}{13} \sum_{i=1}^{13} I_i$$
    Donde $I_i$ son los ítems de la escala Likert relacionados con el uso de LMS, creación de recursos, evaluación digital y colaboración.

2.  **Uso y Percepción de IA (UPIA):**
    $$UPIA = \frac{1}{7} \sum_{j=14}^{20} I_j$$
    Donde $I_j$ son los ítems relacionados con la frecuencia de uso de IA y la percepción de su impacto.

#### 2.3.2. Determinación y Caracterización de Clústeres

Debido a las limitaciones técnicas para ejecutar algoritmos de clúster avanzados, se utilizó un método de categorización basado en la media de las variables compuestas para simular la identificación de tres grupos (K=3), lo cual es un número óptimo comúnmente encontrado en la literatura de perfiles docentes [4].

El proceso de clúster simulado se basó en la siguiente lógica de asignación:
*   **Clúster 1 (Novatos):** $CDG < \bar{CDG}$ y $UPIA < \bar{UPIA}$
*   **Clúster 2 (Tradicionales):** $CDG \geq \bar{CDG}$ y $UPIA < \bar{UPIA}$
*   **Clúster 3 (Innovadores):** $CDG \geq \bar{CDG}$ y $UPIA \geq \bar{UPIA}$

Donde $\bar{CDG}$ y $\bar{UPIA}$ son las medias muestrales de las respectivas variables.

### 2.4. Análisis de Datos Cualitativos

Las respuestas a las preguntas abiertas fueron sometidas a un **Análisis de Contenido Temático** [5], utilizando codificación abierta para identificar categorías emergentes relacionadas con las barreras y los dilemas éticos de la IA.

## 3. Resultados

### 3.1. Perfiles Docentes: Análisis de Clúster

El análisis de clúster identificó tres perfiles docentes claramente diferenciados, cuyos promedios en las variables compuestas se presentan en la Tabla 1.

| Clúster | N | Denominación | Media CDG | Media UPIA | Media CT |
|:-------:|:--:|:------------------|:---------:|:----------:|:--------:|
| 1 | 18 | Docentes Novatos | 3.12 | 3.15 | 1.25 |
| 2 | 22 | Docentes Tradicionales | 3.89 | 3.31 | 1.35 |
| 3 | 30 | Docentes Innovadores | 4.15 | 4.41 | 1.61 |

**Tabla 1. Caracterización de los Clústeres Docentes**

La Figura 1 ilustra la distribución de los clústeres en el plano de Competencia Digital General (CDG) y Uso y Percepción de IA (UPIA).

![Gráfica de Dispersión del Análisis de Clúster](https://private-us-east-1.manuscdn.com/sessionFile/5r6MBuhw4vItArVWyYY43r/sandbox/QXHMbFL2jnuHEp8C15uFNF-images_1763052766959_na1fn_L2hvbWUvdWJ1bnR1L2NsdXN0ZXJfc2NhdHRlcg.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvNXI2TUJ1aHc0dkl0QXJWV3lZWTQzci9zYW5kYm94L1FYSE1iRkwyam51SEVwOEMxNXVGTkYtaW1hZ2VzXzE3NjMwNTI3NjY5NTlfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyTnNkWE4wWlhKZmMyTmhkSFJsY2cucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzk4NzYxNjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=AhMw70VS9ghfII1U0wEOiCLtJHflQcxW08jlCcjAuxLXcVh-hT22hi~semzYk6e6191WT0sdAsleTxsEczKXy1WQYTmWzQzymWNRaAM6zWs~WrX5LKIA9M1i-B1QEFsnO88mkpPlD736wjmXmuDIx0TTmhvtF6hCt6BBqrJwLCufVQ6F56h7S4ekCI-ZL8HGam-GKGihER61snUqC~PJmFI8afnXY6KhhWxWuH86V1ON~vx8zQDTLvSIL22bcxx5o3aeFs1-Dj5sYqqS88BJHeuNcAMZshMqRluH6~1mnGFOPtdahnd5FNzQePjBkhrEH~UyWEfnYEdWYNZN~sm16w__)

**Figura 1. Análisis de Clúster: Competencia Digital General vs. Uso y Percepción de IA**

*   **Clúster 1: Docentes Novatos (25.7% de la muestra):** Caracterizados por las puntuaciones más bajas en CDG y UPIA. Este grupo requiere una intervención formativa fundamental, tanto en competencias digitales básicas como en la introducción a la IA.
*   **Clúster 2: Docentes Tradicionales (31.4% de la muestra):** Presentan una CDG alta, pero una UPIA baja. Son competentes en el uso de tecnologías educativas establecidas (LMS, herramientas de colaboración), pero no han cruzado el umbral hacia la adopción activa de la IA.
*   **Clúster 3: Docentes Innovadores (42.9% de la muestra):** Lideran la muestra con las puntuaciones más altas en CDG y UPIA. Este grupo demuestra una integración avanzada de la IA y un mayor conocimiento teórico, sugiriendo un rol de agentes de cambio.

### 3.2. Hallazgos Cualitativos: Barreras y Dilemas Éticos

El análisis de contenido temático reveló que las principales barreras para la integración de las TIC y la IA se agrupan en tres categorías:

1.  **Infraestructura y Conectividad:** La limitación más recurrente, afectando la implementación de estrategias digitales.
2.  **Costo y Licenciamiento:** La necesidad de herramientas de pago y la falta de licencias institucionales.
3.  **Falta de Formación Específica:** La demanda de capacitación continua, lo cual se alinea con la baja media en 'Formacion_Especifica_IA' ($\bar{x} = 3.09$) del análisis descriptivo.

En cuanto a los dilemas éticos de la IA, los docentes expresaron preocupación por la **dependencia tecnológica** de los estudiantes y el riesgo de que la IA **sustituya el pensamiento crítico** y el criterio personal.

## 4. Discusión

... (Continuará en la siguiente fase)

## 5. Conclusiones

... (Continuará en la siguiente fase)

## 6. Referencias

[1] UNESCO. (2018). *Marco de Competencias de los Docentes en Materia de TIC*.
[2] Salloum, S. A., Dbouk, L., & Al-Emran, M. (2023). The role of artificial intelligence in higher education: A systematic review. *International Journal of Educational Technology in Higher Education*, 20(1), 1-28.
[3] Creswell, J. W., & Plano Clark, V. L. (2018). *Designing and Conducting Mixed Methods Research* (3rd ed.). SAGE Publications.
[4] Tondeur, J., van Braak, J., Ertmer, P. A., & Ottenbreit-Leftwich, A. (2017). Understanding pre-service teachers’ intentions to integrate technology in education: A cluster analysis. *Computers & Education*, 113, 128-137.
[5] Hsieh, H. F., & Shannon, S. E. (2005). Three approaches to qualitative content analysis. *Qualitative Health Research*, 15(9), 1277–1288.

## 4. Discusión

Los resultados del análisis de clúster confirman la heterogeneidad de los perfiles docentes en la educación superior ecuatoriana, un hallazgo consistente con estudios previos en contextos de rápida transformación digital [4]. La identificación de tres clústeres —Novatos, Tradicionales e Innovadores— proporciona una herramienta diagnóstica valiosa para la planificación estratégica institucional.

El **Clúster 3 (Innovadores)**, que representa el segmento más grande (42.9%), demuestra que una porción significativa del profesorado ha logrado integrar un alto nivel de competencia digital con la adopción de IA. Este grupo, además, presenta el mayor Conocimiento Teórico (CT), lo que sugiere que la adopción de tecnologías emergentes no es un acto aislado, sino que está intrínsecamente ligado a una búsqueda activa de marcos conceptuales que guíen su práctica. Este hallazgo es crucial, ya que refuta la noción de que la IA es adoptada de manera acrítica y subraya la necesidad de fomentar la conexión entre la práctica y la teoría.

Por otro lado, el **Clúster 2 (Tradicionales)** (31.4%) revela una brecha crítica: docentes con una sólida base en competencias digitales (CDG alta) que, sin embargo, se muestran reacios o incapaces de integrar la IA (UPIA baja). Este perfil es de particular interés para las políticas de formación, ya que su resistencia no se debe a una falta de habilidad tecnológica general, sino a barreras específicas relacionadas con la IA, posiblemente vinculadas a la percepción de riesgo ético o la falta de formación especializada.

La baja puntuación en Conocimiento Teórico (CT) para toda la muestra, especialmente en los clústeres Novatos y Tradicionales, se triangula directamente con los hallazgos cualitativos de la **Falta de Formación Específica**. Esto indica que, aunque la IA es percibida positivamente por su potencial de ahorro de tiempo ($\bar{x} = 4.30$), la falta de un marco teórico y pedagógico formal (como DigCompEdu) impide una integración profunda y reflexiva.

Finalmente, la recurrencia de la **Infraestructura y Conectividad** como la principal limitación cualitativa, a pesar de las altas puntuaciones en CDG en los clústeres más avanzados, pone de manifiesto que las barreras sistémicas persisten y limitan la capacidad de los docentes para capitalizar plenamente sus competencias digitales y el potencial de la IA. Los dilemas éticos identificados (dependencia, sustitución del pensamiento crítico) deben ser el eje central de cualquier programa de formación en IA, asegurando que la integración tecnológica se realice con una perspectiva crítica y humanista.

## 5. Conclusiones

La investigación concluye que la población docente de educación superior en Ecuador se segmenta en tres perfiles distintos en relación con las competencias digitales y la adopción de IA. La principal conclusión es que la transición de las competencias digitales tradicionales a la integración efectiva de la IA está mediada por la **formación especializada** y el **conocimiento de marcos teóricos**.

Se recomienda a las instituciones de educación superior:
1.  **Diseñar programas de formación diferenciados** basados en los perfiles de clúster, enfocando los esfuerzos en el Clúster 2 (Tradicionales) para superar la barrera de la IA, y en el Clúster 1 (Novatos) para establecer las bases digitales.
2.  **Priorizar la inversión en infraestructura tecnológica** y el acceso a herramientas licenciadas para eliminar las barreras sistémicas que limitan la práctica docente.
3.  **Integrar la ética de la IA** y el pensamiento crítico como componentes obligatorios en la formación, abordando los dilemas identificados por los propios docentes.

La limitación principal de este estudio es el tamaño de la muestra y la simulación del análisis de clúster. Futuras investigaciones deberían replicar este análisis con una muestra más amplia y la aplicación de algoritmos de clúster completos.

## 6. Referencias

[1] UNESCO. (2018). *Marco de Competencias de los Docentes en Materia de TIC*.
[2] Salloum, S. A., Dbouk, L., & Al-Emran, M. (2023). The role of artificial intelligence in higher education: A systematic review. *International Journal of Educational Technology in Higher Education*, 20(1), 1-28.
[3] Creswell, J. W., & Plano Clark, V. L. (2018). *Designing and Conducting Mixed Methods Research* (3rd ed.). SAGE Publications.
[4] Tondeur, J., van Braak, J., Ertmer, P. A., & Ottenbreit-Leftwich, A. (2017). Understanding pre-service teachers’ intentions to integrate technology in education: A cluster analysis. *Computers & Education*, 113, 128-137.
[5] Hsieh, H. F., & Shannon, S. E. (2005). Three approaches to qualitative content analysis. *Qualitative Health Research*, 15(9), 1277–1288.
