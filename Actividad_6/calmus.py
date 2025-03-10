################################################ Función para cargar un archivo como un dataframe #############################################################

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
    elif extension == '.json':
        df = pd.read_json(archivo)
        return(df)
    elif extension == '.html':
        df = pd.read_html(archivo)
        return(df)
    else:
        raise ValueError(f'Formato de archivo no soportado: {extension}')
    
################################################ Funciones mean para sustitución de valores nulos #############################################################

def sustitucion_mean(dataframe):
    import pandas as pd
    import numpy as np
    import matplotlib as plt
    cuantitativas_con_nulos = dataframe.select_dtypes(include=['float64', 'int64','float','int'])
    cualitativas = dataframe.select_dtypes(include=['object', 'datetime','category'])
    cuantitativas = cuantitativas_con_nulos.fillna(round(cuantitativas_con_nulos.mean(), 1))
    Datos_sin_nulos = pd.concat([cuantitativas, cualitativas], axis=1)
    return(Datos_sin_nulos)

################################################ Funciones ffill para sustitución de valores nulos ############################################################

def sustitucion_ffill(dataframe):
    import pandas as pd
    import numpy as np
    import matplotlib as plt
    cuantitativas = dataframe.select_dtypes(include=['float64', 'int64','float','int'])
    cualitativas_con_nulos = dataframe.select_dtypes(include=['object', 'datetime','category'])
    cualitativas = cualitativas_con_nulos.fillna(method='ffill')
    Datos_sin_nulos = pd.concat([cuantitativas, cualitativas], axis=1)
    return(Datos_sin_nulos)

################################################ Funciones bfill para sustitución de valores nulos ############################################################

def sustitucion_bfill(dataframe):
    import pandas as pd
    import numpy as np
    import matplotlib as plt
    cuantitativas = dataframe.select_dtypes(include=['float64', 'int64','float','int'])
    cualitativas_con_nulos = dataframe.select_dtypes(include=['object', 'datetime','category'])
    cualitativas = cualitativas_con_nulos.fillna(method='bfill')
    Datos_sin_nulos = pd.concat([cuantitativas, cualitativas], axis=1)
    return(Datos_sin_nulos)

################################################ Funciones string concreto para sustitución de valores nulos ###################################################

def sustitucion_string_concreto(dataframe,cadena):
    import pandas as pd
    import numpy as np
    import matplotlib as plt
    cuantitativas = dataframe.select_dtypes(include=['float64', 'int64','float','int'])
    cualitativas_con_nulos = dataframe.select_dtypes(include=['object', 'datetime','category'])
    cualitativas = cualitativas_con_nulos.fillna(cadena)
    Datos_sin_nulos = pd.concat([cuantitativas, cualitativas], axis=1)
    return(Datos_sin_nulos)

################################################ Funciones constante para sustitución de valores nulos #########################################################

def sustitucion_constante(dataframe,constante):
    import pandas as pd
    import numpy as np
    import matplotlib as plt
    cuantitativas_con_nulos = dataframe.select_dtypes(include=['float64', 'int64','float','int'])
    cualitativas = dataframe.select_dtypes(include=['object', 'datetime','category'])
    cuantitativas = cuantitativas_con_nulos.fillna(constante)
    Datos_sin_nulos = pd.concat([cuantitativas, cualitativas], axis=1)
    return(Datos_sin_nulos)

################################################ Funciones median para sustitución de valores nulos #########################################################
 
def sustitucion_median(dataframe):
    import pandas as pd
    import numpy as np
    import matplotlib as plt
    cuantitativas_con_nulos = dataframe.select_dtypes(include=['float64', 'int64','float','int'])
    cualitativas = dataframe.select_dtypes(include=['object', 'datetime','category'])
    cuantitativas = cuantitativas_con_nulos.fillna(round(cuantitativas_con_nulos.median(), 1))
    Datos_sin_nulos = pd.concat([cuantitativas, cualitativas], axis=1)
    return(Datos_sin_nulos)

################################################ Funciones Identificación de valores nulos por columna y por dataframe ######################################

def identificacion_nulos(dataframe):
    import pandas as pd
    import numpy as np
    import matplotlib as plt
    nulos_columna = dataframe.isnull().sum()
    nulos_dataframe = dataframe.isnull().sum() .sum()
    print('Nulos por columna:', nulos_columna)
    print('Nulos por dataframe:', nulos_dataframe)
    return