class System:
    def __init__(self, equilibrium_point):
        self.equilibrium_point = equilibrium_point
        self.current_state = equilibrium_point

def disturb(self, disturbance):
        self.current_state += disturbance

def check_stability(self):
        if self.current_state == self.equilibrium_point:
            return "System is stable"
        elif abs(self.current_state - self.equilibrium_point) < 0.1:
            return "System is nearly stable"
        else:
            return "System is unstable"

system = System(equilibrium_point=0.0)
print(system.check_stability())  # Output: System is stable

system.disturb(0.05)
print(system.check_stability())  #output: is nearly stable

system.disturb(0.2)
print(system.check_stability()) #output: system is unstable
