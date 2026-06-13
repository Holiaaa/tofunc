def to_log(params):
    return f"{params[0]} * ln(x + 1) + {params[1]}"

def to_exp(params):
    return f"{params[0]} * e**({params[1]} * x)"