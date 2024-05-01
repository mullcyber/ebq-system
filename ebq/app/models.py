from datetime import datetime


from sqlalchemy import Float, Integer, String, Enum as SQLAEnum, DateTime, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped, mapped_column


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)


class ContactType(SQLAEnum):
    email = "email"
    sms = "sms"
    messenger = "messenger"


class Product(Base):
    __tablename__ = "product"
    name: Mapped[str] = mapped_column(String, nullable=False)
    request = relationship(back_populates="product")


class ProductRequest(Base):
    __tablename__ = "product_request"

    type_: Mapped[ContactType] = mapped_column(SQLAEnum(ContactType), nullable=False)
    value: Mapped[str] = mapped_column(String, nullable=False)

    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("product.id"), nullable=False)
    product_amount: Mapped[float] = mapped_column(Float, nullable=False)

    fabric: Mapped[str] = mapped_column(String, nullable=False)
    truck: Mapped[str] = mapped_column(String, nullable=False)
    create_date: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now)

    product = relationship(back_populates="request")
