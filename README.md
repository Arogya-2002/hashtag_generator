# Gemini Flash Hashtag Generator API

A FastAPI-powered REST API that uses Google's Gemini 1.5 Flash model to generate relevant hashtags for social media captions. Perfect for content creators, marketers, and social media managers to automate hashtag creation with a scalable web service.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
  - [Start the API Server](#start-the-api-server)
  - [API Endpoints](#api-endpoints)
  - [Testing the API](#testing-the-api)
- [Code Architecture](#code-architecture)
- [Configuration](#configuration)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)
- [Production Deployment](#production-deployment)
- [License](#license)

---

## Overview

The Gemini Flash Hashtag Generator API leverages Google's Generative AI to produce relevant hashtags through a RESTful web service. Built with FastAPI, it features modular architecture, comprehensive logging, custom exception handling, and CORS support for web applications.

---

## Features

- **RESTful API**: FastAPI-based web service with automatic OpenAPI documentation
- **AI-Powered**: Uses Google's Gemini 1.5 Flash model for intelligent hashtag generation
- **Modular Architecture**: Organized pipeline structure with separate components
- **Comprehensive Logging**: Detailed logging throughout the application lifecycle
- **Custom Exception Handling**: Robust error handling with custom exception classes
- **CORS Support**: Cross-origin resource sharing for web applications
- **Data Validation**: Pydantic models for request/response validation
- **Scalable Design**: Enterprise-ready architecture with artifact management

---

## Project Structure

```
HASHTAG_GENERATOR/
├── src/
│   ├── __pycache__/
│   ├── components/
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   ├── gemini_model.py           # Gemini AI model integration
│   │   └── hashtag_generator.py     # Core hashtag generation logic
│   ├── constants/                   # Application constants
│   ├── entity/
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   ├── hashtag_artifact_entity.py    # Data models for artifacts
│   │   └── hashtag_config_entity.py      # Configuration entities
│   ├── exceptions/                  # Custom exception classes
│   ├── logger/                      # Logging configuration
│   ├── pipeline/
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   └── hashtag_pipeline.py      # Main processing pipeline
│   ├── utils/                       # Utility functions
│   └── __init__.py
├── logs/                           # Application logs
├── venv/                          # Virtual environment
├── .env                           # Environment variables (API keys)
├── .gitignore                     # Git ignore file
├── app.py                         # FastAPI application entry point
├── README.md                      # Project documentation
└── requirements.txt               # Python dependencies
```

---

## Installation

Follow these steps to set up the project:

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/hashtag_generator.git
cd hashtag_generator
```

### 2. Set Up Virtual Environment
```bash
python3.10 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the project root:
```bash
GOOGLE_API_KEY=your_actual_gemini_api_key_here
LOG_LEVEL=INFO
```

---

## Usage

### Start the API Server
Launch the FastAPI server:
```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at `http://localhost:8000`

### API Endpoints

#### Root Endpoint
- **URL**: `/`
- **Method**: `GET`
- **Response**: API status message

#### Generate Hashtags
- **URL**: `/generate_hashtags`
- **Method**: `POST`
- **Content-Type**: `application/json`
- **Request Body**:
  ```json
  {
    "caption": "Your social media caption here"
  }
  ```
- **Response**:
  ```json
  {
    "hashtags": ["#hashtag1", "#hashtag2", "#hashtag3", "..."]
  }
  ```

#### API Documentation
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

### Testing the API

#### Using cURL
```bash
curl -X POST "http://localhost:8000/generate_hashtags" \
  -H "Content-Type: application/json" \
  -d '{"caption": "Exploring the ancient ruins of Hampi"}'
```

#### Using Python requests
```python
import requests

url = "http://localhost:8000/generate_hashtags"
data = {"caption": "Exploring the ancient ruins of Hampi"}

response = requests.post(url, json=data)

if response.status_code == 200:
    hashtags = response.json()["hashtags"]
    print("Generated hashtags:", hashtags)
else:
    print(f"Error: {response.status_code} - {response.text}")
```

#### Using JavaScript/Fetch
```javascript
fetch('http://localhost:8000/generate_hashtags', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        caption: 'Exploring the ancient ruins of Hampi'
    })
})
.then(response => response.json())
.then(data => {
    console.log('Generated hashtags:', data.hashtags);
})
.catch(error => {
    console.error('Error:', error);
});
```

#### Sample API Response
```json
{
  "hashtags": [
    "#Hampi",
    "#TravelIndia", 
    "#AncientRuins",
    "#HistoricalSites",
    "#Wanderlust",
    "#BackpackingIndia",
    "#IncredibleIndia",
    "#CulturalHeritage",
    "#AdventureTravel",
    "#HiddenGems"
  ]
}
```

---

## Code Architecture

### Core Components

| Component | Description |
|-----------|-------------|
| `app.py` | FastAPI application with CORS middleware and API endpoints |
| `src/pipeline/hashtag_pipeline.py` | Main processing pipeline orchestrating the hashtag generation |
| `src/components/gemini_model.py` | Google Gemini AI model integration and configuration |
| `src/components/hashtag_generator.py` | Core hashtag generation logic and processing |
| `src/entity/hashtag_artifact_entity.py` | Data models for hashtag artifacts and responses |
| `src/entity/hashtag_config_entity.py` | Configuration entities and settings |
| `src/logger/` | Centralized logging configuration and utilities |
| `src/exceptions/` | Custom exception classes for error handling |
| `src/utils/` | Utility functions and helper methods |

### Application Flow

1. **API Request**: Client sends POST request with caption to `/generate_hashtags`
2. **Data Validation**: Pydantic validates the incoming request structure
3. **Pipeline Execution**: `hashtag_pipeline()` processes the caption through multiple stages
4. **AI Processing**: Gemini model generates relevant hashtags based on the caption
5. **Artifact Creation**: Results are packaged into `HashtagGeneratorArtifact`
6. **Response**: JSON response with generated hashtags is returned to client
7. **Logging**: All steps are logged with appropriate levels and timestamps

### Error Handling

The application implements comprehensive error handling:
- **Custom Exceptions**: Domain-specific error types with detailed messages
- **HTTP Status Codes**: Appropriate status codes for different error scenarios
- **Logging**: All errors are logged with full stack traces
- **User-Friendly Messages**: Clean error messages returned to API clients

---

## Configuration

### Environment Variables
Configure the application using environment variables in `.env`:

```env
# Required
GOOGLE_API_KEY=your_gemini_api_key_here

# Optional
LOG_LEVEL=INFO
MAX_HASHTAGS=20
MODEL_NAME=gemini-1.5-flash
REQUEST_TIMEOUT=30
```

### CORS Configuration
Update CORS settings in `app.py` for production:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourdomain.com"],  # Specific domains
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)
```

---

## Customization

### Modify Hashtag Generation Parameters
Update the pipeline configuration:
```python
# In src/components/hashtag_generator.py
def generate_hashtags(caption: str, max_hashtags: int = 15):
    # Customize generation logic
```

### Add New Endpoints
Extend the API with additional functionality:
```python
@app.post("/generate_hashtags_bulk")
def generate_hashtags_bulk(captions: List[str]):
    # Bulk hashtag generation
```

### Custom Logging Configuration
Modify logging settings in `src/logger/`:
```python
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
```

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `No module named 'fastapi'` | Install FastAPI: `pip install fastapi uvicorn` |
| `No module named 'google.generativeai'` | Install Google AI: `pip install google-generativeai` |
| `API key not found` | Ensure `.env` file exists with `GOOGLE_API_KEY` |
| `CORS errors` | Update CORS settings in `app.py` to include your domain |
| `No hashtags generated (204)` | Check API key validity and network connectivity |
| `Internal Server Error (500)` | Check logs in `logs/` directory for detailed error information |
| `Server won't start` | Ensure port 8000 is available or use `--port 8001` |

### Common API Errors
- **400 Bad Request**: Invalid JSON format or missing caption field
- **204 No Content**: Gemini API returned empty response
- **500 Internal Server Error**: Check logs for API key issues or network problems
- **422 Unprocessable Entity**: Caption field validation failed

### Debug Mode
Run the server in debug mode for detailed error information:
```bash
uvicorn app:app --reload --log-level debug
```

---

## Production Deployment

### Using Docker
Create a `Dockerfile`:
```dockerfile
FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

Build and run:
```bash
docker build -t hashtag-generator .
docker run -p 8000:8000 --env-file .env hashtag-generator
```

### Using Gunicorn
For production deployment with Gunicorn:
```bash
pip install gunicorn
gunicorn app:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

### Environment Variables for Production
```env
GOOGLE_API_KEY=your_production_api_key
LOG_LEVEL=WARNING
CORS_ORIGINS=https://yourdomain.com,https://www.yourdomain.com
```

### Health Check Endpoint
Add a health check for monitoring:
```python
@app.get("/health")
def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}
```

---

## Development

### Running Tests
```bash
# Install test dependencies
pip install pytest pytest-asyncio

# Run tests
pytest tests/
```

### Code Quality
```bash
# Install development tools
pip install black flake8 mypy

# Format code
black src/ app.py

# Check code quality
flake8 src/ app.py
mypy src/ app.py
```

### API Testing with Postman
Import the OpenAPI schema from `http://localhost:8000/openapi.json` into Postman for easy API testing.

---

## Requirements

- **Python**: 3.10 or higher
- **Google API Access**: Valid API key for Gemini 1.5 Flash model
- **Network**: Internet connectivity for API calls to Google services

### Dependencies
```txt
fastapi
uvicorn[standard]
google-generativeai
python-dotenv
pydantic
```

---

## Important Notes

### Security
- **API Key Protection**: Never commit `.env` files to version control
- **CORS Configuration**: Restrict origins in production environments
- **Rate Limiting**: Consider implementing rate limiting for production use
- **Authentication**: Add authentication for sensitive deployments

### API Usage
- **Quotas**: Monitor Google API usage quotas and billing
- **Rate Limits**: Be aware of API rate limits for Gemini models
- **Error Handling**: Implement proper retry logic for production applications

### Performance
- **Caching**: Consider caching frequent requests to reduce API calls
- **Async Processing**: The current implementation is synchronous; consider async processing for high-volume use

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For questions, issues, or contributions:
- **GitHub Issues**: [Open an issue](https://github.com/your-username/hashtag_generator/issues)
- **Email**: arogyavamshi.chinnabathini@symphonize.com

---

### Notes for Developers

1. **Environment Setup**: Ensure `.env` file is configured with valid Google API key
2. **API Documentation**: FastAPI automatically generates interactive documentation at `/docs`
3. **Logging**: Monitor the `logs/` directory for application logs and debugging
4. **Pipeline Extension**: The modular architecture allows easy extension of the hashtag generation pipeline
5. **Testing**: Use the provided endpoints and examples to test functionality before deployment