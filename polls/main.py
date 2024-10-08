from fastapi import FastAPI, HTTPException
from models import PollCreate, VoteCreate, PollResults
import storage

app = FastAPI()

@app.post("/polls/", response_model=int)
async def create_poll(topic: PollCreate):
    poll_id = storage.add_poll(topic)
    return poll_id

@app.post("/polls/vote")
async def vote(vote: VoteCreate):
    polls = storage.load_data()["polls"]
    if vote.poll_id < 1 or vote.poll_id > len(polls):
        raise HTTPException(status_code=404, detail="Poll not found")
    
    options = polls[vote.poll_id - 1]["options"]
    if vote.option not in options:
        raise HTTPException(status_code=400, detail="Invalid option")

    storage.add_vote(vote)
    return {"message": "Vote recorded successfully"}

@app.get("/polls/{poll_id}/results", response_model=PollResults)
async def get_results(poll_id: int):
    results = storage.get_poll_results(poll_id)
    return PollResults(poll_id=poll_id, results=results)

@app.get("/polls/")
async def get_polls():
    return storage.get_polls()
