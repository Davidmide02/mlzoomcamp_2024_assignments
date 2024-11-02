# imoport the docker image
FROM python:3.8.12-slim

# install pipenv for virtual environemnt
RUN pip install pipenv

# create a working directory if not available and cd in to it

WORKDIR /app

# copy the files
COPY ["Pipfile", "Pipfile.lock", "./"]

# insall the dependences
RUN pipenv install --system --deploy

# copy the model file and the python file flask is in to serve the model
COPY ["predict.py", "model_C=1.0", "./"]

# To expose the port to the hosting computer
EXPOSE 9696

# entry point
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0.0", "predict:app"]

# Map the exposed port to the computer port
-p port expose:machine/computer port 