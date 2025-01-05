from fastapi import FastAPI, Depends, HTTPException
from routers import users


app = FastAPI
app.include_router(users.router, tags=["users"])