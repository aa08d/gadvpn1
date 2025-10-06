from datetime import datetime, UTC

from uuid6 import uuid7
from sqlalchemy import Column, UUID, String, Numeric, BigInteger, Date, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid7)
    first_name = Column(String(150))
    last_name = Column(String(150), nullable=True)
    role = Column(String(100), default="member")
    language_code = Column(String(2), default="en")

    wallet = relationship("Wallet", back_populates="user", uselist=False)
    referrals = relationship("Referral", back_populates="from_user", cascade="all, delete-orphan")
    telegram = relationship("TelegramAccount", back_populates="user", uselist=False)


class Referral(Base):
    __tablename__ = "referrals"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid7)
    profit = Column(Numeric(precision=10, scale=2), default=0)
    referred_at = Column(Date, default=lambda: datetime.now(UTC).date())

    from_user = relationship("User", back_populates="referrals")
    from_user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))


class Wallet(Base):
    __tablename__ = "wallets"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid7)
    balance = Column(Numeric(precision=10, scale=2), default=0)

    user = relationship("User", back_populates="wallet")
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    transactions = relationship("Transaction", back_populates="wallet", cascade="all, delete-orphan")


class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid7)
    amount = Column(Numeric(precision=10, scale=2), nullable=False)
    date = Column(Date, default=lambda: datetime.now(UTC).date())

    wallet = relationship("Wallet", back_populates="transactions")
    wallet_id = Column(UUID(as_uuid=True), ForeignKey("wallets.id"))


class TelegramAccount(Base):
    __tablename__ = "telegrams"

    id = Column(BigInteger, primary_key=True, unique=True)
    username = Column(String(32))

    user = relationship("User", back_populates="telegram")
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
