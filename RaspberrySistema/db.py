import sqlite3 as sql
import MySQLdb as mysql
from datetime import datetime


class DateBase:
    def __init__(self):
        self.conection()

    def conection(self):
        dataBaseHost = {
            'LETRAN': ('192.168.137.6', 'moodleuser', 'modlemin2018', 'letransistema')
        }

        host, user, passwd, db = dataBaseHost["LETRAN"]
        print "Modo Remoto"
        print "Conectando a Host: %s\tDB: %s" % (host, db)
        
        self.db = mysql.connect(
            host=host, 
            user=user, 
            passwd=passwd, 
            db=db
        )
        self.cursor = self.db.cursor()

        print ".:. Conectado .:."

    def queryGroupList(self, ci, rasp):
        print "=> Buscando para %s %s" % (ci, rasp)
        self.cursor.execute(
            '''
            SELECT Gl.id
            FROM 
                Docencia_studentpersonalinformation AS Student, 
                Docencia_candidate AS Candidate, 
                Docencia_raspberrys AS Rasp, 
                Docencia_groupinformation AS Gp, 
                Docencia_grouplist AS Gl 
            WHERE 
                Student.numberidentification = '%s' AND 
                Rasp.name = '%s' AND 
                Rasp.classroom_id = Gp.classroom_id AND 
                Candidate.student_id = Student.id AND 
                Candidate.course_id = Gp.course_id AND 
                Candidate.id = Gl.student_id AND 
                Gp.id = Gl.group_id;
            ''' % (ci, rasp)
        )

        return self.cursor.fetchall()

    def insertAsistence(self, glId):
        print "=> Insertando ..."

        self.checkAsistence(glId)

        self.cursor.execute(
            '''
            INSERT INTO Docencia_assistence(assis_dateTime, assis_grouplist_id, assis_status, assis_mode) VALUES (now(), %s, 'a', 'a');
            ''' % glId
        )

        self.commit()

        return self.cursor.lastrowid != 0

    def checkAsistence(self, glId):
        fecha = datetime.today()
        fechaIni = datetime(fecha.year, fecha.month, fecha.day, 0, 0, 0)
        fechaFin = datetime(fecha.year, fecha.month, fecha.day, 23, 59, 59)

        self.cursor.execute(
            '''
            DELETE FROM Docencia_assistence WHERE assis_dateTime >= "%s" AND assis_dateTime <= "%s" AND assis_grouplist_id = %s
            ''' % (fechaIni, fechaFin, glId)
        )

        self.commit()
    
    def close(self):
		self.cursor.close()
		self.db.close()
        
    def commit(self):
		self.db.commit()
# <> fin DateBase