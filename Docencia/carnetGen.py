import os, sys, io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

from .carnetgenerador import QR
from random import randint
from hashlib import blake2s

DEBUG = False

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

class CreadorCarnetPDF:    
    documentTitle = "Mi Primer PDF"
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    buffer = BASE_DIR  + "/static/carnets/mydoc.pdf"
    imagefondo = "carnet.png"
    pdf = canvas.Canvas(buffer, pagesize=letter)
    pdf.setAuthor("Josue Isai Hernandez | ElijoSoft")
    pdf.setTitle(documentTitle)

    pc = .75
    w = 321 * pc
    h = 208 * pc

    dim = {
        0: (25, 600), 1: (25, 434), 2: (25, 268), 3: (25, 102),
        4: (286, 600), 5: (286, 434), 6: (286, 268), 7: (286, 102),
    }

    lista = []

    useBuffer = True

    def generar(self):        
        countpag = 1
        count = 0
        for student in self.lista:
            index = count % 8
            x, y = self.dim[index]
            if index == 0 and count > 6:
                self.pdf.drawString(20, 770, "-" * 60 + "Generador de Identificacion" + "-" * 60)
                self.pdf.drawString(20, 20, "-" * 80 + "Pagina %s" % countpag + "-" * 80)        
                self.pdf.showPage()
                countpag += 1

            self.pdf.rect(x, y, self.w, self.h)
            self.pdf.drawImage(self.BASE_DIR + '/static/carnets/%s' % self.imagefondo, x, y, width=self.w, height=self.h)

            qr = QR(student[2])
            
            self.pdf.drawImage(qr.generar(), x + 150, y + 10, width=80, height=80)

            qr.delete()
            
            self.pdf.setFontSize(8)
            self.pdf.setFontSize(10)
            self.pdf.drawString(x + 20, y + 80, "Nombre:")
            self.pdf.drawString(x + 25, y + 65, student[0])
            self.pdf.drawString(x + 25, y + 50, student[1])
            self.pdf.setFontSize(8)
            self.pdf.drawString(x + 20, y + 30, "ID:")
            self.pdf.setFontSize(10)
            self.pdf.drawString(x + 25, y + 15, student[2])
            
            count += 1

        self.pdf.save()

    def delete(self):
        os.remove(os.path.join(os.path.join("static", "image", "perfil", "student", "qrcode"), "%s_%s.png" % (self.codigo, self.hash.hexdigest())))
# <> fin CreadorCarnetPDF

if DEBUG:
    creadorCarnetPDF = CreadorCarnetPDF()
    creadorCarnetPDF.useBuffer = False
    creadorCarnetPDF.buffer = creadorCarnetPDF.BASE_DIR  + "/static/carnets/mydoc.pdf"
    creadorCarnetPDF.pdf = canvas.Canvas(creadorCarnetPDF.buffer, pagesize=letter)
    creadorCarnetPDF.lista.append(("Josue Isai", "Hernandez Sanchez", "94050830909"))
    creadorCarnetPDF.lista.append(("Josue Isai", "Hernandez Sanchez", "93082631641"))
    creadorCarnetPDF.lista.append(("Josue Isai", "Hernandez Sanchez", "95111305021"))

    print(creadorCarnetPDF.generar())