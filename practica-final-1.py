# Paso 1: Definir el valor actual del Euro y el Dolar con respecto al Mex

tipo_cambio_eur_a_mxn = 23.70
tipo_cambio_usd_a_mxn = 20.75


# Paso 2: Solicitar al usuario el tipo de conversion (Euro a Peso Mex)

tipo_conversion = str(input("Ingrese moneda origen para la conversion (EUR/USD): "))

# Paso 3: Solicitar al usuario el monto a convertir.

monto_a_convertir = float(input("Ingrese el monto a convertir: "))

# Paso 4: Realizar la conversion utilizando el cambio correspondiente 
# Paso 5. Mostrar el resultado de la conversion al usuario.

if tipo_conversion.upper() == "EUR":
    resultado = monto_a_convertir * tipo_cambio_eur_a_mxn
    print("El resultado de la conversion de EUR a MXN es: ", resultado)
elif tipo_conversion.upper() == "USD":
    resultado = monto_a_convertir * tipo_cambio_usd_a_mxn
    print("El resultado de la conversion de USD a MXN es: ", resultado)
else:
    print("No esta disponible el tipo de cambio.")
    