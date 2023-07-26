# audit_trail.py - Audit Trail Module

import datetime

class AuditTrail:
    def __init__(self):
        self.audit_log = []

    def log_event(self, event_type, user, details):
        """
        Log an event to the audit trail.

        Parameters:
        - event_type (str): The type of event being logged.
        - user (str): The user or system responsible for the event.
        - details (str): Additional details or description of the event.
        """
        timestamp = datetime.datetime.now()
        event = {
            "timestamp": timestamp,
            "event_type": event_type,
            "user": user,
            "details": details
        }
        self.audit_log.append(event)

    def get_audit_log(self):
        """
        Retrieve the entire audit log.

        Returns:
        - list: List of audit log entries, where each entry is a dictionary containing timestamp, event_type, user, and details.
        """
        return self.audit_log

# Example usage:
if __name__ == "__main__":
    audit = AuditTrail()

    # Log some events
    audit.log_event("Login", "user1", "User 'user1' logged in.")
    audit.log_event("Data Access", "user2", "User 'user2' accessed sensitive data.")
    audit.log_event("System Update", "admin", "System software updated.")

    # Retrieve the audit log
    log_entries = audit.get_audit_log()
    for entry in log_entries:
        print(entry)
