Feature: Verify login functionality

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
        Then the system displays the message <emailErrorMessage> and <passwordErrorMessage>

        Examples:
            |  emailErrorMessage           | passwordErrorMessage  |
            |  E-mail é obrigatorio!       | Senha é obrigatório! |