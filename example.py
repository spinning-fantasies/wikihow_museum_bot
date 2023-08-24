from datetime import UTC, datetime, timedelta
from pathlib import Path


def main() -> int:
    texts_path = Path("texts")
    images_path = Path("images")

    now = datetime.now(tz=UTC)
    day_delta = 0
    for text in texts_path.iterdir():
        with open(text, 'r', encoding='utf-8') as file:
            content = file.read()
            data = {
                "status": content,
                # "status": text,
                "scheduled_at": now + timedelta(day_delta)
            }
        print(data)
        day_delta += 0.5

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
