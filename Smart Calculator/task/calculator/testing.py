import re


def break_formula_into_list(formula: str):
    if re.search("([a-zA-Z][0-9])|([0-9][a-zA-Z])", formula):
        print("Invalid identifier")
        return
    formula_list = re.findall(r"[+\-/*]|[0-9]+|[a-zA-Z]+|[\(\)]", formula)
    if formula.replace(" ", "") == "".join(formula_list):
        print(formula_list)
    else:
        print("Incorrect")


formula = input()
break_formula_into_list(formula)
