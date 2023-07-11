import zxing

class Generator:
    def __init__(self, url, prompt):
        self._url = url
        self._prompt = prompt


    def generate(self):
        print('generate me')
        isValid = self._verifyQr('/Users/artem/Downloads/photo_2023-07-10 15.14.58.jpeg')
        print(isValid)


    def _verifyQr(self, png):
        reader = zxing.BarCodeReader()
        barcode = reader.decode(png)
        print(barcode)
        return barcode.parsed is not None
