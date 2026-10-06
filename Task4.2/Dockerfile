# Step 1: Supply the official Python install runtime
FROM python:3.10-slim

# Step 2: Set the isolated working directory inside the container
WORKDIR /app

# Step 3: Install the Flask dependency
RUN pip install --no-cache-dir flask

# Step 4: Copy the application script into the container filesystem
COPY app.py .

# Step 5: Document the port exposed by the container
EXPOSE 5000

# Step 6: Define default command to start the application
CMD ["python", "app.py"]