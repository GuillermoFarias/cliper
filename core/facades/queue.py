""" Queue Facade """
from core.queue.server import Server as QueueServer
from core.queue.router import Router as QueueRouter
from core.facades.app import App
from core.queue.contracts.job import Job


class Queue:
    """ Queue Facade. """

    @staticmethod
    def register(job: Job):
        """ Register a job route with a callback. """
        queue_router: QueueRouter = App.make(QueueRouter)
        queue_router.register_job(job)

    @staticmethod
    def dispatch(job: Job):
        """ Dispatch a job to the queue. """
        queue_server: QueueServer = App.make(QueueServer)
        queue_server.publish(job.get_idenfier(), job.get_data())
