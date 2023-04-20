# Selenium + Behave + Allure

Learning project about how to use Selenium and BDD(behave) in Python.

This project was based on "SDET- QA Automation Techie" video series on youtube
Link: https://www.youtube.com/watch?v=JIyvAFBx2Fw&list=PLUDwpEzHYYLsARXz1o3Ldt1FnvRbvlxsS

### Prerequisites
- [Python 3.10.11](https://www.example.com)
- [Selenium 4.8.3]
- [Behave 1.2.6]
- [ChromeWebDriver] (https://chromedriver.chromium.org/downloads - Same version as your Chrome)
- Configure PATH_DRIVER variable to your local "chromedriver.exe"
- [Allure-behave==2.13.1]

### Allure (reports)
Follow these instructions to use "allure" commands. (Report creation E.g.)
Link: https://docs.qameta.io/allure/

After allure instalation use:
- To generate reports: behave -f allure_behave.formatter:AllureFormatter -o reports/ features
- To visualize running server: allure serve reports (in Powershell)
