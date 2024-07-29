import time

from src.infrastructure.dependencies import init_rabbitmq


def main():
    init_rabbitmq()


if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)
