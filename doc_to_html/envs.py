
import os
import jinja2


template_loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
template_env = jinja2.Environment(loader=template_loader)
template = template_env.get_template("template.html")


html_start = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DOCUMENTATION</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #f2f2f2;
            padding: 10px;
            text-align: center;
        }
        footer {
            background-color: #f2f2f2;
            padding: 10px;
            text-align: center;
        }
    </style>
</head>
<body>
"""

html_end = """
<footer>
        <p>Generated by Tristan Giandoriggios's "doc_to_web"</p>
    </footer>
</body>
</html>
"""
