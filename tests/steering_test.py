import unittest
from unittest.mock import Mock, MagicMock, patch
ev3dev_mock = MagicMock()
ev3_mock = MagicMock()
import sys
sys.modules["ev3dev"] = ev3dev_mock
sys.modules["ev3dev.ev3"] = ev3_mock
from steering import Steering

class SteeringUnitTest(unittest.TestCase):

    def setUp(self):
        self.settings = MagicMock()

    def test_shouldReadSteeringMotorAddressFromSettings(self):
        # given

        # when
        self.steering = Steering(self.settings)

        # then
        self.settings.getSteeringMotorAddress.assert_called_once()
        self.assertIsNotNone(self.steering.steering_motor)

    def test_shouldReadSteeringMotorSpeedFactorFromSettings(self):
        # given

        # when
        self.steering = Steering(self.settings)

        # then
        self.settings.getSteeringMotorSpeedFactor.assert_called_once()

    def test_shouldReadSteeringSpeedFromSettings(self):
        # given

        # when
        self.steering = Steering(self.settings)

        # then
        self.settings.getSteeringSpeed.assert_called_once()

    def test_shouldReadSteeringMaxRangeFromSettings(self):
        # given

        # when
        self.steering = Steering(self.settings)

        # then
        self.settings.getSteeringMaxRange.assert_called_once()

    def test_shouldCalculateCorrectCurrentSteeringPositionWhenTurnedLeft(self):
        # given
        self.settings.getSteeringMotorAddress.return_value = 'steering_motor'
        self.settings.getSteeringMotorSpeedFactor.return_value = 123
        self.settings.getSteeringSpeed.return_value = 10
        self.settings.getSteeringMaxRange.return_value = 47
        self.steering = Steering(self.settings)
        self.steering.steering_motor = MagicMock()
        self.steering.steering_motor.position = -21

        # when
        actual_steering_position = self.steering.getCurrentSteeringPosition()

        # then
        self.assertAlmostEqual(-21 * 100 / 47, actual_steering_position, places=2)

    def test_shouldCalculateCorrectCurrentSteeringPositionWhenTurnedMaxLeft(self):
        # given
        self.settings.getSteeringMotorAddress.return_value = 'steering_motor'
        self.settings.getSteeringMotorSpeedFactor.return_value = 123
        self.settings.getSteeringSpeed.return_value = 10
        self.settings.getSteeringMaxRange.return_value = 47
        self.steering = Steering(self.settings)
        self.steering.steering_motor = MagicMock()
        self.steering.steering_motor.position = -47

        # when
        actual_steering_position = self.steering.getCurrentSteeringPosition()

        # then
        self.assertAlmostEqual(-100, actual_steering_position, places=2)

    def test_shouldCalculateCorrectCurrentSteeringPositionWhenTurnedRight(self):
        # given
        self.settings.getSteeringMotorAddress.return_value = 'steering_motor'
        self.settings.getSteeringMotorSpeedFactor.return_value = 123
        self.settings.getSteeringSpeed.return_value = 10
        self.settings.getSteeringMaxRange.return_value = 47
        self.steering = Steering(self.settings)
        self.steering.steering_motor = MagicMock()
        self.steering.steering_motor.position = 18

        # when
        actual_steering_position = self.steering.getCurrentSteeringPosition()

        # then
        self.assertAlmostEqual(18 * 100 / 47, actual_steering_position, places=2)

    def test_shouldCalculateCorrectCurrentSteeringPositionWhenTurnedMaxRight(self):
        # given
        self.settings.getSteeringMotorAddress.return_value = 'steering_motor'
        self.settings.getSteeringMotorSpeedFactor.return_value = 123
        self.settings.getSteeringSpeed.return_value = 10
        self.settings.getSteeringMaxRange.return_value = 47
        self.steering = Steering(self.settings)
        self.steering.steering_motor = MagicMock()
        self.steering.steering_motor.position = 47

        # when
        actual_steering_position = self.steering.getCurrentSteeringPosition()

        # then
        self.assertAlmostEqual(100, actual_steering_position, places=2)

    def test_shouldCalculateCorrectCurrentSteeringPositionWhenAtCenter(self):
        # given
        self.settings.getSteeringMotorAddress.return_value = 'steering_motor'
        self.settings.getSteeringMotorSpeedFactor.return_value = 123
        self.settings.getSteeringSpeed.return_value = 10
        self.settings.getSteeringMaxRange.return_value = 47
        self.steering = Steering(self.settings)
        self.steering.steering_motor = MagicMock()
        self.steering.steering_motor.position = 0

        # when
        actual_steering_position = self.steering.getCurrentSteeringPosition()

        # then
        self.assertAlmostEqual(0, actual_steering_position, places=2)

    def test_shouldResetSteeringPositionToCenterWhenInitialized(self):
        # given
        self.settings.getSteeringMotorAddress.return_value = 'steering_motor'
        self.settings.getSteeringMotorSpeedFactor.return_value = 123
        self.settings.getSteeringSpeed.return_value = 10
        self.settings.getSteeringMaxRange.return_value = 47
        self.steering = Steering(self.settings)
        self.steering.steering_motor = MagicMock()
        self.steering.steering_motor.position = 32

        # when
        self.steering.initialize()

        # then
        self.assertAlmostEqual(0, self.steering.getCurrentSteeringPosition(), places=2)

    def test_shouldTurnMaxRangePlusCompensationRightForCenteringWhenInitialized(self):
        # given
        self.settings.getSteeringMotorAddress.return_value = 'steering_motor'
        self.settings.getSteeringMotorSpeedFactor.return_value = 123
        self.settings.getSteeringSpeed.return_value = 10
        self.settings.getSteeringMaxRange.return_value = 47
        self.steering = Steering(self.settings)
        self.steering.steering_motor = MagicMock()
        self.steering.steering_motor.position = 32

        # when
        self.steering.initialize()

        # then
        self.steering.steering_motor.run_to_rel_pos.assert_called_with(position_sp=-(47 + 7), speed_sp=(10 * 123), stop_action='hold')

