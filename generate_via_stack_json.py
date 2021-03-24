# this script takes all keyboard definitions from the VIA src repository
# and generates one big json stack for Vial that is used to identify boards

import os
import json
import git   # requires GitPython

json_files = []

git.Git("./").clone("https://github.com/the-via/keyboards.git")

for subdir, dirs, files in os.walk("./keyboards/src"):
    for filename in files:
        path = os.path.join(subdir, filename)
        if path.endswith(".json"):
            json_files.append(path)

definitions = {"definitions": {}}

for keyboard in sorted(json_files):
    try:
        with open(keyboard, "r") as jf:
            keyboard_data = json.load(jf)
            jf.close()
        vendor_id = int(keyboard_data["vendorId"], 16)
        product_id = int(keyboard_data["productId"], 16)
        via_id = vendor_id * 65536 + product_id
        definitions["definitions"][str(via_id)] = keyboard_data
    except Exception as e:
        print("WARN", keyboard, e)
        continue

with open("./via_keyboard_stack.json", "w") as vf:
    vf.write(json.dumps(definitions, indent=2, sort_keys=True))
    vf.close()
