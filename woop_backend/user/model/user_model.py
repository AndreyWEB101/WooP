from core.database import Base
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import String,func
from datetime import datetime


class User(Base):
    __tablename__="users"
    id:Mapped[int]=mapped_column(primary_key=True)
    email:Mapped[str]=mapped_column(String(100),index=True,unique=True)
    password_hash:Mapped[str]=mapped_column(String(128))
    user_name:Mapped[str|None]=mapped_column(String(100))

    created_at:Mapped[datetime]=mapped_column(server_default=func.now(),nullable=False)