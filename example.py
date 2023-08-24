from datetime import UTC, datetime, timedelta
from pathlib import Path


def main() -> int:
    images_path = Path("images")

    now = datetime.now(tz=UTC)
    day_delta = 1
    for image in images_path.iterdir():
        data = {
            "status": image,
            "scheduled_at": now + timedelta(day_delta)
        }
        print(data)
        day_delta += 1

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
