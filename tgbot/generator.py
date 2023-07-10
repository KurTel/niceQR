class Generator:
    def __init__(self, url, prompt):
        self._url = url
        self._prompt = prompt


    def generate(self):
        print('generate me')
        self._verifyQr('123.png')


    def _verifyQr(self, png):
        print('verify me')
