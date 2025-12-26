# mi_nuevo_repo
El proyecto consiste en desarrollar y desplegar una aplicación web interactiva para el análisis exploratorio de datos (EDA) utilizando Python.  El flujo de trabajo abarca desde la configuración inicial del entorno hasta la publicación de la aplicación en internet.

1. Configuración del entorno y repositorio

Primero, creo un repositorio en GitHub con los archivos básicos del proyecto (README.md, .gitignore con plantilla de Python y requirements.txt).
Luego creo un entorno virtual e instalar las librerías esenciales: pandas para el manejo de datos, plotly-express para visualizaciones interactivas y streamlit para construir la aplicación web.
El proyecto se desarrolla en VS Code, usando el entorno virtual configurado como intérprete de Python.

2. Obtención y preparación de los datos

Descargo un archivo CSV (principalmente el dataset vehicles_us.csv con anuncios de coches) y coloco dentro del directorio del proyecto. Este conjunto de datos es la base para todo el análisis y las visualizaciones.

3. Análisis exploratorio de datos (EDA)

Antes de crear la aplicación web, se realiza un análisis exploratorio en un Jupyter Notebook (EDA.ipynb), ubicado en un directorio llamado notebooks.
En este notebook se exploran los datos y se crean visualizaciones básicas (como histogramas y gráficos de dispersión) usando plotly-express, con el fin de entender la estructura del dataset y probar los gráficos que luego se integrarán en la aplicación.
Este paso es exploratorio; su propósito principal es preparar el terreno para la app.

4. Desarrollo de la aplicación web

Se crea un archivo app.py en la raíz del proyecto donde se desarrolla la aplicación con Streamlit.
La aplicación debe:

Se lee el archivo CSV con pandas.

Se muestra al menos un encabezado descriptivo.

Se incluye elementos interactivos (botones).

Genero un histograma usando plotly-express cuando el usuario interactúa con la app.

Con el fin de mostrar los gráficos de forma interactiva dentro de la página web.

La aplicación se puede ejecutar localmente con streamlit run app.py para verificar que funciona correctamente.

5. Documentación y control de versiones

Actualizo el  archivo README.md 

6. Despliegue en Render

Finalmente, la aplicación se despliega en Render, conectando la cuenta de Render con GitHub.
Se configura un servicio web que:

Instala las dependencias desde requirements.txt.

Ejecuta la aplicación con streamlit run app.py.

Una vez desplegada, la aplicación queda disponible mediante una URL pública, permitiendo que cualquier persona pueda interactuar con los gráficos desde el navegador.

Se desarrollo un proyecto completo de análisis de datos, integrando:

Uso de Git y GitHub.

Análisis exploratorio con pandas y plotly.

Desarrollo de aplicaciones web con Streamlit.

Despliegue en la nube con Render.

http://localhost:8506/
