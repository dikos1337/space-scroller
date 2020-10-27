class States:
    def __init__(self):
        self.current_state = "START_MENU"

    def play(self):
        self.current_state = "PLAY"

    # def start_menu(self):
    #     self.current_state = "START_MENU"

    def restart(self):
        self.current_state = "RESTART"
