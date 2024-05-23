# Delete .py files inside migrations directories except __init__.py
Get-ChildItem -Path . -Recurse -Filter *.py |
    Where-Object { $_.FullName -like "*\migrations\*.py" -and $_.Name -ne "__init__.py" } |
    Remove-Item -Force

# Delete .pyc files inside migrations directories
Get-ChildItem -Path . -Recurse -Filter *.pyc |
    Where-Object { $_.FullName -like "*\migrations\*.pyc" } |
    Remove-Item -Force