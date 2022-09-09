import pandas
import os
import sqlalchemy
import pymysql
import relaciones as rel 

def createDatabase():
    engine = sqlalchemy.create_engine('mysql+pymysql://root:root@localhost:3306')
    sql = "CREATE DATABASE IF NOT EXISTS Defunciones"
    engine.execute(sql)

def createRootTable():
    engine = sqlalchemy.create_engine('mysql+pymysql://root:root@localhost:3306/Defunciones')
    
    try:
        sql = """
        CREATE TABLE IF NOT EXISTS `root` (
        `id` INT NOT NULL AUTO_INCREMENT,
        `tabla` VARCHAR(255),
        PRIMARY KEY (`id`)
        );"""

        engine.execute(sql)
        print("root table created")

    except Exception as e:
        print("Error al crear la tabla root")
        print(e)

def insertRootData(tabla):
    engine = sqlalchemy.create_engine('mysql+pymysql://root:root@localhost:3306/Defunciones')
    sql = "INSERT INTO root (tabla) VALUES (%s)"
    engine.execute(sql, tabla)

def dropDatabase():
    engine = sqlalchemy.create_engine('mysql+pymysql://root:root@localhost:3306')
    sql = "DROP DATABASE IF EXISTS Defunciones"
    engine.execute(sql)

def createTables(pwd):
    tablas = os.listdir(pwd)
    engine = sqlalchemy.create_engine('mysql+pymysql://root:root@localhost:3306/Defunciones')
    print("Conectado a la base de datos")
    print("Creando tablas...")
    
    for tabla in tablas:
        print("Creando tabla: " + tabla)
        if tabla.endswith('.csv'):
            df = pandas.read_csv(os.path.join(pwd, tabla))

            columns = ""
            index = ""
            for column in df.columns:
                columns += "`" + column + "` VARCHAR(255), "
            
                index += f"INDEX (`{column}`), "

            try:
                sql = """
                CREATE TABLE IF NOT EXISTS `""" + tabla[:-4] + """` (
                """ + columns + index[:-2] + """
                );"""

                engine.execute(sql)
                print("Tabla creada")

            except Exception as e:
                print("Error al crear la tabla " + tabla)
                print(e)

def insertData(pwd):
    tablas = os.listdir(pwd)
    engine = sqlalchemy.create_engine('mysql+pymysql://root:root@localhost:3306/Defunciones')
    print("*"*50)
    print("\033[93mConectado a la base de datos\033[00m")
    print("\033[93mInsertando datos...\033[00m")
    
    for tabla in tablas:
        print("\033[94mInsertando datos en la tabla: " + tabla + "\033[00m")

        if tabla.endswith('.csv'):

            df = pandas.read_csv(os.path.join(pwd, tabla))

            columnas = df.columns
            columnas = ", ".join(columnas)
        
            values = ", ".join(["%s"] * len(df.columns))

            try:
                sql = """INSERT INTO `""" + tabla[:-4] + """` (""" + columnas + """) VALUES (""" + values + """)"""
                df = df.astype(str)
                data = [tuple(x) for x in df.values]
                engine.execute(sql, data)
                print("\033[92mDatos insertados\033[00m")
            except Exception as e:
                print("\033[91mError al insertar datos\033[00m",tabla)
                print(e)
          
def createDefunciones(pwd):
    engine = sqlalchemy.create_engine('mysql+pymysql://root:root@localhost:3306/Defunciones')
    
    relaciones = rel.getRelaciones()
    tablas = os.listdir(pwd)

    for tabla in tablas:
        name = tabla[:-4]
        num = ""

        columns = ""
        fk_columns = ""

        for char in name:
            if char.isdigit():
                num += char
        
        for (key, value) in relaciones.items():

            fk_table = value + "%%" + str(num) + "%%"
            
            try:
                result = engine.execute(f"SHOW TABLES LIKE '{fk_table}'")
                try:
                    fk_table = result.fetchone()[0]#Sacamos la tabla correcta para relacionar
                except:
                    columns += f"`{key}` VARCHAR(255), "
                    continue
            
                columns += f"`{key}` VARCHAR(255), "
                
                #Obtenemos las columnas de la tabla a relacionar
                table_columns = engine.execute(f"SHOW COLUMNS FROM `{fk_table}`")
                table_columns = [column[0] for column in table_columns]

                columna_relacionada = "*"
                
                for items in rel.own_rel:
                    try:
                        if items[key]:
                            if items[key] in table_columns:
                                columna_relacionada = items[key]
                    except:
                        pass
                
                if columna_relacionada != "*":
                    fk_columns += f"FOREIGN KEY (`{key}`) REFERENCES `{fk_table}` (`{columna_relacionada}`), "
                
            except Exception as e:
                #print exception in red
                print("\033[91mError al crear la tabla Defunciones\033[00m")
                print(f"\033[91m{e}\033[00m")
                continue

        sql = f"""
        CREATE TABLE IF NOT EXISTS `{name}` (
            {columns}
            {fk_columns[:-2]}
        );
            """

        try:
            engine.execute(sql)
            print(f"Tabla {name} creada")
            insertRootData(name)

        except Exception as e:
            print("\033[91mError al crear la tabla Defunciones  888888\033[00m")
            print(e)
            continue

def insertDefuncionesData(pwd):
    engine = sqlalchemy.create_engine('mysql+pymysql://root:root@localhost:3306/Defunciones')
    tablas = os.listdir(pwd)

    for tabla in tablas:
        name = tabla[:-4]
        num = ""

        for char in name:
            if char.isdigit():
                num += char

        df = pandas.read_csv(os.path.join(pwd, tabla))

        columnas = df.columns
        columnas = ", ".join(columnas)
    
        values = ", ".join(["%s"] * len(df.columns))

        try:
            sql = f"""INSERT INTO `{name}` ({columnas}) VALUES ({values})"""
            df = df.astype(str)
            data = [tuple(x) for x in df.values]
            engine.execute(sql, data)
            print(f"Datos insertados en la tabla {name}")
        except Exception as e:
            print("\033[91mError al insertar datos\033[00m",tabla)
            print(e)