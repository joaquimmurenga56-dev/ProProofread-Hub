import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base configuration"""
    APP_ENV = os.getenv("APP_ENV", "development")
    APP_SECRET_KEY = os.getenv("APP_SECRET_KEY", "dev-secret-key-change-in-production")
    
    # PayPal Configuration
    PAYPAL_CLIENT_ID = os.getenv("PAYPAL_CLIENT_ID", "")
    PAYPAL_SECRET = os.getenv("PAYPAL_SECRET", "")
    PAYPAL_MODE = os.getenv("PAYPAL_MODE", "sandbox")
    
    # Stripe Configuration
    STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY", "")
    STRIPE_PUBLIC_KEY = os.getenv("STRIPE_PUBLIC_KEY", "")
    STRIPE_PRICE_ID_FULL_ACCESS = os.getenv("STRIPE_PRICE_ID_FULL_ACCESS", "")
    STRIPE_PRICE_ID_DAY_PASS = os.getenv("STRIPE_PRICE_ID_DAY_PASS", "")
    
    # Database Configuration
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///proproofread.db")
    
    # Free Tier Limits
    FREE_HUMAN_REVIEWS = 5
    FREE_AI_CHECKS = 5
    
    # Premium Features
    PREMIUM_UNLIMITED = True
    PREMIUM_PLAGIARISM_CHECK = True
    PREMIUM_EXPERT_ESCALATION = True
    PREMIUM_ADVANCED_TONES = True

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False

class TestingConfig(Config):
    """Testing configuration"""
    DEBUG = True
    TESTING = True
    DATABASE_URL = "sqlite:///:memory:"

def get_config():
    """Get configuration based on environment"""
    env = os.getenv("APP_ENV", "development")
    if env == "production":
        return ProductionConfig()
    elif env == "testing":
        return TestingConfig()
    return DevelopmentConfig()
