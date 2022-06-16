Feature: Verify Market Functionality

  # PRECONDITION TO OPEN THE BROWSER
  Background: PRECONDITION - OPEN BROWSER
      Given I open the browser

  @Market
  Scenario Outline: Entering the Market Page
    Given that I login to check the market page with <email> and <password>
    When click on the Market Option
    Then the system directs you to the market pages

    Examples:
      |email                        | password      |
      |plataforma@engenheiroqa.com  | plataformaEQA |

  @Market
  Scenario Outline: Checking Product Search
    Given that I login to check the market page with <email> and <password>
    And click on the Market Option
    When the user fills in the search field with <product>
    Then the system displays the searched <product>

    Examples:
      |email                        | password      | product                 |
      |plataforma@engenheiroqa.com  | plataformaEQA | Mouse                   |
      |plataforma@engenheiroqa.com  | plataformaEQA | Monitor 18 Polegadas    |
      |plataforma@engenheiroqa.com  | plataformaEQA | Teclado                 |
      |plataforma@engenheiroqa.com  | plataformaEQA | Monitor 24" polegadas   |

  # POSTCONDITION TO CLOSE THE BROWSER
  Scenario: POSTCONDITION - CLOSE BROWSER
      Given I want to close the browser
      Then I close the browser