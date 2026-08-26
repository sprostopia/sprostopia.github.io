#For easily creating microblogs
import json, html, datetime

title = html.escape(input("Enter a post title:\n"))
message = html.escape(input("Message:\n")).replace("\\n", "<br>")


with open("docs/microblog/index.html", "r") as file:
    page = str(file.read())
    page = page.replace("<!-- Next Post -->",
    f"""
    <!-- Next Post -->
    <div class="entry">
        <h2>{title}</h2>
        <h3><i>{datetime.datetime.now().strftime("%d/%m/%y, %H:%M:%S")}</i></h3>
        <p>{message}</p>
    </div>      
    """)
with open("docs/microblog/index.html", "w") as file:
    file.write(page)