from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


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
    raise NotImplementedError


@given('multiple passwords already stored')
def multiple_passwords_already_stored():
    """multiple passwords already stored."""
    raise NotImplementedError


@when('User chooses to delete all passwords')
def user_chooses_to_delete_all_passwords():
    """User chooses to delete all passwords."""
    raise NotImplementedError


@when('User chooses to get all passwords')
def user_chooses_to_get_all_passwords():
    """User chooses to get all passwords."""
    raise NotImplementedError


@when('User enters login required to delete')
def user_enters_login_required_to_delete():
    """User enters login required to delete."""
    raise NotImplementedError


@when('User enters login required to get')
def user_enters_login_required_to_get():
    """User enters login required to get."""
    raise NotImplementedError


@then('All passwords displayed')
def all_passwords_displayed():
    """All passwords displayed."""
    raise NotImplementedError


@then('Password for entered login is displayed')
def password_for_entered_login_is_displayed():
    """Password for entered login is displayed."""
    raise NotImplementedError


@then('Password manager does not store any password')
def password_manager_does_not_store_any_password():
    """Password manager does not store any password."""
    raise NotImplementedError


@then('Password manager does not store password for entered login')
def password_manager_does_not_store_password_for_entered_login():
    """Password manager does not store password for entered login."""
    raise NotImplementedError
