
'''
  apscheduler.schedulers.blocking  定时任务阻断代码
'''

from apscheduler.schedulers.blocking  import BlockingScheduler

from caller import search

sched = BlockingScheduler

sched.add_job(search,"interval",hours=1)

sched.start()
