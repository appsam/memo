from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

class Memo(BaseModel):
    id:str
    content:str

memos = []
app = FastAPI()

@app.post("/memos")
def create_memo(memo:Memo):
    memos.append(memo)
    return "메모 추가!"

@app.get("/memos")
def read_memo():
    return memos

@app.put("/memos/{memo_id}")
def put_memo(req_memo:Memo):
    for memo in memos:
        if memo.id==req_memo.id:
            memo.content = req_memo.content
            return '성공!'
    return '그런 메모는 없습니다.' 

@app.delete("/memos/{id}")
def delete_memo(id):
    for index,m in enumerate (memos):
        if m.id==id:
            memos.pop(index)
            return '성공!'
        return '그런 메모는 없습니다.'
        
app.mount("/", StaticFiles(directory='static', html=True),name='static')