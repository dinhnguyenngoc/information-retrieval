# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, jsonify, request
from module.tfidf import initialize_spark, compute_similarity, stop_spark

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
spark = initialize_spark()

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'

@app.route('/api/data', methods=['GET'])
def get_data():
    sample_data = {
        'name': 'John Doe',
        'age': 30,
        'location': 'New York'
    }
    return jsonify(sample_data)

@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.json
    return jsonify({
        "message": "Data received successfully!",
        "data": data
    })

# @app.route('/api/search', methods=['POST'])
# def search():
#     data = request.json
#     return jsonify({
#         "message": "Data received successfully!",
#         "data": data
#     })

@app.route('/api/search', methods=['POST'])
def get_similarity():
    data = request.json
    query = data.get("query", "")
    
    if not query:
        return jsonify({"error": "Query is required"}), 400
    
    similarityDF = compute_similarity(spark, query)
    results = similarityDF.toPandas().to_dict(orient="records")
    
    return jsonify(results)

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    app.run()

    stop_spark(spark)
