Feature: Search user page

    Background: Common steps
        Given I Launch chrome browser
        When I Open orangehrm homepage
        And Enter username "Admin" and password "admin123"
        And Click on login button

    Scenario: Dashboard page
        Then User must successfully login to the dashboard page 

    Scenario: Search user
        When navigate to search page
        Then search page should display

    Scenario: Advanced search user
        When navigate to advance search user
        Then advanced search page should display