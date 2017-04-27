from first.tasks import add, mul, xsum, download
import sys

try:
    download.delay(sys.argv[1])
except IndexError:
    print("No argument with page URL given")
