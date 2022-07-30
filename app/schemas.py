from typing import Union
from datetime import datetime

from pydantic import BaseModel


class ItemBase(BaseModel):
    category1: Union[str, None] = None
    category2: Union[str, None] = None
    category3: Union[str, None] = None
    item_code: Union[str, None] = None
    name: Union[str, None] = None
    detail: Union[str, None] = None
    unit_volume: Union[str, None] = None
    unit_weight: Union[str, None] = None
    memo: Union[str, None] = None


class ItemUpdate(ItemBase):
    is_deleted: Union[bool, None] = None


class ItemCreate(ItemBase):
    name: str


class Item(ItemUpdate):
    id: Union[int, None] = None
    inserted_at: Union[datetime, None] = None
    modified_at: Union[datetime, None] = None
    deleted_at: Union[datetime, None] = None

    class Config:
        orm_mode = True


class WarehouseBase(BaseModel):
    modified_at: Union[datetime, None] = None
    name: str
    address: Union[str, None] = None
    memo: Union[str, None] = None
    is_deleted: bool
    deleted_at: Union[datetime, None] = None


class WarehouseCreate(WarehouseBase):
    inserted_at: datetime


class Warehouse(WarehouseCreate):
    id: int

    class Config:
        orm_mode = True


class CompanyBase(BaseModel):
    modified_at: Union[datetime, None] = None
    name: str
    address: Union[str, None] = None
    phone_number: Union[str, None] = None
    manager: Union[str, None] = None
    memo: Union[str, None] = None
    is_deleted: bool
    deleted_at: Union[datetime, None] = None


class CompanyCreate(CompanyBase):
    inserted_at: datetime


class Company(CompanyCreate):
    id: int

    class Config:
        orm_mode = True


class EmployeeBase(BaseModel):
    modified_at: Union[datetime, None] = None
    name: str
    position: Union[str, None] = None
    phone_number: Union[str, None] = None
    email: Union[str, None] = None
    memo: Union[str, None] = None
    is_deleted: bool
    deleted_at: Union[datetime, None] = None


class EmployeeCreate(EmployeeBase):
    inserted_at: datetime


class Employee(EmployeeCreate):
    id: int

    class Config:
        orm_mode = True


class VehicleBase(BaseModel):
    modified_at: Union[datetime, None] = None
    name: str
    unit_volume: Union[str, None] = None
    unit_weight: Union[str, None] = None
    memo: Union[str, None] = None
    is_deleted: bool
    deleted_at: Union[datetime, None] = None


class VehicleCreate(VehicleBase):
    inserted_at: datetime


class Vehicle(VehicleCreate):
    id: int

    class Config:
        orm_mode = True


class OrderBase(BaseModel):
    modified_at: Union[datetime, None] = None
    is_inbound: bool
    received_at: Union[datetime, None] = None
    target_company_id: int
    expected_at: Union[datetime, None] = None
    total_price: Union[int, None] = None
    is_shipped: bool
    is_paid: bool
    is_completed: bool
    completed_at: Union[datetime, None] = None
    memo: Union[str, None] = None
    is_deleted: bool
    deleted_at: Union[datetime, None] = None


class OrderCreate(OrderBase):
    inserted_at: datetime


class Order(OrderCreate):
    id: int

    class Config:
        orm_mode = True


class InboundOrderItemBase(BaseModel):
    modified_at: Union[datetime, None] = None
    ordered_at: Union[datetime, None] = None
    order_id: int
    item_id: int
    amount: int
    sender_id: int
    warehouse_id: int
    is_shipped: bool
    shipped_at: Union[datetime, None] = None
    memo: Union[str, None] = None
    is_deleted: bool
    deleted_at: Union[datetime, None] = None


class InboundOrderItemCreate(InboundOrderItemBase):
    inserted_at: datetime


class InboundOrderItem(InboundOrderItemCreate):
    id: int

    class Config:
        orm_mode = True


class OutboundOrderItemBase(BaseModel):
    modified_at: Union[datetime, None] = None
    ordered_at: Union[datetime, None] = None
    order_id: int
    item_id: int
    amount: int
    receiver_id: int
    warehouse_id: int
    is_shipped: bool
    shipped_at: Union[datetime, None] = None
    memo: Union[str, None] = None
    is_deleted: bool
    deleted_at: Union[datetime, None] = None


class OutboundOrderItemCreate(OutboundOrderItemBase):
    inserted_at: datetime


class OutboundOrderItem(OutboundOrderItemCreate):
    id: int

    class Config:
        orm_mode = True


class InventoryItemBase(BaseModel):
    modified_at: Union[datetime, None] = None
    item_id: int
    warehouse_id: int
    amount: Union[int, None] = None
    memo: Union[str, None] = None
    is_deleted: bool
    deleted_at: Union[datetime, None] = None


class InventoryItemCreate(InventoryItemBase):
    inserted_at: datetime


class InventoryItem(InventoryItemCreate):
    id: int

    class Config:
        orm_mode = True
