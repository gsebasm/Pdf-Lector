# IA Pdf Lector

Lector de PDF con Langchain

## Requisitos

- Python 3.11.8
- pip

## Instalación

1. **Clona este repositorio:**

   ```sh
   cd tu_proyecto
   ```

2. **Crea y activa un entorno virtual:**

   - En Windows:

     ```sh
     python -m venv venv
     venv\Scripts\activate
     ```

   - En macOS y Linux:

     ```sh
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Instala las dependencias:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Configura las variables de entorno:**

   Crea un archivo `.env` en la raíz del proyecto y añade tus propias claves y configuraciones. Aquí hay un ejemplo:

   ```env
   SECRET_KEY=tu_super_secreta_clave de open ai
   HUGGINGFACEHUB_API_TOKEN= tu key de huggingface
   ```

## Uso

1. **Asegúrate de que el entorno virtual está activado** (si no está ya activado):

   - En Windows:

     ```sh
     venv\Scripts\activate
     ```

   - En macOS y Linux:

     ```sh
     source venv/bin/activate
     ```

2. **Ejecuta tu aplicación**:

   ```sh
   streamlit run app.py
   ```

## Notas

- Recuerda siempre activar el entorno virtual antes de trabajar en tu proyecto para asegurar que estás utilizando las dependencias correctas.
- Asegúrate de que el archivo `.env` no se comparta públicamente ya que contiene información sensible.
