Feature: Login
  login/logout functionality

  Scenario: TC-1
  Login successful
    Given I type my username
    And I type my password
    When I click on login
    Then Verify the homepage loaded successfully