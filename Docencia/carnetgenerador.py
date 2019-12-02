__author__ = "Josue Isai Hernandez Sanchez"
__email__ = "josueisaihs@gmail.com"

import qrcode as _QR_
import os


class QR:
    def __init__(self, codigo):
        self.codigo = codigo

    def generar(self):
        qr = _QR_.QRCode(
            version=1,
            error_correction=_QR_.constants.ERROR_CORRECT_H,
            box_size=10,
            border=0,

        )
        qr.add_data(self.codigo)
        qr.make()
        img = qr.make_image()
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file = open(os.path.join(
                            os.path.join(base_dir, "static", "image", "perfil", "student", "qrcode"),
                            "%s.png" % self.codigo
                        ),
                    "wb")
        img.save(file)
        file.close()

        return os.path.join(os.path.join("static", "image", "perfil", "student", "qrcode"), "%s.png" % self.codigo)
# <> fin QR
