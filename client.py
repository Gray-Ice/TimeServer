import os
import socket
import sys
from datetime import datetime


def get_time_from_server():
    """
    从服务器获取时间, 如果与服务器的连接出错就退出程序
    :return:
    """
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        conn.connect(("picbed.wdnnd.cn", 123))
    except (ConnectionError, ConnectionRefusedError):
        print("False to connect server.")
        sys.exit(-1)

    msg = conn.recv(1000)
    try:
        return msg.decode("utf-8")
    except UnicodeDecodeError:
        return None


def main():
    now: str = get_time_from_server()
    if now is None:
        print("False to get time")
        return -1
    elif not now.isalnum():
        print("Warning!!! The data from server is not timestamp!")
        return -1

    try:
        now: datetime = datetime.fromtimestamp(int(now))
    except Exception:
        print("Error! Timestamp cannot convert to datetime(), maybe your server was hacked by someone")

    print(now)
    years = now.year
    months = now.month
    days = now.day
    hours = now.hour
    minutes = now.minute
    seconds = now.second
    status_code = os.system(f"sudo date -s \"{years}-{months}-{days} {hours}:{minutes}:{seconds}\"")
    if status_code == 0:
        print("Set time successfully")
        return 0
    else:
        print("Meet error when set time")
        return -1


if __name__ == "__main__":
    main()
