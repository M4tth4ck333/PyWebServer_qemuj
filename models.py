from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import create_engine
import datetime

Base = declarative_base()

class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    level = Column(Integer, default=1)
    xp = Column(Float, default=0.0)

class PlasticResource(Base):
    __tablename__ = 'plastic_resources'
    id = Column(Integer, primary_key=True)
    type = Column(String(50))  # e.g., PET, HDPE, LDPE
    weight_grams = Column(Float)
    collected_at = Column(DateTime, default=datetime.datetime.utcnow)
    player_id = Column(Integer, ForeignKey('players.id'))

class MathDiscovery(Base):
    __tablename__ = 'math_discoveries'
    id = Column(Integer, primary_key=True)
    manifold_type = Column(String(100)) # e.g., Riemannian, Pseudo-Riemannian
    curvature_metric = Column(Float)
    coordinates = Column(String(100)) # abstract representation
    discovered_at = Column(DateTime, default=datetime.datetime.utcnow)
    player_id = Column(Integer, ForeignKey('players.id'))

# Database setup
engine = create_engine('sqlite:///game.db')

def init_db():
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    init_db()
    print("Database initialized.")
