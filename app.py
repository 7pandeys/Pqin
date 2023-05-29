from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/random_array', methods=['POST'])
def random_array():
    try:
        sentence = request.json.get('sentence')
        if not sentence:
            return jsonify({'error': 'Missing sentence parameter'}), 400

        array = generate_random_array()
        return jsonify(array)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

def generate_random_array():
    array = [random.uniform(0, 1) for _ in range(500)]
    return array

if __name__ == '__main__':
    app.run()
