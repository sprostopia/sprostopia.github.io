import html

title = html.escape(input("Poem title:\n"))

#Use Ctrl + C to stop entering
poem = ""
print("Poem:")
while True:
    try:
        poem += html.escape(input("> ")) + "<br>"
    except KeyboardInterrupt:
        break

poem = poem[:-4]

with open(f"docs/poetry/{title.lower().replace(' ', '-')}.html", 'w', encoding="UTF-8") as f:
    f.write(
    f"""<!DOCTYPE html>
<html>
    <head>
        <title>{title}</title>
        <link rel="stylesheet" href="../house_style.css">
        <link rel="stylesheet" href="poetry.css">
    </head>
    <body>
        <h1><b>{title}</b></h1>
        <p>
            {poem}
        </p>
        <a href="index.html"><p style="text-align: center;">&lt- All poems</p></a>
    </body>
</html>"""
    )

with open("docs/poetry/index.html", "r") as f:
    page = f.read()
    page = page.replace("<!-- Next Poem-->",
f"""<tr>
                <td><a href="{title.lower().replace(' ', '-')}.html">{title}</a></td>
            </tr>
            <!-- Next Poem-->""")

with open("docs/poetry/index.html", "w") as f:
    f.write(page)