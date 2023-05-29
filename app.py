from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)


@app.route('/api/random_array', methods=['POST'])
def random_array():
    sentence = request.json['sentence']

    # Tokenize the sentence into words
    words = sentence.split()

    # Generate a random 500-dimensional array of floats
    random_array = np.random.rand(500).tolist()

    return jsonify(random_array)


if __name__ == '__main__':
    app.run()
