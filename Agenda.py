from Partida import Partida
from mongoengine import *

connect('heroku_8jrhk4q8', host='mongodb://user:user1234@ds117334.mlab.com:17334/heroku_8jrhk4q8')


class Agenda(Document):
    partidas = []
    nombre = StringField(max_length=50, required=True)

    def crearPartida(self, lugar, fecha, hora):
        p = Partida(lugar, fecha, hora)
        self.partidas.append(p)

    def listarPartidas(self, fecha=""):
        print("###### Agenda de partidas de " + self.nombre)
        for p in self.partidas:
            p.detalles()

    def contarPartidas(self, mes=-1, year=-1):
        numPartidas = 0

        if mes != -1:
            for p in self.partidas:
                if p.fecha.date().month == mes:
                    numPartidas += 1

        elif year != -1:
            for p in self.partidas:
                if p.fecha.date().year == year:
                    numPartidas += 1

        else:
            for p in self.partidas:
                numPartidas += 1

        return numPartidas
