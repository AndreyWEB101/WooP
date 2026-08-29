from dotenv import load_dotenv
load_dotenv()

from fastapi import  FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.database import Base,async_engine_db
from contextlib import asynccontextmanager
from user.routers.auth_router import auth






@asynccontextmanager
async def lifespan(app:FastAPI):
    async with async_engine_db.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield
    await async_engine_db.dispose()

app=FastAPI(title='WooP',lifespan=lifespan)
app.include_router(auth)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # адрес твоего фронтенда
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
async def test():
    return {"hello"}


    