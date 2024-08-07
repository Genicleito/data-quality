from pathlib import Path

from project_configuration import (
    GOLD_ZONE
)

file_name = (
    "_".join(Path(__file__).resolve().parts)
    # .lower()
    # .split("dags_")[-1]
    # .replace(".py", "")
)