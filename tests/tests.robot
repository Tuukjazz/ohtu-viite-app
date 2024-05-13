*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${BASE URL}       http://localhost:5000
${BROWSER}        Firefox

*** Test Cases ***
Submit Valid Form
    Open Browser    ${BASE URL}    ${BROWSER}
    Select From List by Value      id=tyyppi    1 
    Input Text      id=author      John Doe
    Input Text      id=title       Example Title
    Input Text      id=journal     Journal Name
    Input Text      id=year        2023
    Input Text      id=volume      10
    Input Text      id=pages       20-30
    Click Button    id=submit
    Location Should Be    ${BASE URL}/

Submit Invalid Year
    Select From List by Value      id=tyyppi    1 
    Input Text      id=author      John Doe
    Input Text      id=title       Example Title
    Input Text      id=journal     Journal Name
    Input Text      id=year        InvalidYear
    Input Text      id=volume      10
    Input Text      id=pages       20-30
    Click Button    id=submit
    Location Should Be    ${BASE URL}/
    Page Should Contain    Year must be a four-digit number (YYYY).

Submit Invalid Volume
    Select From List by Value      id=tyyppi    1 
    Input Text      id=author      John Doe
    Input Text      id=title       Example Title
    Input Text      id=journal     Journal Name
    Input Text      id=year        2023
    Input Text      id=volume      asdf
    Input Text      id=pages       20-30
    Click Button    id=submit
    Location Should Be    ${BASE URL}/
    Page Should Contain    Volume must be a positive integer.

Submit Invalid Pages
    Select From List by Value      id=tyyppi    1 
    Input Text      id=author      John Doe
    Input Text      id=title       Example Title
    Input Text      id=journal     Journal Name
    Input Text      id=year        2023
    Input Text      id=volume      10
    Input Text      id=pages       asdf
    Click Button    id=submit
    Location Should Be    ${BASE URL}/
    Page Should Contain    Pages must be a range in the format "start-end" or a single number.

*** Keywords ***
Error Message
    Run Keyword And Continue On Failure    Page Should Contain    Error message text here