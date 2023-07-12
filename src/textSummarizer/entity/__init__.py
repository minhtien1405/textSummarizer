from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
  """ This is the data class, not the normal python class. """
  root_dir: Path
  source_URL: str
  local_data_file: Path
  unzip_dir: Path