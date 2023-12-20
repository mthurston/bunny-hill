import mido

class MidiNote:
    def __init__(self, message_name, note, velocity, time):
        self.message_name = message_name
        self.note = note
        self.velocity = velocity
        self.time = time

    def __str__(self):
        return f"{self.message_name} {self.note} {self.velocity} {self.time}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.message_name == other.message_name and self.note == other.note and self.velocity == other.velocity and self.time == other.time

    def __hash__(self):
        return hash((self.message_name, self.note, self.velocity, self.time))

    def to_mido_message(self):
        return mido.Message(self.message_name, note=self.note, velocity=self.velocity, time=self.time)
