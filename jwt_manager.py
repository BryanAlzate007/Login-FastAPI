from jwt import encode


def create_token(data:dict):
    token: str = encode(payload=data, key="", algorithm="HS256")
    return token