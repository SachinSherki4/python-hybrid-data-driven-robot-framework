*** Settings ***
Library    root.test_cases.registration.Registration


*** Test Cases ***
TC_01 Register New First User on Chrome browser
    [Tags]    Sanity    Regression    Smoke
    test register new user    1    Chrome

TC_02 Register New Second User on Firefox browser
    [Tags]    Smoke
    test register new user    2    Firefox

TC_03 Register New Third User on Edge browser
    [Tags]    Smoke    Regression
    test register new user    3    Edge
    

    
