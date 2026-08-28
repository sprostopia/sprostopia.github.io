#For easily creating microblogs
import json, html, datetime

title = html.escape(input("Enter a post title:\n"))

#Use Ctrl + C to stop entering
message = ""
print("Message:")
while True:
    try:
        message += html.escape(input("> ")) + "<br>"
    except KeyboardInterrupt:
        break

message = message[:-4]

with open("docs/microblog/index.html", "r", encoding="UTF-8") as file:
    page = str(file.read())

    #Gets the ID of the last post and adds one
    newId = ""
    offset = page.find("<!-- Next Post -->")#  Ensures that it's only searching for the first id of the entries, not any other html element
    for digit in page[page[offset:].find("id=") + offset + 4:]:
        if digit in "0123456789":
            newId += digit
        else:
            break
    newId = int(newId) + 1

    #Creates the new post
    page = page.replace("<!-- Next Post -->",
    f"""<!-- Next Post -->
        <div class="entry" id="{newId}">
            <h2>{title}</h2>
            <h3><i>{datetime.datetime.now().strftime("%d/%m/%y, %H:%M:%S")} </i><a href="#{newId}">Shareable link</a></h3>
            <p>{message}</p>
        </div>      
    """)
with open("docs/microblog/index.html", "w") as file:
    file.write(page)