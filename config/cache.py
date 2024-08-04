""" Cache configuration """
from core.facades.env import env, int_env

host = env('REDIS_HOST', 'redis')
port = int_env('REDIS_PORT', '6379')
password = env('REDIS_PASSWORD', '')
