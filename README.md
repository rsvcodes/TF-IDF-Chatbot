# Proyecto de Chatbot de Ciencia de Datos

## Descripción del Proyecto

Este proyecto consiste en un chatbot de procesamiento de lenguaje natural que utiliza técnicas de inteligencia artificial para responder preguntas relacionadas con el campo de la ciencia de datos. La inteligencia artificial es un componente esencial para mejorar la capacidad de comprensión y respuesta del chatbot.

### Características Principales

- Utiliza la biblioteca NLTK para el procesamiento de texto.
- Implementa un modelo de vectorización TF-IDF y similitud coseno para generar respuestas.
- Incluye una función de saludo para una experiencia más amigable.
- Puede manejar despedidas y agradecimientos para una interacción más natural.

## Teoría

### Inteligencia Artificial en el Chatbot

#### Funcionamiento Básico

La inteligencia artificial en este chatbot se basa en técnicas de procesamiento de lenguaje natural (NLP) y aprendizaje automático. A continuación, se describe cómo funciona:

1. **Preprocesamiento de Texto**: El texto de entrada se normaliza y tokeniza utilizando la biblioteca NLTK. Se eliminan las puntuaciones y se convierte a minúsculas.

2. **Vectorización TF-IDF**: Se utiliza un modelo de vectorización TF-IDF (Term Frequency-Inverse Document Frequency) para convertir el texto en vectores numéricos. Esto ayuda a representar el contenido semántico de las oraciones.

3. **Modelo de Similitud Coseno**: El modelo utiliza similitud coseno entre los vectores TF-IDF para encontrar la oración más relevante en el corpus con respecto a la entrada del usuario.

4. **Respuesta Generada**: La respuesta se genera a partir de la oración más relevante encontrada. Si la similitud coseno es baja, el chatbot indicará que no comprende la pregunta.

#### Integración de la Inteligencia Artificial

- **NLTK y Procesamiento de Lenguaje Natural**: NLTK proporciona herramientas esenciales para el procesamiento de lenguaje natural, incl
