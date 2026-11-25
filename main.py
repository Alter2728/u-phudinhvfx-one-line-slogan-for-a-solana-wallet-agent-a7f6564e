import os

TEXT = "A Solana wallet that watches while you sleep, so sending money feels like texting."


def main():
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    with open(output_path, "r", encoding="utf-8") as f:
        content = f.read()
    assert 1 <= len(content) <= 140
    assert len(content.split()) <= 20
    assert "\n" not in content and "\r" not in content
    assert content.strip()


if __name__ == "__main__":
    main()
