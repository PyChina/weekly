# -*- coding: utf-8 -*-
#!/usr/bin/env python
import sys
import os
import time
import fnmatch


def j2p(rpath, aimpath):
    print rpath
    all_tid = []
    for md in os.listdir(rpath):
        exp = ""
        if fnmatch.fnmatch(md, '*.md'):
            mdls = open('%s/%s'% (rpath, md)).readlines()
            #print mdls[:7]
            print md
            exp += "Title: %s \n"% mdls[2].split('title: ')[1].strip()
            exp += "Date: %s \n"% md[:10]
            #print "Tags: %s"% mdls[5].split('tags: ')[1].strip().split
            exp +=  "Tags: %s \n"% ','.join(mdls[5].split('tags: ')[1].strip().split())
            exp += "Slug: %s \n"% md[11:-3]
            exp += "".join(mdls[8:])
            print "%s/%s.md"% (aimpath, md[11:-3])
            open("%s/%s.md"% (aimpath, md[11:-3]),'w').write(exp)
            #break
            #for l in open('%s/%s'% (rpath, md)).readlines:
            #    print 

    return None

if __name__ == '__main__':
    if 3 != len(sys.argv) :
        print '''Usage:
$ python jekyll2pelican.py /path/2/[数据文件目录] /path/2/[输出目的目录]
        '''
    else:
        begin = time.time()
        r = sys.argv[1]
        a = sys.argv[2]
        j2p(r, a)

        end = time.time()
        print "\t runing time=%.2fs<<<"%(end - begin)