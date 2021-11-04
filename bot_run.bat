@echo off
 call %~dp0telegram_bot\venv\Scripts\activate
 
 cd %~dp0telegram_bot
 
 set TOKEN=2091158951:AAGaFF3Qf26KuyD5LaWKVoiMak8mH_O6fQs
 
 python main.py
 
 pause