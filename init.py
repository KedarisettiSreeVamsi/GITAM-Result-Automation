from pip._internal.utils.misc import get_installed_distributions
import os
if 'selenium' in get_installed_distributions():
    os.system('pip install selenium')
if 'requests' in get_installed_distributions():
    os.system('pip install requests')
