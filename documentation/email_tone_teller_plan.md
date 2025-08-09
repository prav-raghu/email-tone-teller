# Email Tone Teller - MVP & Expansion Plan

## MVP Blueprint
Read inbox → generate smart reply → show in portal → optionally send via Gmail/Outlook.  
Start with Gmail, then add Outlook. Store email, process with OpenRouter, provide suggestions, and allow sending replies.

## Phase 1 — Gmail
**Auth & Scopes:** OAuth2 with `gmail.readonly`, `gmail.send`, `gmail.modify` later.  
Store refresh tokens encrypted. Use push notifications (Pub/Sub) or poll `users.history.list`.  
**Flow:** Detect new message → fetch → normalize → analyze with OpenRouter → store suggestion → notify UI.  
Send via Gmail API `users.messages.send`.

## Phase 2 — Outlook
Use Microsoft Graph OAuth2 with `Mail.Read`, `Mail.Send`. Add webhooks for change notifications.  
Use delta queries for backfill. Mirror Gmail flow for analysis and reply.

## Data Model
`users`, `oauth_tokens`, `mailboxes`, `threads`, `messages`, `suggestions`, `api_keys`, `usage_events`, `plans` tables.  
Includes storing provider IDs, auth details, and usage for metering.

## Services & Components
FastAPI for API and webhooks. Worker (Celery/RQ + Redis) for async tasks.  
Postgres for DB. Redis for cache/queue. Optional S3 for raw MIME storage.

## Portal + Marketing Site
**Portal:** inbox, suggestion panel, settings (connect Gmail/Outlook, API keys, usage charts).  
**Public site:** landing page, pricing, signup, docs.

## API
- `POST /v1/analyze`
- `POST /v1/suggestion/send`
- `POST /v1/keys`
- `GET /v1/usage`
- Webhooks for Gmail and Outlook

Auth via Bearer API key for customer API, OAuth session for portal.

## LLM Prompt & Response
System role + user content with subject, body, thread summary.  
Return JSON only. Validate with pydantic. Rate limit per API key.

## Security
Encrypt refresh tokens. No logging of email bodies. Verify webhook signatures.  
SCIM/SSO not needed for MVP.

## Next Steps
1. Create Google project, OAuth consent, enable Gmail API.
2. Add OAuth endpoints in FastAPI and token storage.
3. Implement Gmail poller with historyId.
4. Set up Celery/RQ worker for LLM calls.
5. Build portal skeleton with inbox and suggestion pane.
6. Implement API key management.
7. Write Quickstart docs and update README with banner.
