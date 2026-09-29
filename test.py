from pathlib import Path

print(__file__)
print(Path(__file__))
print(Path(__file__).resolve())
print(Path(__file__).resolve().parent)