from flask import Flask, render_template, request, session
import google.generativeai as genai
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-flash-latest")

@app.route("/", methods=["GET", "POST"])
def home():

    # 🧠 لو مفيش history نعمله
    if "chat" not in session:
        session["chat"] = []

    if request.method == "POST":
        user_message = request.form.get("message")

        if user_message:
            try:
                response = model.generate_content(user_message).text
            except:
                response = "Error getting response"

            # 💾 نحفظ الرسائل
            session["chat"].append(("user", user_message))
            session["chat"].append(("bot", response))
            session.modified = True

    return render_template("index.html", chat=session["chat"])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
