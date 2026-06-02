from flask import Flask, render_template, abort

app = Flask(__name__)

INVITATIONS = {
    "lenka-prvi-rodjendan": {
        "child_name": "Ленка",
        "title": "Ленкин први рођендан",
        "date": "19. јул 2026.",
        "time": "17:00",
        "place": "Гуњетинац плус",
        "address": "Власотинце",
        "maps_url": "https://maps.app.goo.gl/3TkwKwwdjUhteC14A",
        "form_url": "https://forms.gle/UTkQD7VPMT3sdT9VA",
        "message": "Наша мала Ленка пуни једну годину! Дођите да заједно прославимо њен први рођендан."
    }
}

@app.route("/")
def home():
    return "Wedding Invites MVP radi ✅"

@app.route("/<slug>")
def invite(slug):
    invitation = INVITATIONS.get(slug)

    if not invitation:
        abort(404)

    return render_template("birthday.html", invitation=invitation)

if __name__ == "__main__":
    app.run(debug=True)