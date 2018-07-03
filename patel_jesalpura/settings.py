
try:
    from patel_jesalpura.local_setting import *
except ImportError as e:
    from patel_jesalpura.production_setting import *