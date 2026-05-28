# CSE-406: Computer Security

This repository contains coursework for CSE-406, covering cryptography, web
security, buffer overflow attacks, and a project on YARA rules.

## Repository Structure

### Offline 01: Cryptosystem with ECDH

Location: `Offline_01/`

Implements a symmetric-key cryptosystem where the shared key is established
through Elliptic Curve Diffie-Hellman (ECDH).

Key files:

- `Offline_01/CSE-406--assignment-01.pdf` - assignment specification
- `Offline_01/1905038/1905038_f1.py` - AES-style encryption/decryption logic
- `Offline_01/1905038/1905038_f2.py` - elliptic curve and ECDH operations
- `Offline_01/1905038/1905038_f3.py` - receiver/Bob socket program
- `Offline_01/1905038/1905038_f4.py` - sender/Alice socket program
- `Offline_01/1905038/INPUT.txt` - plaintext input file

### Offline 02: Cross-Site Scripting

Location: `Offline_02/`

Contains SEED Labs/Elgg XSS attack payloads and the assignment report.

Key files:

- `Offline_02/Assignment_2_Web_Security/Assignment_2_Web_Security/CSE 406 Web Security Assignment.pdf`
- `Offline_02/Assignment_2_Web_Security/Assignment_2_Web_Security/XSSDemo.txt`
- `Offline_02/1905038/1905038_Task_1.js`
- `Offline_02/1905038/1905038_Task_2.js`
- `Offline_02/1905038/1905038_Task_3.js`
- `Offline_02/1905038/1905038_Task_4.js`
- `Offline_02/1905038/1905038_report.pdf`

### Online 02: Buffer Overflow

Location: `Online_02/`

Contains a vulnerable C program, payload generation script, output screenshot,
and assignment files for a buffer overflow attack.

Key files:

- `Online_02/1905038.py` - payload generator
- `Online_02/buffer-overflow-online-A2/buffer-overflow-online-A2/A2.c` - vulnerable C program
- `Online_02/buffer-overflow-online-A2/buffer-overflow-online-A2/output.png` - sample attack output
- `Online_02/buffer-overflow-online-A2/buffer-overflow-online-A2/CSE406_Online_1_Jan2023.pdf`
- `Online_02/buffer-overflow-online-A2/buffer-overflow-online-A2/CSEFESTSERVER/server.py`

### Project: YARA

Location: `project/`

Contains project materials, reports, slides, spreadsheets, and YARA rule
examples for detecting different binary and string patterns.

Key files:

- `project/Security Tools.pptx` - security tools slide deck
- `project/rules/` - YARA rules
- `project/Report/` - project reports
- `project/CSE 406 Project (July 2023).xlsx`
- `project/CSE 406 Project Video Links.xlsx`
- `project/Project-Assignment-18 Batch.xlsx`
- `project/other_project_link.txt`

## Notes

- Some Python scripts use hardcoded Windows paths and may need path updates
  before running on macOS or Linux.
- `Offline_01/1905038/INPUT.txt` is currently empty.
- `project/project.txt` is currently empty.
- PDF, PPTX, XLSX, and PNG files are included as supporting artifacts.
