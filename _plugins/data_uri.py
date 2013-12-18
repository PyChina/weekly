# -*- coding: utf-8 -*-
#!/usr/bin/env python
import sys

if __name__ == '__main__':
    if 3 != len(sys.argv) :
        print '''Usage:
            data_uri.py /path/2/imgfile exp.base64
        '''
    else:
        imgf = sys.argv[1]
        expf = sys.argv[2]
        data_uri = open(imgf, "rb").read().encode("base64").replace("\n", "")
        img_tag = 'data:image/png;base64,{0}'.format(data_uri)
        open(expf,"w").write(img_tag)
        #print img_tag
