# Proyecto-ETL

En este proyecto teníamos la intención de hacer una base de datos de libros de filosofía. En este caso, y con vistas a aumentarlo en el futuro, hemos reducido los datos a 3 columnas, autor, título y el top 10 palabras utilizadas por libro, con la intención de extraer algo de información del libro. Como es lógico, hemos tenido que hacer unas listas con palabras que aparecen mucho, preposiciones, enlaces y cuantificadores, pero que no aportan información. Estas listas no pueden ser tan exahustivas como nos gustaría, pero en muchos casos es suficiente. 

Queríamos centrarnos en la extracción y transformación de los datos, siendo la base de datos, hecha en Mongo, relativamente sencilla. 
Hemos escrapeado datos de Project Gutenberg, hemos realizado el OCR de unos pdfs que no lo tenía y hemos cogido textos de la página del proyecto de Filosofía en Español. 

Página del proyecto de Filosofía en Español : https://www.filosofia.org/
Página del proyecto Gutenberg : https://www.gutenberg.org/

# Problemas


Una serie de complicaciones obvias para tener en cuenta es la heterogeneidad de los datos a recoger, a la hora de hacer la lista de palabras que no entraban en el top 10, precisamente por no aportar información, hemos decidido pecar de cautos, así, palabras como yo o ser las hemos mantenido, por ejemplo. 

Igualmente un problema ha sido la realización de los OCRs, la cual requiere de ciertos condiciones para ser ideal, hemos hecho un trabajo pasable pero no excelente. 

También hemos tenido que tener en cuenta las limitaciones de hardware, en primer lugar teníamos pensado extraer todos los datos y trabajar con ellos en local. Como es lógico manejar los caracteres de un 800 libros era demasiado, nos hemos decantado por cribar por los 10 caracteres que más aparecen en cada texto en el momento de la extracción. 

Finalmente, otra cosa a tener en cuenta es que el análisis realizado, las 10 palabras que más aparecen por texto, es una forma de análisis un tanto pobre, muy susceptible a sesgarse en los textos pequeños y que no necesariamente aporta información cualitativa del mismo. Para realizar un trabajo más adecuado habría que recurrir a técnicas de machine learning, pero dentro del tiempo disponible nos ha parecido suficiente. 




A continuación algunas funciones interesantes que nos han servido para limpiar y extraer junto a su explicación.

# Función don_limpio(urls)

La función don_limpio() recibe una lista de URLs como argumento y devuelve una lista de tuplas que contienen el cuerpo de texto y el título de una obra literaria, extraídos de las páginas web correspondientes a las URLs.
Parámetros

    urls: una lista de cadenas que contienen las URLs de las páginas web a analizar.

Valor de retorno

    resultados: una lista de tuplas que contienen el cuerpo de texto y el título de una obra literaria. Cada tupla tiene la siguiente estructura:

        cuerpo: una lista de cadenas que representan el cuerpo de texto de la obra.

        obra: una cadena que representa el título de la obra.

Funcionamiento

La función realiza las siguientes operaciones para cada URL en la lista de entrada:

    Envía una solicitud HTTP GET a la URL correspondiente para obtener la página web.
    Parsea el contenido de la página utilizando la biblioteca BeautifulSoup de Python.
    Extrae todos los párrafos de texto de la página web y los almacena en una lista.
    Encuentra la posición del separador "———", que indica el final de la información de la obra en la página web.
    Extrae el cuerpo de texto de la obra, eliminando los corchetes y llaves que puedan estar presentes en el texto.
    Extrae el título de la obra, que se encuentra en la segunda posición de la lista de párrafos extraídos.
    Almacena el cuerpo de texto y el título de la obra en una tupla y la agrega a la lista de resultados.
    Retorna la lista de resultados cuando ha terminado de procesar todas las URLs de entrada.




# Extracción de texto de archivos PDF mediante OCR

Este fragmento de código utiliza la biblioteca pdf2image y la herramienta OCR pytesseract para extraer texto de un archivo PDF.
Funcionamiento

    La función convert_from_path() de la biblioteca pdf2image convierte todas las páginas del archivo PDF en una lista de objetos PIL.Image.Image.
    A continuación, se itera por cada página de la lista y se procesa individualmente:
        Se convierte la imagen de la página a escala de grises utilizando el método convert() de PIL.Image.Image.
        Se utiliza la función image_to_string() de pytesseract para extraer el texto de la imagen en escala de grises.
        El texto extraído se almacena en la variable gb.
        Se imprime el texto extraído en la consola junto con su longitud utilizando la función print().

Parámetros

    Una cadena que contiene la ruta del archivo PDF que se desea procesar.
    Una cadena que contiene la ruta del archivo ejecutable de Poppler, que es necesario para que pdf2image funcione correctamente.

Variables

    gb: una variable que almacena el texto extraído de las páginas del archivo PDF mediante OCR.


# La función top10 

Toma un texto y devuelve un diccionario que contiene las 10 palabras más comunes en el texto, excluyendo las palabras comunes predefinidas que se proporcionan en la lista common_words.

La función tiene un argumento opcional n que especifica el número de palabras que se deben incluir en el diccionario resultante. De forma predeterminada, n es 10.

Si no se proporciona una lista personalizada de palabras comunes, la función utiliza una lista predefinida que contiene las palabras más comunes en inglés. La función utiliza expresiones regulares para encontrar todas las palabras en el texto y luego cuenta la frecuencia de cada palabra. Las palabras comunes especificadas en la lista common_words se eliminan de la cuenta de palabras.

El resultado final es un diccionario que contiene las n palabras más comunes y su frecuencia en el texto.



# Conclusiones

En conclusión, este proyecto de ETL se centró en la extracción y transformación de datos para la creación de una base de datos de libros de filosofía. Se han utilizado varias fuentes, incluyendo Project Gutenberg y la página del proyecto de Filosofía en Español, y se han extraído tres columnas para cada libro: autor, título y las 10 palabras más utilizadas en el texto. Se han tenido en cuenta las limitaciones de hardware y las complicaciones inherentes a la realización de OCRs y la heterogeneidad de los datos recogidos. Además, se han proporcionado dos funciones útiles para la limpieza y extracción de texto de las páginas web y archivos PDF. Aunque el análisis de las 10 palabras más utilizadas por libro es un análisis limitado, dentro del tiempo disponible se considera suficiente para los objetivos del proyecto. En el futuro, se podrían utilizar técnicas de machine learning para un análisis más profundo.