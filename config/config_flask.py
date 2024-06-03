import random
import string

random_str = string.ascii_letters + string.digits + string.ascii_uppercase


class Desenvolvimento(object):
    """Developmente configuration, uses to dev environment"""
    DEBUG = True
    SECRET_KEY = "".join(random.choice(random_str) for i in range(12))
    JWT_SECRET_KEY = "".join(random.choice(random_str) for i in range(15))
    SQLALCHEMY_DATABASE_URI = "sqlite:///dev.db"
    CORS_HEADERS = "application/json"
