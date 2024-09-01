import lang2json, json

output = {}

with open("en_US.lang", "r", encoding="utf-8") as file:
    output = lang2json.lang_to_json(file.readlines())

with open("en_US.json", "w") as file:
    file.write(json.dumps(output))