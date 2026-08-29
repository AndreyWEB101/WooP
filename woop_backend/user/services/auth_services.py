from core.security import verify_password
from sqlalchemy import select
from user.model.user_model import User
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from core.jwt_token import create_access
import jwt
import os
class Auth:
    def __init__(self):
        self.key=os.getenv("SECRET_KEY")
        self.algorithm=os.getenv("AlGORITHM")

    async def login(self,email:str,password:str,db:AsyncSession):
        request=select(User).where(User.email==email)
        result= await db.execute(request)
        login_user=result.scalars().one_or_none()
        if login_user is None:
            raise HTTPException(
                status_code=401,
                detail="user_not_auth"
            )
        islogined=verify_password(password,login_user.password_hash)
        return login_user

    

    def refresh_token(self,token:str)->str:
     try:
        payload=jwt.decode(token,self.key,self.algorithm)
        user=payload["sub"]
        token=create_access(user)
        return token
     except:
         return "token invalid"
         
        
        
        
       
      

    def get_user(self,token:str)->str:
            try:
                key=os.getenv("SECRET_KEY")
                algorithm=os.getenv("AlGORITHM")
                payload=jwt.decode(token,key,algorithm)
                user=payload["sub"]
                return user
            
            except jwt.InvalidTokenError:
                raise HTTPException(
                    status_code=401,
                    detail="invalid_token"
                )
                
               
                
            
            


