class Bird:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def describe(self):
        return f'Размер птицы {self.name} — {self.size}.'


class Parrot(Bird):

    def __init__(self, name, size, color):
        super().__init__(name)
        super().__init__(size)
        self.color = color


class Penguin(Bird):

    def __init__(self, name, size, genus):
        super().__init__(name)
        super().__init__(size)
        self.genus = genus


kesha = Parrot('Ара', 'средний', 'красный')
kowalski = Penguin('Королевский', 'большой', 'Aptenodytes')
