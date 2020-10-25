FROM python:3.6-slim
WORKDIR /usr/src/app
COPY requirements.txt setup.py ./
COPY recipes_recommendation ./recipes_recommendation
COPY resources ./resources
RUN pip install --no-cache-dir -r requirements.txt
RUN useradd -M -s /bin/sh psi && chown -R psi:psi /usr/src/app
USER psi
CMD gunicorn -w 4 -b 0.0.0.0:$PORT recipes_recommendation.endpoints:APP
