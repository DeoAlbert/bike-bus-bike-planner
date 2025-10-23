# Use Python 3.13 slim image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Install system dependencies for GeoPandas
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libproj-dev \
    libgeos-dev \
    libspatialindex-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Create temporary directory
RUN mkdir -p /tmp/bike_bus_bike_google

# Expose port (Railway will set PORT environment variable)
EXPOSE 8000

# Run the application
CMD ["python", "start.py"]
