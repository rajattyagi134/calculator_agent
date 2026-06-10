import math


def calculate(expression):

    allowed_names = {
        "sqrt": math.sqrt,
        "pow": pow,
        "abs": abs,
        "round": round
    }

    try:

        result = eval(
            expression,
            {"__builtins__": {}},
            allowed_names
        )

        return result

    except Exception as e:

        return f"Calculation Error: {e}"