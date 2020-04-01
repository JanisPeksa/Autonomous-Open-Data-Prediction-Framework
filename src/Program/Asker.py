class Asker:

    @staticmethod
    def ask_string_answer(message) -> str:
        return input(message)

    @staticmethod
    def ask_update_frequency() -> float:
        update_frequency = float(input('Enter update frequency(integer or float)\n>'))
        return update_frequency
