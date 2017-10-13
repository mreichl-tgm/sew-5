from src.control import rest
from src.view.view import View


class Control():
    def __init__(self, args):
        """
        The GUI's control unit used to update data and process user input
        """
        super().__init__()
        self.response_type = args
        self.view = View()
        # Add Qt Signals
        self.view.button_show.clicked.connect(self.calculate)

    def calculate(self):
        origin_string = self.view.line_origin
        target_string = self.view.line_target

        rest.get_route(origin_string, target_string, self.response_type)
