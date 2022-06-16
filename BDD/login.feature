Feature: Verify login functionality

    # PRECONDITION TO OPEN THE BROWSER
    Background: PRECONDITION - OPEN BROWSER
        Given I open the browser

    @login @LoginValid
    Scenario Outline: Loggin in
        Given I am on the Login Page
        When filling with <email> and <password>
        And click the enter button
        Then the system directs you to the home pages

        Examples:
            |email                        |password       |
            |plataforma@engenheiroqa.com  |plataformaEQA  |

    @Login @ErrorMessage
    Scenario Outline: Error Message
        Given I am on the Login Page
        When filling with <email> and <password>
        And click the enter button
        Then the system display the message <errorMessage>

        Examples:
            |email              |password   | errorMessage              |
            |teste@teste.com    |teste      | Usuário/Senha incorreto!  |

    @Login @MandatoryMessage
    Scenario Outline: Mandatory Message
        Given I am on the Login Page
        When not filling the required field
        Then the system displays the message <emailErrorMessage> and <passwordErrorMessage>

        Examples:
            |  emailErrorMessage           | passwordErrorMessage  |
            |  E-mail é obrigatorio!       | Senha é obrigatório! |

    # POSTCONDITION TO CLOSE THE BROWSER
    Scenario: POSTCONDITION - CLOSE BROWSER
        Given I want to close the browser
        Then I close the browser
