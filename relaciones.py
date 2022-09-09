import os 
import pandas

def getRelaciones():
    # Get the path to the current file
    files = os.listdir()
    files = [f for f in files if f.endswith('.csv')]
    df = pandas.read_csv(files[0])
    relaciones = df[["Variable","RELACION"]]
    relaciones = relaciones.dropna()
    relaciones = relaciones.drop_duplicates()
    relaciones = relaciones.set_index("Variable")

    # Convert the dataframe to a dictionary
    relaciones = relaciones.to_dict()
    relaciones = relaciones["RELACION"]

    return relaciones

# own_rel = [
    {"Ent_regis": "CVE_ENT"},
    {"Mun_regis": "CVE_MUN"},
    {"Ent_resid": "CVE_ENT"},
    {"Mun_resid": "CVE_MUN"},
    {"Ent_ocurr": "CVE_ENT"},
    {"Mun_ocurr": "CVE_MUN"},
    {"TLOC_RESID": "CVE_TLOC"},
    {"ENT_OCURR": "CVE_ENT"},
    {"MUN_OCURR": "CVE_MUN"},
    {"CAUSA_DEF": "CLAVE"},
    {"LISTA_MEX": "CLAVE"},
    {"SEXO": "CVE_SEXO"},
    {"EDAD": "CLAVE"},
    {"DIA_OCURR": "*"},
    {"MES_OCURR": "CVE_MES"},
    {"ANIO_OCUR": "*"},
    {"MES_REGIS": "CVE_MES"},
    {"ANIO_REGIS": "*"},
    {"DIA_NACIM": "*"},
    {"ANIO_NACIM": "*"},
    {"OCUPACION": "CVE_OCUPACION"},
    {"ESCOLARIDA": "CVE_ESCOLARIDAD"},
    {"EDO_CIVIL": "CVE_EDOCIVIL"},
    {"PRESUNTO": "CVE_PRESUNTO"},
    {"OCURR_TRAB": "CVE_OCURRTRAB"},
    {"LUGAR_OCUR": "CVE_LUGAROCURR"},
    {"NECROPSIA": "CVE_NECROPSIA"},
    {"ASIST_MEDI": "CVE_ASISMED"},
    {"SITIO_OCUR": "CVE_SITIOOCURR"},
    {"COND_CERT": "CVE_CONDCERT"},
    {"CERT_NOMED": "CVE_CERT_NOMED"},
    {"NACIONALID": "CVE_NACIONALIDAD"},
    {"DERECHOHAB": "CVE_DERECHOHAB"},
    {"EMBARAZO": "CVE_EMBARAZO"},
    {"REL_EMBA": "CVE_RELEMB"},
    {"HORAS": "*"},
    {"MINUTOS": "*"},
    {"CAPITULO": "CAPITULO"},
    {"GRUPO": "GRUPO"},
    {"LISTA1": ""},
    {"GR_LISMEX": "CLAVE"},
    {"EDAD_AGRU": "CVE_EDADAGRU"},
    {"MATERNAS": "CLAVE"},
    {"DIS_RE_OAX": "CVE_MUN"}
#]

own_rel = [
    {"Ent_regis": "CVE_ENT"},
    {"Mun_regis": "CVE_MUN"},
    {"Ent_resid": "CVE_ENT"},
    {"Mun_resid": "CVE_MUN"},
    {"Ent_ocurr": "CVE_ENT"},
    {"Mun_ocurr": "CVE_MUN"},
    {"TLOC_RESID": "CVE_TLOC"},
    {"ENT_OCURR": "CVE_ENT"},
    {"MUN_OCURR": "CVE_MUN"},
    {"CAUSA_DEF": "CLAVE"},
    {"LISTA_MEX": "CLAVE"},
    {"SEXO": "CVE_SEXO"},
    {"EDAD": "CLAVE"},
    {"DIA_OCURR": "*"},
    {"MES_OCURR": "CVE_MES"},
    {"ANIO_OCUR": "*"},
    {"MES_REGIS": "CVE_MES"},
    {"ANIO_REGIS": "*"},
    {"DIA_NACIM": "*"},
    {"ANIO_NACIM": "*"},
    {"OCUPACION": "CVE_OCUPACION"},
    {"ESCOLARIDA": "CVE_ESCOLARIDAD"},
    {"EDO_CIVIL": "CVE_EDOCIVIL"},
    {"PRESUNTO": "CVE_PRESUNTO"},
    {"OCURR_TRAB": "CVE_OCURRTRAB"},
    {"LUGAR_OCUR": "CVE_LUGAROCURR"},
    {"NECROPSIA": "CVE_NECROPSIA"},
    {"ASIST_MEDI": "CVE_ASISMED"},
    {"SITIO_OCUR": "CVE_SITIOOCURR"},
    {"COND_CERT": "CVE_CONDCERT"},
    {"CERT_NOMED": "CVE_CERT_NOMED"},
    {"NACIONALID": "CVE_NACIONALIDAD"},
    {"DERECHOHAB": "CVE_DERECHOHAB"},
    {"EMBARAZO": "CVE_EMBARAZO"},
    {"REL_EMBA": "CVE_RELEMB"},
    {"HORAS": "*"},
    {"MINUTOS": "*"},
    {"CAPITULO": "CAPITULO"},
    {"GRUPO": "GRUPO"},
    {"LISTA1": ""},
    {"GR_LISMEX": "CLAVE"},
    {"EDAD_AGRU": "CVE_EDADAGRU"},
    {"MATERNAS": "CLAVE"},
    {"DIS_RE_OAX": "CVE_MUN"},
    {"VIO_FAMI": "CVE_VIOFAM"},
    {"TLOC_OCURR": "CVE_TLOC"},
    {"DIA_REGIS": "*"},
    {"AREA_UR": "CVE_AREAUR"},
    {"COMPLICARO": "CVE_COMPLICADO"},
    {"DIA_CERT": "*"},
    {"MES_CERT": "CVE_MES"},
    {"ANIO_CERT": "*"},
    {"PESO": "*"},
    {"LENGUA": "CVE_LENGUA"},
    {"COND_ACT": "CVE_CONDICION"},
    {"PAR_AGRE": "CLAVE"},
    {"ENT_OCULES": "CVE_ENT"},
    {"MUN_OCULES": "CVE_MUN"},
    {"LOC_RESID": "[CVE_TLOC"},
]
