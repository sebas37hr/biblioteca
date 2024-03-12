import tkinter as tk
from tkinter import messagebox, simpledialog

class BibliotecaApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Gestión de Biblioteca")
        
        self.label = tk.Label(master, text="Seleccione una función:")
        self.label.pack()

        self.add_button = tk.Button(master, text="Agregar libro", command=self.agregar_libro)
        self.add_button.pack()

        self.search_button = tk.Button(master, text="Buscar libro", command=self.buscar_libro)
        self.search_button.pack()

        self.update_button = tk.Button(master, text="Actualizar libro", command=self.actualizar_libro)
        self.update_button.pack()

        self.delete_button = tk.Button(master, text="Eliminar libro", command=self.eliminar_libro)
        self.delete_button.pack()

        # Base de datos de libros
        self.libros = []

    def agregar_libro(self):
        self.add_window = tk.Toplevel(self.master)
        self.add_window.title("Agregar Libro")

        # Campos requeridos
        self.titulo_label = tk.Label(self.add_window, text="Título:")
        self.titulo_label.pack()
        self.titulo_entry = tk.Entry(self.add_window)
        self.titulo_entry.pack()

        self.anio_label = tk.Label(self.add_window, text="Año de edición:")
        self.anio_label.pack()
        self.anio_entry = tk.Entry(self.add_window)
        self.anio_entry.pack()

        self.editorial_label = tk.Label(self.add_window, text="Editorial:")
        self.editorial_label.pack()
        self.editorial_entry = tk.Entry(self.add_window)
        self.editorial_entry.pack()

        self.autor_label = tk.Label(self.add_window, text="Autor:")
        self.autor_label.pack()
        self.autor_entry = tk.Entry(self.add_window)
        self.autor_entry.pack()

        self.versiones_label = tk.Label(self.add_window, text="Versiones:")
        self.versiones_label.pack()
        self.versiones_entry = tk.Entry(self.add_window)
        self.versiones_entry.pack()

        self.disponibilidad_label = tk.Label(self.add_window, text="Disponibilidad (si/no):")
        self.disponibilidad_label.pack()
        self.disponibilidad_entry = tk.Entry(self.add_window)
        self.disponibilidad_entry.pack()

        self.guardar_button = tk.Button(self.add_window, text="Guardar", command=self.guardar_libro)
        self.guardar_button.pack()

    def guardar_libro(self):
        # Guardar libro en la base de datos
        titulo = self.titulo_entry.get()
        anio = self.anio_entry.get()
        editorial = self.editorial_entry.get()
        autor = self.autor_entry.get()
        versiones = self.versiones_entry.get()
        disponibilidad = self.disponibilidad_entry.get()

        libro = {
            "Titulo": titulo,
            "Año de edición": anio,
            "Editorial": editorial,
            "Autor": autor,
            "Versiones": versiones,
            "Disponibilidad": disponibilidad
        }
        self.libros.append(libro)

        messagebox.showinfo("Éxito", "Libro agregado correctamente.")
        self.add_window.destroy()

    def buscar_libro(self):
        titulo = tk.simpledialog.askstring("Buscar libro", "Ingrese el título del libro:")
        if titulo:
            for libro in self.libros:
                if libro["Titulo"].lower() == titulo.lower():
                    messagebox.showinfo("Resultado de la búsqueda", f"Libro encontrado:\n{libro}")
                    return
            messagebox.showinfo("Resultado de la búsqueda", "Libro no encontrado.")

    def actualizar_libro(self):
        titulo = tk.simpledialog.askstring("Actualizar libro", "Ingrese el título del libro a actualizar:")
        if titulo:
            for libro in self.libros:
                if libro["Titulo"].lower() == titulo.lower():
                    # Crear ventana para actualizar libro
                    self.update_window = tk.Toplevel(self.master)
                    self.update_window.title("Actualizar Libro")

                    self.editorial_label = tk.Label(self.update_window, text="Nueva editorial:")
                    self.editorial_label.pack()
                    self.editorial_entry = tk.Entry(self.update_window)
                    self.editorial_entry.pack()

                    self.versiones_label = tk.Label(self.update_window, text="Nuevas versiones:")
                    self.versiones_label.pack()
                    self.versiones_entry = tk.Entry(self.update_window)
                    self.versiones_entry.pack()

                    self.disponibilidad_label = tk.Label(self.update_window, text="Disponibilidad actualizada (si/no):")
                    self.disponibilidad_label.pack()
                    self.disponibilidad_entry = tk.Entry(self.update_window)
                    self.disponibilidad_entry.pack()

                    self.guardar_button = tk.Button(self.update_window, text="Guardar", command=lambda: self.guardar_actualizacion(libro))
                    self.guardar_button.pack()
                    return
            messagebox.showinfo("Error", "Libro no encontrado.")

    def guardar_actualizacion(self, libro):
        nueva_editorial = self.editorial_entry.get()
        nuevas_versiones = self.versiones_entry.get()
        nueva_disponibilidad = self.disponibilidad_entry.get()

        # Actualizar los campos del libro
        libro["Editorial"] = nueva_editorial
        libro["Versiones"] = nuevas_versiones
        libro["Disponibilidad"] = nueva_disponibilidad

        messagebox.showinfo("Éxito", "Libro actualizado correctamente.")
        self.update_window.destroy()

    def eliminar_libro(self):
        titulo = tk.simpledialog.askstring("Eliminar libro", "Ingrese el título del libro a eliminar:")
        if titulo:
            for libro in self.libros:
                if libro["Titulo"].lower() == titulo.lower():
                    self.libros.remove(libro)
                    messagebox.showinfo("Éxito", "Libro eliminado correctamente.")
                    return
            messagebox.showinfo("Error", "Libro no encontrado.")

def main():
    root = tk.Tk()
    app = BibliotecaApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()