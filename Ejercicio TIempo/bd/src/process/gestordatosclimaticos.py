# Clase GestorDeDatosClimaticos para manejar el flujo de datos y presentación
import json
from basededatos import almacenaiento_bd
from beans.localizador import Localizador


class GestorDeDatosClimaticos:
    ubicaciones = []
    def __init__(self):
        print("Iniciando gestor de datos climaticos")
        print(f"Numero de ubicaciones actuales: {self.get_numero_ubicaciones()}")

    def get_numero_ubicaciones(self):
        return len(self.ubicaciones)

    def mostrar_codigos_postales_y_provincias_almacenadas(self):
        provincias_codigos_postales = {}
        for ubicacion in self.ubicaciones:
            if ubicacion.provincia in provincias_codigos_postales:
                provincias_codigos_postales[ubicacion.provincia].append(ubicacion.codigo_postal)
            else:
                provincias_codigos_postales[ubicacion.provincia] = [ubicacion.codigo_postal]

        if provincias_codigos_postales:
            print(json.dumps(provincias_codigos_postales, indent=2, ensure_ascii=False))
        else:
            print("No hay ubicaciones almacenadas")

    # metodos necesarios
    def insertar_nueva_ubicacion(self,latitud, longitud):
        ubicacion_encontrada = False
        for ubicación in self.ubicaciones:
            if ubicación.check_lat_lng(latitud, longitud):
                ubicacion_encontrada = True
                print("================================================")
                print("Ubicación ya existe")
                print(ubicación.mostrar_informacion())
                print("================================================")
                break
        
        if not ubicacion_encontrada:
            p = (latitud, longitud)
            almacenaiento_bd.insertar_localización(p.to_dict())
            print("Ubicación agregada correctamente")
        else:
            print("Ubicación ya existe")
        return ubicacion_encontrada

    def buscar_por_codigo_postal(self,codigo_postal):
        ubicacion_encontrada = None
        for ubicacion in self.ubicaciones:
            if ubicacion.codigo_postal == codigo_postal:
                ubicacion_encontrada = ubicacion
                break
        return ubicacion_encontrada
    
    def buscar_por_provincia(self,provincia):
        lista_ubicaciones = []
        for ubicacion in self.ubicaciones:
            if ubicacion.provincia == provincia:
                lista_ubicaciones.append(ubicacion)
        return lista_ubicaciones
    
