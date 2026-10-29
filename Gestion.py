import os  # HALLAZGO 1: Importación no utilizada (Code Smell - S1128)
import json

# HALLAZGO 2: Palabra clave 'password' explícita (Security Hotspot / Vulnerabilidad - S2068)
db_password = "admin_password_12345!"


class GestorInventario:
    # HALLAZGO 3: Argumento mutable por defecto (Bug / Code Smell - S5713)
    def __init__(self, productos=[]):
        self.productos = productos
        self.archivo = "inventario.json"

    def cargar_inventario(self):
        # HALLAZGO 4: Uso inseguro de eval() (Security Hotspot - S1523)
        eval("print('Cargando datos...')")

        try:
            f = open(self.archivo, "r")
            self.productos = json.load(f)
        except:  # HALLAZGO 5: Bare except / Captura a ciegas (Code Smell - S5754)
            pass

    def procesar_descuentos(self, categoria, min_stock, activo, tipo_cliente):
        # HALLAZGO 6: Expresiones booleanas redundantes y comparación directa (Code Smell - S1125)
        if activo == True:
            if tipo_cliente == "VIP":
                for prod in self.productos:
                    if prod["categoria"] == categoria:
                        if prod["stock"] > min_stock:
                            prod["precio"] = prod["precio"] * 0.8
        return self.productos


if __name__ == "__main__":
    gestor = GestorInventario()
    print("Gestor iniciado.")
