from fastapi import FastAPI
from app.api.v1.endpoints import docusign

app = FastAPI(
    title="DocuSign Service",
    description="An API to manage DocuSign envelopes.",
    version="1.0.0"
)

app.include_router(docusign.router, prefix="/docusign", tags=["DocuSign"])

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the DocuSign Service API"}