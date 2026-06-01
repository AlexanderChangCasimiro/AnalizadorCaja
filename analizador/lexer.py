def analizar_lexico(texto):

    tokens = []

    diccionario = {
        "INICIAR_TURNO": "TK_INICIAR",
        "REGISTRAR_VENTA": "TK_VENTA",
        "REGISTRAR_GASTO": "TK_GASTO",
        "CONTAR_EFECTIVO": "TK_CONTAR",
        "VALIDAR_CUADRE": "TK_VALIDAR",
        "GENERAR_REPORTE": "TK_REPORTE",
        "CERRAR_CAJA": "TK_CERRAR"
    }

    lineas = texto.splitlines()

    for linea in lineas:

        palabra = linea.strip()

        if palabra == "":
            continue

        if palabra in diccionario:
            tokens.append(diccionario[palabra])
        else:
            tokens.append(f"ERROR_LEXICO: {palabra}")

    return tokens