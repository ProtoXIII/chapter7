import os

def fun(**args):
    print "[*] In environment module."
    return str(os.environ)
