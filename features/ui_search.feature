Feature: Search functionality on SDAIA website

  @ui
  Scenario Outline: Valid search
    Given I open the SDAIA website
    When I search for "<term>"
    Then I should see search results of the "<term>"

    # Mixed lower-upper letters with numbers
    # English sentence 
    # Arabic search 
    Examples:
      | term                   |
      | SdaIA 10               |
      | National Center for AI |
      | مشكلة تقنية           |

  @ui
  Scenario Outline: Invalid search
    Given I open the SDAIA website
    When I search for "<term>"
    Then I should see no results message

    # random search for word with no results
    # Search with a sentence that contains one word with results and the other not
    # Arabic with typo
    # special characters
    Examples:
      | term               |
      | randomNoResult00   |
      | QC Job             |
      | الذكاأ الاصطناعي   |
      | @@                 |
