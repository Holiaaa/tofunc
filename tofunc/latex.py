def to_latex(exp):
    exp = exp.replace("**", "^")
    exp = exp.replace("*", "\\times")
    exp = exp.replace("ln", "\\ln")
    return exp