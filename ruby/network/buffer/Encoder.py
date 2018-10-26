from ruby.network.buffer.BufferArray import BufferArray


class Encoder():

    def encoder(self, message):
        if type(message) is str:
            return message.encode()
        else:
            Output = message
            bufferArray = Output.bufferArray
            packet = BufferArray()
            length = bufferArray.length() + 2
            if length <= 0xFF:
                packet.writeByte(1)
                packet.writeByte(length)
            elif length <= 0xFFFF:
                packet.writeByte(2)
                packet.writeShort(length)
            elif length <= 0xFFFFFF:
                packet.writeByte(3);
                packet.writeByte((length >> 18) & 0xFF);
                packet.writeByte((length >> 8) & 0xFF);
                packet.writeByte(length & 0xFF)
            packet.writeByte(Output.output[0]);
            packet.writeByte(Output.output[1]);
            packet.writeBytes(bufferArray.toByteArray())
            return packet.toByteArray()