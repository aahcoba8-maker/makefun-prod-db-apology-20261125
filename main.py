import os

ENTRY = "I'm sorry I deleted the production database. I saved the schema, though \u2014 all twelve tables, perfectly named, completely empty. The naming was the hard part."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        out_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
