import nltk
#nltk.download('punkt_tab')
from newspaper import Article
from gtts import gTTS
import os

def texto_a_voz(url, idioma='es', nombre_archivo='articulo.mp3'):
    try:
        #1. Extraemos el texto del articulo con Newspaper3k
        #print("Extrayendo el texto del articulo...")
        articulo=articulo(url, language=idioma)
        #articulo.download()
        #articulo.parse()

        #if not articulo.text:
         #   print("No se encontró texto en el articulo")
          #  return
        
        #2. Procesamos el texto con NLTK
        print("Procesando texto...")
        oraciones = nltk.sent_tokenize(articulo.text)
        texto_limpio = ' '.join(oraciones)

        #3. Convertimos a voz con gTTS
        print("Convirtiendo texto a voz...")
        tts= gTTS(text=texto_limpio, lang=idioma, slow=False)

        #4. Guardamos archivo de audio
        print(f"Guardando el archivo como '{nombre_archivo}'...")
        tts.save(nombre_archivo)
        print(f"¡Conversion completada! {nombre_archivo} está listo.")
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    url_ejemplo = "Hola, soy Alba y estoy estudiando programación"
#    url_ejemplo = "https://elpais.com/us/2025-08-18/el-huracan-erin-vuelve-a-intensificarse-y-alcanza-la-categoria-4-mientras-se-acerca-a-estados-unidos.html?autoplay=1"
    texto_a_voz(url_ejemplo)