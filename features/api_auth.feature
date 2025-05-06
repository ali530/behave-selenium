Feature: DummyJSON Authentication API

  @api
  Scenario: Valid login
    Given I login with correct credentials
    When I send POST request to the login endpoint
    Then I should receive a 200 response
    And I should see a token in the response

  @api
  Scenario: Invalid login
    Given I login with wrong credentials
    When I send POST request to the login endpoint
    Then I should receive a 400 response

  @api
  Scenario: Access protected resource with valid token
    Given I login and get a valid token
    When I access the protected products endpoint
    Then I should receive a 200 response
    And I should see a list of products
