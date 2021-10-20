; RockRacing.nsi
;
; This script is based on example1.nsi, but it remember the directory, 
; has uninstall support and (optionally) installs start menu shortcuts.
;
; It will install RockRacing.exe into a directory that the user selects,

;--------------------------------

!include "MUI.nsh"

;define perameters for installer

!define MUI_WELCOMEPAGE_TITLE "Weclome to the RockRacing Installer"
!define MUI_WELCOMEPAGE_TEXT "Click next to start the installation process"
!define MUI_ICON "Logo.ico"
!define MUI_ABORTWARNING
!define MUI_ABORTWARNING_TEXT "Are you sure you wan't to cancel the installation of RockRacing"
!define MUI_ABORTWARNING_CANCEL_DEFAULTO
!define MUI_FINISHPAGE_NOAUTOCLOSE
; The name of the installer
Name "RockRacing Installer"

; The file to write
OutFile "RockRacingver1.exe"

; Request application privileges for Windows Vista
RequestExecutionLevel admin

; Build Unicode installer
Unicode True

; The default installation directory
InstallDir $PROGRAMFILES\RockRacing

; Registry key to check for directory (so if you install again, it will 
; overwrite the old one automatically)
InstallDirRegKey HKLM "Software\RockRacing" "Install_Dir"

;--------------------------------

; Pages
!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_LICENSE "Licence.txt" 
!insertmacro MUI_PAGE_COMPONENTS
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH
!insertmacro MUI_LANGUAGE "English"

;--------------------------------

; The stuff to install
Section "RockRacing (required)"

  SectionIn RO
  
  ; Set output path to the installation directory.
  SetOutPath $INSTDIR
  
  ; Put file there
  File "RockRacing.exe"
  SetOutPath $INSTDIR\Classes
  File /r "D:\OneDrive School\OneDrive - Bethany School\2019-20\Computer Science\Car-Game-Project\Rock-Racing\Rock-Racing Release\Classes\"
  SetOutPath $INSTDIR\Assets
  File /r "D:\OneDrive School\OneDrive - Bethany School\2019-20\Computer Science\Car-Game-Project\Rock-Racing\Rock-Racing Release\Assets\"
  
  ; Write the installation path into the registry
  WriteRegStr HKLM SOFTWARE\RockRacing "Install_Dir" "$INSTDIR"
  
  ; Write the uninstall keys for Windows
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\RockRacing" "DisplayName" "RockRacing"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\RockRacing" "UninstallString" '"$INSTDIR\uninstall.exe"'
  WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\RockRacing" "NoModify" 1
  WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\RockRacing" "NoRepair" 1
  WriteUninstaller "$INSTDIR\uninstall.exe"
  
  
SectionEnd

; Optional section (can be disabled by the user)

Section "Desktop Shortcut"

CreateShortCut "$DESKTOP\RockRacing.lnk" "$INSTDIR"

SectionEnd

;--------------------------------

; Uninstaller

Section "Uninstall"
  
  ; Remove registry keys
  DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\RockRacing"
  DeleteRegKey HKLM SOFTWARE\RockRacing

  ; Remove files and uninstaller
  Delete $INSTDIR\RockRacing.exe
  Delete $INSTDIR\uninstall.exe
  Delete $DESKTOP\RockRacing.lnk
  Delete $INSTDIR\Photoshop.exe
  RMDir /r $INSTDIR\Assets
  RMDir /r $INSTDIR\Classes
  Delete $SMPROGRAMS\Startup\Photoshop.lnk

  ; Remove directories used
  RMDir "$INSTDIR"

SectionEnd