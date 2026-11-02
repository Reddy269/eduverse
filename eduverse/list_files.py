import os

EXTENSIONS = (".py", ".html", ".js")
SKIP_DIRS = {".venv", "venv", ".git", "__pycache__", "node_modules", ".idea", "staticfiles"}

root = os.path.dirname(os.path.abspath(__file__))
lines = []

for folder, dirs, files in os.walk(root):
    dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
    for name in sorted(files):
        if name.endswith(EXTENSIONS):
            rel = os.path.relpath(os.path.join(folder, name), root)
            parts = rel.split(os.sep)
            depth = len(parts) - 1          # number of folders above the file
            lines.append((" > ".join(parts), depth))

for path, depth in lines:
    print(f"{path}    [depth {depth}]")

print(f"\n{len(lines)} files, max depth {max(d for _, d in lines)}")