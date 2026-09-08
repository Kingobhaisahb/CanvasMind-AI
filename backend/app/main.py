from fastapi import FastAPI

app = FastAPI(
    title="AI Painting Studio API",
    version="1.0.0",
    description="AI-powered painting generation SaaS"
)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "AI Painting Studio API"
    }