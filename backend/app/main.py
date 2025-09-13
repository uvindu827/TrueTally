from fastapi import FastAPI

app = FastAPI(title="Mobile Backend")

@app.get("/")
def root():
    return {"message": "TrueTally Backend is running smoothly🚀"}
