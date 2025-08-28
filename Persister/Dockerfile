# This Dockerfile sets up a prodict server with FastAPI and Uvicorn

# Start from Python 3.13.2
FROM python:3.13.2

# Set working directory
WORKDIR /app

# Copy all files
COPY ./Persister ./Persister
COPY ./requirements.txt ./requirements.txt


# Install dependencies
RUN pip install --no-cache-dir -r ./requirements.txt

# Start the prodict server
CMD ["python", "-m",  "Persister.main"]