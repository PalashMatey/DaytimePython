def lengthLongestPath(input):
    maxlength = 0
    lengthOfNames = {}
    depth = 0
    pathlen = {0:0}
    for line in input.splitlines():
        name = line.lstrip('\t')
        
        depth = len(line) - len(name)
        if '.' in name:
            maxlength = max(maxlength,pathlen[depth] + len(name))
        else:
            pathlen[depth+1] = pathlen[depth] + len(name) + 1
    return maxlength

value = lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")
print value