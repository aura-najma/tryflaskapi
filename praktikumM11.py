from flask import Flask, render_template, request, jsonify
import random


app = Flask(__name__)

default_messages = [
    "Makan patty itu SpongeBob.",
    "Berdansalah, Patrick.",
    "Squidward, mengapa selalu marah?",
    "Gary, apakah kamu lapar?",
    "Sandy, bagaimana kehidupan di bawah laut?",
    "Mr. Krabs, apakah Krabby Patty enak?",
    "Plankton, apa rencanamu kali ini?",
    "Kelpo, makanan sehat ala SpongeBob.",
    "Jellyfish Fields, tempat favorit SpongeBob.",
    "Krusty Krab, tempat bekerja SpongeBob."
]


@app.route("/post", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("nama")
        return render_template("selamatdatang.html", name=name)

    return render_template("form.html")

@app.route("/puja_kerang_ajaib", methods=["GET", "POST"])
@app.route("/puja_kerang_ajaib/<name>", methods=["GET", "POST"])
def puja_kerang_ajaib(name=None):
    if request.method == "GET":
        if name is None:
            response_message = random.choice(default_messages)
        else:
            response_message = f"{name}, {random.choice(default_messages)}"

        return jsonify({"message": response_message})

    elif request.method == "POST":
        name = request.form.get("nama")
        response_message = f"Selamat datang, {name}, anda berhasil masuk ke Puja Kerang Ajaib"
        return jsonify({"message": response_message})


#if __name__ == "__main__":
#    app.run(debug=True)
