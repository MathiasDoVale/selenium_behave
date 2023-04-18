Feature: OrangeHRM Login

    Scenario: Login with valid parameters
        Given I Launch chrome browser
        When I Open orangehrm homepage
        And Enter username "Admin" and password "admin123"
        And Click on login button
        Then User must successfully login to the dashboard page 

    Scenario Outline: Login with multiple parameters
        Given I Launch chrome browser
        When I Open orangehrm homepage
        And Enter username "<username>" and password "<pwd>"
        And Click on login button
        Then User must successfully login to the dashboard page 

        Examples:
            | username | pwd      |
            | Admin    | admin123 |
            | admin    | adminxyz |
            | NoAdmin  | admin123 |
            | admin123 | Admin    |