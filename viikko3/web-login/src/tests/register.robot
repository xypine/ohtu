*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kalleB
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  k
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  kallekolme
    Set Password  k
    Set Password Confirmation  k
    Submit Credentials
    Register Should Fail With Message  Password too short

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Set Username  kalleneljä
    Set Password  yykaakoonee
    Set Password Confirmation  yykaakoonee
    Submit Credentials
    Register Should Fail With Message  Password shouldn't consist of letters only

Register With Nonmatching Password And Password Confirmation
    Set Username  kalleviis
    Set Password  123456
    Set Password Confirmation  abcdef
    Submit Credentials
    Register Should Fail With Message  Password and password confirmation did not match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Fail With Message  That username is already in use

Login After Successful Registration
	Set Username  kayttaja
	Set Password  salasana123
	Set Password Confirmation  salasana123
	Submit Credentials
	Logout
   Set Username  kayttaja
   Set Password  salasana123
   Click Button  Login
   Main Page Should Be Open

Login After Failed Registration
	Set Username  kalleviis
	Set Password  123456
	Set Password Confirmation  abcdef
	Submit Credentials
	Register Should Fail With Message  Password and password confirmation did not match
	Go To Login Page
	Set Username  kalleviis
	Set Password  123456
   Click Button  Login
	Page Should Contain  Invalid username or password

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

Logout
	Go To Main Page
   Click Button  Logout
