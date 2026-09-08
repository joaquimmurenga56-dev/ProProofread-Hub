from sqlalchemy import create_engine, Column, String, DateTime, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from config import get_config

config = get_config()
engine = create_engine(config.DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class User(Base):
    """User model"""
    __tablename__ = "users"
    
    id = Column(String, primary_key=True)
    email = Column(String, unique=True)
    is_premium = Column(Boolean, default=False)
    premium_expires = Column(DateTime)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

class Submission(Base):
    """Submission model"""
    __tablename__ = "submissions"
    
    id = Column(String, primary_key=True)
    user_id = Column(String)
    submission_type = Column(String)
    text = Column(String)
    language = Column(String)
    status = Column(String, default="pending")
    result = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

class Payment(Base):
    """Payment model"""
    __tablename__ = "payments"
    
    id = Column(String, primary_key=True)
    user_id = Column(String)
    amount = Column(Integer)
    payment_method = Column(String)
    transaction_id = Column(String)
    status = Column(String, default="pending")
    created_at = Column(DateTime, default=datetime.now)

class ExpertReview(Base):
    """Expert review request model"""
    __tablename__ = "expert_reviews"
    
    id = Column(String, primary_key=True)
    user_id = Column(String)
    text = Column(String)
    review_type = Column(String)
    priority = Column(String)
    status = Column(String, default="pending")
    expert_id = Column(String)
    feedback = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    completed_at = Column(DateTime)

Base.metadata.create_all(engine)

def get_user(user_id):
    """Get user by ID"""
    session = Session()
    user = session.query(User).filter(User.id == user_id).first()
    session.close()
    return user

def create_user(user_id, email):
    """Create new user"""
    session = Session()
    user = User(id=user_id, email=email)
    session.add(user)
    session.commit()
    session.close()
    return user

def save_submission(user_id, submission_type, text, language):
    """Save submission to database"""
    session = Session()
    submission = Submission(
        user_id=user_id,
        submission_type=submission_type,
        text=text,
        language=language
    )
    session.add(submission)
    session.commit()
    session.close()
    return submission
