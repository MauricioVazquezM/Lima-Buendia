# lima-buendia

El Centro ITAM para Datos + Algoritmos + Sociedad, CDAS, tiene como misión ayudar a las organizaciones a mejorar los servicios que ofrecen con un impacto positivo y en conjunto con SocialTIC, una  institución sin fines de lucro dedicada a la investigación, formación, acompañamiento y promoción de la tecnología digital e información para fines sociales, desarrollan el proyecto Lima Buendía. 

### Contexto del problema

SocialTIC tiene el objetivo de brindar a los grupos
de sociedad civil y de mujeres que están estudiando y haciendo incidencia en materia de violencia de género y feminicidios herramientas más robustas basadas en la evidencia generada para hacer sus reportes. Adicional a esto, generar hallazgos que permitan sensibilizar a la sociedad en temas de feminicidio y que todos los eventos tengan la misma relevancia pues, siempre se habla de la vida de una mujer. Bajo este contexto, el proyecto se centró principalmente en la construcción de visualizaciones a partir del análisis de texto de las conversaciones de las reacciones a notas en redes sociales y encabezados de medios. Las bases de datos fueron proporcionadas por SocialTIC y abarcan el periodo de enero 2017 a junio 2022. 

### Objetivo

El objetivo del proyecto buscar causalidad y poder definir cuándo un feminicidio se vuelve viral. Es decir, una vez que ocurre un feminicidio, ¿se detonan conversaciones en redes sociales? ¿Las conversaciones siguen las investigaciones? 


### Equipo de trabajo

El equipo de trabajo está integrado por:
+ Mauricio Vázquez, alumno del plan conjunto de Actuaría y Ciencia de Datos del ITAM
+ Elizabeth Viveros, alumna de la maestría en Ciencia de Datos del ITAM
+ Ana Bertha Coronel, alumna de la maestría en Ciencia de Datos del ITAM

Los mentores por parte del Centro de Datos del ITAM son **Miguel Angel Escalante** y **Jesús Ramos**; por parte de SocialTIC, **Frida García**. El sponsor del proyecto es **Juan Manuel Casanueva**, CEO de SocialTIC.


### Organización del repositorio
El repositorio está divididio en 3 carpetas que se describen a continuación:

+ [data](https://gitlab.com/datos-algoritmos-sociedad-itam/lima-buendia/-/blob/main/data/extraccion_creacion_datos_limpios.ipynb). Limpieza, transformación y carga de datos a S3.

+ [Notebooks](https://gitlab.com/datos-algoritmos-sociedad-itam/lima-buendia/-/tree/main/notebooks). Notebooks de trabajo durante el desarrollo del proyecto.

+ [Presentaciones](https://gitlab.com/datos-algoritmos-sociedad-itam/lima-buendia/-/tree/main/presentations). Notebooks de resultados que se utilizaron en dos sesiones diferentes:

  - [Presentación para conversación con expertas](https://gitlab.com/datos-algoritmos-sociedad-itam/lima-buendia/-/blob/main/presentations/2022_22_08_Presentacion_conversacion_expertas.ipynb)
  - [Reporte final](https://gitlab.com/datos-algoritmos-sociedad-itam/lima-buendia/-/blob/main/presentations/2022%2009%2001%20Reporte%20final.ipynb)


Dado que se utilizó la liberería plotly express, para poder visualizar las gráficas interactivas dentro del jupyter notebook, es necesario realizar la descarga del mismo y ejecutarlo. En cuanto al reporte en formato .html, también se debe descargar para la visualización y lectura.

--------


