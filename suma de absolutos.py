def suma_absolutos(*args):
    absoluto_n = 0
    absoluto_p = 0
    for arg in args:
        if arg < 0:
            negativo = arg * -1
            absoluto_n += negativo
        else:
            absoluto_p += arg
    absoluto = absoluto_n + absoluto_p
    print(absoluto)
    return absoluto
suma_absolutos(1, 2, 3, -23)
    