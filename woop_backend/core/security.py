from passlib.context import CryptContext
import jwt


pwd_contex=CryptContext(schemes=["bcrypt"],deprecated="auto")
def hash_password(password:str)->str:
    return pwd_contex.hash(password)

def verify_password(plain_password:str,hash_password:str)->bool:
    return pwd_contex.verify(plain_password,hash_password)





