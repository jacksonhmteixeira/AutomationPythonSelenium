Feature: Verify Market functionality

  Scenario Outline: Entering the Products Page
    Given I log in with the <email> and <password>
    When click on the Market Option
    Then the system directs you to the market pages

    Examples:
      |email                        | password      |
      |plataforma@engenheiroqa.com  | plataformaEQA |