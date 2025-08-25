from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        super().__init__(first_name, is_alive)
        self.eyes = "brown"
        self.hairs = "dark"

    def get_eyes(self):
        return self.eyes

    def set_eyes(self, color: str):
        try:
            assert isinstance(color, str), "color is not atr type"
            color = color.lower()
            assert color in [
                "black", "blue", "brown", "gray", "green"
            ], "color is not a valid option"
            self.eyes = color
        except AssertionError as e:
            print(f"AssertionError: {e}")

    def get_hairs(self):
        return self.hairs

    def set_hairs(self, shade: str):
        try:
            assert isinstance(shade, str), "color is not atr type"
            shade = shade.lower()
            assert shade in [
                "dark", "light"
            ], "shade is not a valid option"
            self.hairs = shade
        except AssertionError as e:
            print(f"AssertionError: {e}")
