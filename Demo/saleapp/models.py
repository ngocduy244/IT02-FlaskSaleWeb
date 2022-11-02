from sqlalchemy import Column, Integer, String, Float, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from saleapp import app, db

class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)

class Category(BaseModel):
    __tabname__ = 'category'

    name = Column(String(50), nullable=False)

    def __str__(self):
        return self.name


class Product(BaseModel):
    __tabname__ = 'product'

    name = Column(String(50), nullable=False)
    description = Column(Text)
    price = Column(Float, default=0)
    image = Column(String(100))
    active = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name




if __name__ == "__main__":
    with app.app_context():
        # c1 = Category(name="Điện thoại");
        # c2 = Category(name="Máy tính bảng");
        # c3 = Category(name="Phụ kiện");
        p1 = Product(name="IPhone 14",
                     description="Apple, 128GB, RAM: 6GB",
                     price=24000000,
                     image="https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729569/fi9v6vdljyfmiltegh7k.jpg",
                     category_id=1);
        p2 = Product(name="IPhone 13 Pro",
                     description="Apple, 128GB, RAM: 6GB",
                     price=18000000,
                     image="https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
                     category_id=1);
        p3 = Product(name="Galaxy Note 10",
                     description="Samsung, 128GB, RAM: 6GB",
                     price=2000000,
                     image="https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
                     category_id=1);
        db.session.add_all([p1,p2,p3])
        db.session.commit()
        # db.create_all()
        # P@ssW0rd