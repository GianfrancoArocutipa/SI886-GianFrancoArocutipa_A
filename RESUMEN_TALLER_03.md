# Resumen de Requerimientos: Taller de Laboratorio 03

Este documento resume los pasos y entregables exactos que pide el taller "Análisis comparado del PEI y del Plan de Gobierno Digital", según las instrucciones originales.

## 1. Objetivo Principal
Analizar el Plan Estratégico Institucional (PEI) y el Plan de Gobierno Digital (PGD) de una entidad pública peruana real para verificar su articulación, y aplicar estos conceptos a la organización de tu proyecto de curso mediante la redacción de la Sección 1.2 del PETI.

## 2. Pasos a Ejecutar (Fases del Taller)

- **Paso A (Localizar documentos):** Descargar el PEI y PGD vigentes de una entidad peruana, registrando sus URLs, fecha de descarga y resolución de aprobación.
- **Paso B (Extraer estructura y objetivos):** Usar scripts en Python (`pdfplumber`, `pandas`) para extraer de forma automática la estructura (índice real) y los objetivos de ambos documentos. Se exige revisión manual de lo extraído.
- **Paso C (Verificar articulación):** 
  - Crear una **matriz de articulación** que muestre qué objetivo del PGD se alinea a qué objetivo del PEI, verificando si tienen indicador, línea base y meta.
  - Ejecutar un script para evaluar el **porcentaje de objetivos "completos"**.
  - **Evaluar el PGD** contra la estructura exigida por los lineamientos de la PCM (9 componentes y 4 requisitos adicionales).
- **Paso D (Mapa de instrumentos):** Construir en draw.io (o Mermaid) el diagrama del mapa de instrumentos de planeamiento de **tu propia organización objeto de estudio** y una tabla evaluando la vigencia de los mismos.
- **Paso E (Redactar PETI):** Redactar la **Sección 1.2 del PETI** de tu proyecto (Marco de planeamiento y articulación), definiendo el objetivo superior de enganche y el enfoque estratégico.

## 3. Formato y Reglas de Entrega

1. **Plantilla Word a PDF:** Se debe usar obligatoriamente la plantilla `SI886-PLANTILLA-TALLER.docx`. El entregable final es un **PDF** nombrado `SI886-S03-TALLER-Grupo<N>.pdf`.
2. **Repositorio y Enlaces (IMPORTANTE):** El profesor **no califica capturas de pantalla sueltas**. Todos los archivos generados, scripts, matrices en CSV y redacciones deben subirse a una rama en **GitHub**, hacer un merge y colocarle la etiqueta (tag) `taller-03`.
3. **Evidencias en el Informe:** En la sección "3. Resultados" del documento Word, se deben colocar **las URLs de GitHub** que apunten directamente a los archivos o resultados. Si un resultado se declara en el Word pero no tiene enlace a GitHub, no se califica.

## 4. Conclusiones Esperadas
El informe debe incluir al menos tres conclusiones, enfocadas en:
1. La diferencia entre articulación declarada vs. articulación verificable (con metas e indicadores).
2. El peligro de tener proyectos "huérfanos" (sin ancla en el plan superior).
3. La diferencia entre el enfoque estratégico que una entidad "dice" tener frente a lo que realmente financia.
