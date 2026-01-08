from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from .models import Expense
from .schemas import ExpenseCreate, ExpenseUpdate
import logging

logger = logging.getLogger(__name__)

def create_expense(db: Session, expense: ExpenseCreate):
    """Create a new expense"""
    try:
        db_expense = Expense(
            amount=expense.amount,
            category=expense.category,
            description=expense.description
        )
        db.add(db_expense)
        db.commit()
        db.refresh(db_expense)
        logger.info(f"Created expense with ID: {db_expense.id}")
        return db_expense
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Error creating expense: {str(e)}")
        raise

def get_expenses(db: Session, skip: int = 0, limit: int = 100):
    """Get all expenses with pagination"""
    try:
        return db.query(Expense).offset(skip).limit(limit).all()
    except SQLAlchemyError as e:
        logger.error(f"Error fetching expenses: {str(e)}")
        raise

def get_expense_by_id(db: Session, expense_id: int):
    """Get a single expense by ID"""
    try:
        return db.query(Expense).filter(Expense.id == expense_id).first()
    except SQLAlchemyError as e:
        logger.error(f"Error fetching expense {expense_id}: {str(e)}")
        raise

def update_expense(db: Session, expense_id: int, expense: ExpenseUpdate):
    """Update an existing expense"""
    try:
        db_expense = get_expense_by_id(db, expense_id)
        if not db_expense:
            return None
        
        # Update only provided fields
        update_data = expense.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_expense, key, value)
        
        db.commit()
        db.refresh(db_expense)
        logger.info(f"Updated expense ID: {expense_id}")
        return db_expense
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Error updating expense {expense_id}: {str(e)}")
        raise

def delete_expense(db: Session, expense_id: int):
    """Delete an expense"""
    try:
        db_expense = get_expense_by_id(db, expense_id)
        if not db_expense:
            return None
        
        db.delete(db_expense)
        db.commit()
        logger.info(f"Deleted expense ID: {expense_id}")
        return True
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Error deleting expense {expense_id}: {str(e)}")
        raise

def get_expenses_by_category(db: Session, category: str):
    """Get expenses filtered by category"""
    try:
        return db.query(Expense).filter(Expense.category == category).all()
    except SQLAlchemyError as e:
        logger.error(f"Error fetching expenses by category: {str(e)}")
        raise