from flask import Flask, render_template, jsonify
import redis

app = Flask(__name__)

# Connect to Redis (hostname matches the service name in docker-compose)
r = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)

@app.route('/')
def home():
    # Display the main page
    return render_template('index.html')

@app.route('/count')
def count():
    # Increment visit counter
    visits = r.incr('visits')
    # Render the classy HTML page instead of JSON
    return render_template('count.html', visits=visits)


@app.route('/get_count')
def get_count():
    # Get current count (without incrementing)
    visits = r.get('visits') or 0
    return jsonify({'visits': visits})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
