from pathlib import Path

UPLOADS_DIR = Path("uploads")
CITIES_DIR = UPLOADS_DIR / "cities"
PLAYERS_DIR = UPLOADS_DIR / "players"
STADIUMS_DIR = UPLOADS_DIR / "stadiums"
STUFF_DIR = UPLOADS_DIR / "stuff"
TEAMS_DIR = UPLOADS_DIR / "teams"


def setup_upload_directories():
    for directory in [UPLOADS_DIR, CITIES_DIR, PLAYERS_DIR, STADIUMS_DIR, STUFF_DIR, TEAMS_DIR]:
        directory.mkdir(parents=True, exist_ok=True)
