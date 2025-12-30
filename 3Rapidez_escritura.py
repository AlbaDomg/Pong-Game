# PROGRAMA QUE MIDE LA RAPIDEZ DE ESCRITURA EN TECLADO

import tkinter as tk
import random
import time

# desarrollamos la GUI de nuestro programa
class TypingSpeedTester:
    def __init__(self, master):
        self.master = master
        master.title("Medidor de Velocidad de Escritura")
        master.geometry("700x400") # Ajusta el tamaño de la ventana
        master.resizable(False, False) # Evita que se pueda redimensionar la ventana

        self.phrases = [
            "El veloz murciélago hindú comía feliz cardillo y kiwi. La cigüeña tocaba el saxofón detrás del palenque de paja.",
            "La sabiduría de los antiguos se esconde entre las páginas polvorientas de libros olvidados.",
            "Cinco lobitos tiene la loba, cinco lobitos detrás de la escoba. Cinco lobitos, cinco nidos, cinco lobitos dormidos.",
            "El sol se oculta lentamente en el horizonte, tiñendo el cielo de tonos anaranjados y violetas.",
            "La tecnología avanza a pasos agigantados, transformando la forma en que vivimos y trabajamos cada día.",
            "Un pequeño paso para el hombre, un gran salto para la humanidad.",
            "La persistencia es el camino hacia el éxito, incluso en los desafíos más grandes.",
            "Cien años de soledad es una obra maestra de la literatura universal.",
            "La luna llena ilumina el sendero del bosque, creando sombras misteriosas y alargadas."
        ]
        self.current_phrase = ""
        self.start_time = None
        self.word_count = 0

        # --- Widgets ---
        self.label_instructions = tk.Label(master, text="Escribe la siguiente frase lo más rápido posible:", font=("Arial", 14))
        self.label_instructions.pack(pady=10)

        self.phrase_display = tk.Label(master, text="", wraplength=600, justify="center", font=("Arial", 16, "bold"), fg="blue")
        self.phrase_display.pack(pady=10)

        self.text_input = tk.Text(master, height=5, width=70, font=("Arial", 14))
        self.text_input.pack(pady=10)
        self.text_input.bind("<KeyRelease>", self.check_input) # Monitorea cada vez que se suelta una tecla

        self.start_button = tk.Button(master, text="Empezar / Nueva Frase", command=self.start_test, font=("Arial", 12))
        self.start_button.pack(pady=10)

        self.result_label = tk.Label(master, text="Tiempo: -- segundos | CPM: -- | PPM: --", font=("Arial", 14), fg="green")
        self.result_label.pack(pady=10)

        # Inicializa una frase al iniciar
        self.start_test()

    def start_test(self):
        """Prepara el test seleccionando una nueva frase y reseteando los contadores."""
        self.current_phrase = random.choice(self.phrases)
        self.phrase_display.config(text=self.current_phrase)
        self.text_input.delete("1.0", tk.END) # Borra el contenido del área de texto
        self.text_input.config(state=tk.NORMAL) # Habilita la edición
        self.result_label.config(text="Tiempo: -- segundos | CPM: -- | PPM: --")
        self.start_time = None # Resetea el tiempo de inicio
        self.word_count = len(self.current_phrase.split()) # Cuenta palabras de la frase objetivo

    def check_input(self, event=None):
        """Verifica el texto introducido por el usuario."""
        if self.start_time is None:
            self.start_time = time.time() # Inicia el temporizador la primera vez que se escribe

        typed_text = self.text_input.get("1.0", "end-1c") # Obtiene el texto sin el salto de línea final

        # Compara el texto escrito con la frase original
        # Resalta las letras correctas e incorrectas
        display_text = ""
        for i, char in enumerate(self.current_phrase):
            if i < len(typed_text):
                if typed_text[i] == char:
                    pass
                else:
                    # Si hay un error, podemos cambiar el color del texto de la entrada para indicar
                    self.text_input.tag_add("incorrect", f"1.{i}", f"1.{i+1}")
                    self.text_input.tag_config("incorrect", foreground="red")
            else:
                pass # El resto de la frase aún no se ha escrito, así que no se ejecuta lo anterior

        # Si el texto escrito es exactamente igual a la frase
        if typed_text == self.current_phrase:
            self.end_test()

    def end_test(self):
        """Calcula y muestra los resultados del test."""
        end_time = time.time()
        elapsed_time = round(end_time - self.start_time, 2) # Tiempo en segundos

        characters_typed = len(self.current_phrase)
        words_typed = self.word_count # Usamos el conteo de palabras de la frase objetivo

        # Calcular CPM (Caracteres Por Minuto)
        # Asegurarse de que elapsed_time no sea cero para evitar división por cero
        cpm = round((characters_typed / elapsed_time) * 60) if elapsed_time > 0 else 0

        # Calcular PPM (Palabras Por Minuto)
        ppm = round((words_typed / elapsed_time) * 60) if elapsed_time > 0 else 0

        # Mostrar los resultados de todo el proceso
        self.result_label.config(text=f"Tiempo: {elapsed_time} segundos | CPM: {cpm} | PPM: {ppm}")
        self.text_input.config(state=tk.DISABLED) # Deshabilita la edición después de terminar

# --- Ejemplo de uso ---
if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTester(root)
    root.mainloop()