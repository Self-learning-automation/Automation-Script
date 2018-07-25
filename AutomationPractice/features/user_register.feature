@Register
Feature: User register functionality
  As a user I want to register new account to the system

  @case-1
  Scenario Outline: Register-Verify user login success with random data
    Given the user is in the Automationpractice homepage
    When the user click on Sign in
    And  user enter Email address "<email_address>"
    And User click on "Create Account"
    And User fill all personal information in the form
    Then Verify User register successfully
    Examples:
    |email_address|
    |Tuanbuikfdjkfddddsdsdddddddaa@gmail.com|