FROM python:3.9

WORKDIR /app

COPY app.py /app/
COPY model.h5 /app/
COPY data_daily.csv /app/

RUN pip install Flask
RUN pip install numpy
RUN pip install tensorflow
RUN pip install pandas
RUN pip install scikit-learn
RUN pip install datetime

EXPOSE 5000

CMD ["python", "app.py"]
