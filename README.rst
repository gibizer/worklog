=======
worklog
=======

Simple python script that can calculate your working hours based some
activity log.

Install
-------

Change your i3 config file to print the current datetime into the .worklog
file when a common activity happens. For example when your switch workspaces:

.. code::

  bindsym $mod+1 exec "date >> .worklog ; i3-msg workspace 1"
  bindsym $mod+2 exec "date >> .worklog ; i3-msg workspace 2"
  bindsym $mod+3 exec "date >> .worklog ; i3-msg workspace 3"
  bindsym $mod+4 exec "date >> .worklog ; i3-msg workspace 4"
  bindsym $mod+5 exec "date >> .worklog ; i3-msg workspace 5"
  bindsym $mod+6 exec "date >> .worklog ; i3-msg workspace 6"
  bindsym $mod+7 exec "date >> .worklog ; i3-msg workspace 7"
  bindsym $mod+8 exec "date >> .worklog ; i3-msg workspace 8"
  bindsym $mod+9 exec "date >> .worklog ; i3-msg workspace 9"
  bindsym $mod+0 exec "date >> .worklog ; i3-msg workspace 10"
  bindsym $mod+m exec "date >> .worklog ; i3-msg workspace 10"



Usage
-----

.. code:: bash

  $ worklog -h
  usage: Collect working periods from activity log
  
  optional arguments:
    -h, --help            show this help message and exit
    -w WORKLOG, --worklog WORKLOG
                          The location of the activity log file
    -g GAP, --gap GAP     The maximum inactivity in minutes that does not start
                          a new period. Default is 60 minutes


