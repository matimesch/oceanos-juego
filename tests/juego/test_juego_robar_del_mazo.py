import pytest
from collections import Counter as Multiset
from juego.juego import EstadoDelJuego, JuegoException

def test_SiSeInicióRonda_AlRobarDelMazo_SeDevuelvenDosCartas():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	cartasParaRobarDelMazo = juego.robarDelMazo()
	
	assert len(cartasParaRobarDelMazo) == 2

def test_SiSeInicióRonda_AlRobarDelMazo_LasCartasDevueltasSonLasDelTopeDelMazo():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	cartasParaRobarDelMazo = juego.robarDelMazo()
	
	assert cartasParaRobarDelMazo[0] == juego.mazo[-1]
	assert cartasParaRobarDelMazo[1] == juego.mazo[-2]

def test_SiElMazoTieneUnaCarta_AlRobarDelMazo_SeDevuelveUnaCarta():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.mazo = [juego.mazo[0]]
	
	cartasParaRobarDelMazo = juego.robarDelMazo()
	
	assert len(cartasParaRobarDelMazo) == 1

def test_SiElMazoTieneUnaCarta_AlRobarDelMazo_LaCartaDevueltaEsLaDelTopeDelMazo():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	cartasParaRobarDelMazo = juego.robarDelMazo()
	
	assert cartasParaRobarDelMazo[0] == juego.mazo[-1]

def test_SiElMazoNoTieneCartas_NoSePuedeRobarDelMazo():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.mazo = []
	
	with pytest.raises(JuegoException) as excepcion:
		juego.robarDelMazo()
	
	assert "No se puede robar de un mazo vacío" in str(excepcion.value)

def test_SiSeIntentóRobarDelMazoSinElegir_NoSePuedeRobarDelMazo():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelMazo()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.robarDelMazo()
	
	assert "No se ha concretado el robo del mazo (¡falta elegir!)" in str(excepcion.value)

def test_SiSeIntentóRobarDelMazoSinElegir_NoSePuedeJugarDúos():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelMazo()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.jugarDuo(Multiset())
	
	assert "No se ha concretado el robo del mazo (¡falta elegir!)" in str(excepcion.value)

def test_SiSeIntentóRobarDelMazoSinElegir_NoSePuedePasarDeTurno():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelMazo()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.pasarTurno()
	
	assert "No se ha concretado el robo del mazo (¡falta elegir!)" in str(excepcion.value)

def test_SiSeIntentóRobarDelMazoSinElegir_NoSePuedeRobarDelDescarte():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelMazo()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.robarDelDescarte(0)
	
	assert "No se ha concretado el robo del mazo (¡falta elegir!)" in str(excepcion.value)

def test_SiSeInicióRondaYSeRobóDelMazo_NoSePuedeRobarDelMazo():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	
	with pytest.raises(JuegoException) as excepcion:
		juego.robarDelMazo()
	
	assert "Ya se ha robado en este turno" in str(excepcion.value)