import sys
import os

msg = os.environ["APPVEYOR_REPO_COMMIT_MESSAGE"]
if msg.startswith('[release]') or sys.version_info[1] == 6:
  exit(0)
else:
  exit(1) # Do not compile for this build. See appveyor.yml