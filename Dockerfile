FROM python:3.6.9

WORKDIR /

RUN wget https://s3.amazonaws.com/shopify-managemant-app/wkhtmltopdf-0.9.9-static-amd64.tar.bz2
RUN tar xvjf wkhtmltopdf-0.9.9-static-amd64.tar.bz2
RUN mv wkhtmltopdf-amd64 /usr/local/bin/wkhtmltopdf
RUN chmod +x /usr/local/bin/wkhtmltopdf

COPY src/installs.txt .

RUN pip3 install -r installs.txt

COPY ./src .

EXPOSE 5000

CMD [ "python", "./pyhtml2pdf.py" ]

EXPOSE 8000