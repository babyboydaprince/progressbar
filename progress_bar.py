from time import sleep
from colorama import Fore
from tqdm import trange


def progress_bar():
    t = trange(100, desc="Desc", leave=True)
    for _ in t:
        t.set_description("Loading caffeine")
        t.refresh()  # live update
        sleep(0.1)


def coffee():
    print(rf"""{Fore.RED}
         )))
        ((({Fore.RESET}{Fore.YELLOW}
      +-----+
      |     |]
      `-----' {Fore.RESET}{Fore.BLUE}
    ___________
    `---------'{Fore.RESET}{Fore.GREEN}
 In Coffee we trust{Fore.RESET}
    """)


if __name__ == "__main__":
    coffee()
    print("Sipping...")
    progress_bar()
    tick = u'\u2713'
    print(f"Coffee injection ready! [{tick}]")
