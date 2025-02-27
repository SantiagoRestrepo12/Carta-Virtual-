import tkinter as tk
from PIL import Image, ImageTk
import webbrowser
import os

class CartaVirtual:
    def __init__(self, root):
        self.root = root
        self.root.title("Carta Virtual Sushisom")
        self.root.geometry("500x600")
        self.background_frame = tk.Canvas(self.root, width=500, height=600)
        self.background_frame.pack(fill="both", expand=True)

        # Crear degradado suave
        self.background_frame.create_rectangle(0, 0, 500, 600, outline="", fill="#f8f5f2")
        self.background_frame.create_rectangle(0, 300, 500, 600, outline="", fill="#f4a261")

        # Cargar y mostrar el logo usando la imagen 
        self.cargar_imagen_multiple("Sushisom", self.background_frame, (200, 150))

        # Título
        titulo = tk.Label(self.background_frame, text="Bienvenido a Sushisom", font=("Helvetica", 24, "bold"), bg="#f0f0f0", fg="#333")
        titulo.pack(pady=10)

        # Botones de Menú Principal
        self.menu_btn = tk.Button(self.background_frame, relief="raised", bd=3, cursor="hand2", text="Menú", command=self.mostrar_menu, width=20, height=2, bg="#bc6c25", activebackground="#dda15e", fg="#2b2d42", font=("Georgia", 14, "bold"))
        self.menu_btn.pack(pady=10)

        self.reservas_btn = tk.Button(self.background_frame, relief="raised", bd=3, cursor="hand2", text="Reservaciones", command=self.reservaciones, width=20, height=2, bg="#bc6c25", activebackground="#dda15e", fg="#2b2d42", font=("Georgia", 14, "bold"))
        self.reservas_btn.pack(pady=10)

        self.ubicaciones_btn = tk.Button(self.background_frame, relief="raised", bd=3, cursor="hand2", text="Ubicaciones", command=self.mostrar_ubicaciones, width=20, height=2, bg="#bc6c25", activebackground="#dda15e", fg="#2b2d42", font=("Georgia", 14, "bold"))
        self.ubicaciones_btn.pack(pady=10)

    # Método para buscar tanto .png como .jpg
    def cargar_imagen_multiple(self, nombre_base, parent, tamaño):
        extensiones = [".png", ".jpg", ".jpeg"]  # Soporta PNG y JPG
        ruta = None

        # Verificar ambas extensiones
        for ext in extensiones:
            posible_ruta = f"imagenes/{nombre_base}{ext}"
            if os.path.exists(posible_ruta):
                ruta = posible_ruta
                break

        
        if ruta is None:
            ruta = "imagenes/Sushisom.jpg"

        # Cargar y mostrar la imagen
        img = Image.open(ruta)
        img = img.resize(tamaño, Image.Resampling.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)
        img_label = tk.Label(parent, image=img_tk, bg="#f8f5f2")
        img_label.image = img_tk
        img_label.pack(pady=5)

    def mostrar_items(self, titulo, items):
        ventana = tk.Toplevel(self.root)
        ventana.title(titulo)
        ventana.geometry("350x600")
        ventana.config(bg="#f8f5f2")

        titulo_label = tk.Label(ventana, text=titulo, font=("Georgia", 22, "bold"), bg="#f8f5f2", fg="#333")
        titulo_label.pack(pady=10)

        for item, nombre_base in items:
            self.cargar_imagen_multiple(nombre_base, ventana, (150, 100))
            tk.Label(ventana, text=item, wraplength=300, justify="left", bg="#f8f5f2", fg="#555", font=("Helvetica", 12)).pack(anchor="w", padx=20, pady=5)

    def mostrar_entradas(self):
        entradas = [
            ("Edamame: Vainas de soja al vapor.", "edamame"),
            ("Takoyaki: Albóndigas de pulpo.", "takoyaki"),
            ("Ensalada Wakame: Algas con sésamo.", "wakame")
        ]
        self.mostrar_items("Entradas", entradas)

    def mostrar_platos_fuertes(self):
        platos_fuertes = [
    ("Sake Teppanyaki: Salmón a la plancha.", "sake_teppanyaki"),
    ("Yaki Tori: Pinchos de pollo teriyaki.", "yaki_tori"),
    ("Pollo al Curry con Coco.", "pollo_curry")
]
        self.mostrar_items("Platos Fuertes", platos_fuertes)

    def mostrar_bebidas(self):
        bebidas = [
    ("Cerveza Asahi.", "asahi"),
    ("Cerveza Sapporo.", "sapporo"),
    ("Agua.", "agua")
]
        self.mostrar_items("Bebidas", bebidas)

    def mostrar_postres(self):
        postres = [
    ("Bomba de Frutos Rojos.", "bomba_frutos_rojos"),
    ("Huevo de Chocolate Blanco.", "huevo_chocolate"),
    ("Cheesecake de Frutos Rojos.", "cheesecake")
]
        self.mostrar_items("Postres", postres)

    def mostrar_licores(self):
        licores = [
    ("Sake.", "sake"),
    ("Whisky Japonés.", "whisky_japones"),
    ("Licor de Ciruela.", "licor_ciruela")
]
        self.mostrar_items("Licores", licores)

    def mostrar_menu(self):
        menu_ventana = tk.Toplevel(self.root)
        menu_ventana.title("Menú")
        menu_ventana.geometry("350x500")
        menu_ventana.config(bg="#f8f5f2")

        titulo = tk.Label(menu_ventana, text="Menú de Sushisom", font=("Georgia", 22, "bold"), bg="#f8f5f2", fg="#444")
        titulo.pack(pady=10)

        tk.Button(menu_ventana, text="Entradas", command=self.mostrar_entradas, width=20, height=2, bg="#8d99ae", activebackground="#edf2f4", fg="#2b2d42", font=("Georgia", 12, "bold")).pack(pady=5)
        tk.Button(menu_ventana, text="Platos Fuertes", command=self.mostrar_platos_fuertes, width=20, height=2, bg="#8d99ae", activebackground="#edf2f4", fg="#2b2d42", font=("Georgia", 12, "bold")).pack(pady=5)
        tk.Button(menu_ventana, text="Bebidas", command=self.mostrar_bebidas, width=20, height=2, bg="#8d99ae", activebackground="#edf2f4", fg="#2b2d42", font=("Georgia", 12, "bold")).pack(pady=5)
        tk.Button(menu_ventana, text="Postres", command=self.mostrar_postres, width=20, height=2, bg="#8d99ae", activebackground="#edf2f4", fg="#2b2d42", font=("Georgia", 12, "bold")).pack(pady=5)
        tk.Button(menu_ventana, text="Licores", command=self.mostrar_licores, width=20, height=2, bg="#8d99ae", activebackground="#edf2f4", fg="#2b2d42", font=("Georgia", 12, "bold")).pack(pady=5)

    def reservaciones(self):
        webbrowser.open("https://wa.me/1234567890")

    def mostrar_ubicaciones(self):
        webbrowser.open("https://www.google.com/maps?q=restaurante+sushisom")

if __name__ == "__main__":
    root = tk.Tk()
    app = CartaVirtual(root)
    root.mainloop()
