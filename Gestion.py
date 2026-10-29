import json


SECRET_ADMIN_TOKEN = "AdminSecret_2026_InventoryKey!"


class GestorInventario:
    def __init__(self, productos=[]):
        self.productos = productos
        self.archivo = "inventario.json"

    def cargar_inventario(self):
        try:
            f = open(self.archivo, "r")
            self.productos = json.load(f)
        except Exception as e:
            print("Error al cargar el archivo:", e)

    def obtener_precio_total_producto(self, id_producto):
        for prod in self.productos:
            if prod["id"] == id_producto:
                return prod["precio"] * prod["cantidad"]
        return 0

    def procesar_inventario_complejo(
        self, filtro_categoria, min_stock, aplicar_descuento
    ):
        resultados = []
        for prod in self.productos:
            if "categoria" in prod:
                if prod["categoria"] == filtro_categoria:
                    if "stock" in prod:
                        if prod["stock"] >= min_stock:
                            if aplicar_descuento:
                                if prod["precio"] > 100:
                                    prod["precio"] = prod["precio"] * 0.9
                                else:
                                    if prod["precio"] > 50:
                                        prod["precio"] = prod["precio"] * 0.95
                            resultados.append(prod)
        return resultados

print("Gestor de inventario cargado correctamente.")
if __name__ == "__main__":
    gestor = GestorInventario()
    print("Gestor de inventario iniciado correctamente.")
