"""
Script to be run on startup to set up PYTHONPATH variable

In Spyder, you can set this to be run every time Spyder is open
1. Tools > Preferences > IPython console > Startup
2. Under 'Run a file', browse to startup.py

Can be easily customised for different setups, by varying the type of roots used
"""

import pandas as pd
import sys
import os
def main():
    ### PYTHONPATH
    root = os.path.expanduser("~")
    paths = {'github_root':rf'{root}\Documents\GitHub',
             'coding_root':rf'{root}\Documents\Coding',
             'local_root':rf'{root}\Documents\local_pyth_config',
             'legatum_root':rf'{root}\Documents\Legatum\centreformetrics'}
    
    # Iterate over subdirectory tree, append to path. Remove root, paths from local memory
    for root_type, path in paths.items():
        sys.path.append(path)
        for subdir, dirs, files in os.walk(path):
            git_or_env_path = '\env' in subdir or '\.git' in subdir
            if not git_or_env_path:
                sys.path.append(subdir)
    
    
    ### PANDAS preferences
    # Make dataframes easier to read in the console
    pd.set_option('max_columns',10)
    pd.set_option('expand_frame_repr',False)
    pd.set_option('precision',8)
    
if __name__ == '__main__':
    main()