Feature: Verify Product Functionality

  # PRECONDITION TO OPEN THE BROWSER
  Background: PRECONDITION - OPEN THE BROWSER
      Given I open the browser

  @Product
  Scenario Outline: Entering the Product Page
    Given that I login to check the product page with <email> and <password>
    When click on the Product Option
    Then the system directs you to the product pages

    Examples:
      |email                        | password      |
      |plataforma@engenheiroqa.com  | plataformaEQA |

    # POSTCONDITION TO CLOSE THE BROWSER
    Scenario: POSTCONDITION - CLOSE BROWSER
        Given I want to close the browser
        Then I close the browser