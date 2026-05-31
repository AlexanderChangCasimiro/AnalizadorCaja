def ejecutar_afd(tokens):

    estado = "q0"

    recorrido = []

    transiciones = {

        ("q0", "TK_ABRIR"): "q1",

        ("q1", "TK_VENTA"): "q2",
        ("q1", "TK_GASTO"): "q2",

        ("q2", "TK_VENTA"): "q2",
        ("q2", "TK_GASTO"): "q2",

        ("q2", "TK_CONTAR"): "q3",

        ("q3", "TK_VALIDAR"): "q4",

        ("q4", "TK_CERRAR"): "q5"
    }

    for token in tokens:

        if token.startswith("ERROR"):
            return recorrido, "RECHAZADO"

        clave = (estado, token)

        if clave not in transiciones:

            recorrido.append(
                f"ERROR: transición inválida desde {estado} con {token}"
            )

            return recorrido, "RECHAZADO"

        nuevo_estado = transiciones[clave]

        recorrido.append(
            f"{estado} -- {token} --> {nuevo_estado}"
        )

        estado = nuevo_estado

    if estado == "q5":
        return recorrido, "ACEPTADO"

    return recorrido, "RECHAZADO"