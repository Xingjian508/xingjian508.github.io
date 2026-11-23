"""Copy only public website files into the static deployment directory."""

from pathlib import Path
import shutil

root = Path(__file__).resolve().parent.parent
output = root / "dist"
if output.exists():
    shutil.rmtree(output)
output.mkdir()
for name in ("index.html", "styles.css", ".nojekyll", "teaching", "papers", "notes", "experiments"):
    source = root / name
    destination = output / name
    if source.is_dir():
        shutil.copytree(source, destination)
    else:
        shutil.copy2(source, destination)
print(f"Built static website in {output}")
