from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,EmailStr
from typing import Dict,List
import json,os,string,random



app= FastAPI()

User_FILE= "User_FILE.json"
ANALYSIS_FILE= "ANALYSIS_FILE.json"

if os.path.exists(User_FILE):
    with open(User_FILE,"r") as f:
        users =json.load(f)

else:
    users={}

if os.path.exists(ANALYSIS_FILE):
    with open(ANALYSIS_FILE, "r") as f:
        analysis_data = json.load(f)
else:
    analysis_data = {}




class User(BaseModel):
    name:str
    email:EmailStr
    text:str


@app.post('/user',status_code=201)
def create (user:User):
    if not user.text or len(user.text)>200:
        raise(HTTPException(status_code=400,detail="text len 1 to 200 words"))

    while True:
        new_id = str(random.randint(1000, 9999))
        if new_id not in users:
            break


    word_count=len(user.text.split())
    uppercase_count =sum(1 for char in user.text if char.isupper())   
    special_char_count =sum(1 for char in user.text if char in string.punctuation)

    user_dict = {
        "id": int(new_id),
        "name": user.name,
        "email": user.email,
        "text": user.text
    }

    analysis_dict = {
        "id": int(new_id),
        "user_id": int(new_id),
        "text": user.text,
        "analysis": {
            "word_count": word_count,
            "uppercase_count": uppercase_count,
            "special_char": special_char_count
        }
    }
    
    users[new_id]=user_dict

    with open(FILE,"w") as f:
        json.dump(users,f,indent=4)

    return data
    
    
        # Save in analysis.json
    analysis_data[new_id] = analysis_dict
    with open(ANALYSIS_FILE, "w") as f:
        json.dump(analysis_data, f, indent=4)

@app.get("/users")
def get_users():
    return list(users.values())


@app.get("/users/{user_id}")
def get_user(user_id:int):

    if str(user_id) not in users:
        raise HTTPException(status_code=404,detail="user not found")

    return users[str(user_id)]

@app.get("/analysis/{analysis_id}")
def get_analysis(analysis_id: int):
    key = str(analysis_id)
    if key not in analysis_data:
        raise HTTPException(status_code=404, detail="analysis not found")

    return analysis_data[key]



@app.delete("/users/{user_id}")
def del_user(user_id:int):
    if str(user_id) not in users:
        raise HTTPException(status_code=404,detail="user not fount ")
    
    deleted_user = users[str(user_id)] 


    del users[str(user_id)]

    with open (FILE,"w") as f:
        json.dump(users,f,indent=4)

    return {"message":"user deleted",
           "deleted_data": deleted_user
           }