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

    @Login @MandatoryMessage
    Scenario Outline: Mandatory Message
        Given I am on the Login Page
        When filling with <email> and <password>
        And click the enter button
        Then the system displays the message <emailErrorMessage> and <passwordErrorMessage>

        Examples:
            |  emailErrorMessage           | passwordErrorMessage  |
            |  E-mail é obrigatorio!       | E-mail é obrigatorio! |


    Scenario Outline:
        Given I am on the Login Page
        When filling with <email> and <password>
        Then click the enter button
        Then the system displays the message <errorMessage>

        Examples:
            | errorMessage              |
            | Usuário/Senha incorreto!  |