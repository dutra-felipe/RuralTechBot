import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import SQLAlchemyError
from database.models import Base, Feedback, Contact
from config import DB_URL


class DatabaseManager:
    def __init__(self, db_uri=DB_URL):
        self.engine = create_engine(db_uri)
        self.Session = scoped_session(sessionmaker(bind=self.engine))
        
    def init_db(self):
        """Initialize the database by creating all tables"""
        Base.metadata.create_all(self.engine)
        logging.info("Database initialized")
    
    def get_session(self):
        """Get a new session"""
        return self.Session()
    
    def close_sessions(self):
        """Close all sessions"""
        self.Session.remove()
    
    # Feedback querys
    def save_feedback(self, user_id, name, feedback_text):
        """Save feedback to database"""
        session = self.get_session()
        try:
            feedback = Feedback(
                user_id=user_id,
                name=name,
                feedback=feedback_text
            )
            session.add(feedback)
            session.commit()
            return True
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f"Error saving feedback: {e}")
            return False
        finally:
            session.close()
    
    def get_all_feedbacks(self):
        """Get all feedbacks"""
        session = self.get_session()
        try:
            return session.query(Feedback).all()
        except SQLAlchemyError as e:
            logging.error(f"Error retrieving feedbacks: {e}")
            return []
        finally:
            session.close()
    
    # Contato querys
    def save_contact(self, user_id, name, email, message):
        """Save contact to database"""
        session = self.get_session()
        try:
            contact = Contact(
                user_id=user_id,
                name=name,
                email=email,
                message=message
            )
            session.add(contact)
            session.commit()
            return True
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f"Error saving contact: {e}")
            return False
        finally:
            session.close()
    
    def get_all_contacts(self):
        """Get all contacts"""
        session = self.get_session()
        try:
            return session.query(Contact).all()
        except SQLAlchemyError as e:
            logging.error(f"Error retrieving contacts: {e}")
            return []
        finally:
            session.close()

db_manager = DatabaseManager()