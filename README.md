
# Email Tone Teller (ETT)

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
- OpenAI / Claude (LLM APIs)
- Mailgun or Gmail API (for live email)
- Slack Bolt SDK & Microsoft Graph (for bot integrations)
- React / HTMX frontend (optional phase)

## Planned Structure

```
email-tone-teller/
├── backend/
│   ├── main.py              # FastAPI app
│   ├── routes/analyze.py    # Email tone/urgency endpoint
│   └── utils/llm.py         # LLM prompt + call logic
├── slackbot/
│   └── handler.py           # Slack events
├── teamsbot/
│   └── handler.py           # Microsoft Teams connector
├── frontend/
│   └── index.html           # Web UI (optional)
├── .env.example             # Environment variable template
├── requirements.txt         # Python dependencies
└── README.md
```
## Running the projects

pip install -r requirements.txt