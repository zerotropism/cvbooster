import yaml
from pathlib import Path
from typing import Dict, Any


def load_config(config_path: str | Path | None = None) -> Dict[str, Any]:
    """Load configuration from a YAML file."""
    if config_path is None:
        # Chemin absolu relatif à ce fichier config.py
        config_path = Path(__file__).parent.parent / "config.yaml"

    config_file = Path(config_path)
    if not config_file.is_file():
        raise FileNotFoundError(f"Configuration file '{config_path}' not found.")

    with open(config_file, "r") as f:
        return yaml.safe_load(f)


# Chargement unique au démarrage de l'application
_config = load_config()

MODEL: str = _config.get("model", "llama3.2")
PROMPT_RANK: str = _config.get("prompts", {}).get("rank", {}).get("custom", "")
PROMPT_REWRITE: str = _config.get("prompts", {}).get("rewrite", {}).get("custom", "")
