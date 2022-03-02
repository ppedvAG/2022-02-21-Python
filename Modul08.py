import traceback
import logging
# Fehlerbehandlung

logging.basicConfig(filename="test.log", encoding="utf-8", level=logging.DEBUG, filemode="w")

class BspException(TypeError):
    def __init__(self, msg):
        super(BspException, self).__init__("Ich bin eine Beispielexception: " + msg)


def who_to_greet(person):
    logging.debug("Die Funktion who_to_greet wurde aufgerufen")
    logging.debug(f"person: {person} Type: {type(person)}")
    return person if person else input('Greet who? ')


def greet(someone, greeting='Hello'):
    if type(someone) == str:
        print(greeting + ', ' + who_to_greet(someone))
    else:
        logging.warning(f"someone invalid type: {type(someone)}")
        raise BspException("Ungltige eingabe")

# https://stackoverflow.com/questions/51385195/writing-to-windows-event-log-using-win32evtlog-from-pywin32-library

def greet_many(people):
    for person in people:
        try:
            greet(person)
        except BspException as e:
            person = str(person)
            print("hi" + person)
            tb = traceback.format_exc()
            # Speichert uns den Traceback in eine Variable und erlaubt es uns diesen dann in ein log zu schreiben
            logging.error(tb)
        else:
            print("greet wurd erfolgreich ausgeführt")
        finally:
            print("Alles fertig, aber es wurde eventuell ein Fehler geworfen")
            # Nützlich um Dateien oder Datenbankverbindungen zu schließen, egal ob die Operation
            # erfolgreich oder unerfolgreich lief


        # except Exception as e:
        #     print(e)
        #     print('hi, ' + person)


greet_many(['Chad', 'Dan', 1])

