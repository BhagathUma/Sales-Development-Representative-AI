# ScaleSDR

### Human-grade outreach at machine-scale.

ScaleSDR is an autonomous AI-powered Sales Development Representative (SDR) platform that transforms a company URL into actionable sales intelligence. It automates prospect research, lead qualification, competitor analysis, personalized outreach generation, follow-up creation, and report generation using a multi-agent AI workflow.

Built by me for the FlowZint AI Hackathon 2026.

---

## Problem Statement

Sales representatives spend significant time researching prospects, understanding business challenges, analyzing competitors, qualifying leads, and crafting personalized outreach. These repetitive tasks reduce the time available for actual customer engagement.

Most AI sales tools focus only on generating emails and lack strategic context.

ScaleSDR addresses this problem by acting as an autonomous AI SDR that automates the complete pre-sales intelligence workflow.

---

## Features

### Company Intelligence Agent

Automatically extracts:

* Company overview
* Industry classification
* Business model
* Products and services
* Target customers

### Pain Point Analysis Agent

Identifies:

* Operational challenges
* Growth bottlenecks
* Customer support issues
* Business opportunities

### Lead Qualification Agent

Generates:

* Lead score (0–100)
* Qualification status
* Sales readiness insights

### Outreach Agent

Creates personalized:

* Email subject
* Cold email
* LinkedIn message

### Dynamic Tone Generator

Supports multiple communication styles:

* Professional
* Executive
* Friendly
* Consultative
* Challenger

Generated tones are cached to prevent redundant AI calls.

### Competitor Intelligence Agent

Performs external market research to:

* Discover competitors
* Analyze feature gaps
* Identify pricing gaps
* Generate strategic sales wedges

### Follow-Up Sequence Agent

Generates:

* Day 3 Follow-Up
* Day 7 Follow-Up
* Final Breakup Email

All follow-ups are generated on demand and cached.

### SDR Intelligence Report

Exports a professional PDF report containing:

* Executive Summary
* Company Analysis
* Lead Qualification
* Pain Point Analysis
* Competitor Intelligence
* Outreach Assets
* Follow-Up Strategy
* Agent Execution Summary

---

## System Architecture

```text
Company URL
      ↓
Company Intelligence Agent
      ↓
Pain Point Analysis Agent
      ↓
Lead Qualification Agent
      ↓
Outreach Agent
      ↓
Competitor Intelligence Agent
      ↓
Follow-Up Agent
      ↓
SDR Intelligence Report
```

---

## Technology Stack

### Frontend

* Next.js
* React
* TypeScript
* Tailwind CSS
* Framer Motion

### Backend

* FastAPI
* Python
* Pydantic

### AI Layer

* Google Gemini API
* Prompt Engineering
* Structured JSON Outputs

### Search

* Tavily Search API

### Reporting

* ReportLab

---

## Project Structure

```text
ScaleSDR/
│
├── frontend/
│   ├── src/
│   │   ├── app/
│   │   ├── components/
│   │   ├── services/
│   │   └── types/
│   │
│   └── public/
│
├── backend/
│   ├── agents/
│   ├── models/
│   ├── services/
│   ├── utils/
│   └── main.py
│
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd ScaleSDR
```

### Backend Setup

```bash
cd backend

python -m venv venv

source venv/bin/activate
# Windows:
# venv\Scripts\activate

pip install -r requirements.txt
```

Create a `.env` file:

```env
GOOGLE_API_KEY=your_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Run backend:

```bash
uvicorn main:app --reload
```


### Frontend Setup

```bash
cd frontend

npm install

npm run dev
```


## Usage

### Step 1

Enter a company website URL.

Example:

```text
https://notion.so
```

### Step 2

Click:

```text
Analyze Lead
```

ScaleSDR generates:

* Company Analysis
* Pain Points
* Lead Score
* Outreach Assets

### Step 3

Generate advanced intelligence:

* Competitor Analysis
* Tone-based Outreach
* Follow-Up Sequences

### Step 4

Download the generated Sales Intelligence Report.

---

## Key Innovations

ScaleSDR goes beyond traditional AI outreach tools by combining:

* Autonomous company research
* Lead qualification
* Competitive intelligence
* Strategic sales wedges
* Personalized outreach
* Follow-up automation
* Sales report generation

into a unified multi-agent workflow.

---

## Example Workflow

```text
User enters company URL
        ↓
AI agents analyze company
        ↓
Generate sales intelligence
        ↓
Create outreach assets
        ↓
Discover competitors
        ↓
Generate follow-ups
        ↓
Export PDF report
```

---

## Future Enhancements

* CRM Integration
* Real-time buying signals
* LinkedIn enrichment
* Email campaign automation
* Team collaboration dashboard

