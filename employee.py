class Employee:
    email: str
    manager: str | None

    def __init__(self, email, manager=None):
        self.email = email
        self.manager = manager

    def __str__(self):
        return f"Employee(email='{self.email}', manager='{self.manager}')"

