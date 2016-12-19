class Relay:

    def __init__(self, pin: int):
        self.pin = pin

    def cleanup(self):
        ""

    def set_state(self, state: bool):
        self.state = state

    def get_state(self) -> bool:
        return self.state
