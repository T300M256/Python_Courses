"""
Filter file contents using a sequence of generators.
"""

def nocomment(f):
    "Generate the non-comment lines of a file"
    for line in f:
        if not line.startswith("#"):
            yield line

def nospaces(f):
    "generate the lines of a file with out leading or trailing spaces"
    for line in f:
        yield line.strip()

def noblanks(f):
    "generate the non-blank lines of a file"
    for line in f:
        if line:
            yield line

if __name__ == "__main__":
    for line in nocomment(noblanks(nospaces(open("py08-01.txt")))):
        print(line)
    