from fastapi import FastAPI, Request
from pydantic import BaseModel

from github_util import write_comment
from gpt import gpt

import time

app = FastAPI(title="GPT")

@app.get("/")
async def home():
    return "<h2>SS</h2>"

@app.get("/prompt")
def get_gpt(prompt: str):
    start = time.time()
    generated = gpt(prompt)
    end = time.time()
    print(end - start)

    return {"generated": generated, "time": end - start}

@app.post("/issue")
async def get_issue(request: Request):
    content = await request.json()

    action =   content['action']
    if action != 'opened': 
      return -1 # Nothing to do

    repos_name = content['repository']['full_name']
    issue = content['issue']

    no = issue['number']
    user = issue['user']['login']

    title = issue['title']
    body = issue['body']
  
    res = gpt(body)

    print(repos_name, no, user, title, body, res)

    write_comment(res, repos_name, no)
    return 100