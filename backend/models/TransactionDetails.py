from sqlalchemy import Integer, DECIMAL, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship, mapped_column
from models.Base import Base


class TransactionDetails(Base):
    __tablename__ = "transaction_details"
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    transaction_id = mapped_column(Integer, ForeignKey("transactions.id"))
    product_id = mapped_column(Integer, ForeignKey("products.id"))
    quantity = mapped_column(Integer)
    price = mapped_column(DECIMAL(10, 2))
    created_at = mapped_column(DateTime, default=func.now())
    updated_at = mapped_column(DateTime, default=func.now(), onupdate=func.now())

    transaction = relationship("Transactions", back_populates="transaction_details")
    product = relationship("Products", back_populates="transaction_details")