import relaciones as rel
import bd
import os

relaciones = rel.getRelaciones()

path = os.path.dirname(os.path.abspath(__file__))

carpetas = os.listdir(path)
carpetas = [c for c in carpetas if c.startswith('CATALOGOS')]

bd.createDatabase()
bd.createRootTable()

for carpeta in carpetas:
    print("\033[93mCrando tablas para:\033[00m " + carpeta)
    
    bd.createTables(os.path.join(path, carpeta))
    bd.insertData(os.path.join(path, carpeta))
    
defunciones = os.listdir(os.path.join(path, 'DEFUNCIONES'))

for dir in defunciones:
    bd.createDefunciones(os.path.join(os.path.join(path, 'DEFUNCIONES'), dir))
    bd.insertDefuncionesData(os.path.join(os.path.join(path, 'DEFUNCIONES'), dir))

