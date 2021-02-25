###Import Python3 from Docker
FROM python:3.7

###Install fastapi and uvicorn
RUN pip install fastapi uvicorn

###Expose port 8080
EXPOSE 8080

###Copy the contents of the app directory to the app directory on the new server
COPY ./app /app

###Tell uvicorn to run the main.py script and host it on port 8080
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]