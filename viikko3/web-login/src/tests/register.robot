*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kalle2
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  k
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Fail With Message  username too short

Register With Valid Username And Too Short Password
    Set Username  kalle3
    Set Password  k
    Set Password Confirmation  k
    Submit Credentials
    Register Should Fail With Message  username too short

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Set Username  kalle4
    Set Password  k
    Set Password Confirmation  k
    Submit Credentials
    Register Should Fail With Message  lalalala

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle5
    Set Password  123456
    Set Password Confirmation  abcdef
    Submit Credentials
    Register Should Fail With Message  lalalala

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Succeed

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page
