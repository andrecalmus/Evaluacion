#Función para cargar archivos con extensiones .csv y .xlsx y los convierte en un dataframe, si es un archivo con cualquier otra extensión, emitirá el raise ("Este formato no está soportado para esta función: .formato")

def cargar_dataset(archivo):
    import pandas as pd
    import os
    extension = os.path.splitext(archivo)[1].lower()
    if extension == '.csv':
        df = pd.read_csv(archivo)
        return(df)
    elif extension == '.xlsx':
        df = pd.read_excel(archivo)
        return(df)
    else:
        raise ValueError(f'Este formato no está soportado para esta función: {extension}')

#Funcion que sustituye los valores nulos de las variables pares numéricas con el método mean y de las impares numéricas con la constante "99". Las columnas que no sean de tipo numérico se sustituirán con el string "Este_es_un_valor_nulo"

def sustituir_valores_nulos(df):
    import pandas as pd
    import numpy as np
    for column in df.columns:
        if df[column].dtype == 'float64' or df[column].dtype == 'int64':
            if df.columns.get_loc(column) % 2 == 0:
                df[column].fillna(round(df[column].mean(), 1), inplace=True)
            else:
                df[column].fillna(99, inplace=True)
        else:
            df[column].fillna("Este_es_un_valor_nulo", inplace=True)
    return df

#Función Identificación de valores nulos por columna y por dataframe

def identificacion_nulos(dataframe):
    import pandas as pd
    import numpy as np
    import matplotlib as plt
    nulos_columna = dataframe.isnull().sum()
    nulos_dataframe = dataframe.isnull().sum() .sum()
    print('Nulos por columna:', nulos_columna)
    print('Nulos por dataframe:', nulos_dataframe)
    return

#Función Sustituye  los valores atípicos de las columnas numéricas con el método de “Rango intercuartílico”

def sustituir_atipicos(df):
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    import calmus as cs
    dfc = df.copy()
    dfc1 = cs.sustitucion_ffill(dfc)
    dfc2 = cs.sustitucion_mean(dfc1)
    cuantitativas = dfc2.select_dtypes(include=['int64', 'float64'])
    cualitativas = dfc2.select_dtypes(include=['object','datetime64[ns]'])
    y = cuantitativas
    percenttile25 = y.quantile(0.25)
    percenttile75 = y.quantile(0.75) 
    iqr = percenttile75 - percenttile25
    Limite_Superior_iqr = percenttile75 + 1.5 * iqr
    Limite_Inferior_iqr = percenttile25 - 1.5 * iqr
    iqr = cuantitativas[(y<Limite_Superior_iqr) & (y>Limite_Inferior_iqr)]
    iqr2 = iqr.copy()
    iqr2 = cs.sustitucion_mean(iqr2)
    iqr2 = iqr2.dropna(axis=1, how='all')
    nulos_iqr2 = cs.identificacion_nulos(iqr2)
    Datos_limpios = pd.concat([cualitativas, iqr2], axis=1)
    print(nulos_iqr2)
    return Datos_limpios

