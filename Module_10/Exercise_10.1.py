class Elevator:
    def __init__(self, bf, tf):
        self.bottom = bf
        self.top = tf
        self.current = bf

    def go_to_floor(self, floor):
        while floor != self.current:
            if floor > self.current:
                self.floor_up()
            else:
                self.floor_down()

    def floor_up(self):
        self.current += 1
        print(f"↑ Is now in floor {self.current}")

    def floor_down(self):
        self.current -= 1
        print(f"↓ Is now in floor {self.current}")


def main():
    new_elevator = Elevator(0, 10)
    new_elevator.go_to_floor(6)
    new_elevator.go_to_floor(0)


main()
