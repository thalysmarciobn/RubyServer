from commons.communication.Output import Output


class OPShamanSkills(Output):
    tokens = [8, 22]

    def __init__(self, skills: dict, update: bool):
        super().__init__()
        self.bufferArray.writeByte(len(skills))
        for _key, _value in skills:
            self.bufferArray.writeByte(_key)
            self.bufferArray.writeByte(_value)
        self.bufferArray.writeBool(update)
