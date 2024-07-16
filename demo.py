# from fastapi import FastAPI,Header,HTTPException,Depends
# from typing import List
# import random
# import string
# from userauth import userauth

# # Sample data for todo tasks
# todos = [
#     {"id": 1, "task": "Complete assignment"},
#     {"id": 2, "task": "Buy groceries"},
#     {"id": 3, "task": "Exercise"},
# ]
# app = FastAPI()

# # @app.post()


# @app.get('/docs')
# async def api_docs():
#     return {
#         "Action":"Please include this API key in the 'api' header for authentication.",
#         "Method":"'/todos' to get list of all todos list." 
#     }

# @app.get("/")
# async def generate_token(length = 40):
#     characters = string.ascii_letters + string.digits
#     api_key = ''.join(random.choice(characters) for _ in range(length))

#     with open("api_keys.txt","a") as file:
#         file.write(api_key+"\n")
#     message = {
#         "Your API key is": api_key,
#         "Action": "Please include this API key in the 'api' header for authentication. Go to '/docs' for documentations."
#     }

#     return message
#     # return [{"Your API key is": f"{api_key}" 
#     #         , "Action":"Please include this API key in the 'api' header for authentication. go to '/docs' for documentation."
#     #         }]

# @app.get("/todos/", response_model=List[dict])
# async def get_todos(apiKey_val: bool = Depends(userauth.auth_user)):
#     if apiKey_val:

#         return todos
#     else:
#         raise HTTPException(status_code=401, detail="Invalid API key")

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="localhost", port=8000)

from fastapi import FastAPI, Header, HTTPException, Depends,Query
from typing import List
import random
import string
from userauth import userauth
import mysql.connector as connector

# Sample data for todo tasks
todos = [
    {"id": 1, "task": "Complete assignment"},
    {"id": 2, "task": "Buy groceries"},
    {"id": 3, "task": "Exercise"},
]
app = FastAPI()

@app.get('/docs')
async def api_docs():
    """
    Endpoint to return API documentation.
    """
    return {
        "Action": "Please include the API key in the 'api' header for authentication.",
        "Method": "'/todos' to get list of all todos."
    }
    
@app.get("/")
async def generate_token(length):
    """
    Endpoint to generate an API key.
    """
    characters = string.ascii_letters + string.digits
    api_key = ''.join(random.choice(characters) for _ in range(int(length))
    with open("api_keys.txt", "a") as file:
        file.write(api_key + "\n")
    message = {
        "Your API key is": api_key,
        "Action": "Please include this API key in the 'api' header for authentication. Go to '/docs' for documentation."
    }
    return message

@app.get("/todos_byid/", response_model=dict)
async def get_todos_by_id(id:int = Query(...),apiKey_val: bool = Depends(userauth.auth_user)):
    """
    Endpoint to retrieve todos. you can pass 'id' as your parameter.
    
    Usage:
    
    /todos_buyid/YOUR_TASK_ID
    """
    if apiKey_val:
        for tasks in todos:
            if tasks["id"] ==id:
                return tasks
        raise HTTPException(status_code=404,detail="no data found") 
    else:
        raise HTTPException(status_code=401, detail="Invalid API key")
    
@app.get("/todos/", response_model=List[dict])
async def get_todos(apiKey_val: bool = Depends(userauth.auth_user)):
    """
    Endpoint to retrieve todos.
    """
    if apiKey_val:
        return todos
    else:
        raise HTTPException(status_code=401, detail="Invalid API key")
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)

