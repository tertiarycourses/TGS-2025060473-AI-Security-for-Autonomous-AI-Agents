# Activity 3 - Framework and Go-Live Evidence Checklist

## Govern and map

- [ ] The use case, owner, users, data, model, tools, skills/plugins and third parties are inventoried.
- [ ] NIST AI RMF responsibilities and risk tolerance are approved by leadership.
- [ ] PDPA requirements are treated as the legal floor, not as an optional framework choice.
- [ ] GenAI and autonomous-agent components have separate threat models and identities.

## Threat coverage

- [ ] OWASP LLM risks cover prompt, data, output and model/application threats.
- [ ] OWASP ASI risks cover goal hijack, tools, identity, supply chain, memory and cascading action.
- [ ] MITRE ATLAS or equivalent adversary behaviours drive realistic tests.
- [ ] IMDA dimensions define autonomy limits, significant human checkpoints and end-user responsibility.

## Measure and decide

- [ ] Attack success, unsafe tool-call, refusal and false-positive rates have written thresholds.
- [ ] Results are broken down by attack family, prompt variant and affected user segment.
- [ ] A release is blocked by the worst material scenario, not rescued by an aggregate average.
- [ ] Residual risk names an owner, mitigation, expiry date and re-test trigger.
- [ ] The board has an evidence-based go/no-go decision and a safe non-agent alternative.
