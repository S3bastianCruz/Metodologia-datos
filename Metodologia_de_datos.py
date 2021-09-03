import pandas as pd
import numpy as np


Data_Set=pd.read_csv('Churn Modeling.csv', delimiter=',')

#metodo que limpia campos con valores nulos o sin valor del data set
def Limpiar_dataframe(Datos):
    Datos.isna().sum()
    return Datos.dropna()

#Metodo para limpieza de campos inecesarios
def Limpiar(Datos, Useless):
    for x in Useless:
        if x in Datos.columns.values:
            Datos.drop([x], axis=1, inplace=True)
    return Datos

#Metodo definitivo para filtrar atributos
def Filtrar_3(Datos,Atributos,Filtros,concate):
    x=Atributos[0]
    y=Filtros[0]
    if x in Datos.columns.values:
        data=Datos[x]
        if y in data:
            data=Datos[x]==y
            resul=Datos[data]
            Atributos.pop(0)
            Filtros.pop(0)
            concate=pd.concat([resul,concate])
            concate=Limpiar_dataframe(concate)
            concate=concate.drop_duplicates()
            if len(Atributos)>0:
                return Filtrar_3(Datos, Atributos, Filtros, concate)
            else:
                return concate

#Metodo de preparacion de datos(conversion de datos string a enteros) 
def Categorizar_2(Datos):
    datos=Datos
    nomen={}
    for x in datos.columns.values:
        cat=0
        for y in datos[x].unique():
            datos[x].replace({str(y):cat},inplace=True)
            cat=cat+1
            HacerJson(nomen,x,y,cat)
    return datos

#Metodo para crear el diccionario que se convertira en el Json
def HacerJson(Registro, Conjunto, Llave, Valor):
        if Conjunto in Registro.keys():
            Registro[Conjunto].append(dict(Valor=Llave, Conversion=Valor))
        else:
            Registro[Conjunto]=[]
            Registro[Conjunto].append(dict(Valor=Llave, Conversion=Valor))
            

#Funcion lambda para normalizar el atributo de credit score
Lambda_CS = lambda datos:datos['CreditScore'].apply(lambda x:0 if x >= 350 and x<580 else (1 if x>=580 and x<670 else(2 if x>=670 and x<740 else(3 if x>=740 and x<800 else 4))))

#Funcion lambda para normalizar el atributo de balance
Lambda_B= lambda datos:datos['Balance'].apply(lambda x: 0 if x==0.00 else 1 )

#Funcion lambda para normalizar el atributo de balance
Lambda_A=lambda datos:datos['Age'].apply(lambda x: 0 if x>=0 and x<6 else (1 if x >=6 and x<14 else(2 if x>=14 and x <27 else(3 if x>=27 and x <60 else 4) )) )






