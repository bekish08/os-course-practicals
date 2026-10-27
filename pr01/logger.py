#!/usr/bin/env python3

import time
from datetime import datetime
from pathlib import Path

LOG_FILE = Path.home() / "os-course" / "pr01" / "results" / "time.log"


def main():
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    print(f"Logging time to {LOG_FILE}")

    while True:
        current_time = datetime.now().astimezone().isoformat(
            timespec="seconds"
        )

        with LOG_FILE.open("a", encoding="utf-8") as file:
            file.write(f"{current_time}\n")

        print(f"Recorded: {current_time}", flush=True)
        time.sleep(10)


if __name__ == "__main__":
    main()
