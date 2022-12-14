@echo off
rem Combines multiple Markdown files, then uses Pandoc (https://pandoc.org/) to convert 
rem it to docx format.

echo.
echo Decompress new zip archive (if exists)
tar -xf securityKB-main.zip
echo.
echo Files being included:
type securityKB-main\*.md >> combined.md
echo.
echo Converting combined file to docx
pandoc --quiet -o security_KB.docx -f markdown -t docx combined.md
echo.
echo Delete combined file
del combined.md
echo.
echo Done! New file is security_KB.docx.
echo.
