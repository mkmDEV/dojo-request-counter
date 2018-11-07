from flask import Flask, request, url_for, render_template

app = Flask(__name__)
counts = 0

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/request-counter', methods=['GET', 'POST'])
def request_counter(counts):
    if request.method == 'GET':
        counts += 1
        return counts


if __name__ == '__main__':
    app.run(
        debug=True
    )
