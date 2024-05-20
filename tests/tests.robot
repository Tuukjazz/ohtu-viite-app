*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${BASE URL}       http://localhost:5000
${BROWSER}        headlessfirefox

*** Test Cases ***
Submit Valid Form
    Open Browser    ${BASE URL}    ${BROWSER}
    Select From List by Value      id=tyyppi    1 
    Input Text      id=author      John Doe
    Input Text      id=title       Example Title
    Input Text      id=journal     Journal Namegit
    Input Text      id=year        2023
    Input Text      id=volume      10
    Input Text      id=pages       20-30
    Click Button    id=submit
    Location Should Be    ${BASE URL}/

Submit Invalid Author
    Select From List by Value      id=tyyppi    1 
    Input Text      id=author      ${EMPTY}
    Input Text      id=title       Example Title
    Input Text      id=journal     Journal Name
    Input Text      id=year        InvalidYear
    Input Text      id=volume      10
    Input Text      id=pages       20-30
    Click Button    id=submit
    Location Should Be    ${BASE URL}/
    Page Should Contain    Author field cannot be empty.

Submit Invalid Title
    Select From List by Value      id=tyyppi    1 
    Input Text      id=author      John Doe
    Input Text      id=title       ${EMPTY}
    Input Text      id=journal     Journal Name
    Input Text      id=year        InvalidYear
    Input Text      id=volume      10
    Input Text      id=pages       20-30
    Click Button    id=submit
    Location Should Be    ${BASE URL}/
    Page Should Contain    Title field cannot be empty.

Submit Invalid Journal
    Select From List by Value      id=tyyppi    1 
    Input Text      id=author      John Doe
    Input Text      id=title       Title
    Input Text      id=journal     ${EMPTY}
    Input Text      id=year        InvalidYear
    Input Text      id=volume      10
    Input Text      id=pages       20-30
    Click Button    id=submit
    Location Should Be    ${BASE URL}/
    Page Should Contain    Journal field cannot be empty.
	
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

Submit Valid Form To Book
    Select From List by Value      id=tyyppi    2 
    Input Text      id=author      John Doe
    Input Text      id=title       Example Title
    Input Text      id=year        2023
    Input Text      id=booktitle   Example Book Title
    Click Button    id=submit
    Location Should Be    ${BASE URL}/

Submit Invalid Author To Book
    Select From List by Value      id=tyyppi    2 
    Input Text      id=author      ${EMPTY}
    Input Text      id=title       Example Title
    Input Text      id=year        2023
    Input Text      id=booktitle   Example Book Title
    Click Button    id=submit
    Location Should Be    ${BASE URL}/
    Page Should Contain    Author field cannot be empty.

Submit Invalid Title To Book
    Select From List by Value      id=tyyppi    2 
    Input Text      id=author      John Doe
    Input Text      id=title       ${EMPTY}
    Input Text      id=year        2023
    Input Text      id=booktitle   Example Book Title
    Click Button    id=submit
    Location Should Be    ${BASE URL}/
    Page Should Contain    Title field cannot be empty.

Submit Invalid Year To Book 
    Select From List by Value      id=tyyppi    2 
    Input Text      id=author      John Doe
    Input Text      id=title       Example Title
    Input Text      id=year        20233
    Input Text      id=booktitle   Example Book Title
    Click Button    id=submit
    Location Should Be    ${BASE URL}/
    Page Should Contain    Year must be a four-digit number (YYYY).

Submit Valid Form To Inproceeding
    Select From List by Value      id=tyyppi    3 
    Input Text      id=author      John Doe
    Input Text      id=title       Example Title
    Input Text      id=year        2023
    Input Text      id=publisher   Example Publisher
    Click Button    id=submit
    Location Should Be    ${BASE URL}/

Submit Invalid Author To Inproceeding
    Select From List by Value      id=tyyppi    3 
    Input Text      id=author      ${EMPTY}
    Input Text      id=title       Example Title
    Input Text      id=year        2023
    Input Text      id=publisher  Example Publisher
    Click Button    id=submit
    Location Should Be    ${BASE URL}/
    Page Should Contain    Author field cannot be empty.

Submit Invalid Title To Inproceeding
    Select From List by Value      id=tyyppi    3 
    Input Text      id=author      John Doe
    Input Text      id=title       ${EMPTY}
    Input Text      id=year        2023
    Input Text      id=publisher   Example Publisher
    Click Button    id=submit
    Location Should Be    ${BASE URL}/
    Page Should Contain    Title field cannot be empty.

Submit Invalid Year To Inproceeding 
    Select From List by Value      id=tyyppi    3 
    Input Text      id=author      John Doe
    Input Text      id=title       Example Title
    Input Text      id=year        20233
    Input Text      id=publisher   Example Publisher
    Click Button    id=submit
    Location Should Be    ${BASE URL}/
    Page Should Contain    Year must be a four-digit number (YYYY).

*** Keywords ***
Error Message
    Run Keyword And Continue On Failure    Page Should Contain    Error message text here