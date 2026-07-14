# OSS Audit Platform

An AI-powered Open Source Software (OSS) Audit Platform designed to automate Software Bill of Materials (SBOM), Cryptography Bill of Materials (CBOM), compliance analysis, and AI-generated audit reports.

---

## Features

- Automated OSS repository scanning
- SBOM generation
- CBOM generation
- AI-powered executive summaries
- Compliance scoring
- Cryptographic analysis
- PDF report generation
- Interactive dashboard
- GitHub Actions automation
- Configurable project policies

---

## Project Structure

```text
oss-audit-platform/
│
├── .github/
├── config/
├── automation/
├── scanners/
├── ai/
├── dashboard/
├── storage/
├── logs/
├── scripts/
├── tests/
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── README.md
└── LICENSE
```

---

## Architecture

```text
GitHub Workflow
        │
        ▼
Automation
        │
        ▼
Repository Manager
        │
        ▼
SCANOSS
        │
        ▼
SBOM
        │
        ▼
CryptoFinder
        │
        ▼
CBOM
        │
        ▼
AI Report Generator
        │
        ▼
Storage
        │
        ▼
Dashboard
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd oss-audit-platform
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

---

## Project Setup

```bash
chmod +x scripts/*.sh

./scripts/setup.sh

./scripts/install.sh
```

---

## Running the Pipeline

Execute the full OSS audit pipeline:

```bash
./scripts/run_pipeline.sh
```

---

## Starting the Dashboard

```bash
./scripts/start.sh
```

Backend API:

```
http://localhost:5000
```

---

## Running with Docker

Build the image:

```bash
docker build -t oss-audit-platform .
```

Run using Docker Compose:

```bash
docker compose up -d
```

---

## Running Tests

```bash
python -m unittest discover tests
```

---

## Technologies Used

- Python
- Flask
- React
- GitHub Actions
- SCANOSS
- CryptoFinder
- ReportLab
- Docker

---

## Modules

- Configuration
- Automation
- Scanners
- AI Report Generator
- Dashboard
- Storage
- Logging
- Scripts
- Testing

---

## License

See the LICENSE file for licensing information.
