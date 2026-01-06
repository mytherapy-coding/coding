'''
Coding Problem: Bank Account System

Implement a class Bank that manages simple bank accounts identified by a unique owner name.

Public API

Implement a class Bank with the following methods:

— create_account(owner: str, initial_funds: int) -> Status
— deposit(owner: str, amount: int) -> Status
— withdraw(owner: str, amount: int) -> Status
— remove_account(owner: str) -> Status
— transfer(from_owner: str, to_owner: str, amount: int) -> Status
— status(owner: str) -> Status

Account Rules

- Each account is uniquely identified by owner (string).
- An account balance must never be negative.
- An owner can have only one account.
- All monetary values are integers and must be non-negative.
- Operations on non-existing accounts must fail.

Status Object

Each method returns a Status object.

Status represents either:

Success

— balance: current account balance after the operation
— volume: total transaction volume for the account (sum of all money transferred in and out, excluding the initial balance)

Error

— An error describing why the operation failed (e.g. "ACCOUNT_NOT_FOUND", "INSUFFICIENT_FUNDS", "ACCOUNT_ALREADY_EXISTS")
'''

from dataclasses import dataclass
from typing import Optional, Dict

@dataclass
class Status:
    balance: Optional[int] = None
    volume: Optional[int] = None
    error: Optional[str] = None

class Account:
    def __init__(self, owner: str, initial_funds: int):
        self.owner = owner
        self.balance = initial_funds
        self.volume = 0  # total in/out transactions (excluding initial balance)

    def deposit(self, amount: int) -> Status:
        if amount < 0:
            return Status(error="INVALID_AMOUNT")
        self.balance += amount
        self.volume += amount
        return Status(balance=self.balance, volume=self.volume)

    def withdraw(self, amount: int) -> Status:
        if amount < 0:
            return Status(error="INVALID_AMOUNT")
        if amount > self.balance:
            return Status(error="INSUFFICIENT_FUNDS")
        self.balance -= amount
        self.volume += amount
        return Status(balance=self.balance, volume=self.volume)

    def get_status(self) -> Status:
        return Status(balance=self.balance, volume=self.volume)

class Bank:
    def __init__(self):
        self.accounts: Dict[str, Account] = {}

    def create_account(self, owner: str, initial_funds: int) -> Status:
        if initial_funds < 0:
            return Status(error="INVALID_INITIAL_FUNDS")
        if owner in self.accounts:
            return Status(error="ACCOUNT_ALREADY_EXISTS")
        self.accounts[owner] = Account(owner, initial_funds)
        return Status(balance=initial_funds, volume=0)

    def deposit(self, owner: str, amount: int) -> Status:
        account = self.accounts.get(owner)
        if not account:
            return Status(error="ACCOUNT_NOT_FOUND")
        return account.deposit(amount)

    def withdraw(self, owner: str, amount: int) -> Status:
        account = self.accounts.get(owner)
        if not account:
            return Status(error="ACCOUNT_NOT_FOUND")
        return account.withdraw(amount)

    def remove_account(self, owner: str) -> Status:
        account = self.accounts.pop(owner, None)
        if not account:
            return Status(error="ACCOUNT_NOT_FOUND")
        return account.get_status()

    def transfer(self, from_owner: str, to_owner: str, amount: int) -> Status:
        if amount < 0:
            return Status(error="INVALID_AMOUNT")
        from_account = self.accounts.get(from_owner)
        to_account = self.accounts.get(to_owner)
        if not from_account or not to_account:
            return Status(error="ACCOUNT_NOT_FOUND")
        # Withdraw from sender
        withdraw_status = from_account.withdraw(amount)
        if withdraw_status.error:
            return withdraw_status
        # Deposit to receiver
        to_account.deposit(amount)
        return from_account.get_status()

    def status(self, owner: str) -> Status:
        account = self.accounts.get(owner)
        if not account:
            return Status(error="ACCOUNT_NOT_FOUND")
        return account.get_status()
