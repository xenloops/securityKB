@echo off
rem Combines multiple Markdown files, then uses Pandoc (https://pandoc.org/) to convert 
rem it to docx format.

echo.
echo Delete existing combined file
del securityKB-main\combined.md
echo.
echo Files being included:
type securityKB-main\*.md >> securityKB-main\combined.md
echo.
echo Converting combined file to docx
pandoc --quiet -o security_KB.docx -f markdown -t docx securityKB-main\combined.md
echo.
echo Done! New file is security_KB.docx.
echo.
