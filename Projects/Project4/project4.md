# Project 4: User Testing with Selenium

## MSSE640 - Software Quality and Test

### Table of Contents 

- [Introduction](#introduction)
- [Part 1: Lab Procedure](#part-1-lab-procedure)
- [Part 2: Lab Procedure - Expanded](#part-2-lab-procedure---expanded)
- [Conclusion & Recommendations](#conclusion--recommendations)

### Introduction 

In this project we explore automated user testing using Selenium, a popular framework for automating web browsers. The objective is to simulate user actions, such as browsing, adding items to a cart, and verifying transaction outcomes on the GCP Online Boutique website. Part 1 introduces basic test scripting using Selenium IDE, and part 2 involves writing three unique automated test cases on a testable public website. Through this exercise, we develop skills in web element inspection and script automating.

### Part 1: Lab Procedure

![Part 1 Screenshot](/Assets/seleniumPart1.png)

### Part 2: Lab Procedure - Expanded

#### Test Home Grid
The purpose of this story is to test the home grid of products to ensure all products are loading into the grid correctly. I know this story is complete when we see 9 loaded products in the grid

![Test 1: Test home grid](/Assets/testHomeGrid.png)

#### Test Footer Presence
The purpose of this story is to test the footer to ensure all footer content is loaded correctly. I know this story is complete when the footer is loaded and contains all necessary content.

![Test 2: Test footer presence](/Assets/testFooter.png)

#### Test Currency Dropdown
The purpose of this story is the test the currency dropdown to ensure all currency options are present. I know this story is complete when the user can click on JPY.

![Test 3: Test currency dropdown](/Assets/testDropdown.png)


### Conclusion & Recommendations

This project demonstrates how Selenium can automate real-world user flows and validate UI behavior through scripting. We gained practical experience with browser developer tools, locators (like IDs, classes, and XPaths), and creating repeatable test scripts in Python. It reinforced how automated testing contributes to quality assurance and CI/CD practices. Going forward, improving this assignment with structured test case templates, more diverse websites, and integration into GitHub Actions for CI testing would further reflect real-world applications.