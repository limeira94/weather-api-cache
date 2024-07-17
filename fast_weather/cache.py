import redis
import os
from dotenv import load_dotenv

load_dotenv()

redis_host = os.getenv('REDIS_HOST')
redis_port = os.getenv('REDIS_PORT')
redis_db = os.getenv('REDIS_DB')

cache = redis.Redis(host=redis_host, port=redis_port, db=redis_db)

def set_cache(key, value, expire):
    cache.set(key, value, ex=expire)
    
    
def get_cache(key):
    return cache.get(key)
