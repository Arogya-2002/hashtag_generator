from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.pipeline.hashtag_pipeline import hashtag_pipeline
from src.logger import logging
from src.exceptions import CustomException

# FastAPI app initialization
app = FastAPI(title="Hashtag Generator API")

# CORS configuration - allow all origins for now
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request schema
class CaptionInput(BaseModel):
    caption: str

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Hashtag Generator API is running."}

# Hashtag generation endpoint
@app.post("/generate_hashtags")
def generate_hashtags(input_data: CaptionInput):
    try:
        logging.info("API call received for hashtag generation.")
        result = hashtag_pipeline(input_data.caption)

        if result:
            return {"hashtags": result}
        else:
            raise HTTPException(status_code=204, detail="No hashtags generated.")

    except CustomException as ce:
        logging.error("Custom exception in API", exc_info=True)
        raise HTTPException(status_code=500, detail=str(ce))

    except Exception as e:
        logging.error("Unhandled exception in API", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal Server Error")
