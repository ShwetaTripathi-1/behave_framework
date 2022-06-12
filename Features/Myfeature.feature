Feature: Numpy logo
  Scenario: Logo present on DSAlgo Page
    Given Launch chrome browser
    When Open DSAlgo page
    Then Varify logo on Home Page
    And Close browser
