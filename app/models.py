from enum import auto

import sqlalchemy
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from .database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    inserted_at = Column(DateTime, nullable=False)
    modified_at = Column(DateTime)
    category1 = Column(String(45))
    category2 = Column(String(45))
    category3 = Column(String(45))
    item_code = Column(String(45))
    name = Column(String(100), nullable=False)
    detail = Column(String(100))
    unit_volume = Column(String(45))
    unit_weight = Column(String(45))
    memo = Column(String(200))
    is_deleted = Column(Boolean, nullable=False, default=False)
    deleted_at = Column(DateTime)


class Warehouse(Base):
    __tablename__ = "warehouses"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    inserted_at = Column(DateTime, nullable=False)
    modified_at = Column(DateTime)
    name = Column(String(100), nullable=False)
    address = Column(String(200))
    memo = Column(String(200))
    is_deleted = Column(Boolean, nullable=False, default=False)
    deleted_at = Column(DateTime)


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    inserted_at = Column(DateTime, nullable=False)
    modified_at = Column(DateTime)
    name = Column(String(100), nullable=False)
    address = Column(String(200))
    phone_number = Column(String(45))
    manager = Column(String(45))
    memo = Column(String(200))
    is_deleted = Column(Boolean, nullable=False, default=False)
    deleted_at = Column(DateTime)


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    inserted_at = Column(DateTime, nullable=False)
    modified_at = Column(DateTime)
    name = Column(String(45), nullable=False)
    position = Column(String(45))
    phone_number = Column(String(45))
    email = Column(String(100))
    memo = Column(String(200))
    is_deleted = Column(Boolean, nullable=False, default=False)
    deleted_at = Column(DateTime)


class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    inserted_at = Column(DateTime, nullable=False)
    modified_at = Column(DateTime)
    name = Column(String(45), nullable=False)
    unit_volume = Column(String(45))
    unit_weight = Column(String(45))
    memo = Column(String(200))
    is_deleted = Column(Boolean, nullable=False, default=False)
    deleted_at = Column(DateTime)


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    inserted_at = Column(DateTime, nullable=False)
    modified_at = Column(DateTime)
    is_inbound = Column(Boolean, nullable=False)
    received_at = Column(DateTime)
    target_company_id = Column(Integer, nullable=False)
    expected_at = Column(DateTime)
    total_price = Column(Integer)
    is_shipped = Column(Boolean, nullable=False, default=False)
    is_paid = Column(Boolean, nullable=False, default=False)
    is_completed = Column(Boolean, nullable=False, default=False)
    completed_at = Column(DateTime)
    memo = Column(String(250))
    is_deleted = Column(Boolean, nullable=False, default=False)
    deleted_at = Column(DateTime)


class InboundOrderItem(Base):
    __tablename__ = "inbound_order_items"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    inserted_at = Column(DateTime, nullable=False)
    modified_at = Column(DateTime)
    ordered_at = Column(DateTime)
    order_id = Column(Integer, nullable=False)
    item_id = Column(Integer, nullable=False)
    amount = Column(Integer)
    sender_id = Column(Integer, nullable=False)
    warehouse_id = Column(Integer, nullable=False)
    is_shipped = Column(Boolean, nullable=False, default=False)
    shipped_at = Column(DateTime)
    memo = Column(String(250))
    is_deleted = Column(Boolean, nullable=False, default=False)
    deleted_at = Column(DateTime)


class OutboundOrderItem(Base):
    __tablename__ = "outbound_order_items"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    inserted_at = Column(DateTime, nullable=False)
    modified_at = Column(DateTime)
    ordered_at = Column(DateTime)
    order_id = Column(Integer, nullable=False)
    item_id = Column(Integer, nullable=False)
    amount = Column(Integer)
    warehouse_id = Column(Integer, nullable=False)
    receiver_id = Column(Integer, nullable=False)
    is_shipped = Column(Boolean, nullable=False, default=False)
    shipped_at = Column(DateTime)
    memo = Column(String(250))
    is_deleted = Column(Boolean, nullable=False, default=False)
    deleted_at = Column(DateTime)


class InventoryItem(Base):
    __tablename__ = "inventory_items"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    inserted_at = Column(DateTime, nullable=False)
    modified_at = Column(DateTime)
    item_id = Column(Integer, nullable=False)
    warehouse_id = Column(Integer, nullable=False)
    amount = Column(Integer)
    memo = Column(String(200))
    is_deleted = Column(Boolean, nullable=False, default=False)
    deleted_at = Column(DateTime)
