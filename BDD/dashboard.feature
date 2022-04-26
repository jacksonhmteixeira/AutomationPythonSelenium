Feature: Verify dashboard functionality

    Scenario Outline: Verify Dashboard
        Given I log in with the <email> and <password>
        When I click the enter button
        Then the system directs you to the home pages

        Examples:
            |email                        |password       |
            |plataforma@engenheiroqa.com  |plataformaEQA  |

    Scenario Outline: Clicking on View Product
        Given I log in with the <email> and <password>
        And click the enter button
        When the user is on the home page
        And click the button "Visualizar Produto"

        Examples:
            |email                           |password             |
            |plataforma@engenheiroqa.com     |plataformaEQA        |