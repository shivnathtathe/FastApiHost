from fastapi import FastAPI,Header,HTTPException,Depends

class userauth:
    @staticmethod
    def auth_user(api: str = Header(...)):
        with open("api_keys.txt", "r") as file:
            existing_keys = file.read().splitlines()
        if api in existing_keys:
            return True
        else:
            return False