"""Jobs router"""
from core.facades.queue import Queue
from app.jobs.create_new_url import CreateNewUrl
from app.jobs.record_url_access import RecordUrlAccess
from app.jobs.update_general_stats import UpdateGeneralStats
from app.jobs.update_general_stats_by_url import UpdateGeneralStatsByUrl

Queue.register(CreateNewUrl)
Queue.register(RecordUrlAccess)
Queue.register(UpdateGeneralStats)
Queue.register(UpdateGeneralStatsByUrl)
