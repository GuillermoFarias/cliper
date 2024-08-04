""" Cache configuration """
from core.facades.env import env

database_uri = env('DATABASE_URI', 'mongodb://localhost:27017')
max_pool_size = env('DATABASE_MAX_POOL_SIZE', 10)
