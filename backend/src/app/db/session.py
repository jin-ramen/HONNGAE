from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

engine = create_engine(
    settings.database_url.unicode_string(),
    echo=settings.db_echo,
    pool_pre_ping=settings.db_pre_ping
)

Session = sessionmaker(engine)

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()