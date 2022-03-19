Feature: Verify login functionality

    Scenario Outline: Loggin in
        Given I am on the Login Page
        When to fill with <email> in the email field
        And to fill with <password> in the password field
        And click the button ENTRAR
        Then the system directs you to the home pages

        Examples:
            |email                        |password       |
            |plataforma@engenheiroqa.com  |plataformaEQA  |

#    Scenario Outline: Invalid Login
#        Given I am on the Login Page
#        When to fill <email> in the email field
#        And to fill with <password> in the password field
#        And click the button "Entrar"
#        Then then system show a error message
#
#        Examples:
#            |email                             | password        |
#            | logininvalide@email.com          | invalidPassword |