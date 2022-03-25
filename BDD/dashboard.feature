Feature: Verify dashboard functionality

    Scenario Outline: Verify Dashboard
        Given I am on the Login Page
        When filling with <email> and <password>
        And click the enter button
        Then the system directs you to the home pages

        Examples:
            |email                        |password       |
            |plataforma@engenheiroqa.com  |plataformaEQA  |

    Scenario Outline: Clicking on View Product
        Given I am on the Login Page
        And filling with <email> and <password>
        And click the enter button
        When the user is on the home page
        And click the button "Visualizar Produto"

        Examples:
            |email                           |password             |
            |plataforma@engenheiroqa.com     |plataformaEQA        |