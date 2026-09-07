from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class AcceptedUser(Base):
    __tablename__ = "accepted_users"
    id = Column(Integer, primary_key=True)
    osu_id = Column(Integer, unique=True, nullable=False)
    osu_username = Column(String, nullable=False)
    role = Column(String, nullable=False)

class Captain(Base):
    __tablename__ = "captains"
    id = Column(Integer, primary_key=True)
    accepted_user_id = Column(Integer, ForeignKey("accepted_users.id"))
    tier = Column(String, nullable=False)
    seed = Column(Integer, nullable=False)
    budget_remaining = Column(Integer, default=60)
    accepted_user = relationship("AcceptedUser")

class Player(Base):
    __tablename__ = "players"
    id = Column(Integer, primary_key=True)
    osu_id = Column(Integer, unique=True, nullable=False)
    osu_username = Column(String, nullable=False)
    tier = Column(String, nullable=False)
    status = Column(String, default="queued")
    sold_to_id = Column(Integer, ForeignKey("captains.id"), nullable=True)
    sold_price = Column(Integer, nullable=True)

class Bid(Base):
    __tablename__ = "bids"
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey("players.id"))
    captain_id = Column(Intneger, ForeignKey("captains.id"))
    amount = Column(Integer, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

class AdminUser(Base):
    __tablename__ = "admin_users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)