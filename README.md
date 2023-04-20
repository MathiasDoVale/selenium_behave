# Selenium + Behave + Allure

Learning project about how to use Selenium and BDD(behave) in Python.

This project was based on "SDET- QA Automation Techie" video series on youtube
Link: https://www.youtube.com/watch?v=JIyvAFBx2Fw&list=PLUDwpEzHYYLsARXz1o3Ldt1FnvRbvlxsS

### Prerequisites
- [Python 3.10.11](https://www.example.com)
- [Selenium 4.8.3]
- [Behave 1.2.6]
- [ChromeWebDriver] (https://chromedriver.chromium.org/downloads - Same version as your Chrome)
- [Allure-behave==2.13.1]
- [Python-dotenv==1.0.0]
- Configure PATH_DRIVER variable to your local "chromedriver.exe" in .env file. (PATH_DRIVER="your/chromedriver.exe/route")

### Allure (reports)
Follow these instructions to use "allure" commands. (Report creation E.g.)
Link: https://docs.qameta.io/allure/

After allure instalation use:
- To generate reports: behave -f allure_behave.formatter:AllureFormatter -o reports/ features
- To visualize running server: allure serve reports (in Powershell)


![report1](https://user-images.githubusercontent.com/25461133/233237083-1b92be4f-c2a7-490f-a76a-5029e0e6a0a6.png)


![report2](https://user-images.githubusercontent.com/25461133/233237090-b5dd7592-4959-4302-abef-5ad07bfb74f0.png)