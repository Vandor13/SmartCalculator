import re

var_dict = {}


# write your code here
def calculation(list_of_operations):
    subtraction = False
    result = 0
    for operation in list_of_operations:
        if operation.lstrip("+-").isnumeric():
            if subtraction:
                result -= int(operation)
            else:
                result += int(operation)
            subtraction = False
        elif operation == " ":
            continue
        elif re.fullmatch(r"[a-zA-Z]+", operation):
            if operation in var_dict.keys():
                if subtraction:
                    result -= int(var_dict[operation])
                else:
                    result += int(var_dict[operation])
                subtraction = False
            else:
                print("Unknown variable")
                return
        else:
            for sign in operation:
                if sign == "-":
                    subtraction = not subtraction
    print(result)


def calculate_postfix(postfix: list):
    calculation_stack = list()
    for item in postfix:
        if isinstance(item, int):
            calculation_stack.append(item)
        else:
            if len(calculation_stack) < 2:
                print("Invalid expression")
                return
            number1 = calculation_stack.pop()
            number2 = calculation_stack.pop()
            if item == "+":
                calculation_stack.append(number1 + number2)
            elif item == "-":
                calculation_stack.append(number2 - number1)
            elif item == "*":
                calculation_stack.append(number1 * number2)
            elif item == "/":
                calculation_stack.append(number2 // number1)
    return calculation_stack.pop()


def infix_to_postfix(infix_string) -> list:
    infix_list = break_formula_into_list(infix_string)
    operator_precedence = {
        "+": 0,
        "-": 0,
        "*": 1,
        "/": 1
    }
    if not infix_list:
        return None
    postfix = list()
    operator_stack = list()
    for item in infix_list:
        item_type = define_symbol_type(item)
        if item_type == "number":
            postfix.append(int(item))
        elif item_type == "word":
            dict_item = var_dict.get(item)
            if dict_item:
                postfix.append(int(dict_item))
            else:
                print("Unknown variable")
                return None
        elif item_type == "operator":
            if len(operator_stack) == 0 or operator_stack[-1] == "(":
                operator_stack.append(item)
            else:
                old_operator = operator_stack[-1]
                if operator_precedence[item] > operator_precedence[old_operator]:
                    operator_stack.append(item)
                else:
                    while True:
                        postfix.append(operator_stack.pop())
                        if len(operator_stack) == 0 or \
                                operator_stack[-1] == "(" or \
                                operator_precedence[item] > operator_precedence[operator_stack[-1]]:
                            break
                    operator_stack.append(item)
        elif item == "(":
            operator_stack.append(item)
        elif item == ")":
            if len(operator_stack) == 0:
                print("Invalid expression")
                return None
            old_operator = operator_stack.pop()
            while old_operator != "(":
                if len(operator_stack) == 0:
                    print("Invalid expression")
                    return None
                postfix.append(old_operator)
                old_operator = operator_stack.pop()
    while len(operator_stack) > 0:
        postfix.append(operator_stack.pop())
    return postfix


def break_formula_into_list(formula: str) -> list:
    if re.search("([a-zA-Z][0-9])|([0-9][a-zA-Z])", formula):
        print("Invalid identifier")
        return None
    if re.search(r"(\*\*)|(//)", formula):
        print("Invalid expression")
        return None
    formula_list = re.findall(r"[+\-/*]|[0-9]+|[a-zA-Z]+|[\(\)]", formula)
    if formula.replace(" ", "") == "".join(formula_list):
        return formula_list
    else:
        print("Incorrect")
        return None


#     formula_list = list()
#     current_symbol_type = None
#     symbol_memory = None
#     number_open_brackets = 0
#
#     for symbol in formula:
#         symbol_type = define_symbol_type(symbol)
#         if not current_symbol_type:
#             if symbol_type in ["digit", "letter"]:
#                 current_symbol_type = symbol_type
#                 symbol_memory = str(symbol)
#                 continue
#             else:
#                 if current_symbol_type and current_symbol_type != symbol_type:
#                     if current_symbol_type == "digit":
#
#
#
def define_symbol_type(symbol: str) -> str:
    parant = ["(", ")"]
    operator = ["+", "-", "*", "/"]

    if symbol in parant:
        return "parant"
    elif symbol.isnumeric():
        return "number"
    elif symbol in operator:
        return "operator"
    elif re.fullmatch("[a-zA-Z]+", symbol):
        return "word"
    else:
        return "unknown"


def var_determination(var_string):
    string_parts = var_string.split("=")
    if len(string_parts) != 2:
        print("Invalid assignment")
        return
    match_var_name = re.fullmatch(r"[a-zA-Z]+", string_parts[0])
    # print("Var valid:", bool(match_var_name))
    match_assignment = re.fullmatch(r"([a-zA-Z]+)|([\+\-]?\d+)", string_parts[1])
    # print("Assignment valid:", bool(match_assignment))
    if not match_var_name:
        print("Invalid identifier")
        return
    if not match_assignment:
        print("Invalid assignment")
        return
    if string_parts[1].lstrip("+-").isnumeric():
        var_dict[string_parts[0]] = string_parts[1]
    else:
        if string_parts[1] in var_dict.keys():
            var_dict[string_parts[0]] = var_dict[string_parts[1]]
        else:
            print("Unknown variable")


while True:
    user_input = input()
    input_list = list(user_input.split(" "))
    user_input_cleaned = user_input.replace(" ", "")
    if user_input.count("=") >= 1:
        var_determination(user_input_cleaned)
    elif len(input_list) >= 2:
        postfix_list = infix_to_postfix(user_input)
        if postfix_list:
            result = calculate_postfix(postfix_list)
            if result or result == 0:
                print(result)
    elif len(input_list) == 1:
        if input_list[0] == "/exit":
            break
        elif input_list[0] == "/help":
            print("The program calculates formulas includin +-*/()")
        elif input_list[0].lstrip("+-").isnumeric():
            print(int(input_list[0]))
        elif input_list[0].startswith("/"):
            print("Unknown command")
        elif input_list[0] in var_dict.keys():
            print(var_dict[input_list[0]])
        elif re.fullmatch(r"[a-zA-Z]+", input_list[0]):
            print("Unknown variable")
        elif input_list[0] != "":
            print("Invalid identifier")
print("Bye!")
