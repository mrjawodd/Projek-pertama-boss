import random
import sys
import time


class Player:
    def __init__(self, name: str):
        self.name = name
        self.health = 100
        self.hunger = 0
        self.thirst = 0
        self.inventory = {"food": 1, "water": 1}
        self.day = 1

    def status(self) -> str:
        return (
            f"Day {self.day} | {self.name} - Health: {self.health}, Hunger: {self.hunger}, Thirst: {self.thirst}\n"
            f"Inventory: food={self.inventory.get('food',0)}, water={self.inventory.get('water',0)}"
        )

    def end_of_turn(self):
        self.hunger = min(100, self.hunger + random.randint(5, 12))
        self.thirst = min(100, self.thirst + random.randint(7, 15))
        if self.hunger > 70:
            self.health -= (self.hunger - 70) // 3
        if self.thirst > 70:
            self.health -= (self.thirst - 70) // 2
        self.day += 1

    def is_alive(self) -> bool:
        return self.health > 0


def explore(player: Player):
    roll = random.randint(1, 100)
    print("Anda menjelajah area...")
    time.sleep(0.7)
    if roll <= 40:
        print("Tidak ada yang ditemukan.")
    elif roll <= 65:
        found_food = random.randint(1, 2)
        player.inventory['food'] = player.inventory.get('food', 0) + found_food
        print(f"Beruntung! Anda menemukan {found_food} makanan.")
    elif roll <= 85:
        found_water = 1
        player.inventory['water'] = player.inventory.get('water', 0) + found_water
        print("Anda menemukan 1 air bersih.")
    else:
        damage = random.randint(5, 25)
        player.health -= damage
        print(f"Anda diserang hewan liar dan kehilangan {damage} kesehatan!")


def rest(player: Player):
    heal = random.randint(5, 18)
    player.health = min(100, player.health + heal)
    print(f"Istirahat singkat. Memulihkan {heal} kesehatan.")


def eat(player: Player):
    if player.inventory.get('food', 0) > 0:
        player.inventory['food'] -= 1
        player.hunger = max(0, player.hunger - random.randint(15, 35))
        print("Anda makan makanan. Lapar berkurang.")
    else:
        print("Tidak ada makanan di inventori.")


def drink(player: Player):
    if player.inventory.get('water', 0) > 0:
        player.inventory['water'] -= 1
        player.thirst = max(0, player.thirst - random.randint(25, 45))
        print("Anda minum air. Dahaga berkurang.")
    else:
        print("Tidak ada air di inventori.")


def help_text():
    print("Perintah yang tersedia:")
    print("  explore  - Menjelajah area (mungkin menemukan makanan/air atau cedera)")
    print("  rest     - Istirahat untuk memulihkan kesehatan")
    print("  eat      - Makan makanan jika tersedia")
    print("  drink    - Minum air jika tersedia")
    print("  status   - Lihat status saat ini")
    print("  quit     - Keluar dari permainan")


def main():
    print("=== Survival Terminal Game ===")
    name = input("Masukkan nama karakter Anda: ").strip() or "Survivor"
    player = Player(name)

    help_text()

    while player.is_alive():
        cmd = input('\n> ').strip().lower()
        if cmd == 'explore':
            explore(player)
        elif cmd == 'rest':
            rest(player)
        elif cmd == 'eat':
            eat(player)
        elif cmd == 'drink':
            drink(player)
        elif cmd == 'status':
            print(player.status())
        elif cmd == 'help':
            help_text()
        elif cmd == 'quit':
            print('Keluar dari permainan. Sampai jumpa!')
            sys.exit(0)
        else:
            print('Perintah tidak dikenal. Ketik "help" untuk daftar perintah.')

        player.end_of_turn()
        if not player.is_alive():
            break
        if player.health <= 30:
            print("PERINGATAN: Kesehatan Anda rendah. Pertimbangkan untuk istirahat atau mencari makanan/air.")

    print('\n=== GAME OVER ===')
    print(f"{player.name} bertahan sampai hari {player.day - 1}.")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nKeluar oleh pengguna.')
  