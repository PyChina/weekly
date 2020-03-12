#!/bin/bash
#
### changelog::
#   200306:ZQ re-define for rMBP local Pyenv
#   191213:ZQ re-define for YAtrigger restartr self
#   191204:ZQ re-define for Yaz
#1 0 * * * /opt/srv/yaz_studio/yeti/yazi/cmd/inv4pub.sh >> /opt/log/cron/_hook4yaz.log 2>&1

#   191031:ZQ refactory as inv4pub.sh
#   170818:ZQ refactory for N3160 miniPC Aoi
#   150803:ZQ re-pub with github
#   141022:ZQ creat base hook-deploy-by-git.sh
#=========================================================== var defines
VER="pub4trigger v.200306.2142"
#DATE=`date "+%y%m%d"`
#NOW=$(date +"%Y-%m-%d")

PBIN=~/.pyenv/versions/dama2712/bin
SELF=~/Sites/PyChina.org/weekly

GIT=$( which git)

PY=$PBIN/python
PIP=$PBIN/pip
ACTI=$PBIN/activate
#=========================================================== path defines
NOW=`date +"%y%m%d_%H%M%S"`
YEAR=`date +"%Y"`
MONTH=`date +"%m"`
#AIMP=/opt/log/cron
#LOGF=$AIMP/$YEAR-$MONTH-YAtrigger.log

#TARGET=/opt/log/yazi/_upd_trigger.log
#=========================================================== action defines
source $ACTI
$PIP list | grep pelican
python -V

cd $SELF

git pl 

fab ?
fab pub


#=========================================================== action DONE
exit  0


# SEE:
#   Is there a preferred way to use pyenv in a shell script? · Issue #492 · pyenv/pyenv https://github.com/pyenv/pyenv/issues/492
#   cron定时运行python virtualenv中的python程序 - SegmentFault 思否 https://segmentfault.com/q/1010000000319231
#   How to set virtualenv for a crontab? | RubyPDF Blog http://blog.rubypdf.com/2018/10/12/how-to-set-virtualenv-for-a-crontab/


