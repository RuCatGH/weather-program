import eel
import pyowm
owm = pyowm.OWM("bb02973a865efc3f9127ee438670e44f")


@eel.expose
def get_weather(place):
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(place)
    w = observation.weather
    temp = w.temperature('celsius')['temp']
    return "В городе " + str(place) + " сейчас " + str(temp) + " градусов!"


eel.init('web')

eel.start('main.html', size=(700, 700))
