from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base


db = create_engine('sqlite:///mydatabase.db')

Session = sessionmaker(bind=db)
session = Session()



Base = declarative_base()

class User(Base):

    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

# CRUD Operations
def create_user(name, email, password):
    new_user = User(name=name, email=email, password=password)
    session.add(new_user)
    session.commit()
    return new_user

def get_user_by_email(email):
    return session.query(User).filter_by(email=email).first()

def update_user_email(user_id, new_email):
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        user.email = new_email
        session.commit()
    return user

def delete_user(user_id):
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        session.delete(user)
        session.commit()
    return user

if __name__ == '__main__':
    new_user1 = create_user(name='John Doe', email="johndoe142@gmail.com", password='securepassword') 
    new_user2 = create_user(name='Jane Smith', email="janesmith312@gmail.com", password='anotherpassword')
    print(f'Created User: {new_user1.name}, Email: {new_user1.email}, Password: {new_user2.password}')


Base.metadata.create_all(db)

