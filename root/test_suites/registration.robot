*** Settings ***
Library    root.test_cases.registration.Registration


*** Test Cases ***
TC_01 Register New First User
    test register new user    1

TC_02 Register New Second User
    test register new user    2

TC_03 Register New Third User
    test register new user    3

TC_04 Register New Forth User
    test register new user    4