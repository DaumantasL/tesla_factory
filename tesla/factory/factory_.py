class Tesla:
    def __init__(self, model: str, color: str, autopilot: bool = False, efficiency: float=0.3):
        self.__model = model
        self.__color = color
        self.__autopilot = autopilot
        self.__battery_charge = 99.9
        self.__is_locked = True
        self.__seats_count = 5
        self.__efficiency = efficiency
        self.__battery_discharge_percent = 0.0
        
    def welcome(self) -> str:
        raise NotImplementedError

    @property
    def color(self) -> str:
        return self.__color
    
    @color.setter
    def color(self, new_color: str) -> str:
        self.__color = new_color
        
    @color.deleter
    def color(self) -> None:
        print("Color is removed")
        del self.__color
        
    def autopilot(self, obstacle: str) -> str:
      self.__obstacle = obstacle
      if self.__autopilot:
        return f"Tesla model {self.__model} avoids {self.__obstacle}"
      return "Autopilot is not available"
    
    @property
    def seats_count(self) -> int:
      return self.__seats_count
    
    @seats_count.setter
    def seats_count(self, new_seats_count: int) -> int:
      self.__new_seats_count = new_seats_count
      if new_seats_count >=2:
        self.__seats_count = new_seats_count
    
    def unlock(self)-> bool:
      self.__is_locked = False

    def lock(self)-> bool:
      self.__is_locked = True
    
    def open_doors(self) -> str:
        if self.__is_locked == True:
          return "Car is locked!"
        return "Doors opens sideways"

    def check_battery_level(self) -> str:
        return f"Battery charge level is {self.__battery_charge}%"
    
    def charge_battery(self):
        self.__battery_charge = 100
        self.check_battery_level()

    def drive(self, travel_range: float):
      self.__travel_range = travel_range
      self.__battery_discharge_percent = self.__travel_range * self.__efficiency

      if self.__battery_charge - self.__battery_discharge_percent >= 0:
        self.__battery_charge = self.__battery_charge - self.__battery_discharge_percent
      return self.check_battery_level()
    
    @property
    def is_locked(self) -> bool:
      return self.__is_locked

    @is_locked.setter
    def is_locked(self, new_is_locked: bool) -> bool:
        self.__is_locked = new_is_locked
