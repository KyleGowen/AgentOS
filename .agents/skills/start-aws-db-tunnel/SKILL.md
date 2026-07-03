---
name: start-aws-db-tunnel
description: Excelsior production PostgreSQL tunnel workflow. Use when the user asks to start the AWS tunnel, SSM DB tunnel, production RDS access, connect TablePlus or psql to prod, or run scripts/ssm-prod-db-tunnel.sh in the background through AWS Systems Manager Session Manager port forwarding.
---

# Start AWS DB Tunnel

Start or guide a long-lived local tunnel so clients can reach production RDS as
`127.0.0.1:<local-port>` through AWS SSM and the app EC2 instance. RDS is not
publicly exposed.

## Source Of Truth

- `docs/current/DEPLOYMENT.md`, section "Production database access (SSM port forwarding)".
- `scripts/ssm-prod-db-tunnel.sh`.
- `docs/examples/ssm-prod-db-tunnel-policy.json.sample` for IAM examples.

Do not duplicate IAM policy JSON in chat; route to the runbook.

## Prerequisites

Confirm AWS CLI v2, Session Manager plugin, credentials, and IAM permissions.
Use `--profile NAME` on every AWS command when the user relies on a non-default
profile.

## Windows Guidance

Kyle's primary Excelsior machine is Windows with PowerShell. If the agent shell
cannot run `aws.exe` reliably, do not attempt to start AWS commands from the
agent shell. Give the user copy-paste PowerShell commands and continue from
pasted output.

PowerShell setup:

```powershell
$env:Path = "C:\Program Files\Amazon\AWSCLIV2;" + $env:Path
$env:AWS_PAGER = ""
```

If Session Manager plugin is missing, install it and open a new terminal:

```powershell
Invoke-WebRequest -Uri "https://s3.amazonaws.com/session-manager-downloads/plugin/latest/windows/SessionManagerPluginSetup.exe" -OutFile "$env:TEMP\SessionManagerPluginSetup.exe"
Start-Process "$env:TEMP\SessionManagerPluginSetup.exe" -ArgumentList "/quiet" -Wait
```

Use a parameter file because PowerShell can mangle inline JSON:

```powershell
@'
{"host":["op-deckbuilder-postgres.cdaeyc0ik7bu.us-west-2.rds.amazonaws.com"],"portNumber":["5432"],"localPortNumber":["15432"]}
'@ | Set-Content -Encoding ascii "$env:TEMP\ssm-params.json"

aws ssm start-session --region us-west-2 --target i-INSTANCE_ID --document-name AWS-StartPortForwardingSessionToRemoteHost --parameters file://$env:TEMP/ssm-params.json
```

Check port 15432:

```powershell
Get-NetTCPConnection -LocalPort 15432 -State Listen -ErrorAction SilentlyContinue
```

Stop with Ctrl+C in the tunnel window or by terminating the owning PID.

## Resolve Instance

Prefer an instance id supplied by the user. Otherwise list the running app
instance tagged `Name=op-deckbuilder-app` in `us-west-2`:

```bash
aws ec2 describe-instances --region us-west-2 \
  --filters "Name=tag:Name,Values=op-deckbuilder-app" "Name=instance-state-name,Values=running" \
  --query 'Reservations[].Instances[].[InstanceId,State.Name,Tags[?Key==`Name`].Value|[0]]' \
  --output table
```

Verify SSM Online status before trusting the instance.

## Avoid Duplicates

Default local port is `15432`. On macOS/Linux:

```bash
lsof -nP -iTCP:15432 -sTCP:LISTEN
```

If the port is already in use, reuse that tunnel if appropriate or pick another
port, such as `LOCAL_PORT=15433`.

## Start Tunnel

The `start-session` process must keep running. Do not block the whole agent turn
on a foreground session unless the user asks.

On non-Windows environments where AWS CLI works from the shell:

```bash
nohup ./scripts/ssm-prod-db-tunnel.sh i-INSTANCE_ID >>"${HOME}/.ssm-op-deckbuilder-db-tunnel.log" 2>&1 &
echo $!
```

If needed, make the script executable once with
`chmod +x scripts/ssm-prod-db-tunnel.sh`.

Environment overrides: `AWS_REGION`, `LOCAL_PORT`, `RDS_PORT`, and `RDS_HOST`.

## Verify And Connect

Confirm the local port is listening. Connect clients to `127.0.0.1` and the
local port, not the RDS hostname. Use `sslmode=require` for `psql`.

For TablePlus:

```text
postgresql://postgres:YOUR_PASSWORD@127.0.0.1:15432/overpower?sslmode=require
```

Use the documented SSM parameter path for the password and URL-encode special
characters. Never paste real production passwords into files, commits, or logs.
