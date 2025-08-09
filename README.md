
# Email Tone Teller (ETT)

<img src="./assets/banner.png" width="600">

**Email Tone Teller (ETT)** is a smart assistant that reads client emails and helps you understand:

- The tone (friendly, annoyed, passive-aggressive, etc.)
- The urgency level
- Suggested replies
- Key action items

Designed for agencies, freelancers, support teams, and professionals who deal with high-volume, high-stakes email.

## Planned Features

- Web interface to paste or upload email threads
- Slack and Teams integrations for tone analysis on demand
- Smart reply generator powered by LLMs
- Email-to-email relay system for live tone suggestions
- Admin dashboard for tracking sentiment over time (future)

## Powered By

- Python (FastAPI backend)
- OpenAI / Claude / LLama via Openrouter (LLM Models)
- Mailgun (for live email)
- Slack Bolt SDK & Microsoft Graph (for bot integrations)
- React / HTMX frontend (optional phase)

## Planned Structure

```bash
email-tone-teller/
├── backend/
│   ├── api-gateway/
│   ├── customer-api/
│   └── sentiment-api/
│       └── app/
│           ├── config/
│           │   └── llm_clients/
│           ├── dtos/
│           ├── routes/
│           ├── services/
│           ├── utilities/
│           └── main.py
│       ├── logs/
│       └── tests/
├── bots/
│   ├── slack/
│   ├── teams/
│   └── whatsapp/
├── frontend/
│   └── customer-web/
├── .env
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt

```

## Running the projects

```bash
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## Future Ideas

- Fallback logic (OpenAI → Claude → LLaMA)
- Slack + Teams notification integration
- Attachments summary (PDF, DOCX)
- Web frontend with email history
