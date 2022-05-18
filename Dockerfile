FROM python:3.8.2-alpine

RUN python -m pip install --upgrade pip

WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

COPY . /app

# CMD [ "python3", "-m" , "flask", "run"]


#Expose the required port
EXPOSE 5000
#Run the command
CMD gunicorn main:app

