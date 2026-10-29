def convertir_unidades(cantidad, origen, destino):
    #Lista con las unidades a convertir
    Lista = ["Kb", "Mb", "Gb", "Tb", "Pb"]
    #si hay alguna unidad inexistente, se cancela
    if origen not in Lista:
        return "unidad no encontrada"
    elif destino not in Lista: 
        return "unidad no encontrada"
    else:
        #buscamos la ubicacion de las unidades en la lista
        origenUbicacion = Lista.index(origen)+1
        DestinoUbicacion = Lista.index(destino)+1
        distancia = DestinoUbicacion-origenUbicacion

        resultado = cantidad
        #si la distancia es positiva, significa que tenemos que dividir
        if distancia > 0:
            #dividimos por 1000 cada bucle subiendo así de unidad
            while(origenUbicacion < DestinoUbicacion):
                resultado = resultado/1000
                origenUbicacion = origenUbicacion+1
            return resultado
        
        #si la distancia es negativa, significa que tenemos que multiplicar
        elif distancia < 0:
            #multiplicamos por 1000 cada bucle bajando así de unidad
            while(origenUbicacion > DestinoUbicacion):
                resultado = resultado*1000
                origenUbicacion = origenUbicacion-1
            return resultado
        
        #si la distancia es 0, significa que no tenemos que calcular nada
        elif distancia == 0:
            return cantidad

def convertir_base(numero, base_origen, base_destino):
    Lista = ["decimal", "binario", "hexadecimal", "octal"]
    if base_origen not in Lista:
        return "base no encontrada"
    elif base_destino not in Lista: 
        return "base no encontrada"
    #para no hacer conversiones innecesarias, enviamos el numero original
    elif base_origen == base_destino:
        return numero
    else:
        decimal = 0
        if base_origen == "decimal":
            decimal = numero
        elif base_origen == "binario":
            valor = str(numero) 
            punto = valor.find('.')
            if punto != -1:
                entero =  valor[:punto]
                entero = str(entero)[::-1]

                binario = []
                for x in valor:
                    if x == "0" or x == "1":
                        binario.append(int(x))

                resultado = (0.0)
                potencias = len(entero)-1
                for x in binario:
                    resultado = resultado + (float(x)*(2**potencias))
                    potencias= potencias-1

                
            else:
                valor = str(valor)[::-1]
                binario = []
                #poner en una lista solo los valores binarios
                for x in valor:
                    if x == "0" or x == "1":
                        binario.append(int(x))
                
                posiciones = len(binario)
                potencias = []
                x = 0
                while(x < posiciones):
                    #guardamos las potencias de 2 en una lista 
                    potencias.append(int(2**x))
                    x= x+1

                multiplicar = []
                x = 0
                while(x < posiciones):
                    #multiplicamos cada digito para pasarlo a decimal
                    multiplicar.append(int(potencias[x]*binario[x]))
                    x= x+1

                resultado = 0
                for x in multiplicar:
                    #sumamos las multiplicaciones 
                    resultado= resultado+x

                decimal = float(resultado)
        elif base_origen == "hexadecimal":
            valor = str(numero)
            #para hacer el .find y localizar el punto
            valor = valor.upper()
            punto = valor.find('.')

            # Diccionario de letras hexadecimales a numeros
            hexANum = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}

            #si hay punto
            if punto != -1:
                #separa en dos variables el entero y la fracción
                parteEntera = valor[:punto]
                parteFraccion = valor[punto+1:]

                # Convertir parte entera: cada digito * 16^posicion
                #invertir la parte entera
                parteEntera = parteEntera[::-1]
                resultadoEntero = 0
                potencia = 0
                #bucle para pasar y traducir el entero a hexadecimal
                for x in parteEntera:
                    if x in hexANum:
                        digito = hexANum[x]
                    else:
                        digito = int(x)
                    #la formula para pasar a hexadecimal
                    resultadoEntero = resultadoEntero + digito * (16**potencia)
                    potencia = potencia + 1

                # Convertir parte fraccionaria: cada digito * 16^(-posicion)
                resultadoFraccion = 0.0
                potencia = 1
                #bucle para pasar y traducir la fracción a hexadecimal
                for x in parteFraccion:
                    if x in hexANum:
                        digito = hexANum[x]
                    else:
                        digito = int(x)
                        #la formula para pasar a hexadecimal
                    resultadoFraccion = resultadoFraccion + digito * (16**(-potencia))
                    potencia = potencia + 1
                #juntar el entero y la fraccion de nuevo
                resultado = resultadoEntero + resultadoFraccion
                decimal = float(resultado)
            else:
                # Solo parte entera
                valor = valor[::-1]
                resultado = 0
                potencia = 0
                for x in valor:
                    if x in hexANum:
                        digito = hexANum[x]
                    else:
                        digito = int(x)
                    resultado = resultado + digito * (16**potencia)
                    potencia = potencia + 1
                decimal = float(resultado)


        elif base_origen == "octal":
            valor = str(numero) 
            punto = valor.find('.')
            if punto != -1:
                entero =  valor[:punto]
                entero = str(entero)
                parteFraccion = valor[punto+1:]
                completo = entero+parteFraccion

                resultado = (0.0)
                potencias = len(entero)-1
                multiplicacion = []
                x = 0
                while(x < len(completo)):
                    multiplicacion.append(float(8**potencias)*float(completo[x]))

                    potencias = potencias-1
                    x= x+1
                resultado = 0
                for x in multiplicacion:
                    resultado = float(resultado) + float(x)
                decimal = float(resultado)

            else:
                resultado = 0
                potencias = len(valor)-1
                for x in valor:
                    resultado = resultado + (float(x)*(8**potencias))
                    potencias= potencias-1
                decimal = float(resultado)
        
        if base_destino == "decimal":
            return decimal
        elif base_destino == "binario":
            valor = str(decimal)
            punto = str(valor).find('.')
            fraccion = "0"+valor[punto:]
            fraccion = float(fraccion)

            #si la fraccion es mayor que 0 significa que existe
            if fraccion > 0:

                #guardamos la parte entera en una variable con ayuda de la variable punto
                entero =  int(valor[:punto])


                binarioEntero= ""
                binariofraccion= ""
                while (int(entero)>0):
                    #guardamos en un string el residuo del entero
                    binarioEntero = binarioEntero+str(int(entero%2))
                    #dividimos el entero para el siguiente bucle
                    entero = int(entero/2)


                #invertimos los valores
                binarioEntero = binarioEntero[::-1]


                while (fraccion<1):
                    #multiplicamos la fraccion por 2 y lo que salga entero lo añadimos al resultado
                    binariofraccion = binariofraccion+str(float((fraccion*2)))[0]
                    fraccion = float(fraccion*2)
    
                return binarioEntero+"."+binariofraccion
            else:
                binario = ""
                valor =  int(valor[:punto])
                while (valor>0):
                    binario = binario+str(int(valor%2))
                    valor = int(valor/2)

                #invertimos el valor
                binario = str(binario)[::-1]
                return binario
        elif base_destino == "hexadecimal":
            valor = str(decimal)
            punto = str(valor).find('.')

            #si la variable punto no valiese -1 significaria que existe y por lo tanto es una fracción
            if punto != -1:
                #separamos la parte entera de la fracción en variables separadas y lo pasamos a int y float respectivamente para más adelante
                enteroDecimal = int(valor[:punto])
                fraccion = float("0"+valor[punto:])
                print(fraccion)
                print(enteroDecimal)
                # Parte entera: dividir entre 16 y guardar restos (de abajo hacia arriba)
                hexaEntero = []
                while enteroDecimal > 0:
                    #guardamos el resto en la lista hexaEntero creada con anterioridad
                    hexaEntero.append(enteroDecimal % 16)
                    enteroDecimal = enteroDecimal // 16

                # Parte fraccionaria: multiplicar por 16 y guardar parte entera
                hexaFraccion = []
                x = 0
                while fraccion > 0 and x < 8:
                    fraccion = fraccion * 16
                    #al pasar a int, guardamos solo la parte entera
                    hexaFraccion.append(int(fraccion))
                    fraccion = fraccion - int(fraccion)
                    x = x + 1

                # Traducir digitos a letras hexadecimales en un diccionario
                letras = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

                resultadoEntero = ""
                #Usando un bucle y el diccionario de arriba, pasamos a letras los valores necesarios  
                for x in hexaEntero:
                    if x >= 10:
                        resultadoEntero = resultadoEntero + letras[x]
                    else:
                        resultadoEntero = resultadoEntero + str(x)
                #invertimos el orden de los simbolos 
                resultadoEntero = resultadoEntero[::-1]

                resultadoFraccion = ""
                #repetimos lo mismo pero ahora con las fracciones
                for x in hexaFraccion:
                    if x >= 10:
                        resultadoFraccion = resultadoFraccion + letras[x]
                    else:
                        resultadoFraccion = resultadoFraccion + str(x)

                #juntamos ambos valores para tener el resultado
                resultado = resultadoEntero + "." + resultadoFraccion
                return resultado
            else:
                hexa = []
                while(valor > 0):
                    #si la division no da residuo entonces se añade directamente a la lista
                    if valor%16 == 0:
                        hexa.append(int(valor%16))
                        valor = valor/16
                    else:
                        #si hay residuo, entonces separamos la fraccion del entero para sacar la multiplicacion
                        valor = valor/16
                        valor = str(valor)
                        punto = valor.find('.')
                        entero = int(valor[:punto])
                        decimal = "0"+valor[punto:]
                        decimal = float(decimal)
                        #multiplicando por 16 la fraccion, sacamos el valor en entero
                        hexa.append(int(decimal*16))
                        valor = float(entero)
                
                resultado = ""
                for x in hexa:
                    if x >= 10:
                        #usando if/elif para decidir que letra tiene cada valor
                        if x == 10:
                            resultado = resultado+"A"
                        elif x == 11:
                            resultado = resultado+"B"
                        elif x == 12:
                            resultado = resultado+"C"
                        elif x == 13:
                            resultado = resultado+"D"
                        elif x == 14:
                            resultado = resultado+"E"
                        elif x == 15:
                            resultado = resultado+"F"
                    else:
                        resultado = resultado+str(x)
                resultado = str(resultado)[::-1]
                return resultado
        elif base_destino == "octal":
            valor = str(decimal)
            punto = str(valor).find('.')

            if punto != -1:
                fraccion = "0"+valor[punto:]
                print(fraccion)
                fraccion = float(fraccion)


                #guardamos la parte entera en una variable con ayuda de la variable punto
                entero =  int(valor[:punto])


                octalEntero= ""
                octalfraccion= ""
                while (int(entero)>0):
                    #guardamos en un string el residuo del entero
                    octalEntero = octalEntero+str(int(entero%8))
                    #dividimos el entero para el siguiente bucle
                    entero = int(entero/8)


                #invertimos los valores
                octalEntero = octalEntero[::-1]


                while (fraccion<1):
                    #multiplicamos la fraccion por 2 y lo que salga entero lo añadimos al resultado
                    octalfraccion = octalfraccion+str(float((fraccion*8)))[0]
                    fraccion = float(fraccion*8)
    
                return octalEntero+"."+octalfraccion
            else:

                octal = ""
                valor =  float(decimal)
                while (valor>0.9):

                    octal = octal+str(int(float(valor)%8))
                    
                    valor = float(valor)/8

                #invertimos el valor
                octal = str(octal)[::-1]
                return octal
    
            return octal

print(convertir_base(2457, "decimal", "octal"))