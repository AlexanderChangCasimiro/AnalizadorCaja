def analizar_lexico(texto):

    tokens = []

    diccionario = {
        "ABRIR_CAJA": "TK_ABRIR",
        "VENTA": "TK_VENTA",
        "GASTO": "TK_GASTO",
        "CONTAR": "TK_CONTAR",
        "VALIDAR": "TK_VALIDAR",
        "CERRAR": "TK_CERRAR"
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