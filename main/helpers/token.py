import jwt
from django.conf import settings


def encode(payload):
  print("at encoder============== PAYLOAD IS", payload)
  token = jwt.encode(
    payload,
    settings.JWT_SECRET,
    algorithm=settings.JWT_ALGORITHM
    )
  print(token)
  return token
  

def decode(token):
    try:
        print("at encoder============== PAYLOAD IS", token)
        decoded = jwt.decode(token,
        settings.JWT_SECRET,
        algorithms = settings.JWT_ALGORITHM
        )
        print(decoded)
        return decoded
    except :
        return False
        
