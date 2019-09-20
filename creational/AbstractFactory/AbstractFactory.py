from __future__ import annotations
from abc import ABC, abstractmethod


class Button:
    def press(self):
        pass


class Checkbox:
    def check(self):
        pass


class WinButton(Button):
    def press(self):
        return super().press()


class MacButon(Button):
    def press(self):
        return super().press()


class WinCheckbox(Checkbox):
    def check(self):
        return super().check()


class MacCheckbox(Checkbox):
    def check(self):
        return super().check()


class GUIFactory(ABC):
    def createButton(self) -> Button():
        pass

    def createCheckbox() -> Checkbox():
        pass


class WinFactory(GUIFactory):
    def createButton(self):
        return WinButton()

    def createCheckbox(self):
        return WinCheckbox()


class MacFactory(GUIFactory):
    def __init__(self, button=None, checkbox=None):
        self.button = button
        self.checkbox = checkbox

    def __repr__(self):
        return (
            "MacFactory("
            "button={button}, "
            "checkbox={checkbox}"
            ")".format(
                button=self.button,
                checkbox=self.checkbox
            )
        )

    def createButton(self):
        return MacButon()

    def createCheckbox(self):
        return MacCheckbox()


class Applications:
    # factory = GUIFactory()
    # button = Button()
    # checkbox = Checkbox()
    def __init__(self, factory):
        self.factory = factory
        self.button = None
        self.checkbox = None

    # def set_factory(self, factory):
    #     self.factory = factory

    def createUI(self):
        self.button = self.factory.createButton()
        self.checkbox = self.factory.createCheckbox()
        return self.button, self.checkbox

    def press(self):
        self.button.press()

    def check(self):
        self.checkbox.check()


if __name__ == "__main__":
    available_os = ['Windows', 'Mac']
    factory = MacFactory()
    print(factory)
    app = Applications(factory)
    button, checkbox = app.createUI()
    button.press()
    checkbox.check()
    print(button, checkbox)
    print(app.factory)

