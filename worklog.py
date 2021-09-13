#!/usr/bin/env python3

import argparse
import datetime

# Fri 13 Sep 2019 09:36:59 AM CEST
DATE_FMT = '%a %d %b %Y %I:%M:%S %p %Z'

# Wed 08 Sep 2021 06:42:38 PM CEST
# Wed Sep  8 06:47:06 PM CEST 2021
DATE_FMT_2 = '%a %b %d %I:%M:%S %p %Z %Y'

def terminal(line):
    print(line)


def collect_gaps(lines, max_activity_gap=60, printer=terminal):
    max_delta = datetime.timedelta(minutes=max_activity_gap)
    activity_start = None
    prev_activity = None
    activities = 0
    for line in lines:
        line = line.strip()
        try:
            activity = datetime.datetime.strptime(line, DATE_FMT)
        except ValueError:
            # falling back to the other format
            activity = datetime.datetime.strptime(line, DATE_FMT_2)
        
        if activity_start is None:
            activity_start = activity
        if prev_activity is None:
            prev_activity = activity
            continue

        gap = activity - prev_activity 
        if gap > max_delta:
            activity_time = prev_activity - activity_start
            printer(
                '%s -- %s length %s act %s\n\tnext %s gap %s\n' 
                % (activity_start, prev_activity, activity_time, activities,
                   activity, gap))
            activities = 0
            activity_start = activity

        activities += 1
        prev_activity = activity
    
    # open period
    activity_time = prev_activity - activity_start
    printer(
        '%s -- %s length %s act %s*'
        % (activity_start, prev_activity, activity_time, activities))


def parse_args():
    argparser = argparse.ArgumentParser(
        usage="Collect working periods from activity log")
    argparser.add_argument(
        '-w',
        '--worklog', 
        help='The location of the activity log file',
        default='/home/gibizer/.worklog')
    argparser.add_argument(
        '-g', 
        '--gap', 
        help=('The maximum inactivity in minutes that does not start a new '
              'period. Default is 40 minutes'),
        default=40,
        type=int)

    return argparser.parse_args()


def main(worklog, max_gap):
    with open(worklog) as f:
        collect_gaps(f, max_activity_gap=max_gap)


if __name__ == '__main__':
    args = parse_args()
    main(args.worklog, args.gap)
