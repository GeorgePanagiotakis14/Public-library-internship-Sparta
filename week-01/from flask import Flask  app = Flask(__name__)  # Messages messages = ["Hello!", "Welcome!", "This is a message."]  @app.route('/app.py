from flask import Flask

app = Flask(__name__)

# Messages
messages = ["Hello!", "Welcome!", "This is a message."]

@app.route('/')
def home():
    return "<br>".join(messages)

if __name__ == '__main__':
    app.run(debug=True)
