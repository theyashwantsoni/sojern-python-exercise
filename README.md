## Use the App

Run `pip3 install -r requirements.txt`  in the terminal.

Run `python app.py` in the terminal.

## To Run App in Docker

1. Checkout `Dockerfile`.
2. I have changed it to accomodate latest version of ununtu and `python3`
3. To build docker image `docker build -t sojern-flask:latest .`
4. To run the docker container `docker run -it -p 5000:8888 sojern-flask `