# Ghost Journal

MVP for an automated trade journal that ingests trades from the Alpaca Paper API, generates charts, and provides a simple dashboard for review.

## Requirements
- Docker and docker-compose
- Python 3.9+

## Development
```bash
docker-compose up --build
```
The backend will be available at `http://localhost:8000`.

## Environment Variables
See `.env.example` for the required configuration. Create a `.env` file with your credentials.

## Tests
```bash
pytest
```
