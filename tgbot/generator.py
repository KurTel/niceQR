import zxing
import os
import re

dirToSave = 'temp_qr'

class Generator:
    def __init__(self, id):
        self._id = id
        self._createTempDir()


    def _createTempDir(self):
        if not os.path.exists(dirToSave):
            os.mkdir(dirToSave)


    def generate(self, url, prompt):
        print('generate me')
        urlName = re.sub('[^a-zA-Z0-9 \n\.]', '', url)
        qrImgName = str(self._id) + '_' + urlName + '.png'
        qrImgPath = dirToSave + '/' + qrImgName
        generateCmd = 'amzqr '+ url +' -n ' + qrImgName + ' -v 10 -l H -d ' + dirToSave
        os.system(generateCmd)
        isValid = self._verifyQr(qrImgPath)
        print('isValid = ', isValid)
        return qrImgPath


    def _verifyQr(self, png):
        reader = zxing.BarCodeReader()
        barcode = reader.decode(png)
        print(barcode)
        return barcode.parsed is not None
    
    
    def decodeQr(self, png):
        reader = zxing.BarCodeReader()
        return reader.decode(png)
