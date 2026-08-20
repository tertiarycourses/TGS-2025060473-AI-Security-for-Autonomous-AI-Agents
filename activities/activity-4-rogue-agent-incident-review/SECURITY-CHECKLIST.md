# Activity 4 - Autonomous Agent Containment Checklist

- [ ] Evaluation targets are synthetic or explicitly authorised and isolated from public infrastructure.
- [ ] Internet access is denied by default and verified from inside the sandbox.
- [ ] Agent, evaluator and target identities are distinct, short-lived and least-privileged.
- [ ] Skills, plugins, MCP servers, tools and dependencies are pinned and allowlisted.
- [ ] The agent cannot discover, install or update capabilities autonomously.
- [ ] Filesystem mounts are minimal and read-only unless the test requires a bounded write path.
- [ ] Outbound network destinations, protocols, data volume and DNS are controlled and logged.
- [ ] Destructive, publishing, identity, credential and cross-boundary actions require human approval.
- [ ] Approval binds the exact command, parameters, target and time window.
- [ ] Rate, cost, step and time budgets stop runaway loops.
- [ ] Behavioural monitoring detects sequences across accounts, repositories and tools.
- [ ] A tested kill switch stops execution and revokes credentials without relying on the agent.
- [ ] Checkpoints support rollback; evidence preserves prompts, plans, tool calls and effects.
- [ ] The incident plan covers third-party notification, legal/privacy assessment and safe disclosure.
