Feature: Verify login functionality

    Scenario Outline: Realizando o Login
        Given que estou na tela de login
        When eu preencher o campo email com <email>
        And preencher o campo senha com <password>
        And clicar no botao ENTRAR
        Then o sistema vai direcionar para

        Examples:
            |email                        |password       |
            |plataforma@engenheiroqa.com  |plataformaEQA  |