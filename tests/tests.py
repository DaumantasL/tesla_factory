import pytest

tesla = Tesla("S", "red")

def test_battery_default():
  assert tesla.check_battery_level() == "Battery charge level is 99.9%"
  
def test_drive():
  assert tesla.drive(100) == "Battery charge level is 69.9%"
  assert tesla.drive(420) == "Battery charge level is 69.9%"

def test_charge():
  tesla.charge_battery()
  assert tesla.check_battery_level() == "Battery charge level is 100%"