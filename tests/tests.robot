*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${BASE URL}       http://localhost:5000
${BROWSER}        Firefox

*** Test Cases ***
Submit Valid Form
    Open Browser    ${BASE URL}    ${BROWSER}
    Input Text      id=author      John Doe
    Input Text      id=title       Example Title
    Input Text      id=journal     Journal Name
    Input Text      id=year        2023
    Input Text      id=volume      10
    Input Text      id=pages       20-30
    Click Button    id=submit
    Location Should Be    ${BASE URL}/

*** Comments ***
Submit Invalid Form
    Open Browser    ${BASE URL}    ${BROWSER}
    Input Text      id=author      John Doe
    Input Text      id=title       Example Title
    Input Text      id=journal     Journal Name
    Input Text      id=year        InvalidYear
    Input Text      id=volume      10
    Input Text      id=pages       20-30
    Click Button    id=submit
    Location Should Be    ${BASE URL}/submit
    Page Should Contain    Error Message

*** Keywords ***
Error Message
    Run Keyword And Continue On Failure    Page Should Contain    Error message text here