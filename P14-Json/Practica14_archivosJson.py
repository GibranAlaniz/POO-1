import json
import requests

class GestorJson:
    def __init__(self, arch):
        self.arch = arch 
    def leerJson(self):
        try:
            with open(self.arch, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print("Archivo no existe")
            return {}
        except json.JSONDecodeError:
            print("El archivo no es JSON")
            return {}
    def escribirJson(self, datos):
        with open(self.arch, 'w') as f:
            json.dump(datos, f, indent=4)
    def modificarJson(self, llave, valor):
        datos = self.leerJson()
        datos[llave] = valor
        self.escribirJson(datos)
    def obtenerPokemon(self, pokemon):       
        try:
            url = f"https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            self.escribirJson(data)
        except requests.exceptions.HTTPError:
            print("El enlace no existe")
        except requests.exceptions.RequestException:
            print("No se pudo realizar la petición")

pokemon = input("Que pokemon quieres saber su informacion?")

gJson = GestorJson("pokemon.json")
gJson.obtenerPokemon(pokemon)
pokemonInfo = gJson.leerJson()

if pokemonInfo:
    print("Numero de pokedex;", pokemonInfo["id"])
    print("Nombre:", pokemonInfo["name"])
    print("Altura:", pokemonInfo["height"])
    print("Peso:", pokemonInfo["weight"])
    print("Tipos:", [t["type"]["name"] for t in pokemonInfo["types"]])
    
 
    habilidades = [habilidad["ability"]["name"] for habilidad in pokemonInfo["abilities"]]
    print("Habilidades:", habilidades)

    print("Estadísticas:")
    for stat in pokemonInfo["stats"]:
        print(f"{stat['stat']['name'].capitalize()}: {stat['base_stat']}")

    movimientos = [movimiento["move"]["name"] for movimiento in pokemonInfo["moves"][:5]]  # Limitado a 5 movimientos
    print("Movimientos (5 primeros):", movimientos)