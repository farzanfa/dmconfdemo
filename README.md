# Hello CACD + MCP Demo

A minimal project to demo **Shift-Left Release Management** from **Cursor** using:
- **GitHub MCP server** to dispatch a workflow
- **AWS CloudWatch MCP server** to fetch logs & metrics
- **AWS Lambda Function URL** to expose a public "Hello World" page

## What happens
1. Trigger the workflow (`deploy.yml`) via **GitHub MCP** from Cursor.
2. The workflow creates/updates a **Lambda** and ensures a **Function URL** is public.
3. The job prints the URL; open it in your browser.
4. The job also writes a CloudWatch **metric** and a **log** for your CloudWatch MCP demo.

## One-time setup
- In your GitHub repo → Settings → Secrets and variables → *Actions*:
  - `AWS_ACCESS_KEY_ID`
  - `AWS_SECRET_ACCESS_KEY`
  - *(optional)* `AWS_SESSION_TOKEN` (only if using temporary creds)
- Ensure the IAM user has permissions to:
  - Lambda create/update + function URL
  - IAM create/get/attach for the Lambda execution role
  - Logs create stream/group and put events
  - CloudWatch `PutMetricData`

## Run the demo (from Cursor)
**A) Trigger deploy**
> Using GitHub, dispatch the workflow `.github/workflows/deploy.yml` on branch `main` with input `env=dev`. Then give me the run URL and status.

**B) Grab the Function URL**
The workflow prints `Function URL: ...` — open it in the browser to see “Hello from CACD + MCP 👋”.

**C) Observe with CloudWatch MCP**
- Metrics prompt:  
  > Using CloudWatch, get metric data for namespace `Demo/Deployments`, metric `DeploymentCount`, dimensions `Repo=<owner/repo>,Commit=<sha>,Env=dev`, last 15 minutes, statistic `Sum`.

- Logs prompt:  
  > Using CloudWatch, run a Logs Insights query on log group `/aws/demo/deployments` for the last 15 minutes: `fields @timestamp,@message | sort @timestamp desc | limit 20`.

## Notes
- Default region in the workflow is **us-east-1**; change `AWS_REGION` if needed.
- Lambda name defaults to `hello-cacd-mcp`; change via env in the workflow.
