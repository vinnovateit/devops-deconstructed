import time
import redis
import os
from flask import Flask

app = Flask(__name__)

cache = redis.Redis(host=os.environ.get('REDIS_HOST', 'redis'), port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return f"<h1>Hello REDIS!</h1><p>I have been seen {count} times.</p>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
