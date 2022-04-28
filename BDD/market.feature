Feature: Verify Market functionality

  #### PRECONDITION TO OPEN THE BROWSER
  Background: PRECONDITION - OPEN BROWSER
      Given I open the browser

  Scenario Outline: Entering the Products Page
    Given that you login to check the market page with <email> and <password>
    When click on the Market Option
    Then the system directs you to the market pages

    Examples:
      |email                        | password      |
      |plataforma@engenheiroqa.com  | plataformaEQA |

  #### POSTCONDITION TO CLOSE THE BROWSER
  Scenario: POSTCONDITION - CLOSE BROWSER
      Given I want to close the browser
      Then I close the browser