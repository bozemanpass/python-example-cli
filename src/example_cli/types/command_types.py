
from dataclasses import dataclass

@dataclass
class BaseOptions:
    debug: bool
    quiet: bool
    verbose: bool
