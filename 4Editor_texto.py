# CREAR UN EDITOR DE TEXTO SENCILLO

import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox

# Creación de la interfaz (GUI) para el editor de texto y sus funciones
class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor de Texto Sencillo")
        self.root.geometry("800x600")

        # Crear el menú
        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)

        # Menú Archivo
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Archivo", menu=self.file_menu)
        self.file_menu.add_command(label="Nuevo", command=self.new_file)
        self.file_menu.add_command(label="Abrir", command=self.open_file)
        self.file_menu.add_command(label="Guardar", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Salir", command=self.root.quit)

        # Menú Editar
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Editar", menu=self.edit_menu)
        self.edit_menu.add_command(label="Deshacer", command=self.undo, accelerator="Ctrl+Z")
        self.edit_menu.add_command(label="Rehacer", command=self.redo, accelerator="Ctrl+Y")
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cortar", command=self.cut)
        self.edit_menu.add_command(label="Copiar", command=self.copy)
        self.edit_menu.add_command(label="Pegar", command=self.paste)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Buscar y Reemplazar", command=self.find_and_replace)

        # Área de texto desplazable
        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, undo=True, font=("Helvetica", 12))
        self.text_area.pack(expand=True, fill="both", padx=10, pady=10)

        # Incorporar atajos de teclado para las funciones de hacer y deshacer
        self.text_area.bind("<Control-z>", lambda event: self.undo())
        self.text_area.bind("<Control-y>", lambda event: self.redo())

        # Estado del archivo
        self.current_file = None

    # Dar lugar a un nuevo archivo en blanco editable
    def new_file(self):
        self.text_area.delete("1.0", tk.END)
        self.root.title("Nuevo archivo - Editor de Texto Sencillo")
        self.current_file = None

    # Abrir un archivo de texto 
    def open_file(self):
        file_path = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
        )
        if file_path:
            self.current_file = file_path
            self.root.title(f"{file_path} - Editor de Texto Sencillo")
            self.text_area.delete("1.0", tk.END)   #Limpia el area de texto para que no quede ningun contenido anterior
            with open(file_path, "r", encoding="utf-8") as file:
                self.text_area.insert(tk.END, file.read())

    # Desplegar ventana para guardar archivo de texto
    def save_file(self):
        if self.current_file:
            self._save_to_path(self.current_file)
        else:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
            )
            if file_path:
                self.current_file = file_path
                self._save_to_path(file_path)

    # Guardar el contenido del archivo guardado
    def _save_to_path(self, file_path):
        try:
            content = self.text_area.get("1.0", tk.END)
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(content)
            self.root.title(f"{file_path} - Editor de Texto Sencillo")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")

    # Implementar funciones de cortar, copiar, pegar, deshacer y rehacer
    def cut(self):
        self.text_area.event_generate("<<Cut>>")

    def copy(self):
        self.text_area.event_generate("<<Copy>>")

    def paste(self):
        self.text_area.event_generate("<<Paste>>")

    def undo(self):
        self.text_area.edit_undo()

    def redo(self):
        self.text_area.edit_redo()

    def find_and_replace(self):
        # Crear una ventana de búsqueda
        search_window = tk.Toplevel(self.root)
        search_window.title("Buscar y Reemplazar")
        search_window.geometry("300x150")

        # Widgets
        tk.Label(search_window, text="Buscar:").pack(padx=5, pady=5)
        search_entry = tk.Entry(search_window)
        search_entry.pack(padx=5, pady=5)
        
        tk.Label(search_window, text="Reemplazar con:").pack(padx=5, pady=5)
        replace_entry = tk.Entry(search_window)
        replace_entry.pack(padx=5, pady=5)

        # Realizar una busqueda en el archivo de texto
        def find_text():
            search_term = search_entry.get()
            if search_term:
                start_pos = self.text_area.search(search_term, "1.0", stopindex=tk.END)
                if start_pos:
                    self.text_area.tag_remove("found", "1.0", tk.END)
                    while start_pos:
                        end_pos = f"{start_pos}+{len(search_term)}c"
                        self.text_area.tag_add("found", start_pos, end_pos)
                        start_pos = self.text_area.search(search_term, end_pos, stopindex=tk.END)
                    self.text_area.tag_config("found", background="yellow")
                    messagebox.showinfo("Búsqueda", "Se encontraron todas las coincidencias.")
                else:
                    messagebox.showinfo("Búsqueda", "No se encontraron coincidencias.")
            else:
                messagebox.showerror("Error", "El campo de búsqueda no puede estar vacío.")

        # Realizar un reemplazo de texto en el contenido del archivo
        def replace_text():
            search_term = search_entry.get()
            replace_term = replace_entry.get()
            if search_term:
                start_pos = self.text_area.search(search_term, "1.0", stopindex=tk.END)
                if start_pos:
                    while start_pos:
                        end_pos = f"{start_pos}+{len(search_term)}c"
                        self.text_area.delete(start_pos, end_pos)
                        self.text_area.insert(start_pos, replace_term)
                        start_pos = self.text_area.search(search_term, end_pos, stopindex=tk.END)
                    messagebox.showinfo("Reemplazo", "Reemplazo completado.")
                else:
                    messagebox.showinfo("Reemplazo", "No se encontraron coincidencias para reemplazar.")
            else:
                messagebox.showerror("Error", "El campo de búsqueda no puede estar vacío.")

        # Implementar los botones de "Buscar" y "Reemplazar"
        tk.Button(search_window, text="Buscar", command=find_text).pack(side="left", padx=5, pady=5)
        tk.Button(search_window, text="Reemplazar", command=replace_text).pack(side="right", padx=5, pady=5)

# Ejemplo de uso
if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()