from db import DateBase, datetime
from datetime import timedelta
from time import sleep

print "**** Middle Version 2.1 ****"


class Stock:
	def __init__(self):
		self.Qr = []
		self.Hour = []
		self.Insert = []

	def addStock(self, qr):
		if not qr in set(self.Qr):
			print "Agregando lectura"
			self.Qr.append(qr)
			self.Hour.append(datetime.today())
			self.Insert.append(False)
			return True
		else:
			index = self.Qr.index(qr)
			fecha = self.Hour[index]
			# print fecha, datetime.today() - timedelta(days = 1. / (60. * 24.)), fecha < datetime.today() - timedelta(days = 1. / (60. * 24.))
			if fecha < datetime.today() - timedelta(days= 1. / (60. * 24.)):
				print "\n.:. Actualizando lectura"
				self.Hour[index] = datetime.today()
				self.Insert[index] = False
				return True
			else:
				print "=> Este codigo ya ha sido insertado: {}".format(qr)
				return False
	def getQr(self):
		try:
			index = self.Insert.index(False)
			self.Insert[index] = True
			return self.Qr[index]
		except ValueError:
			return None
# <> fin Stock


class Analisis:
	def __init__(self, raspberry):
		self.raspberryName = raspberry
		self.stock = Stock()
		self.analizando = True
		self.working = False

	def run(self):
		qr = self.stock.getQr()
		print ' ** Qr: %s ** ' % qr
		#try:
		self.insertarAsistencia = DateBase()

		if qr:
			return self.tomarAsistencia(qr)
		else:
			return False
		#except:
		#	print ".:. No se encuentra conectado, no se pudo subir a %s" % qr
		#	return False

	def tomarAsistencia(self, qr):
		#try:
		print '.:. Insertado lectura: {}'.format(qr)
		for glId in self.insertarAsistencia.queryGroupList(qr, self.raspberryName):
			return self.insertarAsistencia.insertAsistence(glId[0])
		
		print ".:. No se agrego la asistencia %s" % qr
		return False
		#except:
		#	print "=> No se encuentra conectado (ERROR)"
		#	return False

	def addStock(self, qr):
		print "=> Recibiendo Lectura: %s" % qr
		if self.stock.addStock(qr):
			return self.run()
		else:
			return False

	def close(self):
		try:
			self.insertarAsistencia.close()
		except:
			print "No se encuentra conectado"
# <> fin Analisis
