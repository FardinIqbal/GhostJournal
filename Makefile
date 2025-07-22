install:
pip install -r requirements.txt

run:
uvicorn app.main:app --reload

test:
pytest

worker:
celery -A app.workers.celery_app worker --loglevel=info
