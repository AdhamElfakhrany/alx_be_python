import ast
import os

REQUIREMENTS = [
    "File exists and is not empty",
    "Definition of global conversion factors",
    "Implementation of conversion functions",
    "User interaction",
    "Implementation of ValueError"
]

def check_file_exists_and_not_empty(filepath):
    return os.path.isfile(filepath) and os.path.getsize(filepath) > 0

def check_global_conversion_factors(tree):
    factors = {"FAHRENHEIT_TO_CELSIUS", "CELSIUS_TO_FAHRENHEIT"}
    found = set()
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id in factors:
                    found.add(target.id)
    return factors == found

def check_conversion_functions(tree):
    functions = {"convert_to_celsius", "convert_to_fahrenheit"}
    found = set()
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in functions:
            found.add(node.name)
    return functions == found

def check_user_interaction(tree):
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            if node.func.id == "input":
                return True
    return False

def check_value_error(tree):
    for node in ast.walk(tree):
        if isinstance(node, ast.ExceptHandler):
            if getattr(node.type, 'id', None) == "ValueError":
                return True
    return False

def review_code(filepath):
    results = {}
    results[REQUIREMENTS[0]] = check_file_exists_and_not_empty(filepath)
    if not results[REQUIREMENTS[0]]:
        return results

    with open(filepath, "r", encoding="utf-8") as f:
        source = f.read()
    tree = ast.parse(source)

    results[REQUIREMENTS[1]] = check_global_conversion_factors(tree)
    results[REQUIREMENTS[2]] = check_conversion_functions(tree)
    results[REQUIREMENTS[3]] = check_user_interaction(tree)
    results[REQUIREMENTS[4]] = check_value_error(tree)
    return results

if __name__ == "__main__":
    filepath = "shop.py"
    review = review_code(filepath)
    for req, passed in review.items():
        print(f"{req}: {'✅' if passed else '❌'}")
