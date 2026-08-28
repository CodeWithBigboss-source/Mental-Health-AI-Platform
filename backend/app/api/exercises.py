from fastapi import APIRouter, HTTPException
from app.data.exercises import EXERCISES

router = APIRouter(prefix="/exercises", tags=["exercises"])

@router.get("/")
def list_exercises():
    return EXERCISES

@router.get("/{exercise_id}")
def get_exercise(exercise_id: str):
    for ex in EXERCISES:
        if ex["id"] == exercise_id:
            return ex
    raise HTTPException(404, "Exercise not found")