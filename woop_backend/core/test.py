import jwt
import os
from dotenv import load_dotenv
load_dotenv()

key=os.getenv("SECRET_KEY")
algorithm=os.getenv("AlGORITHM")

print(algorithm)
encode="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMCIsImV4cCI6MTc4NzkzMjU2OCwidHlwZSI6InJlZnJlc2giLCJpYXQiOjE3ODc4NDYxNjh9.tTOyBTY1vTuhYkxwcD_JuDyRBFdvUCyKuOgazBSwyg8"
token=jwt.decode(encode,key=key,algorithms=algorithm)
print(token)

