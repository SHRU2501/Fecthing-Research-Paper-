# Initializes the papers package
__all__ = ["fetch", "filter"]

from .fetch import fetch_papers
from .filter import filter_authors
from . import fetch 
from . import filt
from .filter import filter_authors                  
from . import __version__

__version__ = "0.1.0"  # Update this version as needed
__all__ = ["fetch_papers", "filter_authors", "__version__"]
__author__ = "Shruti A. Wadettiwar"
__email__ = "shrutiashokwadettiwar@gmail.com"