from app.db.session import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db      # Yielding the database session for use in API endpoints
    finally:
        db.close()