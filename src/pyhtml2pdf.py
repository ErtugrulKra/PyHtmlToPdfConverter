from logging import fatal
from jsonschema.validators import validate
from DeflateConverter import DeflateConverter
import pdfkit
from flask import Flask
import os
from flask.helpers import send_file
from flask_restplus import Api, Resource, fields
from flask import request, make_response
import base64 

options = {
    'page-size': 'A4',
    'margin-top': '0.40in',
    'margin-right': '0.40in',
    'margin-bottom': '0.1in',
    'margin-left': '0.25in',
    'encoding': "UTF-8",
    'no-outline': None
}

pdfApp=Flask(__name__)
api = Api(app=pdfApp,version='1.0', title='Html to Pdf Convert API',
    description='Html to PDF Convert API with wk2htmlpdf',)

resource_fields = api.model('Resource', {
     'DummyFieldGenerated-ReplaceWithBase64Content':fields.String,
})
 

@api.route('/htmltopdfConvert')
class PdfApiBase64(Resource):
    @api.doc(body=resource_fields)
    def post(self):
        file = request.data
        print (file)
        html = base64.b64decode(file)  # bytes

        pdfFileResult=pdfkit.from_string(html.decode("utf-8"), False) 

        result = base64.b64encode(pdfFileResult)
        response = make_response(result)
        response.headers.set('Content-Type', 'application/octet-stream')
        response.headers.set('Content-Disposition', 'attachment', filename='output.pdf')
        return response

@api.route('/metrics')
class Metic(Resource):
    def get(self):
        return "metric"

@api.route('/htmltopdfConvertComp')
class PdfApiCompress(Resource):
    @api.doc(body=resource_fields)
    def post(self):
        file = request.data
        
        converter=DeflateConverter()

        htmlData=converter.DecompressModel(file)

        pdfFileResult=pdfkit.from_string(htmlData.HtmlContent, False) 

        response = make_response(pdfFileResult)
        response.headers.set('Content-Type', 'application/octet-stream')
        response.headers.set('Content-Disposition', 'attachment', filename='output_gzip.pdf')
        return response


if __name__ == "__main__":
    pdfApp.run(host='0.0.0.0',port=5000,debug=True)


