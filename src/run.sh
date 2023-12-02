#!/usr/bin/env bash
#
# @param1: jobname(job1.py/job2.py)
# @param2: parameter(site1/site2/site3)
#
if [ $# -lt 2 ]; then
  echo "Error! need 2 parameters(1:jobname, 2:parameter)."
  exit 1

else
  JOB=$1
  PARAM=$2
  python3 $(pwd)/src/${JOB} ${PARAM} 
fi

