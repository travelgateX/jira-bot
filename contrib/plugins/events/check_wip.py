from app.tasks.base_tasks import Event
import app.common.util

# Commands
class Task(Event):
    async def execute(self):
        self.logger.info(f"CheckWIP.execute[{self.event_in}]")
      