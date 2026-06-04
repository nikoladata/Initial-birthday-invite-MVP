from flask import Flask, render_template, abort

app = Flask(__name__)

INVITATIONS = {
    "lenka-prvi-rodjendan": {
        "type": "birthday",
        "child_name": "Ленка",
        "title": "Ленкин први рођендан",
        "date": "19. jul 2026.",
        "time": "17:00",
        "place": "Гуњетинац плус",
        "address": "Власотинце",
        "maps_url": "https://maps.google.com",
        "form_url": "https://forms.gle/C45QD2WVDoX8piz67",
        "message": "Дођите да заједно прославимо Ленкин први рођендан, уз осмехе, игру и пуно љубави 💕"
    },

    "andrej-andjela": {
        "type": "wedding",
        "groom": "Андреј",
        "bride": "Анђела",
        "title": "Андреј и Анђела",
        "date": "20. септембар 2026.",
        "datetime": "2026-09-20T15:00:00",
        "church_time": "15:00",
        "church": "Црква Свете Тројице",
        "restaurant_time": "17:30",
        "restaurant": "Бавка скај",
        "address": "Власотинце",
        "maps_url": "https://maps.google.com",
        "form_url": "TVOJ_GOOGLE_FORM_LINK",
        "message": "Са великом радошћу Вас позивамо да будете део нашег најлепшег дана и да са нама прославите почетак заједничког живота."
    }
}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/<slug>")
def invite(slug):
    invitation = INVITATIONS.get(slug)

    if not invitation:
        abort(404)

    if invitation["type"] == "birthday":
        return render_template("birthday.html", invitation=invitation)

    if invitation["type"] == "wedding":
        return render_template("wedding.html", invitation=invitation)

    abort(404)

if __name__ == "__main__":
    app.run(debug=True)