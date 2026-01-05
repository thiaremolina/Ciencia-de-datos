import math 
def promedio(vals):
    """
    Calcula el promedio de una lista de números.
    Verifica y elimina NaNs en los datos.

    Parámetros
    ---------
    vals: lista
         lista con los números

    Retorna
    -------
    promedio: float
          el promedio de los números
    """
    # 1. Revisar valores Nan:
    vals = [x for x in vals if not math.isnan(x)] 
    if not vals:
        return float('Nan')
    # 2.Calcular el promedio:
    promedio = sum(vals) / len(vals)
    return promedio

def mediana(vals):
    """
    Calcula la mediana de una lista de datos.
    
    Parámetros
    ---------
    vals: lista
         lista con los números

    Retorna
    -------
    mediana: float
          la mediana de los números
    """
    # 1. Revisar valores Nan:
    vals = [x for x in vals if not math.isnan(x)] 
    if not vals:
        return float('Nan')

    #  2. Ordenar los valores y calcular n(el largo de la lista):
    lista_ordenada = sorted(vals)
    n = len(lista_ordenada)

    # 3. Si el número de datos es par, promediamos los dos valores centrales:
    if n % 2 == 0:
        mid1 = lista_ordenada[n // 2 - 1] 
        # pq []? porque los [] acceden a los elemento de unna lista, mientras que los () llaman a una función.
        mid2 = lista_ordenada[n // 2]
        return (mid1 + mid2) / 2
    else:
        # Si es impar, el valor central es la mediana:
        return lista_ordenada[n // 2]

def moda(vals):
    """
    Calcula la moda de una lista de datos.
    
    Parámetros
    ---------
    vals: lista
         lista con los números

    Retorna
    -------
    moda: int
          la moda de los números
    """
        
    # 1. determinar las categorias 
    categorias = []
    for i in vals: 
        if i not in categorias:
            categorias.append(i)
        else:
            None
    
    # 2. frecuencia:       
    frecuencia = [] 
    for categoria in categorias:
        contador = 0
        for i in vals:
            if i  == categoria:
                contador += 1
        frecuencia.append(contador) 

    # 3. maximo valor de la frecuencia y a que categoria pertenece:             
    max_frecuencia= 0
    for valor in frecuencia:
        if valor > max_frecuencia:
            max_frecuencia = valor
            
    moda= []
    for i in range(len(categorias)):
        if frecuencia[i] == max_frecuencia:
            moda.append(categorias[i])


      # 4. categorias iguales        
    if len(moda) == len(categorias) and len(categorias) > 1: 
        return None
    if len(moda) == 1: 
        return moda[0]
        
    return moda


def rango(vals):
     """
    Calcula el rango de una lista de datos.
    
    Parámetros
    ---------
     vals: lista
         lista con los números

    Retorna
    -------
    rango: int
          el rango de los números
    """
     rango = max(vals) - min(vals)
     return rango

def varianza(vals, tipo ='Poblacional'):
     """
    Calcula la varianza poblacional de una lista de datos.
    A menos de que se especifique que es muestral.
    
    Parámetros
    ---------
    vals: lista
         lista con los números

    Retorna
    -------
    varianza: int
         la varianza de los números
          
    """
    # 1. Revisar valores Nan:
     vals = [x for x in vals if not math.isnan(x)] 
     if not vals:
        return float('Nan')
        
    # 2. condiciones iniciales:
     n = len(vals)
     if n < 2:
         return 0
     media = promedio(vals)
     # 3. calcular la sumatoria de las  diferencias al cuadrado:
     diferencias_cuadrado = sum([(x - media) ** 2 for x in vals])
     # 4. Determinar el denominador según el tipo:
     if tipo =='Muestral': 
         denominador =  n-1 
     else:
         denominador = n
         varianza = diferencias_cuadrado/denominador
     return varianza

     
def desviacion_estandar(vals):  
    """
    Calcula la desviacion estándar de una lista de números.
    
    Parametros
    ---------------
    vals: lista
         lista con los números
    Retorna
    --------------------
    desviación estándar: float
         la desviación estándar de los números
          
    """
    # 1. Revisar valores Nan:
    vals = [x for x in vals if not math.isnan(x)] 
    if not vals:
        return float('Nan')
    
    v = varianza(vals, tipo='Poblacional')
    desviacion_estandar = math.sqrt(v)
    return desviacion_estandar

def desviacion_mediana_absoluta(vals):  
    """
    Calcula la desviacion mediana absoluta de una lista de números.
    
    Parametros
    ---------------
    vals: lista
         lista con los números
    Retorna
    --------------------
    desviación mediana aboluta: float
         la desviacion mediana absoluta de la mediana de los números
          
    """
    # 1. Revisar valores Nan:
    vals = [x for x in vals if not math.isnan(x)] 
    if not vals:
        return float('Nan')
        
    med = mediana(vals)
    desviaciones = [abs(x - med) for x in vals] #abs() devuelve el valor absoluto de un número
    return mediana(desviaciones)

def percentil(vals,percentil):
    """
    Calcula el percentil de una lista de números.
    Verifica y elimina NaNs en los datos.
    
    Parametros
    ---------------
    vals: lista
         lista con los números
    percentil: int
         percentil que se quiere calcular
    
    Retorna
    --------------------
    percentil : float
         percentil solicitado de una lista de números
          
    """
    # 1. Revisar valores Nan:
    vals = [x for x in vals if not math.isnan(x)] 
    if not vals:
        return float('Nan')
        
    # 2. ordenar los datos:
    lista = sorted(vals)
    n = len(lista)
    # 3. encontrar la posicion:
    posicion = (percentil*(n-1) /100)
    # 4. revisar si la posicion es exacta o decimal:
    parte_entera = int(posicion)
    parte_decimal = posicion - parte_entera
    if parte_decimal == 0:
        percentil = lista[parte_entera]
    # 5. calcular el valor antecesor, sucesor y su distancia
    else:
        primer_valor = lista[parte_entera]
        segundo_valor = lista[parte_entera+1]
        distancia = segundo_valor - primer_valor
        # 6. calcular el percentil
        percentil = primer_valor + (parte_decimal * distancia)

    return percentil

def rango_intercuartilico(vals):
    """
    Calcula el rango intercuartílico de una lista de números.
    
    Parametros
    ---------------
    vals: lista
         lista con los números

    Retorna
    --------------------
    rango intercuartilico: float
         rango intercuartilico de una lista de números
          
    """
    q1 = percentil(vals, 25)
    q3 = percentil(vals, 75)
    rango_intercuartilico = q3 - q1
    return rango_intercuartilico

def covarianza(vals_x,vals_y):
    """
    Calcula la covarianza de dos listas de números.
    Detecta y elimina valores NaN

    Parametros
    ---------------
    vals_x, vals_y: lista
               lista con los dos atributos
    Retorna
    -------
    covarianza: float
          covarianza de los atributos
    """
    # 1. Revisar los valores Nan:
    vals_x = [x for x in vals_x if not math.isnan(x)]
    vals_y = [x for x in vals_y if not math.isnan(x)]
    
    # 2. Condiciones:
    n = len(vals_x)
    if len(vals_y) != n:
        return 'Las listas tienen que ser de la misma longuitud'
    if n < 2:
        return 0
    
    # 3. Calcular las medias:
    m1 = promedio(vals_x)
    m2 = promedio(vals_y)

     # 4. Calcular la suma de los productos de las diferencias:
    sumatoria = 0 
    for i in range(n):
        dif_x = vals_x[i] - m1
        dif_y = vals_y[i] - m2
        sumatoria+= dif_x * dif_y
    covarianza = sumatoria / n

    return covarianza


def correlacion (vals_x,vals_y):
    """
    Calcula la correlación de dos listas de números.
    Detecta y elimina valores NaN

    Parametros
    ---------------
    vals_x, vals_y: lista
               lista con los dos atributos
    Retorna
    -------
    correlacion: float
          correlacion de los atributos
    """
    # 1. Revisar valores Nan:
    vals_x = [x for x in vals_x if not math.isnan(x)]
    vals_y = [x for x in vals_y if not math.isnan(x)]

    # 2.Calcular desviacion estandar de x e y:
    desv_x = desviacion_estandar(vals_x)
    desv_y = desviacion_estandar(vals_y)

    # 3. calcular correlacion:
    correlacion = covarianza(vals_x, vals_y) / (desv_x * desv_y)

    # 4. en caso de que la desviacion sea cero:
    if desv_x == 0 or desv_y == 0:
        return None
    else:
        return correlacion
