def generar_resumen(tokens):

    ventas = 0
    gastos = 0

    for token in tokens:

        if token == "TK_VENTA":
            ventas += 1

        if token == "TK_GASTO":
            gastos += 1

    return {
        "ventas": ventas,
        "gastos": gastos
    }