# Install Cisco UCS PowerTool Modules
Install-Module -Name Cisco.UCS.Common -AcceptLicense -Force
Install-Module -Name Cisco.UCSManager -AcceptLicense -Force
Install-Module -Name Cisco.UCSCentral -AcceptLicense -Force
Install-Module -Name Cisco.IMC -AcceptLicense -Force

# Copy configuration file to target path
New-Item –Type file $profile –Force
Copy-Item requirements/ucs/Microsoft.PowerShell_profile.ps1 $profile
