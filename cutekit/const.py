import os
import sys

VERSION = (0, 5, 0, "dev")
VERSION_STR = f"{VERSION[0]}.{VERSION[1]}.{VERSION[2]}{'-' + VERSION[3] if VERSION[3] else ''}"
MODULE_DIR = os.path.dirname(os.path.realpath(__file__))
ARGV0 = os.path.basename(sys.argv[0])
PROJECT_CK_DIR = ".cutekit"
GLOBAL_CK_DIR = os.path.join(os.path.expanduser("~"), ".cutekit")
BUILD_DIR = os.path.join(PROJECT_CK_DIR, "build")
CACHE_DIR = os.path.join(PROJECT_CK_DIR, "cache")
EXTERN_DIR = os.path.join(PROJECT_CK_DIR, "extern")
SRC_DIR = "src"
META_DIR = f"meta"
TARGETS_DIR = os.path.join(META_DIR, "targets")
DEFAULT_REPO_TEMPLATES = "cute-engineering/cutekit-templates"
DESCRIPTION = "A build system and package manager for low-level software development"
PROJECT_LOG_FILE = os.path.join(PROJECT_CK_DIR, "cutekit.log")
GLOBAL_LOG_FILE = os.path.join(os.path.expanduser("~"), ".cutekit", "cutekit.log")
