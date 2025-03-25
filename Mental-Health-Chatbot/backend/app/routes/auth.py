from fastapi import APIRouter

# Define the router instance
router = APIRouter()

# Example routes
@router.post("/login")
def login():
    return {"message": "Login route works!"}

@router.post("/register")
def register():
    return {"message": "Register route works!"}
