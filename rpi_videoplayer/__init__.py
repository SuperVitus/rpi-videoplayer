from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

from .videoplayer import VideoPlayer

__all__ = ['VideoPlayer']
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
