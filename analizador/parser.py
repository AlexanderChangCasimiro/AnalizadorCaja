def analizar_sintaxis(tokens):

    secuencia = []

    for token in tokens:

        if token.startswith("ERROR"):
            return "Error sintáctico: existen errores léxicos"

        secuencia.append(token)

    if not secuencia:
        return "Error: no se ingresó ningún proceso"

    if secuencia[0] != "TK_ABRIR":
        return "Error: debe iniciar con ABRIR_CAJA"

    if "TK_CONTAR" not in secuencia:
        return "Error: falta CONTAR"

    if "TK_VALIDAR" not in secuencia:
        return "Error: falta VALIDAR"

    if secuencia[-1] != "TK_CERRAR":
        return "Error: debe terminar con CERRAR"

    posicion_contar = secuencia.index("TK_CONTAR")
    posicion_validar = secuencia.index("TK_VALIDAR")

    if posicion_validar < posicion_contar:
        return "Error: VALIDAR debe ir después de CONTAR"

    return "Sintaxis Correcta"