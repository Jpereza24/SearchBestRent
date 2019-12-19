# SearchBestRent

El objetivo principal de este proyecto es que un usuario pueda localizar los pisos disponibles para alquilar en Madrid. Además, tiene otra función para predecir cuánto puede costar poner una vivienda en alquiler en Madrid (esto todavía está en proceso de desarrollo). 

Para ello he creado una API que pueda devolver los resultados que busca el usuario.

Para crear la base de datos tuve que pedir acceso a la API del Idealista, de dónde pude sacar un tercio de los pisos de la base de datos. Sin embargo, la principal fuente de datos con la que he alimentado mi base de datos es la página web de pisos.com mediante un web scrapping. La base está cargada en mi cuenta de Mongo Atlas.

La estructura de archivos de mi proyecto es la siguiente:

- src: Dónde tengo guardada la función con la que conecto a Mongo Atlas para devolver los resultados que busca el usuario.

- Static: Aquí esta guardado el diseño de la interfaz de la API.

- Templates: Aquí esta guardada la estructura html de la interfaz.

- Dockerfile: Lo he hecho con la intención de subir la API a Heroku pero no me ha sido posible al final, lo intentaré de nuevo en el futuro.

- main: Este es el archivo de Python principal para la API, dónde están las funciones que devuelven resultados al usuario. Las dos funciones principales son las siguientes:
    
    - map_price_rooms: El usuario introduce en la API el número de habitaciones y precio máximo que está dispuesto a pagar por el alquiler y la API le devuelve un mapa con la geolocalización de las viviendas que cumplan dichos parámetros.

    - prediction: Esta función está pensada para aquellos usuarios que tengan una vivienda vacía y estén pensando ponerla en alquiler. Funciona de la siguiente manera:
        
        - El usuario introduce el distrito en el que está la vivienda, el tipo de vivienda, los metros cuadrados que tiene y el número de habitaciones y la API le devuelve una predicción de a cuánto podría poner el alquiler.

        - Es importante resaltar que las predicciones todavía no son muy ajustadas, ya que el modelo que he elegido no tiene mucha precisión, es el que mejor tiene de los que he probado, pero tengo que buscar nuevos modelos que puedan sacar mayor partido de los datos que tengo.