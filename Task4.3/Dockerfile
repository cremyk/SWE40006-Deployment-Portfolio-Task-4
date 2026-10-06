# Step 1: Base Python runtime
FROM python:3.10-slim

# Step 2: Set working directory
WORKDIR /app

# Step 3: Copy requirements and install dependencies (Layer Caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Step 4: Copy application source and templates
COPY . .

# Step 5: Expose internal port
EXPOSE 5001

# Step 6: Define application start command
CMD ["python", "app.py"]