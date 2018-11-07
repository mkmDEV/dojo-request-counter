from flask import Flask

app = Flask(__name__)
counts = 0

@app.route('/')
def home()
    return f"<h1><center>Visitors: {counts}"


@app.route('/request-counter', methods=['GET', 'POST'])
def request_counter()
    return counter += 1


if __name__ == '__main__':
    app.run(
        debug=True
    )
