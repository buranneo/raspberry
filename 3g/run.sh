#!/bin/sh
./umtskeeper --sakisoperators "USBINTERFACE='0' OTHER='USBMODEM' USBMODEM='12d1:1001' APN='CUSTOM_APN' CUSTOM_APN='internet' SIM_PIN='1234' APN_USER='megafon' APN_PASS='megafon'" --sakisswitches "--sudo --console" --devicename 'Huawei' --log --silent --nat 'no'
