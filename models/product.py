from sqlalchemy import Column, Integer, String, DECIMAL

from orm import Base

class Product(Base):

    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(DECIMAL, default=0)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price
        }