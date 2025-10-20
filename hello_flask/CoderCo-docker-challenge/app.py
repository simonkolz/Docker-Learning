import os
from flask import Flask
import redis

app = Flask(__name__)
redis_host = os.getenv('REDIS_HOST', 'redis')
redis_port =int(os.getenv('REDIS_PORT', 6379 ))
# Connect to Redis
# (use "redis" as the hostname if you use Docker Compose)
r = redis.Redis(host=redis_host, port=redis_port)

@app.route('/')
def home():
    return "Welcome to the Flask + Redis app!"

@app.route('/count')
def count():
    visits = r.incr('visits')  # increment the "visits" key by 1
    return f"This page has been visited {visits} times."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
