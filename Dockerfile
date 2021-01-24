# docker file run scraper with restful api microservice

FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /scraper_service
WORKDIR /scraper_service

COPY requirements /scraper_service/
RUN pip install -r /scraper_service/requirements

COPY scraper/ /scraper_service/scraper/
COPY restful_api/ /scraper_service/restful_api/

# listing files after copying - debug feature
RUN ls -la /scraper_service/scraper/*
RUN ls -la /scraper_service/restful_api/*

# migrate db
RUN python /scraper_service/restful_api/simple_rest_api/manage.py migrate
# prepare and run service
ENTRYPOINT ["python"]
CMD ["/scraper_service/restful_api/simple_rest_api/manage.py", "runserver", "0.0.0.0:8000"]