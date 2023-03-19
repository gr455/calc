FROM python:3

COPY calc.py /opt/calc.py

WORKDIR /opt

CMD ["python3", "calc.py"]