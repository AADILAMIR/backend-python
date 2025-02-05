from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import logging

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.DEBUG)  # Change to DEBUG for detailed logs
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)  # To allow unrestricted access from any origin

try:
    mongo_uri = os.getenv('MONGO_URI')
    logger.debug(f"Connecting to MongoDB at {mongo_uri}")
    mongo_client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)
    mongo_client.server_info()  # Trigger a connection test
    db = mongo_client['mydatabase']
    collection = db['mycollection']
    logger.info("Connected to MongoDB successfully")
except Exception as e:
    logger.error(f"Error connecting to MongoDB: {e}")
    raise SystemExit("Exiting application due to MongoDB connection failure.")

@app.route('/api/')
def index():
    logger.debug("Accessed index route")
    return jsonify({"message": "Welcome to the Python Flask API!"})

@app.route('/api/add')
def add_data():
    try:
        # Example MongoDB write
        data = {"name": "example", "value": "Hello MongoDB"}
        collection.insert_one(data)
        logger.debug("Inserted data into MongoDB")

        return jsonify({"message": "Data added to MongoDB!"})
    except Exception as e:
        logger.error(f"Error in add_data route: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/data')
def get_data():
    try:
        # Fetch data from MongoDB
        mongo_data = list(collection.find({}, {"_id": 0}))
        logger.debug("Fetched data from MongoDB")

        return jsonify({"source": "database", "data": mongo_data})
    except Exception as e:
        logger.error(f"Error in get_data route: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/mongo-test')
def mongo_test():
    try:
        # Test MongoDB connection
        test_data = {"test_key": "test_value"}
        collection.insert_one(test_data)
        logger.debug("Inserted test data into MongoDB")
        return jsonify({"message": "MongoDB is working!"})
    except Exception as e:
        logger.error(f"MongoDB test failed: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    flask_host = os.getenv('FLASK_RUN_HOST', '0.0.0.0')
    flask_port = int(os.getenv('FLASK_RUN_PORT', 8000))
    logger.info(f"Starting Flask app on {flask_host}:{flask_port}")
    app.run(host=flask_host, port=flask_port)
