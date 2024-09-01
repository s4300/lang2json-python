## Lang2JSON - Converts language files to JSON

def filter_line(line: str):
    """Filter a language file line."""
    return line.replace("\n", "").replace("\t", "").replace("  ", "").split("#")[0]

def lang_to_json(lines: list):
    """Convert lang to JSON"""
    output = {}
    for line in lines:
        if line.startswith("#") or "=" not in line: continue

        key = filter_line(line.split("=")[0])
        value = filter_line(line.split("=")[1])

        output[key] = value
    return output

def json_to_lang(dict: dict):
    """Convert JSON dictionary to lang"""
    result = ""
    for key in dict:
        value = dict[key]
        result += f"{key}={value}\n"
    return result
