@echo off
echo Running tests and collecting Allure results...
pytest --alluredir=allure-results
echo Allure results collected in ./allure-results

echo Generating Allure report...
allure generate allure-results -o allure-report
echo Allure report generated in ./allure-report

echo You can now view the report by opening allure-report/index.html
echo Or by running:
echo allure serve allure-results