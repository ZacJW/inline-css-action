FROM python:3.8

COPY inline-css.py /inline-css.py
COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
