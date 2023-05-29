# Problem
Use a web framework of your choice (Flask, Django, FastAPI, etc) to develop a single
production-quality API endpoint that takes a sentence as input and returns a random 500
dimensional array of floats. For example:
Input: “This is an example sentence”
Output: [1.32, 0.393, .... 0.9312]
Accompanying your code submission, please write a short statement justifying the
considerations you took to make your solution production-quality. What tests and checks
would you do to ensure this fits the purpose?

# Setup
- pip install flask flask-testing numpy

# App
- The API will start running on the local server. You can then send a POST request to the endpoint http://localhost:5000/api/random_array with a JSON payload containing the sentence:
- Attached Sample.json
- The API will respond with a JSON object containing the random 500-dimensional array of floats:
- Attached Sample_out.json


# App test
- A single test method test_random_array_endpoint. Within this test method, we prepare the request payload as a dictionary, send a POST request to the /api/random_array endpoint, and perform various assertions on the response.
- We check the response status code, content type, and validate the structure and data of the response JSON. Specifically, we ensure that the response data is a list with 500 elements, and each element is a float.
- To run the test, execute the script. The unittest.main() function discovers the test cases within the file and runs them.
- Installed before running the test (pip install flask flask-testing numpy).
