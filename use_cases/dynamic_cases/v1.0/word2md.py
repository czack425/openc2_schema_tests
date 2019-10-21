import os
import pypandoc

md_files = []
formats = {
    # File format, Pandoc format
    "from": ("docx", "docx"),
    "to": ("md", "gfm")
}
doc = "UpdatedCases"


for root, dirs, files in os.walk("./"):
    for file in files:
        if file == f"{doc}.{formats['from'][0]}":
            print(f"Converting {doc}.{formats['from'][0]} to {doc}.{formats['to'][0]} in {root}")
            pypandoc.convert_file(
                source_file=os.path.join(root, f"{doc}.{formats['from'][0]}"),
                format=formats['from'][1],
                to=formats['to'][1],
                outputfile=os.path.join(root, f"{doc}.{formats['to'][0]}"),
            )