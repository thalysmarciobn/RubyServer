import socket

from ruby.network.buffer.BufferArray import BufferArray

server_address = ('localhost', 5555)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
client_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, 60)
client_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, 10)
client_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPCNT, 5)

try:
    client_socket.connect(server_address)

    buffer = BufferArray()

    # 1 - 1 ( tokens: IMDummy )
    buffer.writeByte(1)
    buffer.writeByte(1)

    client_socket.sendall(buffer.toByteArray())

    response = client_socket.recv(1024)

    # OPDummy
    responseBuffer = BufferArray(response)

    token1 = responseBuffer.readByte()
    token2 = responseBuffer.readByte()

    ok = responseBuffer.readBool()

    print(ok)
except Exception as e:
    print(f'Error: {str(e)}')

finally:
    client_socket.close()