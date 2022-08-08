class Validator:
    @staticmethod
    def check_if_the_string_is_empty(value, number):
        if len(value) < number:
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
