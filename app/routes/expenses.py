from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ..database import SessionLocal
from .. import crud, schemas
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/expenses", tags=["Expenses"])

def get_db():
    """Database session dependency"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post(
    "/",
    response_model=schemas.ExpenseResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new expense"
)
def create_expense(
    expense: schemas.ExpenseCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new expense with:
    - **amount**: Positive number
    - **category**: Category name (min 2 chars)
    - **description**: Expense description (min 3 chars)
    """
    try:
        return crud.create_expense(db, expense)
    except SQLAlchemyError as e:
        logger.error(f"Database error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create expense"
        )

@router.get(
    "/",
    response_model=list[schemas.ExpenseResponse],
    summary="Get all expenses"
)
def list_expenses(
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(100, ge=1, le=1000, description="Maximum number of records"),
    db: Session = Depends(get_db)
):
    """
    Retrieve all expenses with pagination:
    - **skip**: Number of records to skip (default: 0)
    - **limit**: Maximum records to return (default: 100)
    """
    try:
        return crud.get_expenses(db, skip=skip, limit=limit)
    except SQLAlchemyError as e:
        logger.error(f"Database error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch expenses"
        )

@router.get(
    "/{expense_id}",
    response_model=schemas.ExpenseResponse,
    summary="Get a specific expense"
)
def get_expense(
    expense_id: int,
    db: Session = Depends(get_db)
):
    """
    Get a specific expense by ID
    """
    try:
        db_expense = crud.get_expense_by_id(db, expense_id)
        if not db_expense:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Expense with ID {expense_id} not found"
            )
        return db_expense
    except HTTPException:
        raise
    except SQLAlchemyError as e:
        logger.error(f"Database error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch expense"
        )

@router.put(
    "/{expense_id}",
    response_model=schemas.ExpenseResponse,
    summary="Update an expense"
)
def update_expense(
    expense_id: int,
    expense: schemas.ExpenseUpdate,
    db: Session = Depends(get_db)
):
    """
    Update an existing expense. All fields are optional.
    """
    try:
        db_expense = crud.update_expense(db, expense_id, expense)
        if not db_expense:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Expense with ID {expense_id} not found"
            )
        return db_expense
    except HTTPException:
        raise
    except SQLAlchemyError as e:
        logger.error(f"Database error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to update expense"
        )

@router.delete(
    "/{expense_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete an expense"
)
def delete_expense(
    expense_id: int,
    db: Session = Depends(get_db)
):
    """
    Delete an expense by ID
    """
    try:
        result = crud.delete_expense(db, expense_id)
        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Expense with ID {expense_id} not found"
            )
        return None
    except HTTPException:
        raise
    except SQLAlchemyError as e:
        logger.error(f"Database error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to delete expense"
        )

@router.get(
    "/category/{category}",
    response_model=list[schemas.ExpenseResponse],
    summary="Get expenses by category"
)
def get_by_category(
    category: str,
    db: Session = Depends(get_db)
):
    """
    Get all expenses for a specific category
    """
    try:
        return crud.get_expenses_by_category(db, category)
    except SQLAlchemyError as e:
        logger.error(f"Database error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch expenses by category"
        )