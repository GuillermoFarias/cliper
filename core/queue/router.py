""" Queue Router """
from typing import Type, List, Optional
from core.queue.contracts.job import Job


class Router:
    """ Queue Router """

    def __init__(self):
        self.jobs: List[Type[Job]] = []

    def register_job(self, job_class: Type[Job]):
        """ Add a job class to the router """
        self.jobs.append(job_class)

    def get_jobs(self) -> List[Type[Job]]:
        """ Get the job classes """
        return self.jobs

    def resolve(self, name: str) -> Optional[Type[Job]]:
        """ Resolve the route """
        for job_class in self.get_jobs():
            if job_class.__name__ == name:
                return job_class
        return None

    async def process_job(self, job_name: str, job_data: dict):
        """ Process the incoming message """
        job_class = self.resolve(job_name)

        if job_class:
            # Crea una instancia del trabajo con los datos
            job_instance: Job = job_class()
            job_instance.set_data(job_data)
            return await job_instance.handle(job_data)

        return None
