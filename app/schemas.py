from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ExpenseBase(BaseModel):
    """Base expense schema"""
    amount: float = Field(gt=0, description="Amount must be positive")
    category: str = Field(min_length=2, max_length=50)
    description: str = Field(min_length=3, max_length=200)

class ExpenseCreate(ExpenseBase):
    """Schema for creating an expense"""
    pass

class ExpenseUpdate(BaseModel):
    """Schema for updating an expense - all fields optional"""
    amount: Optional[float] = Field(None, gt=0, description="Amount must be positive")
    category: Optional[str] = Field(None, min_length=2, max_length=50)
    description: Optional[str] = Field(None, min_length=3, max_length=200)

class ExpenseResponse(ExpenseBase):
    """Schema for expense response"""
    id: int

    class Config:
        from_attributes = True

class ExpenseList(BaseModel):
    """Schema for paginated expense list"""
    total: int
    expenses: list[ExpenseResponse]

class ErrorResponse(BaseModel):
    """Schema for error responses"""
    detail: str
    
class HealthCheck(BaseModel):
    """Schema for health check response"""
    status: str
    database: str