class InvalidJobState(Exception):
    """Raised when an invalid job state transition is attempted."""

    def __init__(self, current_status: str, requested_status: str):
        self.current_status = current_status
        self.requested_status = requested_status

        super().__init__(
            f"Invalid job state transition: "
            f"{current_status.value} -> {requested_status.value}"
        )