class BaseConfig:
    """Base configuration"""
    DEBUG = False
    TESTING = False


class DevelopmentConfig(BaseConfig):
    """Development Configuration"""
    DEBUG = True


class TestingConfig(BaseConfig):
    DEBUG = True
    TESTING = True


class ProductionConfig(BaseConfig):
    """Production Configuration"""
    DEBUG = False
