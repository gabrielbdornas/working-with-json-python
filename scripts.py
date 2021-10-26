# https://stackoverflow.com/a/13949837/11755155
import json

with open("json_file.json", "r+") as jsonFile:
    data = json.load(jsonFile)

    data["owner"] = "Jao e Maria"

    jsonFile.seek(0)  # rewind
    json.dump(data, jsonFile, indent=4)
    jsonFile.truncate()
