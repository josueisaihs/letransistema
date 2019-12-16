__author__ = "Josue Isai Hernandez Sanchez"
__email__ = "josueisaihs@gmail.com"

import qrcode as _QR_
import os
from io import BytesIO
from random import randint
from hashlib import blake2s

class QR:
    def __init__(self, codigo):
        self.codigo = codigo

        self.buffer = BytesIO()

        self.hash = blake2s(bytes(str(randint(0, 1000)), "UTF-8"), digest_size=4)

    def generar(self, outPutBuffer=False):
        qr = _QR_.QRCode(
            version=1,
            error_correction=_QR_.constants.ERROR_CORRECT_H,
            box_size=10,
            border=0,

        )
        qr.add_data(self.codigo)
        qr.make()
        img = qr.make_image()        

        if outPutBuffer:
            val = self.buffer.getvalue()
            img.save(self.buffer)
            return val
        else:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            file = open(os.path.join(
                                os.path.join(base_dir, "static", "image", "perfil", "student", "qrcode"),
                                "%s_%s.png" % (self.codigo, self.hash.hexdigest())
                            ),
                        "wb")
            img.save(file)
            file.close()

            return os.path.join(os.path.join("static", "image", "perfil", "student", "qrcode"), "%s_%s.png" % (self.codigo, self.hash.hexdigest()))
    
    def delete(self):
        os.remove(os.path.join(os.path.join("static", "image", "perfil", "student", "qrcode"), "%s_%s.png" % (self.codigo, self.hash.hexdigest())))
# <> fin QR
