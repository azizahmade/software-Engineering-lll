from command import Command
from receiver import Light
from invoker import RemoteControl

class TurnOnLightCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

    def undo(self):
        self.light.turn_off()

def main():
    light = Light()
    turn_on_command = TurnOnLightCommand(light)
    remote_control = RemoteControl()

    remote_control.set_command(turn_on_command)
    remote_control.press_button()

if __name__ == "__main__":
    main()