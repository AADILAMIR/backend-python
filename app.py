# from flask import Flask, jsonify, request
# from pymongo import MongoClient
# import redis
# from dotenv import load_dotenv
# import os

# # Load environment variables
# load_dotenv()

# app = Flask(__name__)

# # MongoDB connection
# mongo_uri = os.getenv('MONGO_URI')
# mongo_client = MongoClient(mongo_uri)
# db = mongo_client['mydatabase']
# collection = db['mycollection']

# # Redis connection
# redis_host = os.getenv('REDIS_HOST')
# redis_client = redis.StrictRedis(host=redis_host, port=6379, decode_responses=True)

# @app.route('/')
# def index():
#     return jsonify({"message": "Welcome to the Python Flask API!"})

# @app.route('/add')
# def add_data():
#     user_ip = request.remote_addr  # Get user's IP address for rate limiting
#     rate_limit_key = f"rate_limit:{user_ip}"

#     # Increment request count in Redis
#     request_count = redis_client.incr(rate_limit_key)

#     if request_count == 1:
#         # Set expiration for the rate limit key (e.g., 60 seconds)
#         redis_client.expire(rate_limit_key, 60)

#     if request_count > 5:
#         return jsonify({"error": "Rate limit exceeded. Try again later."}), 429

#     # Example MongoDB write
#     data = {"name": "example", "value": "Hello MongoDB"}
#     collection.insert_one(data)

#     # Example Redis write
#     redis_client.set("example_key", "Hello Redis")

#     return jsonify({"message": "Data added to MongoDB and Redis!"})

# @app.route('/data')
# def get_data():
#     cache_key = "mongo_data_cache"

#     # Check Redis cache for the data
#     cached_data = redis_client.get(cache_key)
#     if cached_data:
#         # Return cached data if available
#         return jsonify({"source": "cache", "data": eval(cached_data)})

#     # Fetch data from MongoDB (cache miss)
#     mongo_data = list(collection.find({}, {"_id": 0}))

#     # Cache the MongoDB data in Redis for 60 seconds
#     redis_client.set(cache_key, str(mongo_data), ex=60)

#     return jsonify({"source": "database", "data": mongo_data})

# if __name__ == '__main__':
#     app.run(host=os.getenv('FLASK_RUN_HOST', '0.0.0.0'), port=int(os.getenv('FLASK_RUN_PORT', 8000)))
# from flask import Flask, jsonify, request
# from flask_cors import CORS
# from pymongo import MongoClient
# import redis
# from dotenv import load_dotenv
# import os

# # Load environment variables
# load_dotenv()

# app = Flask(__name__)

# # Enable CORS for all routes
# CORS(app)  # To allow unrestricted access from any origin

# # Alternatively, restrict CORS to a specific origin (e.g., frontend on localhost:3000)
# # CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

# # MongoDB connection
# mongo_uri = os.getenv('MONGO_URI')
# mongo_client = MongoClient(mongo_uri)
# db = mongo_client['mydatabase']
# collection = db['mycollection']

# # Redis connection
# redis_host = os.getenv('REDIS_HOST')
# redis_client = redis.StrictRedis(host=redis_host, port=6379, decode_responses=True)

# @app.route('/')
# def index():
#     return jsonify({"message": "Welcome to the Python Flask API!"})

# @app.route('/add')
# def add_data():
#     user_ip = request.remote_addr  # Get user's IP address for rate limiting
#     rate_limit_key = f"rate_limit:{user_ip}"

#     # Increment request count in Redis
#     request_count = redis_client.incr(rate_limit_key)

#     if request_count == 1:
#         # Set expiration for the rate limit key (e.g., 60 seconds)
#         redis_client.expire(rate_limit_key, 60)

#     if request_count > 5:
#         return jsonify({"error": "Rate limit exceeded. Try again later."}), 429

#     # Example MongoDB write
#     data = {"name": "example", "value": "Hello MongoDB"}
#     collection.insert_one(data)

#     # Example Redis write
#     redis_client.set("example_key", "Hello Redis")

#     return jsonify({"message": "Data added to MongoDB and Redis!"})

# @app.route('/data')
# def get_data():
#     cache_key = "mongo_data_cache"

#     # Check Redis cache for the data
#     cached_data = redis_client.get(cache_key)
#     if cached_data:
#         # Return cached data if available
#         return jsonify({"source": "cache", "data": eval(cached_data)})

#     # Fetch data from MongoDB (cache miss)
#     mongo_data = list(collection.find({}, {"_id": 0}))

#     # Cache the MongoDB data in Redis for 60 seconds
#     redis_client.set(cache_key, str(mongo_data), ex=60)

#     return jsonify({"source": "database", "data": mongo_data})

# @app.route('/redis-test')
# def redis_test():
#     try:
#         redis_client.ping()  # Test Redis connection
#         return jsonify({"message": "Redis is working!"})
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# @app.route('/mongo-test')
# def mongo_test():
#     try:
#         # Test MongoDB connection
#         test_data = {"test_key": "test_value"}
#         collection.insert_one(test_data)
#         return jsonify({"message": "MongoDB is working!"})
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == '__main__':
#     app.run(host=os.getenv('FLASK_RUN_HOST', '0.0.0.0'), port=int(os.getenv('FLASK_RUN_PORT', 8000)))
# from flask import Flask, jsonify, request
# from flask_cors import CORS
# from pymongo import MongoClient
# import redis
# from dotenv import load_dotenv
# import os
# import logging

# # Load environment variables
# load_dotenv()

# # Configure logging
# logging.basicConfig(level=logging.DEBUG)  # Change to DEBUG for detailed logs
# logger = logging.getLogger(__name__)

# app = Flask(__name__)

# # Enable CORS for all routes
# CORS(app)  # To allow unrestricted access from any origin

# try:
#     mongo_uri = os.getenv('MONGO_URI')
#     logger.debug(f"Connecting to MongoDB at {mongo_uri}")
#     mongo_client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)
#     mongo_client.server_info()  # Trigger a connection test
#     db = mongo_client['mydatabase']
#     collection = db['mycollection']
#     logger.info("Connected to MongoDB successfully")
# except Exception as e:
#     logger.error(f"Error connecting to MongoDB: {e}")
#     raise SystemExit("Exiting application due to MongoDB connection failure.")

# try:
#     # redis_host = os.getenv('REDIS_HOST')
#     # logger.debug(f"Connecting to Redis at {redis_host}:6379")
#     # redis_client = redis.StrictRedis(host=redis_host, port=6379, decode_responses=True)
#     # redis_client.ping()  # Test Redis connection
#     # logger.info("Connected to Redis successfully")
# except Exception as e:
#     logger.error(f"Error connecting to Redis: {e}")
#     raise SystemExit("Exiting application due to Redis connection failure.")

# @app.route('/')
# def index():
#     logger.debug("Accessed index route")
#     return jsonify({"message": "Welcome to the Python Flask API!"})

# @app.route('/add')
# def add_data():
#     user_ip = request.remote_addr  # Get user's IP address for rate limiting
#     logger.debug(f"User IP: {user_ip}")

#     rate_limit_key = f"rate_limit:{user_ip}"

#     try:
#         # Increment request count in Redis
#         request_count = redis_client.incr(rate_limit_key)
#         logger.debug(f"Request count for {user_ip}: {request_count}")

#         if request_count == 1:
#             # Set expiration for the rate limit key (e.g., 60 seconds)
#             redis_client.expire(rate_limit_key, 60)
#             logger.debug(f"Rate limit key {rate_limit_key} set with expiration of 60 seconds")

#         if request_count > 5:
#             logger.warning(f"Rate limit exceeded for IP: {user_ip}")
#             return jsonify({"error": "Rate limit exceeded. Try again later."}), 429

#         # Example MongoDB write
#         data = {"name": "example", "value": "Hello MongoDB"}
#         collection.insert_one(data)
#         logger.debug("Inserted data into MongoDB")

#         # Example Redis write
#         redis_client.set("example_key", "Hello Redis")
#         logger.debug("Set example_key in Redis")

#         return jsonify({"message": "Data added to MongoDB and Redis!"})
#     except Exception as e:
#         logger.error(f"Error in add_data route: {e}")
#         return jsonify({"error": str(e)}), 500

# @app.route('/data')
# def get_data():
#     cache_key = "mongo_data_cache"
#     logger.debug(f"Checking Redis cache for key: {cache_key}")

#     try:
#         # Check Redis cache for the data
#         # cached_data = redis_client.get(cache_key)
#         # if cached_data:
#         #     logger.debug("Cache hit - returning data from Redis")
#         #     return jsonify({"source": "cache", "data": eval(cached_data)})

#         # Fetch data from MongoDB (cache miss)
#         # logger.debug("Cache miss - fetching data from MongoDB")
#         mongo_data = list(collection.find({}, {"_id": 0}))
#         redis_client.set(cache_key, str(mongo_data), ex=60)
#         logger.debug("Cached MongoDB data in Redis")

#         return jsonify({"source": "database", "data": mongo_data})
#     except Exception as e:
#         logger.error(f"Error in get_data route: {e}")
#         return jsonify({"error": str(e)}), 500

# @app.route('/redis-test')
# def redis_test():
#     try:
#         redis_client.ping()  # Test Redis connection
#         logger.debug("Redis ping successful")
#         return jsonify({"message": "Redis is working!"})
#     except Exception as e:
#         logger.error(f"Redis test failed: {e}")
#         return jsonify({"error": str(e)}), 500

# @app.route('/mongo-test')
# def mongo_test():
#     try:
#         # Test MongoDB connection
#         test_data = {"test_key": "test_value"}
#         collection.insert_one(test_data)
#         logger.debug("Inserted test data into MongoDB")
#         return jsonify({"message": "MongoDB is working!"})
#     except Exception as e:
#         logger.error(f"MongoDB test failed: {e}")
#         return jsonify({"error": str(e)}), 500

# if __name__ == '__main__':
#     flask_host = os.getenv('FLASK_RUN_HOST', '0.0.0.0')
#     flask_port = int(os.getenv('FLASK_RUN_PORT', 8000))
#     logger.info(f"Starting Flask app on {flask_host}:{flask_port}")
#     app.run(host=flask_host, port=flask_port)
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

@app.route('/')
def index():
    logger.debug("Accessed index route")
    return jsonify({"message": "Welcome to the Python Flask API!"})

@app.route('/add')
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

@app.route('/data')
def get_data():
    try:
        # Fetch data from MongoDB
        mongo_data = list(collection.find({}, {"_id": 0}))
        logger.debug("Fetched data from MongoDB")

        return jsonify({"source": "database", "data": mongo_data})
    except Exception as e:
        logger.error(f"Error in get_data route: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/mongo-test')
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
