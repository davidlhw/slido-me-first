"""
User inputs:
-l https://app.sli.do/event/aoBxKxqz2rCcTLpYwLpZFC/live/questions
-q 48098817
-v vote_count

parse link for hash=aoBxKxqz2rCcTLpYwLpZFC

GET to https://app.sli.do/api/v0.5/app/events?hash={hash} = {
    :
    "uuid": "4c0a848b-e5d0-4556-9fa1-12bcc7743c96",
    :
    :
}

parse uuid=4c0a848b-e5d0-4556-9fa1-12bcc7743c96

POST to https://app.sli.do/api/v0.5/events/{uuid}/auth = {
    "access_token": "9468b31f456dacbcb1dc84a40dddeb3a0e1a5217",
    "event_id": 6337663,
    "event_user_id": 238594972
}

parse access_token=9468b31f456dacbcb1dc84a40dddeb3a0e1a5217

POST to https://app.sli.do/api/v0.5/events/4c0a848b-e5d0-4556-9fa1-12bcc7743c96/questions/48098894/like = {
    "event_question_id": 48098894,
    "event_question_score": 55,
    "event_question_user_score": 1    
}

Score += 1

"""
