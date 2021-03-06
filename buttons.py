import ev3dev.ev3 as ev3
import logging
from threading import Thread


class Buttons(Thread):
    
    def __init__(self):
        Thread.__init__(self)
        self.setName('Buttons')
        self.stop_command_received = False
        self.ev3_buttons = ev3.Button()
        self.start_button_listener = None
        self.stop_button_listener = None

    def _anyArrowButtonPressed(self):
        return (self.ev3_buttons.up | self.ev3_buttons.down | self.ev3_buttons.left | self.ev3_buttons.right)

    def _backButtonPressed(self):
        return self.ev3_buttons.backspace

    def _hasStartButtonListener(self):
        return (self.start_button_listener != None)
        
    def _hasStopButtonListener(self):
        return not (self.stop_button_listener is None)

    def addStartButtonListener(self, start_button_listener):
        logging.debug('Start button listener added')
        self.start_button_listener = start_button_listener

    def addStopButtonListener(self, stop_button_listener):
        logging.debug('Stop button listener added')
        self.stop_button_listener = stop_button_listener

    def removeStartButtonListener(self):
        logging.debug('Start button listener removed')
        self.start_button_listener = None

    def removeStopButtonListener(self):
        logging.debug('Stop button listener removed')
        self.stop_button_listener = None

    def run(self):
        logging.debug('Buttons started.')
        while (self.stop_command_received == False):
            if (self._hasStartButtonListener() and self._anyArrowButtonPressed()):
                logging.debug('Any arrow button pressed and start button listener is present')
                self.start_button_listener.startButtonPressed()
            if (self._hasStopButtonListener() and self._backButtonPressed()):
                logging.debug('Back button pressed and stop button listener is present')
                self.stop_button_listener.stopButtonPressed()
        logging.debug('Buttons stopped.')

    def stop(self):
        logging.debug('Stop requested.')
        self.stop_command_received = True

