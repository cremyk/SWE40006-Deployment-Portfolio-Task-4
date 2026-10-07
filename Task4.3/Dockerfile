#Base Python runtime
FROM python:3.10-slim

#Set working directory
WORKDIR /app

#Copy requirements and install dependencies (Layer Caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#Copy application source and templates
COPY . .

#Expose internal port
EXPOSE 5001

#Define application start command
CMD ["python", "app.py"]