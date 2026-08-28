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
        <a href="../"><p style="text-align: center;">&lt- Return home</p></a>
    </body>
</html>"""
    )
