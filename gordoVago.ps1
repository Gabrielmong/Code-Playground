param($sleep = 240) # seconds
$announcementInterval = 10 # loops

Clear-Host

$WShell = New-Object -com "Wscript.Shell"
$date = Get-Date -Format "dddd MM/dd HH:mm (K)"

$stopwatch

try {
    $stopwatch = [system.diagnostics.stopwatch]::StartNew()
} catch {
   Write-Host "Couldn't start the stopwatch."
}

Write-Host "Executing ScrollLock-toggle NoSleep routine."
Write-Host "Start time:" $(Get-Date -Format "dddd MM/dd HH:mm (K)")

Write-Host "<3" -fore red

$index = 0
while ( $true )
{
    Write-Host "< 3" -fore red     
    $WShell.sendkeys("{SCROLLLOCK}")

    Start-Sleep -Milliseconds 200

    $WShell.sendkeys("{SCROLLLOCK}")
    Write-Host "<3" -fore red     

    Start-Sleep -Seconds $sleep

    # Announce runtime on an interval
    if ( $stopwatch.IsRunning -and (++$index % $announcementInterval) -eq 0 )
    {
        Write-Host "Elapsed time: " $stopwatch.Elapsed.ToString('dd\.hh\:mm\:ss')
    }
}