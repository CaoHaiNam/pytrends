from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import keyword_suggestion, keyword_ranking

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app = FastAPI()

app.include_router(keyword_suggestion.router)
app.include_router(keyword_ranking.router)
