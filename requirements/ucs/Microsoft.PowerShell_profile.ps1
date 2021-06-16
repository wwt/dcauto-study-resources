# Configure UCS PowerShell at Startup
Import-Module Cisco.UCS.Common
Import-Module Cisco.UCSManager
Import-Module Cisco.UCSCentral
Import-Module Cisco.IMC

$version = Get-UcsPowerToolConfiguration

write-host "          Welcome to Cisco UCS PowerTool Core Suite $($version.Version)"
write-host ""
write-host "Log in to UCS Manager:                                                  " -NoNewLine
write-host "Connect-Ucs" -foregroundcolor yellow
write-host "To generate PowerShell code for UCS Manager use:                        " -NoNewLine
write-host "ConvertTo-UcsCmdlet" -foregroundcolor yellow
write-host "To show object metadata for UCS PowerTool Cmdlets:                      " -NoNewLine
write-host "Get-UcsCmdletMeta" -foregroundcolor yellow
write-host ""
write-host "Log in to the IMC of standalone UCS server:                             " -NoNewLine
write-host "Connect-Imc" -foregroundcolor yellow
write-host "To generate PowerShell code for an IMC of a standalone UCS server:      " -NoNewLine
write-host "ConvertTo-ImcCmdlet" -foregroundcolor yellow
write-host "To show object metadata for IMC PowerTool Cmdlets:                      " -NoNewLine
write-host "Get-ImcCmdletMeta" -foregroundcolor yellow
write-host ""
write-host "Log in to UCS Central:                                                  " -NoNewLine
write-host "Connect-UcsCentral" -foregroundcolor yellow
write-host "To generate PowerShell code for UCS Central use:                        " -NoNewLine
write-host "ConvertTo-UcsCentralCmdlet" -foregroundcolor yellow
write-host "To show object metadata for UCS Central PowerTool Cmdlets:              " -NoNewLine
write-host "Get-UcsCentralCmdletMeta" -foregroundcolor yellow
write-host ""
write-host "To display the details of the UCS PowerTool Configuration:              " -NoNewLine
write-host "Get-UcsPowerToolConfiguration" -foregroundcolor yellow
write-host "To display details of UCS, IMC, and UCS Central active session(s):      " -NoNewLine
write-host "Get-UcsPSSession" -foregroundcolor yellow
write-host ""

if ((Test-Path env:UCS_PS_1)) {
    function prompt {$env:UCS_PS_1 + $(Get-Location) + "> "}
} else {
    function prompt {"[UCS PowerTool]: PS " + $(Get-Location) + "> "}
}
