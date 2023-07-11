import zxing
import os
import re
from amzqr import amzqr

dirToSave = os.getcwd() + '/temp_qr'

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

        version, level, qr_name = amzqr.run(
            url,
            version=10,
            level='H',
            picture=None,
            colorized=False,
            contrast=1.0,
            brightness=1.0,
            save_name=qrImgName,
            save_dir=dirToSave
        )
        isValid = self._verifyQr(qr_name)
        print('isValid = ', isValid)
        
        return qr_name


    def _verifyQr(self, png):
        reader = zxing.BarCodeReader()
        barcode = reader.decode(png)
        print(barcode)
        return barcode.parsed is not None
    
    
    def decodeQr(self, png):
        reader = zxing.BarCodeReader()
        return reader.decode(png)
