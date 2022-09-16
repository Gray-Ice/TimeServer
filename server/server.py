import datetime
import socket


def get_time() -> str:
    """获取当前的时间的字符串格式(精确到秒)"""
    now = datetime.datetime.now()
    return str(int(now.timestamp()))


def main():
    print("Start main...")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Start binding...")
    sock.bind(("0.0.0.0", 123))
    print("Start listening...")
    sock.listen()

    while True:
        print("waiting for connection...")
        client, addr = sock.accept()

        # 获取当前系统时间
        now = get_time()
        # 返回客户端时间
        client.send(now.encode("utf-8"))
        print(addr)
        client.close()


if __name__ == "__main__":
    main()
