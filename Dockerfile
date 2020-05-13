FROM tiangolo/uvicorn-gunicorn:python3.8

# prometheus multiproc (gunicorn)
ENV prometheus_multiproc_dir multiproc-tmp
RUN mkdir $prometheus_multiproc_dir


COPY ./app /app/app

# copy resources
COPY ./contrib   /app/contrib

# install additional dependencies
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt --no-cache-dir