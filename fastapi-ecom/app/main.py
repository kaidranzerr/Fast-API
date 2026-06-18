from fastapi import FastAPI
app = FastAPI()


# first endpoint
@app.get('/')
def root():
    return {"message": "Welcome to main bitch"}