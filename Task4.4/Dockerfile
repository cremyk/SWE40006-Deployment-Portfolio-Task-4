FROM python:3.10-slim

#Set isolated application directory
WORKDIR /app

#Copy source code into container
COPY hospital_app.py .

#Define CLI launch entrypoint
CMD ["python", "hospital_app.py"]