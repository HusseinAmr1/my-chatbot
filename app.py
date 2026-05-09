from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = "secret123"

@app.route("/", methods=["GET", "POST"])
def home():

    if "chat" not in session:
        session["chat"] = []

    if request.method == "POST":
        user_message = request.form.get("message")

        if user_message:
            session["chat"].append({"user": user_message})

            if user_message.lower() == "hello":
                bot_response = "Hi!"
            elif user_message.lower() == "how are you":
                bot_response = "I'm fine 😊"
            else:
                bot_response = "I don't understand you."

            session["chat"].append({"bot": bot_response})
            session.modified = True

    return render_template("index.html", chat=session["chat"])

if __name__ == "__main__":
    app.run(debug=True)