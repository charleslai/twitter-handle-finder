# Twitter handle finder: Brute force Twitter for handles

import sys, os
import requests

def main(argv):
    # Check if arguments formed correctly
    if len(argv) < 1:
        sys.stderr.write("Usage: %s <dictionary>\n" % (argv[0],))
        return 1

    if not os.path.exists(argv[1]):
        sys.stderr.write("ERROR: Dictionary %r was not found!\n" % (argv[1],))
        return 1

    base_url = "https://twitter.com/"

    # Iterate through the dictionary and save valid handles
    print "Checking available Twitter handles..."
    with open(argv[1],'r') as dictionary:
        with open("results.txt", 'a') as out:
            for w in dictionary:
                if requests.get(base_url + w.rstrip()).status_code == 404:
                    out.write(w)
    print "Done."

if __name__ == "__main__":
    sys.exit(main(sys.argv))
