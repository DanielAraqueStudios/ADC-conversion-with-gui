class Button:
    def __init__(self, label, command):
        self.label = label
        self.command = command

    def click(self):
        self.command()


class Slider:
    def __init__(self, min_value, max_value, initial_value, callback):
        self.min_value = min_value
        self.max_value = max_value
        self.value = initial_value
        self.callback = callback

    def set_value(self, value):
        if self.min_value <= value <= self.max_value:
            self.value = value
            self.callback(value)


class Label:
    def __init__(self, text):
        self.text = text

    def update(self, new_text):
        self.text = new_text


class Checkbox:
    def __init__(self, label, initial_state=False):
        self.label = label
        self.checked = initial_state

    def toggle(self):
        self.checked = not self.checked


class Dropdown:
    def __init__(self, options, selected_option):
        self.options = options
        self.selected_option = selected_option

    def select(self, option):
        if option in self.options:
            self.selected_option = option
```