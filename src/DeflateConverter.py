from htmltopdfModel import HtmlToPdfModel
import deflate
import json 
from types import SimpleNamespace

class DeflateConverter:
    def DecompressModel(self,byteData)-> HtmlToPdfModel:
        result=deflate.gzip_decompress(byteData)

        model=json.loads(result, object_hook=lambda d: SimpleNamespace(**d))

        return model

    def Compress(self,byteData):
        result=deflate.gzip_compress(byteData)

        return result




 
