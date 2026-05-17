# PowerShell script to automatically create a Windows Scheduled Task for the File Organizer

$TaskName = "Syntecxhub_File_Organizer"
$PythonPath = "F:\SYNTEC\file-organizer-script\venv\Scripts\python.exe"
$ScriptPath = "organizer.py"
$WorkingDirectory = "F:\SYNTEC\file-organizer-script\"

Write-Host "=== Registering File Organizer Scheduled Task ===" -ForegroundColor Magenta

# Check if Python exists in venv
if (-not (Test-Path $PythonPath)) {
    Write-Error "Virtual environment Python interpreter not found at $PythonPath! Please create the venv first."
    exit
}

# Create Scheduled Task Action
$Action = New-ScheduledTaskAction -Execute $PythonPath -Argument $ScriptPath -WorkingDirectory $WorkingDirectory

# Create Trigger (Daily at 12:00 PM)
$Trigger = New-ScheduledTaskTrigger -Daily -At 12:00PM

# Create Task Settings (allow running on battery, etc.)
$Settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries

# Register the Scheduled Task
Register-ScheduledTask -TaskName $TaskName -Action $Action -Trigger $Trigger -Settings $Settings -Description "Automatically organizes files in test_folder daily at 12:00 PM." -Force | Out-Null

Write-Host "✅ Scheduled Task '$TaskName' successfully registered!" -ForegroundColor Green
Write-Host "📅 It is set to run Daily at 12:00 PM." -ForegroundColor Cyan
Write-Host "`nTo showcase it running immediately, you can trigger it manually with:" -ForegroundColor Yellow
Write-Host "Start-ScheduledTask -TaskName `"$TaskName`"" -ForegroundColor White
