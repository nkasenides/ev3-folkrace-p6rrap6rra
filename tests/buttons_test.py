import unittest
import time
from unittest.mock import MagicMock
from tests.ev3dev_test_util import Ev3devTestUtil
Ev3devTestUtil.create_fake_ev3dev_module()
from buttons import Buttons


class ButtonsUnitTest(unittest.TestCase):

    def setUp(self):
        self.buttons = Buttons()
        self.start_button_listener = MagicMock()
        self.ev3_buttons = MagicMock()
        self.buttons.ev3_buttons = self.ev3_buttons
        self.ev3_buttons.up = False
        self.ev3_buttons.down = False
        self.ev3_buttons.left = False
        self.ev3_buttons.right = False
        self.buttons.start()

    def _emulateUpButtonClick(self):
        self.ev3_buttons.up = True
        time.sleep(0.01)
        self.ev3_buttons.up = False

    def _emulateDownButtonClick(self):
        self.ev3_buttons.down = True
        time.sleep(0.01)
        self.ev3_buttons.down = False

    def _emulateLeftButtonClick(self):
        self.ev3_buttons.left = True
        time.sleep(0.01)
        self.ev3_buttons.left = False

    def _emulateRightButtonClick(self):
        self.ev3_buttons.right = True
        time.sleep(0.01)
        self.ev3_buttons.right = False

    def tearDown(self):
        self.buttons.stop()

    def test_shouldFireStartButtonPressedWhenEV3UpButtonPressed(self):
        #given
        self.buttons.addStartButtonListener(self.start_button_listener)

        #when 
        self._emulateUpButtonClick()

        #then
        self.start_button_listener.startButtonPressed.assert_called()

    def test_shouldNotFireStartButtonPressedWhenNoStartButtonListenerAddedAndEV3UpButtonPressed(self):
        #given

        #when 
        self._emulateUpButtonClick()

        #then
        self.start_button_listener.startButtonPressed.assert_not_called()

    def test_shouldNotFireStartButtonPressedWhenStartButtonListenerRemovedAndEV3UpButtonPressed(self):
        #given
        self.buttons.addStartButtonListener(self.start_button_listener)
        self.buttons.removeStartButtonListener()

        #when 
        self._emulateUpButtonClick()

        #then
        self.start_button_listener.startButtonPressed.assert_not_called()

    def test_shouldFireStartButtonPressedWhenEV3DownButtonPressed(self):
        #given
        self.buttons.addStartButtonListener(self.start_button_listener)

        #when 
        self._emulateDownButtonClick()

        #then
        self.start_button_listener.startButtonPressed.assert_called()

    def test_shouldNotFireStartButtonPressedWhenNoStartButtonListenerAddedAndEV3DownButtonPressed(self):
        #given

        #when 
        self._emulateDownButtonClick()

        #then
        self.start_button_listener.startButtonPressed.assert_not_called()

    def test_shouldNotFireStartButtonPressedWhenStartButtonListenerRemovedAndEV3DownButtonPressed(self):
        #given
        self.buttons.addStartButtonListener(self.start_button_listener)
        self.buttons.removeStartButtonListener()

        #when 
        self._emulateDownButtonClick()

        #then
        self.start_button_listener.startButtonPressed.assert_not_called()

    def test_shouldFireStartButtonPressedWhenEV3LeftButtonPressed(self):
        #given
        self.buttons.addStartButtonListener(self.start_button_listener)

        #when 
        self._emulateLeftButtonClick()

        #then
        self.start_button_listener.startButtonPressed.assert_called()

    def test_shouldNotFireStartButtonPressedWhenNoStartButtonListenerAddedAndEV3LeftButtonPressed(self):
        #given

        #when 
        self._emulateLeftButtonClick()

        #then
        self.start_button_listener.startButtonPressed.assert_not_called()

    def test_shouldNotFireStartButtonPressedWhenStartButtonListenerRemovedAndEV3LeftButtonPressed(self):
        #given
        self.buttons.addStartButtonListener(self.start_button_listener)
        self.buttons.removeStartButtonListener()

        #when 
        self._emulateLeftButtonClick()

        #then
        self.start_button_listener.startButtonPressed.assert_not_called()

    def test_shouldFireStartButtonPressedWhenEV3RightButtonPressed(self):
        #given
        self.buttons.addStartButtonListener(self.start_button_listener)

        #when 
        self._emulateRightButtonClick()

        #then
        self.start_button_listener.startButtonPressed.assert_called()

    def test_shouldNotFireStartButtonPressedWhenNoStartButtonListenerAddedAndEV3RightButtonPressed(self):
        #given

        #when 
        self._emulateRightButtonClick()

        #then
        self.start_button_listener.startButtonPressed.assert_not_called()

    def test_shouldNotFireStartButtonPressedWhenStartButtonListenerRemovedAndEV3RightButtonPressed(self):
        #given
        self.buttons.addStartButtonListener(self.start_button_listener)
        self.buttons.removeStartButtonListener()

        #when 
        self._emulateRightButtonClick()

        #then
        self.start_button_listener.startButtonPressed.assert_not_called()

if __name__ == '__main__':
    unittest.main()
