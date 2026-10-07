#Python install runtime
FROM python:3.10-slim

#Set the isolated working directory inside the container
WORKDIR /app

#Install the Flask dependency
RUN pip install --no-cache-dir flask

#Copy the application script into the container filesystem
COPY app.py .

#Document the port exposed by the container
EXPOSE 5000

#Define default command to start the application
CMD ["python", "app.py"]