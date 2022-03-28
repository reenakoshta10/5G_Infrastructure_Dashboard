FROM python:3.9
EXPOSE 8501
RUN mkdir /app
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

# ENTRYPOINT ["streamlit", "run"]

# CMD ["code/app.py"]

CMD streamlit run code/app.py --server.port $PORT