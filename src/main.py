from fastapi import FastAPI
from api.router import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(router)


app.add_middleware(
    CORSMiddleware,
    #TODO for development only
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
