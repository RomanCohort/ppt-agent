$ErrorActionPreference = 'Stop'

$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $projectRoot

$python = 'C:/Users/LENOVO/anaconda3/python.exe'

& $python -m pip install pyinstaller

& $python -m PyInstaller `
  --clean `
  --noconfirm `
  --onedir `
  --name PPTAgentDir `
  --add-data "streamlit.py;." `
  --add-data "utils.py;." `
  app_launcher.py

Write-Host "Build finished. Output: $projectRoot\dist\PPTAgentDir" -ForegroundColor Green
