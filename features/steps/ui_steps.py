from behave import given, when, then
from pages.ui_search_page import SearchPage

@given("I open the SDAIA website")
def step_open_site(context):
    context.page = SearchPage(context.driver)

# Searching for the dynamic term based on the scenario
@when('I search for "{term}"')
def step_search(context, term):
    context.page.search(term)

# Valid search assertion
@then('I should see search results of the "{term}"')
def step_assert_results(context, term):
    context.page.assert_results(term)

# Invalid search assertion
@then("I should see no results message")
def step_assert_no_results(context):
    context.page.assert_no_results_message()
