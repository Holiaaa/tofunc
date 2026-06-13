def to_polyn(n, params):
    terms = []
    params = params[::-1]

    for i in range(n + 1):
        coef = params[i]
        if coef < 0:
            coef = f"({coef})"
        if coef == 0:
            continue

        if i == 0:
            terms.append(f"{coef}")
        elif i == 1:
            terms.append(f"{coef}x")
        else:
            terms.append(f"{coef}x**" + "{" + f"{i}" + "}")

    terms = terms[::-1]
    return " + ".join(terms)

def to_poly2(params):
    return to_polyn(2, params)

def to_poly3(params):
    return to_polyn(3, params)