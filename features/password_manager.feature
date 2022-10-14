Feature: Password manager application
  Password manager is used to store passwords in encrypted file.
  To have access to password manager entering key is required.

  Scenario: Deleting all passwords
    Given Password manager key is entered by user
    And multiple passwords already stored
    When User chooses to delete all passwords
    Then Password manager does not store any password

  Scenario: Getting all passwords
    Given Password manager key is entered by user
    And multiple passwords already stored
    When User chooses to get all passwords
    Then All passwords displayed

  Scenario: Deleting password by login
    Given Password manager key is entered by user
    When User enters login required to delete
    Then Password manager does not store password for entered login

  Scenario: Getting password by login
    Given Password manager key is entered by user
    When User enters login required to get
    Then Password for entered login is displayed
