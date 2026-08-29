import os 
import jwt
from enum import Enum
from datetime import timedelta,datetime,UTC
from uuid import uuid4
key=os.getenv("SECRET_KEY")
algorithm=os.getenv("AlGORITHM")

class TokenType(str,Enum):
    ACCESS='access'
    REFRESH='refresh'



def create_JWT(data:dict,type_token:str,expire_delta:timedelta)->str:

    encoding_data=data.copy()
    now=datetime.now(UTC)
    encoding_data.update({
        "jti":str(uuid4()),
        "exp":now+expire_delta,
        "type":type_token,
        "iat":now


    })
    token=jwt.encode(encoding_data,key=key,algorithm=algorithm)
    return token

    
def create_access(sub:str)->str:
    now=datetime.now(UTC)

    payload={
        "sub":sub,
        "type":TokenType.ACCESS,
        "iat":now,
        "exp":now+timedelta(minutes=15)
    }
    token=jwt.encode(payload,key=key,algorithm=algorithm)
    return token


def create_refresh(sub:str)->str:
    now=datetime.now(UTC)
    jti=str(uuid4())
    payload={
        "sub":sub,
        "type":TokenType.REFRESH,
        "iat":now,
        "exp":now+timedelta(days=7),
        "jti":jti
    }
    token=jwt.encode(payload,key=key,algorithm=algorithm)
    return token