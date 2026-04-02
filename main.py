
from fastapi import FastAPI
from app.routes import users, records, dashboard
from app.routes import auth
from app.core.database import Base, engine
from app.models import db_models

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Finance Dashboard Backend")

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(records.router, prefix="/records", tags=["Records"])
app.include_router(dashboard.router, prefix="/dashboard", tags=["Dashboard"])
app.include_router(auth.router, prefix="/auth", tags=["Auth"])

@app.get("/")
def root():
    return {"message": "Finance Backend Running"}
