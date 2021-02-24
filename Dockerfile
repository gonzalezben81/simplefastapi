###Import Python3 from Docker
FROM python:3.7

###Install fastapi and uvicorn
RUN pip install fastapi uvicorn

###Expose port 80
EXPOSE 80

###Copy the contents of the app directory to the app directory on the new server
COPY ./app /app

###Tell uvicorn to run the main.py script and host is on port 80
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]