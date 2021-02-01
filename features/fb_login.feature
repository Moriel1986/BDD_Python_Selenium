# Created by Demoriel Purnell at 1/18/2021
  @smoke
Feature: Facebook Login
  # Enter feature description here

  Scenario: Verify User can successfully login to Facebook.com
    Given user has launched browser
    When user enters username and password
    And user clicks login button
    Then user should land of profile page

  @smoke
  Scenario: Verify User can successfully login to Facebook.com and go to profile page
    Given user has launched browser
    When user enters username and password
    And user clicks login button
    And user clicks profile picture
    Then user verifies title
  @smoke
    Scenario: Verify User can successfully login and click display and accessibility from dropdown
    Given user has launched browser
    When user enters username and password
    And user clicks login button
    And user enters data in search field
