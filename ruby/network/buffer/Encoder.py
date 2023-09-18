from ruby.network.buffer.BufferArray import BufferArray


class Encoder:

    @staticmethod
    def encoder(message):
        if type(message) is str:
            return message.encode()
        else:
            output = message
            buffer_array = output.bufferArray
            packet = BufferArray()
            for token in output.output:
                packet.writeByte(token)
            packet.writeBytes(buffer_array.toByteArray())
            return packet.toByteArray()