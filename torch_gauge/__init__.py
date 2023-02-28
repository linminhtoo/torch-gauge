import os
import tempfile
from torch_gauge.verlet_list import VerletList
from torch_gauge._version import get_versions

__version__ = get_versions()["version"]
del get_versions

# ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = tempfile.TemporaryDirectory().name
print(f"torch gauge, storing o3_cache at: {ROOT_DIR}")
