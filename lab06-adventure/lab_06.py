class Room:
    def __init__(self, description: str = "", north: int | None = None, south: int | None = None, east: int | None = None, west: int | None = None):
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west


def generate_rooms() -> list[Room]:
    office = Room(
        "Estás en tu oficina.\nTienes una puerta a cada lado y un ventilador en la mesa.",
        east=1,
        west=3
    )
    east_hall = Room(
        "Estás en el pasillo este.\nAl norte está el comedor y al oeste tu oficina.\nTambién hay una sala al este.",
        north=5,
        east=2,
        west=0
    )
    kitchen = Room(
        "Estás en la cocina.\nHay platos y sartenes por todos lados. Qué desastre.\nTe has topado con Chica y te ha matado. GAME OVER.",
    )
    west_hall = Room(
        "Estás en el pasillo oeste.\nAl norte está el comedor y al este tu oficina.\nTambién hay una sala al oeste.",
        north=6,
        east=0,
        west=4
    )
    supply_closet = Room(
        "Estás en el armario.\nHay fregonas y otros utensilos de limpieza.\nAl este hay un pasillo.",
        east=3
    )
    east_dining_hall = Room(
        "Estás en la zona este del comedor.\nEs una sala muy grande, con muchas mesas.\nAl sur hay un pasillo y al oeste más comedor.",
        south=1,
        west=6
    )
    west_dining_hall = Room(
        "Estás en la zona oeste del comedor.\nEs una sala muy grande, con muchas mesas.\nAl sur hay un pasillo y al este más comedor.",
        south=3,
        east=5
    )
    return [
        office,
        east_hall,
        kitchen,
        west_hall,
        supply_closet,
        east_dining_hall,
        west_dining_hall
    ]


def print_rooms(rooms: list[Room]) -> None:
    for room in rooms:
        print(room.description)
        if room.north is not None:
            s = f"    n:\n{rooms[room.north].description}"
            print(s.replace("\n", "\n        "))
        if room.south is not None:
            s = f"    s:\n{rooms[room.south].description}"
            print(s.replace("\n", "\n        "))
        if room.east is not None:
            s = f"    e:\n{rooms[room.east].description}"
            print(s.replace("\n", "\n        "))
        if room.west is not None:
            s = f"    w:\n{rooms[room.west].description}"
            print(s.replace("\n", "\n        "))
        print()


def main() -> None:
    rooms = generate_rooms()
    print_rooms(rooms)

    cur_room = 0
    while True:
        room = rooms[cur_room]

        print(room.description)
        dir = input("¿Dirección? ")

        next_room = -1
        match dir:
            case 'n':
                next_room = room.north
            case 's':
                next_room = room.south
            case 'e':
                next_room = room.east
            case 'o' | 'w':
                next_room = room.west
            case 's' | 'q':
                break

        if next_room == -1:
            print("Entrada inválida. Escribe [n, s, e, o/w, s/q].")
        elif next_room is None:
            print("Dirección no disponible.")
        else:
            cur_room = next_room
        print()


if __name__ == "__main__":
    main()
