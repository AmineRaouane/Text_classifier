# Text Classification API

A FastAPI-based text classification service for AI content detection.

## Features

- **FastAPI Framework**: Modern, fast web framework for building APIs
- **TensorFlow Integration**: Uses Keras models for text classification
- **Single & Batch Processing**: Support for both individual and batch text classification
- **Render Ready**: Optimized for Render.com deployment
- **Health Checks**: Comprehensive health monitoring
- **Logging**: Structured logging with configurable levels
- **Error Handling**: Robust error handling and validation
- **CORS Support**: Cross-origin resource sharing enabled
- **Environment Configuration**: Configurable via environment variables

## API Endpoints

- `GET /` - Welcome message and API information
- `GET /health` - Health check endpoint
- `GET /model-info` - Model information and configuration
- `POST /predict` - Single text classification endpoint
- `POST /predict-batch` - Batch text classification endpoint (up to 10000 texts)

## Quick Start

### Local Development

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

3. **Run the application**
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

## Configuration

The application can be configured using environment variables. Copy `.env.example` to `.env` and modify as needed:

```env
# Application Configuration
APP_NAME=Text Classification API
APP_VERSION=1.0.0
DEBUG=False
LOG_LEVEL=INFO

# Server Configuration
HOST=0.0.0.0
PORT=8000
WORKERS=1

# Model Configuration
MAX_SEQUENCE_LENGTH=50
MODEL_PATH=model/model.h5
TOKENIZER_PATH=model/tokenizer.json

# Security (optional - not used in current implementation)
# SECRET_KEY=your-secret-key-here
```

## API Usage

### Health Check
```bash
curl http://localhost:8000/health
```

Response:
```json
{
  "status": "ok",
  "model_loaded": true,
  "timestamp": "2024-01-01 12:00:00",
  "version": "1.0.0"
}
```

### Single Text Classification
```bash
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"text": "This is a sample text to classify"}'
```

Response:
```json
{
  "prediction": 1,
  "probability": 0.85,
  "text_length": 7
}
```

### Batch Text Classification
```bash
curl -X POST "http://localhost:8000/predict-batch" \
     -H "Content-Type: application/json" \
     -d '{
       "texts": [
         "This is the first text to classify",
         "This is the second text to classify",
         "This is the third text to classify"
       ]
     }'
```

Response:
```json
{
  "predictions": [
    {
      "prediction": 1,
      "probability": 0.85,
      "text_length": 7
    },
    {
      "prediction": 0,
      "probability": 0.23,
      "text_length": 7
    },
    {
      "prediction": 1,
      "probability": 0.92,
      "text_length": 7
    }
  ],
  "total_texts": 3
}
```

## Deployment

### Render.com (Recommended)

The easiest way to deploy this API is using Render.com:

1. **Push to GitHub**: Make sure your code is in a GitHub repository
2. **Connect to Render**: Link your GitHub account to Render
3. **Create Web Service**: Use the provided `render.yaml` configuration
4. **Deploy**: Render will automatically build and deploy your application

**Environment Variables** (set in Render dashboard):
- `DEBUG`: `False`
- `LOG_LEVEL`: `INFO`
- `MAX_SEQUENCE_LENGTH`: `50`
- `MODEL_PATH`: `model/model.h5`
- `TOKENIZER_PATH`: `model/tokenizer.json`

### Manual Render Setup

If you prefer manual setup:

1. Go to [render.com](https://render.com)
2. Create a new "Web Service"
3. Connect your GitHub repository
4. Use these settings:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Python Version**: `3.11.0`

### Production Considerations

1. **Security**:
   - Configure CORS origins properly for production
   - Render provides HTTPS automatically
   - Implement authentication if needed
   - Consider rate limiting for batch endpoints

2. **Performance**:
   - Render automatically handles scaling
   - Monitor batch processing performance for large requests
   - Consider upgrading to a paid plan for better performance

3. **Monitoring**:
   - Use Render's built-in logging and monitoring
   - Monitor health check endpoints
   - Set up alerts for service failures
   - Track batch processing metrics

4. **Model Management**:
   - Version your models
   - Monitor model performance
   - Consider model caching for batch operations
   - Keep model files under Render's size limits

## Development

### Adding New Features

1. **New Endpoints**: Add routes in `main.py`
2. **Configuration**: Add new variables to `config.py` and `.env.example`
3. **Dependencies**: Update `requirements.txt`
4. **Documentation**: Update this README
5. **Batch Processing**: Use the `predict_batch` function in `helpers.py` for new batch endpoints

## Troubleshooting

### Common Issues

1. **Model not loading**:
   - Check if model files exist in the `model/` directory
   - Verify file permissions
   - Check logs for specific error messages

2. **Port conflicts**:
   - Change the PORT environment variable
   - Update docker-compose.yml if using Docker Compose

3. **Memory issues**:
   - Increase container memory limits
   - Optimize model size if possible

### Logs
```bash
# Local development
# Logs will appear in your terminal when running uvicorn

# Render deployment
# View logs in the Render dashboard under your service's "Logs" tab
```
