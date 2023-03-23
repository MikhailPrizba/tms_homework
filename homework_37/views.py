
def calculate(string_command:str) -> str:
    operators_all = {
        '+': lambda x,y: x + y,
        '-': lambda x,y: x - y,
        '/': lambda x,y: x / y,
        '*': lambda x,y: x * y,
    }
    try:
        val1, operators, val2 = string_command.split()
        answer = operators_all[operators](float(val1), float(val2))
    except Exception:
        answer = ' '
    return str(answer)
