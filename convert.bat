@echo off
rem Combines multiple Markdown files, then uses Pandoc (https://pandoc.org/) to convert 
rem it to docx format. Dedicated to those who still think in terms of huge 3-ring binders.

echo.
echo Decompress new zip archive (if exists)
tar -xf securityKB-main.zip
echo.
echo Files being included:
type securityKB-main\security_principles.md >> combined.md
type securityKB-main\architecture.md >> combined.md
type securityKB-main\authentication.md >> combined.md
type securityKB-main\access_control.md >> combined.md
type securityKB-main\session_management.md >> combined.md
type securityKB-main\input_output.md >> combined.md
type securityKB-main\tainted_input.md >> combined.md
type securityKB-main\data_protection.md >> combined.md
type securityKB-main\encrypted_communications.md >> combined.md
type securityKB-main\cryptographic_storage.md >> combined.md
type securityKB-main\web_services.md >> combined.md
type securityKB-main\api.md >> combined.md
type securityKB-main\business_logic.md >> combined.md
type securityKB-main\configuration.md >> combined.md
type securityKB-main\error_logging.md >> combined.md
type securityKB-main\files_resources.md >> combined.md
type securityKB-main\malicious_code.md >> combined.md
type securityKB-main\standards.md >> combined.md
type securityKB-main\resources.md >> combined.md
echo.
echo Converting combined file to docx
pandoc --quiet -o security_KB.docx -f markdown -t docx combined.md
echo.
echo Delete combined file
del combined.md
echo.
echo Done! New file is security_KB.docx.
echo.
