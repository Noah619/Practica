from pymongo import MongoClient

# Conexión a MongoDB
client = MongoClient('mongodb://localhost:27017/')

db_name = "Noah"
collection_name = "localizaciones"

def insertar_localización(localización):
    client[db_name][collection_name].insert_one(localización)

def obtener_nombre_bases_de_datos():
    # Obtener una lista de todos los nombres de bases de datos
    all_dbs = client.list_database_names()

    # mostramos todas las bases de datos que hay
    print("Todos los nombres de bases de datos:")
    for db_name in all_dbs:
        print(db_name)

def mostrar_todos_ls_datos_base_de_datos():
    # mostramos los datos de una base de datos
    print("Mostramos los datos de una base de datos Noah-eda")
    db_pruebas = client[db_name][collection_name].find({})
    for x in db_pruebas:
        print(x)


def buscar_codigo_postal(codigo_postal):
    # mostramos los datos de una base de datos mediante el filtro
    print("Mostramos los datos especificos de una base de datos Noah-eda")
    db_pruebas = client[db_name][collection_name].find({"codigo_postal": codigo_postal})
    for x in db_pruebas:
        print(x)