import folder_paths
import os
from pathlib import Path

here = Path(__file__).parent.absolute()

total_fonts = []
font_extensions = ["*.ttf", "*.otf", "*.woff", "*.woff2", "*.eot"]

for extension in font_extensions:
    total_fonts.extend(Path(os.path.join(str(here), "font")).glob(extension))
    total_fonts.extend(Path(os.path.join(folder_paths.models_dir, "fonts")).glob(extension))