from time import sleep

def scrolltype(
    text, time: float = 0.05, sep: str = "", end: str = "", flush: bool = True
):
    for letter in list(text):
        print(f"{letter}{sep}", end=end, flush=flush)
        sleep(time)
    print("")


if __name__ == "__main__":
    scrolltype("BRUH")