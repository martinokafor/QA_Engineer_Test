# Acceptance criteria for QA Interview Test | DLG Digital
Feature: Login to QA Interview Test

  Scenario: Login using valid credential
    Given User on login page
    When User enter Username
    And Enter Password
    And Click Login button
    Then User should be logged in


  Scenario: Login with password of length less than eight
    Given User on login page
    When User enter Username
    And Enter Password of length less than eight
    Then Verify error message

