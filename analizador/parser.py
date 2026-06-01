def analizar_sintaxis(tokens):

    secuencia = []

    for token in tokens:

        if token.startswith("ERROR"):
            return "Error sintáctico: existen errores léxicos"

        secuencia.append(token)

    if not secuencia:
        return "Error: no se ingresó ningún proceso"

    if secuencia[0] != "TK_INICIAR":
        return "Error: debe iniciar con INICIAR_TURNO"

    if "TK_CONTAR" not in secuencia:
        return "Error: falta CONTAR_EFECTIVO"

    if "TK_VALIDAR" not in secuencia:
        return "Error: falta VALIDAR_CUADRE"

    if "TK_REPORTE" not in secuencia:
        return "Error: falta GENERAR_REPORTE"

    if secuencia[-1] != "TK_CERRAR":
        return "Error: debe terminar con CERRAR_CAJA"

    posicion_contar = secuencia.index("TK_CONTAR")
    posicion_validar = secuencia.index("TK_VALIDAR")
    posicion_reporte = secuencia.index("TK_REPORTE")

    if posicion_validar < posicion_contar:
        return "Error: VALIDAR_CUADRE debe ir después de CONTAR_EFECTIVO"

    if posicion_reporte < posicion_validar:
        return "Error: GENERAR_REPORTE debe ir después de VALIDAR_CUADRE"

    return "Sintaxis Correcta"