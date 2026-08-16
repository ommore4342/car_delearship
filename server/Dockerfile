FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY djangoapp/   djangoapp/
COPY djangoproj/  djangoproj/
COPY frontend/static/ frontend/static/
COPY manage.py .

# Build static files
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "djangoproj.wsgi:application"]
