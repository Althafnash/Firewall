import yara
from YARA_RULES import yara_rules

def compile_rules(rules):
    try:
        compiled_rule = yara.compile(source=rules)
        return compiled_rule
    except yara.SyntaxError as e:
        print(f"Syntax error in YARA rule: {e}")
        raise e
    except Exception as e:
        print(f"Error compiling YARA rules: {e}")
        raise e

def scan_file(compiled_rule, file_path):
    try:
        matches = compiled_rule.match(file_path)
        if matches:
            print("Matched rules:")
            for match in matches:
                print(f"Rule: {match.rule}")
            return matches  # Return matches for further processing
        else:
            print("No matches found")
            return None  # Return None if no matches found
    except Exception as e:
        print(f"Error scanning file: {e}")
        raise e
