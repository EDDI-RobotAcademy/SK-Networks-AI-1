REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = os.getenv('REDIS_PORT')
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD')

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f'redis://{REDIS_HOST}:{REDIS_PORT}/0',  # Redis의 0번 DB를 사용합니다. 필요에 따라 DB 번호를 수정할 수 있습니다.
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'PASSWORD': REDIS_PASSWORD,  # Redis 비밀번호를 설정합니다.
            'SOCKET_CONNECT_TIMEOUT': 5,  # Redis 서버와의 연결 시도 제한 시간을 설정합니다.
        }
    }
}
INSTALLED_APPS = [
    'django_extensions',
]