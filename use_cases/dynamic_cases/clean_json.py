import json
import os


for root, dirs, files in os.walk("./"):
    for file in files:
        if file.endswith(".json"):
            src = os.path.join(root, file)
            with open(src, "r") as f:
                src_str = f.read()
                try:
                    src_obj = json.loads(src_str)
                except Exception as e:
                    src_obj = None

            if src_obj:
                clean_obj = json.dumps(src_obj, indent=2)
                if src_str != clean_obj:
                    print(f"Cleaning {src}")
                    with open(src, "w") as f:
                        f.write(clean_obj)
