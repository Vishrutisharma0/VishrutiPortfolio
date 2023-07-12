from flask import Flask, render_template,abort

app=Flask(__name__)


projects = [
    {
        "name": "MindSpire",
        "thumb": "img/mindspire.png",
        "hero": "img/mindspire.png",
        "categories": ["python", "web"],
        "slug": "mindspire",
        "prod": "https://mindspire-icrj.onrender.com",
    },
    {
        "name": "CinemaLog",
        "thumb": "img/cinemalog.png",
        "hero": "img/cinemalog.png",
        "categories": ["python", "web"],
        "slug": "cinemalog",
        "prod": "https://cinemalog.onrender.com",
    },
    {
        "name": "TextCloak",
        "thumb": "img/textcloak.png",
        "hero": "img/textcloak.png",
        "categories": ["python","web"],
        "slug": "textcloak",
        "prod": "https://github.com/Vishrutisharma0/TextCloak",
    },
    
]

slug_to_project = {project["slug"]: project for project in projects}

@app.route("/")
def home():
    return render_template("home.html", projects=projects)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    return render_template(f"{slug}.html", project=slug_to_project[slug])   

