from apscheduler.schedulers.background import BackgroundScheduler
from naukri import (
apply_single_job,
refresh_profile,
update_application_status
)

scheduler = BackgroundScheduler()

from pytz import timezone

scheduler = BackgroundScheduler(
    timezone=timezone("Asia/Kolkata")
)

# APPLY 1 JOB EVERY 5 MINUTES

scheduler.add_job(
apply_single_job,
'interval',
minutes=5
)

# REFRESH PROFILE AT 9 AM

scheduler.add_job(
refresh_profile,
'cron',
hour=9,
minute=30
)

# REFRESH PROFILE AT 2:30 PM

scheduler.add_job(
refresh_profile,
'cron',
hour=14,
minute=30
)

# UPDATE STATUS AT 8 PM

scheduler.add_job(
update_application_status,
'cron',
hour=20,
minute=0
)

scheduler.start()
