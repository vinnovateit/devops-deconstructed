from flask import Flask
import time

app = Flask(__name__)
start_time = time.time()

@app.route('/')
def hello_world():
    return f"<h1>Hello from my local machine!</h1><p>Uptime: {int(time.time() - start_time)} seconds.</p>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
