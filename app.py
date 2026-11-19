from flask import Flask
app =Flask(__name__)

@app.route('/')
def home():
    return "Hello from multi stage pipeline"

if __name__ == '__main__':
    app.run(debug=True)
