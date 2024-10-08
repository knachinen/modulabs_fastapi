import json
from pathlib import Path
from poll.v0.models import PollCreate, VoteCreate

DATA_FILE = Path("polls.json")

def load_data():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"polls": [], "votes": []}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

def add_poll(poll: PollCreate):
    data = load_data()
    poll_id = len(data["polls"]) + 1
    data["polls"].append({"id": poll_id, "title": poll.title, "options": poll.options})
    save_data(data)
    return poll_id

def add_vote(vote: VoteCreate):
    data = load_data()
    data["votes"].append({"poll_id": vote.poll_id, "option": vote.option})
    save_data(data)

def get_poll_results(poll_id: int):
    data = load_data()
    votes = [vote for vote in data["votes"] if vote["poll_id"] == poll_id]
    results = {option: 0 for option in data["polls"][poll_id - 1]["options"]}
    for vote in votes:
        results[vote["option"]] += 1
    return results

def get_polls():
    data = load_data()
    return data["polls"]
