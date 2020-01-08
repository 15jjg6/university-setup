from datetime import datetime
from pathlib import Path

def get_week(d=datetime.today()):
    return (int(d.strftime("%W")) + 52 - 5) % 52

CURRENT_COURSE_SYMLINK = Path('~/Notes/current-course').expanduser()
CURRENT_COURSE_ROOT = CURRENT_COURSE_SYMLINK.resolve()
# Comment out watch file until I find good use for it
# CURRENT_COURSE_WATCH_FILE = Path('/tmp/current_course').resolve()
ROOT = Path('~/Notes/bachelor-3/semester-2').expanduser()
DATE_FORMAT = '%a %d %b %Y %H:%M'
