import pytest
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from src.password_manager import PasswordManager


@pytest.fixture
def password_manager():
    password_manager_key = 'Ar1Vider4I'
    password_json_file_path = 'data/encrypted_passwords_test'
    password_manager = PasswordManager(password_json_file_path, password_manager_key)
    return password_manager


@pytest.fixture
def login():
    return 'pavelihno'


@pytest.fixture
def password():
    return '321'


@scenario('features/password_manager.feature', 'Deleting all passwords')
def test_deleting_all_passwords():
    """Deleting all passwords."""


@scenario('features/password_manager.feature', 'Deleting password by login')
def test_deleting_password_by_login():
    """Deleting password by login."""


@scenario('features/password_manager.feature', 'Getting all passwords')
def test_getting_all_passwords():
    """Getting all passwords."""


@scenario('features/password_manager.feature', 'Getting password by login')
def test_getting_password_by_login():
    """Getting password by login."""


@given('Password manager key is entered by user')
def password_manager_key_is_entered_by_user():
    """Password manager key is entered by user."""
    return password_manager


@given('multiple passwords already stored')
def multiple_passwords_already_stored(password_manager, login, password):
    """multiple passwords already stored."""
    password_manager.save_password(login, password)
    password_manager.save_password('pavel', '123')

    assert len(password_manager.get_passwords()) == 2

    return password_manager


@when('User chooses to delete all passwords')
def user_chooses_to_delete_all_passwords(password_manager):
    """User chooses to delete all passwords."""
    password_manager.delete_passwords()

    return password_manager


@when('User chooses to get all passwords')
def user_chooses_to_get_all_passwords(password_manager):
    """User chooses to get all passwords."""

    return password_manager.get_passwords()


@when('User enters login required to delete')
def user_enters_login_required_to_delete(password_manager, login):
    """User enters login required to delete."""
    password = password_manager.delete_password(login)

    return password


@when('User enters login required to get')
def user_enters_login_required_to_get(password_manager, login):
    """User enters login required to get."""
    password = password_manager.get_password(login)

    return password


@then('All passwords displayed')
def all_passwords_displayed(password_manager):
    """All passwords displayed."""

    assert len(password_manager.get_passwords()) == 2


@then('Password for entered login is displayed')
def password_for_entered_login_is_displayed(password_manager, login, password):
    """Password for entered login is displayed."""
    assert password_manager.get_password(login) == password


@then('Password manager does not store any password')
def password_manager_does_not_store_any_password(password_manager):
    """Password manager does not store any password."""

    assert len(password_manager.get_passwords()) == 0


@then('Password manager does not store password for entered login')
def password_manager_does_not_store_password_for_entered_login(password_manager, login):
    """Password manager does not store password for entered login."""

    password_manager.delete_password(login)

    assert password_manager.get_password(login) is None

