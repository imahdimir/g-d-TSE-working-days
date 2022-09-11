"""

    """

import json

from githubdata import GithubData
from mirutil.df_utils import save_df_as_a_nice_xl as sxl


class GDUrl :
    with open('gdu.json' , 'r') as fi :
        gj = json.load(fi)

    cur = gj['cur']
    trg = gj['trg']

gu = GDUrl()

class ColName :
    jd = 'JDate'

c = ColName()

def main() :
    pass

    ##

    gd = GithubData(gu.trg)
    gd.overwriting_clone()
    df = gd.read_data()
    ##
    df = df.astype("string")
    ##
    df = df.drop_duplicates(subset = c.jd)
    ##
    fp = gd.data_fp
    sxl(df , fp)

    ##

    msg = 'governed by: '
    msg += gu.cur
    ##

    gd.commit_and_push(msg)

    ##


    gd.rmdir()


    ##

##
if __name__ == "__main__" :
    main()
