from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from app.domain.enums.job_status import JobStatus
from app.domain.exceptions.invalid_job_state import InvalidJobState

@dataclass
class Job:
    id: UUID
    status: JobStatus
    created_at: datetime
    updated_at: datetime

    _VALID_TRANSITIONS = {
        JobStatus.CREATED: {
            JobStatus.PROCESSING
        },
        JobStatus.PROCESSING: {
            JobStatus.COMPLETED,
            JobStatus.FAILED
        },
        JobStatus.COMPLETED: set(),
        JobStatus.FAILED: set(),
    }

    def start_processing(self) -> None:
        self._change_status(JobStatus.PROCESSING)
    
    def complete(self) -> None:
        self._change_status(JobStatus.COMPLETED)
    
    def fail(self) -> None:
        self._change_status(JobStatus.FAILED)
    
    def _change_status(self, new_status: JobStatus) -> None:
        allowed_states = self._VALID_TRANSITIONS[self.status]

        if new_status not in allowed_states:
            raise InvalidJobState(
               self.status,
               new_status,
            )
        
        self.status = new_status
        self.updated_at = datetime.utcnow()
