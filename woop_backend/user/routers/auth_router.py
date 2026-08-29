from fastapi import APIRouter,Depends,HTTPException,status
from user.schemas.user_schema import UserCreate,UserResponse,UserLogin
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import get_db
from core.security import hash_password,verify_password
from user.model.user_model import User
from sqlalchemy import select
from core.jwt_token import create_JWT,TokenType,create_access,create_refresh
from datetime import timedelta
import uuid
from user.services.auth_services import Auth


auth=APIRouter(tags=["Auth"])


@auth.post("/api/register")
async def register(data:UserCreate ,db:AsyncSession=Depends(get_db))->UserResponse:
    query=select(User).where(data.email==User.email)
    result= await db.execute(query)
    user=result.scalar_one_or_none()
    if user is not  None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="a user with this email already exists."
        )
    hash=hash_password(data.password)
    new_user=User(
        email=data.email,
        password_hash=hash
    )
    db.add(new_user)
    await db.flush()
    await db.commit()
    data={"sub":str(new_user.id)}
          
    access=create_access(sub=data)
    refresh=create_refresh(sub=data)
    return UserResponse(
        id=str(new_user.id),
        email=new_user.email,
        created_at=new_user.created_at,
        access_token=access,
        refresh_token=refresh
    )


@auth.post("/api/login")
async def login(data:UserLogin,db:AsyncSession=Depends(get_db)):
    email=data.email
    password=data.password
    auth=Auth()
    user= await auth.login(email=email,password=password,db=db)
    return user
    



    
    
      