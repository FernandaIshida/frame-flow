from datetime import datetime
from uuid import uuid4

import pytest
from app.domain.entities.job import Job
from app.domain.enums.job_status import JobStatus
from app.domain.exceptions.invalid_job_state import InvalidJobState

def create_job() -> Job:
    now = datetime.utcnow()

    return Job(
        id=uuid4(),
        status=JobStatus.CREATED,
        created_at=now,
        updated_at=now,
    )

def test_job_should_start_as_created():
    job = create_job()
    
    assert job.status == JobStatus.CREATED

def test_job_should_transition_to_processing():
    job = create_job()

    job.start_processing()

    assert job.status == JobStatus.PROCESSING

def test_job_should_complete_after_processing():
    job = create_job()

    job.start_processing()
    job.complete()

    assert job.status == JobStatus.COMPLETED

def test_job_should_fail_after_processing():
    job = create_job()

    job.start_processing()
    job.fail()

    assert job.status == JobStatus.FAILED

def test_job_should_not_complete_before_processing():
    job = create_job()

    with pytest.raises(InvalidJobState):
        job.complete()
