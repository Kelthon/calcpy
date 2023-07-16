# Observer
from src.event.event import Event

class EventManager():
    def __init__(self) -> None:
        self.listeners = []

    def listen(self, event: Event) -> None:
        self.listeners.append(event)

    def unlisten(self, event: Event) -> None:
        self.listeners.remove(event)

    def notify(self, type, data):
        for listener in self.listeners:
            if type is listener.type:
                listener.update(data)

    def __str__(self) -> str:
        pass