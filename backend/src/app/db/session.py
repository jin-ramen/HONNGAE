from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import Settings

engine = create_engine(
    Settings.database_url,
    echo=Settings.db_echo,
    pool_pre_ping=Settings.db_pre_ping
)

Session = sessionmaker(engine)