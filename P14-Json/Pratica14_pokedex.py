import json
import requests
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from io import BytesIO

class GestorJson:
    def __init__(self, arch):
        self.arch = arch 
    def leerJson(self):
        try:
            with open(self.arch, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            return {}
    def escribirJson(self, datos):
        with open(self.arch, 'w') as f:
            json.dump(datos, f, indent=4)
    def obtenerPokemon(self, pokemon):       
        try:
            url = f"https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            self.escribirJson(data)
        except:
            messagebox.showerror("Error", "No se pudo obtener información del Pokémon")

def mostrarDatos():
    nombrePokemon = entradaNombre.get()
    if not nombrePokemon:
        messagebox.showwarning("Atención", "Ingresa un nombre de Pokémon")
        return
    
    gestor.obtenerPokemon(nombrePokemon)
    datos = gestor.leerJson()

    if datos:
        etiquetaNombre.config(text=f"Nombre: {datos['name']}")
        etiquetaId.config(text=f"Número Pokédex: {datos['id']}")
        etiquetaAltura.config(text=f"Altura: {datos['height']}")
        etiquetaPeso.config(text=f"Peso: {datos['weight']}")
        tipos = [t["type"]["name"] for t in datos["types"]]
        habilidades = [h["ability"]["name"] for h in datos["abilities"]]
        stats = [f"{s['stat']['name']}: {s['base_stat']}" for s in datos["stats"]]
        movimientos = [m["move"]["name"] for m in datos["moves"][:5]]

        etiquetaTipos.config(text=f"Tipos: {', '.join(tipos)}")
        etiquetaHabilidades.config(text=f"Habilidades: {', '.join(habilidades)}")
        etiquetaStats.config(text="Estadísticas:\n" + "\n".join(stats))
        etiquetaMovimientos.config(text="Movimientos:\n" + ", ".join(movimientos))

        urlImg = datos["sprites"]["front_default"]
        if urlImg:
            imagen = requests.get(urlImg)
            img = Image.open(BytesIO(imagen.content))
            img = img.resize((200, 200))
            imgTk = ImageTk.PhotoImage(img)
            etiquetaImagen.config(image=imgTk)
            etiquetaImagen.image = imgTk
        else:
            etiquetaImagen.config(image='', text="Sin imagen")
    else:
        messagebox.showerror("Error", "No se encontró información del Pokémon")

gestor = GestorJson("pokemon.json")

ventana = tk.Tk()
ventana.title("Pokédex")
ventana.geometry("400x600")

entradaNombre = tk.Entry(ventana, font=("Arial", 14))
entradaNombre.pack(pady=10)

botonBuscar = tk.Button(ventana, text="Buscar Pokémon", command=mostrarDatos)
botonBuscar.pack()

etiquetaImagen = tk.Label(ventana)
etiquetaImagen.pack(pady=0)

etiquetaNombre = tk.Label(ventana, text="", font=("Arial", 12))
etiquetaNombre.pack()
etiquetaId = tk.Label(ventana, text="", font=("Arial", 12))
etiquetaId.pack()
etiquetaAltura = tk.Label(ventana, text="", font=("Arial", 12))
etiquetaAltura.pack()
etiquetaPeso = tk.Label(ventana, text="", font=("Arial", 12))
etiquetaPeso.pack()
etiquetaTipos = tk.Label(ventana, text="", font=("Arial", 12))
etiquetaTipos.pack()
etiquetaHabilidades = tk.Label(ventana, text="", font=("Arial", 12))
etiquetaHabilidades.pack()
etiquetaStats = tk.Label(ventana, text="", font=("Arial", 12), justify="left")
etiquetaStats.pack()
etiquetaMovimientos = tk.Label(ventana, text="", font=("Arial", 12), justify="left", wraplength=300)
etiquetaMovimientos.pack()

ventana.mainloop()
