from apscheduler.schedulers.background import BackgroundScheduler

from naukri import (
apply_single_job,
refresh_profile,
update_application_status
)

scheduler = BackgroundScheduler()
print("SCHEDULER LOADED")
# APPLY EVERY 5 MIN

scheduler.add_job(
apply_single_job,
'interval',
minutes=5
)

# REFRESH PROFILE

scheduler.add_job(
refresh_profile,
'cron',
hour=10,
minute=0
)

scheduler.add_job(
refresh_profile,
'cron',
hour=14,
minute=30
)

# UPDATE STATUS

scheduler.add_job(
update_application_status,
'cron',
hour=20,
minute=0
)

scheduler.start()

print("Scheduler Started")
