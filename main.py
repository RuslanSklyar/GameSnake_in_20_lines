import pygame


def maim():
    y, step, head = segments = [15, 16, 17]
    n, apple = step, 99
    window = pygame.display.set_mode([225] * 2, pygame.SCALED).fill

    while segments.count(head) % 2 * head % n * (head & 240):
        if e := pygame.event.get(768):
            step = (e[0].key % 4 * 17 + 15) % 49 - n
        segments = segments[apple != head:] + [head + step]

        window("black")
        if apple == head:
            apple = segments[0]

        for i, v in enumerate([apple] + segments):
            window("green" if i else "red", ((v - 1) % n * y, (v - n) // n * y, y, y))
        pygame.display.flip()
        head += step
        pygame.time.wait(100)


if __name__ == "__main__":
    maim()
