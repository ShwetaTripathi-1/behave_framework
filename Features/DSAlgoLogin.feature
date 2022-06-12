Feature: DSAlgo Login
  Scenario: Login to DSAlgo with valid parameters
    Given I launch chrome browser
    When I opened DSAlgo home Page
    And Enter Username "shweta.tripathi.mtech@gmail.com" and Password "k-.hu8EVFhsTLnw"
    And click on login button
    Then User successfully login

  Scenario Outline: Login to DSAlgo with  multiple parameters
    Given I launch chrome browser
    When I opened DSAlgo home Page
    And Enter Username "<Username>" and Password "<Password>"
    And click on login button
    Then User successfully login

    Examples:
      |Username                        |Password       |
      |shweta.tripathi.mtech@gmail.com |k-.hu8EVFhsTLnw|
      |abcd                            |1234           |
      |corporate.shweta@gmail.com      |1@malive       |
      |shweta.tripathibsr@gmail.com    |bulandshahr    |

