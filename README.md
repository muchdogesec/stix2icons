# stix2icons

## Overview

stix2icons is a collection of icons that represent all the of core STIX objects. The aim is to provide a central source of icons that can be used to represent STIX objects by software tools (or anything else).

This repo is designed so that new icons can be added for custom STIX objects you're developing. See: "Adding your own objects".

## Where to find icons in this repository

The icons are provided in three colour versions: color, black, and white.

There are two variations of each colour provided; 1) with (normal) and 2) without a 'circle' (round) behind the icons.

Each icon has an `.svg` version and a `.png` (256x256) version. Generally you should use the `.svg` version and scale as required.

```txt
output/
├── black/
│   ├── normal/
│   │   ├── png
│   │   └── svg
│   ├── round/
│   │   ├── png
│   │   └── svg
├── rgb/
│   ├── normal/
│   │   ├── png
│   │   └── svg
│   ├── round/
│   │   ├── png
│   │   └── svg
└── white/
    ├── normal/
    │   ├── png
    │   └── svg
    └── round/
        ├── png
        └── svg
```

## Currently supported objects

| Object | Type | RGB | HEX | RGB Icon | RGB Circle Icon | Black Icon | Black Circle Icon | White Icon | White Circle Icon |
|--------|------|-----|-----|----------|-----------------|------------|------------------|------------|------------------|
| attack-pattern | SDO | 34, 119, 181 | #2277b5 | ![](output_files/rgb/normal/png/SDO/attack-pattern.png) | ![](output_files/rgb/round/png/SDO/attack-pattern.png) | ![](output_files/black/normal/png/SDO/attack-pattern.png) | ![](output_files/black/round/png/SDO/attack-pattern.png) | ![](output_files/white/normal/png/SDO/attack-pattern.png) | ![](output_files/white/round/png/SDO/attack-pattern.png) |
| campaign | SDO | 80, 182, 30 | #50b61e | ![](output_files/rgb/normal/png/SDO/campaign.png) | ![](output_files/rgb/round/png/SDO/campaign.png) | ![](output_files/black/normal/png/SDO/campaign.png) | ![](output_files/black/round/png/SDO/campaign.png) | ![](output_files/white/normal/png/SDO/campaign.png) | ![](output_files/white/round/png/SDO/campaign.png) |
| course-of-action | SDO | 161, 198, 40 | #a1c628 | ![](output_files/rgb/normal/png/SDO/course-of-action.png) | ![](output_files/rgb/round/png/SDO/course-of-action.png) | ![](output_files/black/normal/png/SDO/course-of-action.png) | ![](output_files/black/round/png/SDO/course-of-action.png) | ![](output_files/white/normal/png/SDO/course-of-action.png) | ![](output_files/white/round/png/SDO/course-of-action.png) |
| grouping | SDO | 163, 53, 139 | #a3358b | ![](output_files/rgb/normal/png/SDO/grouping.png) | ![](output_files/rgb/round/png/SDO/grouping.png) | ![](output_files/black/normal/png/SDO/grouping.png) | ![](output_files/black/round/png/SDO/grouping.png) | ![](output_files/white/normal/png/SDO/grouping.png) | ![](output_files/white/round/png/SDO/grouping.png) |
| identity | SDO | 0, 150, 136 | #009688 | ![](output_files/rgb/normal/png/SDO/identity.png) | ![](output_files/rgb/round/png/SDO/identity.png) | ![](output_files/black/normal/png/SDO/identity.png) | ![](output_files/black/round/png/SDO/identity.png) | ![](output_files/white/normal/png/SDO/identity.png) | ![](output_files/white/round/png/SDO/identity.png) |
| incident | SDO | 251, 182, 22 | #fbb616 | ![](output_files/rgb/normal/png/SDO/incident.png) | ![](output_files/rgb/round/png/SDO/incident.png) | ![](output_files/black/normal/png/SDO/incident.png) | ![](output_files/black/round/png/SDO/incident.png) | ![](output_files/white/normal/png/SDO/incident.png) | ![](output_files/white/round/png/SDO/incident.png) |
| indicator | SDO | 220, 149, 71 | #dc9547 | ![](output_files/rgb/normal/png/SDO/indicator.png) | ![](output_files/rgb/round/png/SDO/indicator.png) | ![](output_files/black/normal/png/SDO/indicator.png) | ![](output_files/black/round/png/SDO/indicator.png) | ![](output_files/white/normal/png/SDO/indicator.png) | ![](output_files/white/round/png/SDO/indicator.png) |
| infrastructure | SDO | 255, 87, 34 | #ff5722 | ![](output_files/rgb/normal/png/SDO/infrastructure.png) | ![](output_files/rgb/round/png/SDO/infrastructure.png) | ![](output_files/black/normal/png/SDO/infrastructure.png) | ![](output_files/black/round/png/SDO/infrastructure.png) | ![](output_files/white/normal/png/SDO/infrastructure.png) | ![](output_files/white/round/png/SDO/infrastructure.png) |
| intrusion-set | SDO | 56, 178, 193 | #38b2c1 | ![](output_files/rgb/normal/png/SDO/intrusion-set.png) | ![](output_files/rgb/round/png/SDO/intrusion-set.png) | ![](output_files/black/normal/png/SDO/intrusion-set.png) | ![](output_files/black/round/png/SDO/intrusion-set.png) | ![](output_files/white/normal/png/SDO/intrusion-set.png) | ![](output_files/white/round/png/SDO/intrusion-set.png) |
| location | SDO | 233, 30, 99 | #e91e63 | ![](output_files/rgb/normal/png/SDO/location.png) | ![](output_files/rgb/round/png/SDO/location.png) | ![](output_files/black/normal/png/SDO/location.png) | ![](output_files/black/round/png/SDO/location.png) | ![](output_files/white/normal/png/SDO/location.png) | ![](output_files/white/round/png/SDO/location.png) |
| malware | SDO | 244, 67, 54 | #f44336 | ![](output_files/rgb/normal/png/SDO/malware.png) | ![](output_files/rgb/round/png/SDO/malware.png) | ![](output_files/black/normal/png/SDO/malware.png) | ![](output_files/black/round/png/SDO/malware.png) | ![](output_files/white/normal/png/SDO/malware.png) | ![](output_files/white/round/png/SDO/malware.png) |
| malware-analysis | SDO | 231, 118, 172 | #e776ac | ![](output_files/rgb/normal/png/SDO/malware-analysis.png) | ![](output_files/rgb/round/png/SDO/malware-analysis.png) | ![](output_files/black/normal/png/SDO/malware-analysis.png) | ![](output_files/black/round/png/SDO/malware-analysis.png) | ![](output_files/white/normal/png/SDO/malware-analysis.png) | ![](output_files/white/round/png/SDO/malware-analysis.png) |
| note | SDO | 46, 125, 50 | #2e7d32 | ![](output_files/rgb/normal/png/SDO/note.png) | ![](output_files/rgb/round/png/SDO/note.png) | ![](output_files/black/normal/png/SDO/note.png) | ![](output_files/black/round/png/SDO/note.png) | ![](output_files/white/normal/png/SDO/note.png) | ![](output_files/white/round/png/SDO/note.png) |
| observed-data | SDO | 27, 94, 32 | #1b5e20 | ![](output_files/rgb/normal/png/SDO/observed-data.png) | ![](output_files/rgb/round/png/SDO/observed-data.png) | ![](output_files/black/normal/png/SDO/observed-data.png) | ![](output_files/black/round/png/SDO/observed-data.png) | ![](output_files/white/normal/png/SDO/observed-data.png) | ![](output_files/white/round/png/SDO/observed-data.png) |
| opinion | SDO | 139, 195, 74 | #8bc34a | ![](output_files/rgb/normal/png/SDO/opinion.png) | ![](output_files/rgb/round/png/SDO/opinion.png) | ![](output_files/black/normal/png/SDO/opinion.png) | ![](output_files/black/round/png/SDO/opinion.png) | ![](output_files/white/normal/png/SDO/opinion.png) | ![](output_files/white/round/png/SDO/opinion.png) |
| report | SDO | 194, 24, 91 | #c2185b | ![](output_files/rgb/normal/png/SDO/report.png) | ![](output_files/rgb/round/png/SDO/report.png) | ![](output_files/black/normal/png/SDO/report.png) | ![](output_files/black/round/png/SDO/report.png) | ![](output_files/white/normal/png/SDO/report.png) | ![](output_files/white/round/png/SDO/report.png) |
| threat-actor | SDO | 230, 27, 92 | #e61b5c | ![](output_files/rgb/normal/png/SDO/threat-actor.png) | ![](output_files/rgb/round/png/SDO/threat-actor.png) | ![](output_files/black/normal/png/SDO/threat-actor.png) | ![](output_files/black/round/png/SDO/threat-actor.png) | ![](output_files/white/normal/png/SDO/threat-actor.png) | ![](output_files/white/round/png/SDO/threat-actor.png) |
| tool | SDO | 87, 80, 157 | #57509d | ![](output_files/rgb/normal/png/SDO/tool.png) | ![](output_files/rgb/round/png/SDO/tool.png) | ![](output_files/black/normal/png/SDO/tool.png) | ![](output_files/black/round/png/SDO/tool.png) | ![](output_files/white/normal/png/SDO/tool.png) | ![](output_files/white/round/png/SDO/tool.png) |
| vulnerability | SDO | 255, 209, 0 | #ffd100 | ![](output_files/rgb/normal/png/SDO/vulnerability.png) | ![](output_files/rgb/round/png/SDO/vulnerability.png) | ![](output_files/black/normal/png/SDO/vulnerability.png) | ![](output_files/black/round/png/SDO/vulnerability.png) | ![](output_files/white/normal/png/SDO/vulnerability.png) | ![](output_files/white/round/png/SDO/vulnerability.png) |
| weakness | SDO | 94,49,128 | #5e3180 | ![](output_files/rgb/normal/png/SDO/weakness.png) | ![](output_files/rgb/round/png/SDO/weakness.png) | ![](output_files/black/normal/png/SDO/weakness.png) | ![](output_files/black/round/png/SDO/weakness.png) | ![](output_files/white/normal/png/SDO/weakness.png) | ![](output_files/white/round/png/SDO/weakness.png) |
| exploit | SDO | 0,132,80 | #008450 | ![](output_files/rgb/normal/png/SDO/exploit.png) | ![](output_files/rgb/round/png/SDO/exploit.png) | ![](output_files/black/normal/png/SDO/exploit.png) | ![](output_files/black/round/png/SDO/exploit.png) | ![](output_files/white/normal/png/SDO/exploit.png) | ![](output_files/white/round/png/SDO/exploit.png) |
| x-mitre-detection-strategy | SDO | 0, 191, 255 | #00bfff | ![](output_files/rgb/normal/png/SDO/x-mitre-detection-strategy.png) | ![](output_files/rgb/round/png/SDO/x-mitre-detection-strategy.png) | ![](output_files/black/normal/png/SDO/x-mitre-detection-strategy.png) | ![](output_files/black/round/png/SDO/x-mitre-detection-strategy.png) | ![](output_files/white/normal/png/SDO/x-mitre-detection-strategy.png) | ![](output_files/white/round/png/SDO/x-mitre-detection-strategy.png) |
| x-mitre-analytic | SDO | 255, 61, 0 | #ff3d00 | ![](output_files/rgb/normal/png/SDO/x-mitre-analytic.png) | ![](output_files/rgb/round/png/SDO/x-mitre-analytic.png) | ![](output_files/black/normal/png/SDO/x-mitre-analytic.png) | ![](output_files/black/round/png/SDO/x-mitre-analytic.png) | ![](output_files/white/normal/png/SDO/x-mitre-analytic.png) | ![](output_files/white/round/png/SDO/x-mitre-analytic.png) |
| x-mitre-log-source | SDO | 72, 61, 139 | #483d8b | ![](output_files/rgb/normal/png/SDO/x-mitre-log-source.png) | ![](output_files/rgb/round/png/SDO/x-mitre-log-source.png) | ![](output_files/black/normal/png/SDO/x-mitre-log-source.png) | ![](output_files/black/round/png/SDO/x-mitre-log-source.png) | ![](output_files/white/normal/png/SDO/x-mitre-log-source.png) | ![](output_files/white/round/png/SDO/x-mitre-log-source.png) |
| x-mitre-tactic | SDO | 198, 40, 40 | #c62828 | ![](output_files/rgb/normal/png/SDO/x-mitre-tactic.png) | ![](output_files/rgb/round/png/SDO/x-mitre-tactic.png) | ![](output_files/black/normal/png/SDO/x-mitre-tactic.png) | ![](output_files/black/round/png/SDO/x-mitre-tactic.png) | ![](output_files/white/normal/png/SDO/x-mitre-tactic.png) | ![](output_files/white/round/png/SDO/x-mitre-tactic.png) |
| x-mitre-asset | SDO | 0, 255, 127 | #00ff7f | ![](output_files/rgb/normal/png/SDO/x-mitre-asset.png) | ![](output_files/rgb/round/png/SDO/x-mitre-asset.png) | ![](output_files/black/normal/png/SDO/x-mitre-asset.png) | ![](output_files/black/round/png/SDO/x-mitre-asset.png) | ![](output_files/white/normal/png/SDO/x-mitre-asset.png) | ![](output_files/white/round/png/SDO/x-mitre-asset.png) |
| x-mitre-data-source | SDO | 0, 188, 212 | #00bcd4 | ![](output_files/rgb/normal/png/SDO/x-mitre-data-source.png) | ![](output_files/rgb/round/png/SDO/x-mitre-data-source.png) | ![](output_files/black/normal/png/SDO/x-mitre-data-source.png) | ![](output_files/black/round/png/SDO/x-mitre-data-source.png) | ![](output_files/white/normal/png/SDO/x-mitre-data-source.png) | ![](output_files/white/round/png/SDO/x-mitre-data-source.png) |
| x-mitre-data-component | SDO | 63, 81, 181 | #3f51b5 | ![](output_files/rgb/normal/png/SDO/x-mitre-data-component.png) | ![](output_files/rgb/round/png/SDO/x-mitre-data-component.png) | ![](output_files/black/normal/png/SDO/x-mitre-data-component.png) | ![](output_files/black/round/png/SDO/x-mitre-data-component.png) | ![](output_files/white/normal/png/SDO/x-mitre-data-component.png) | ![](output_files/white/round/png/SDO/x-mitre-data-component.png) |
| attack-flow | SDO | 156, 39, 176 | #9c27b0 | ![](output_files/rgb/normal/png/SDO/attack-flow.png) | ![](output_files/rgb/round/png/SDO/attack-flow.png) | ![](output_files/black/normal/png/SDO/attack-flow.png) | ![](output_files/black/round/png/SDO/attack-flow.png) | ![](output_files/white/normal/png/SDO/attack-flow.png) | ![](output_files/white/round/png/SDO/attack-flow.png) |
| attack-action | SDO | 0, 105, 92 | #00695c | ![](output_files/rgb/normal/png/SDO/attack-action.png) | ![](output_files/rgb/round/png/SDO/attack-action.png) | ![](output_files/black/normal/png/SDO/attack-action.png) | ![](output_files/black/round/png/SDO/attack-action.png) | ![](output_files/white/normal/png/SDO/attack-action.png) | ![](output_files/white/round/png/SDO/attack-action.png) |
| artifact | sco | 149,229,250 | #95e5fa | ![](output_files/rgb/normal/png/sco/artifact.png) | ![](output_files/rgb/round/png/sco/artifact.png) | ![](output_files/black/normal/png/sco/artifact.png) | ![](output_files/black/round/png/sco/artifact.png) | ![](output_files/white/normal/png/sco/artifact.png) | ![](output_files/white/round/png/sco/artifact.png) |
| autonomous-system | sco | 161,248,128 | #a1f880 | ![](output_files/rgb/normal/png/sco/autonomous-system.png) | ![](output_files/rgb/round/png/sco/autonomous-system.png) | ![](output_files/black/normal/png/sco/autonomous-system.png) | ![](output_files/black/round/png/sco/autonomous-system.png) | ![](output_files/white/normal/png/sco/autonomous-system.png) | ![](output_files/white/round/png/sco/autonomous-system.png) |
| directory | sco | 183,245,206 | #b7f5ce | ![](output_files/rgb/normal/png/sco/directory.png) | ![](output_files/rgb/round/png/sco/directory.png) | ![](output_files/black/normal/png/sco/directory.png) | ![](output_files/black/round/png/sco/directory.png) | ![](output_files/white/normal/png/sco/directory.png) | ![](output_files/white/round/png/sco/directory.png) |
| domain-name | sco | 255,185,167 | #ffb9a7 | ![](output_files/rgb/normal/png/sco/domain-name.png) | ![](output_files/rgb/round/png/sco/domain-name.png) | ![](output_files/black/normal/png/sco/domain-name.png) | ![](output_files/black/round/png/sco/domain-name.png) | ![](output_files/white/normal/png/sco/domain-name.png) | ![](output_files/white/round/png/sco/domain-name.png) |
| email-addr | sco | 186,168,250 | #baa8fa | ![](output_files/rgb/normal/png/sco/email-addr.png) | ![](output_files/rgb/round/png/sco/email-addr.png) | ![](output_files/black/normal/png/sco/email-addr.png) | ![](output_files/black/round/png/sco/email-addr.png) | ![](output_files/white/normal/png/sco/email-addr.png) | ![](output_files/white/round/png/sco/email-addr.png) |
| email-message | sco | 249,177,233 | #f9b1e9 | ![](output_files/rgb/normal/png/sco/email-message.png) | ![](output_files/rgb/round/png/sco/email-message.png) | ![](output_files/black/normal/png/sco/email-message.png) | ![](output_files/black/round/png/sco/email-message.png) | ![](output_files/white/normal/png/sco/email-message.png) | ![](output_files/white/round/png/sco/email-message.png) |
| file | sco | 199,148,187 | #c794bb | ![](output_files/rgb/normal/png/sco/file.png) | ![](output_files/rgb/round/png/sco/file.png) | ![](output_files/black/normal/png/sco/file.png) | ![](output_files/black/round/png/sco/file.png) | ![](output_files/white/normal/png/sco/file.png) | ![](output_files/white/round/png/sco/file.png) |
| ipv4-addr | sco | 222,130,171 | #de82ab | ![](output_files/rgb/normal/png/sco/ipv4-addr.png) | ![](output_files/rgb/round/png/sco/ipv4-addr.png) | ![](output_files/black/normal/png/sco/ipv4-addr.png) | ![](output_files/black/round/png/sco/ipv4-addr.png) | ![](output_files/white/normal/png/sco/ipv4-addr.png) | ![](output_files/white/round/png/sco/ipv4-addr.png) |
| ipv6-addr | sco | 222,130,171 | #de82ab | ![](output_files/rgb/normal/png/sco/ipv6-addr.png) | ![](output_files/rgb/round/png/sco/ipv6-addr.png) | ![](output_files/black/normal/png/sco/ipv6-addr.png) | ![](output_files/black/round/png/sco/ipv6-addr.png) | ![](output_files/white/normal/png/sco/ipv6-addr.png) | ![](output_files/white/round/png/sco/ipv6-addr.png) |
| mac-addr | sco | 247,184,203 | #f7b8cb | ![](output_files/rgb/normal/png/sco/mac-addr.png) | ![](output_files/rgb/round/png/sco/mac-addr.png) | ![](output_files/black/normal/png/sco/mac-addr.png) | ![](output_files/black/round/png/sco/mac-addr.png) | ![](output_files/white/normal/png/sco/mac-addr.png) | ![](output_files/white/round/png/sco/mac-addr.png) |
| mutex | sco | 240,228,153 | #f0e499 | ![](output_files/rgb/normal/png/sco/mutex.png) | ![](output_files/rgb/round/png/sco/mutex.png) | ![](output_files/black/normal/png/sco/mutex.png) | ![](output_files/black/round/png/sco/mutex.png) | ![](output_files/white/normal/png/sco/mutex.png) | ![](output_files/white/round/png/sco/mutex.png) |
| network-traffic | sco | 132,207,240 | #84cff0 | ![](output_files/rgb/normal/png/sco/network-traffic.png) | ![](output_files/rgb/round/png/sco/network-traffic.png) | ![](output_files/black/normal/png/sco/network-traffic.png) | ![](output_files/black/round/png/sco/network-traffic.png) | ![](output_files/white/normal/png/sco/network-traffic.png) | ![](output_files/white/round/png/sco/network-traffic.png) |
| process | sco | 187,199,153 | #bbc799 | ![](output_files/rgb/normal/png/sco/process.png) | ![](output_files/rgb/round/png/sco/process.png) | ![](output_files/black/normal/png/sco/process.png) | ![](output_files/black/round/png/sco/process.png) | ![](output_files/white/normal/png/sco/process.png) | ![](output_files/white/round/png/sco/process.png) |
| software | sco | 233,145,202 | #e991ca | ![](output_files/rgb/normal/png/sco/software.png) | ![](output_files/rgb/round/png/sco/software.png) | ![](output_files/black/normal/png/sco/software.png) | ![](output_files/black/round/png/sco/software.png) | ![](output_files/white/normal/png/sco/software.png) | ![](output_files/white/round/png/sco/software.png) |
| url | sco | 206,207,241 | #cecff1 | ![](output_files/rgb/normal/png/sco/url.png) | ![](output_files/rgb/round/png/sco/url.png) | ![](output_files/black/normal/png/sco/url.png) | ![](output_files/black/round/png/sco/url.png) | ![](output_files/white/normal/png/sco/url.png) | ![](output_files/white/round/png/sco/url.png) |
| user-account | sco | 213,191,132 | #d5bf84 | ![](output_files/rgb/normal/png/sco/user-account.png) | ![](output_files/rgb/round/png/sco/user-account.png) | ![](output_files/black/normal/png/sco/user-account.png) | ![](output_files/black/round/png/sco/user-account.png) | ![](output_files/white/normal/png/sco/user-account.png) | ![](output_files/white/round/png/sco/user-account.png) |
| windows-registry-key | sco | 132,196,170 | #84c4aa | ![](output_files/rgb/normal/png/sco/windows-registry-key.png) | ![](output_files/rgb/round/png/sco/windows-registry-key.png) | ![](output_files/black/normal/png/sco/windows-registry-key.png) | ![](output_files/black/round/png/sco/windows-registry-key.png) | ![](output_files/white/normal/png/sco/windows-registry-key.png) | ![](output_files/white/round/png/sco/windows-registry-key.png) |
| x509-certificate | sco | 246,160,242 | #f6a0f2 | ![](output_files/rgb/normal/png/sco/x509-certificate.png) | ![](output_files/rgb/round/png/sco/x509-certificate.png) | ![](output_files/black/normal/png/sco/x509-certificate.png) | ![](output_files/black/round/png/sco/x509-certificate.png) | ![](output_files/white/normal/png/sco/x509-certificate.png) | ![](output_files/white/round/png/sco/x509-certificate.png) |
| bank-account | sco | 232,228,170 | #e8e4aa | ![](output_files/rgb/normal/png/sco/bank-account.png) | ![](output_files/rgb/round/png/sco/bank-account.png) | ![](output_files/black/normal/png/sco/bank-account.png) | ![](output_files/black/round/png/sco/bank-account.png) | ![](output_files/white/normal/png/sco/bank-account.png) | ![](output_files/white/round/png/sco/bank-account.png) |
| bank-card | sco | 145,178,181 | #91b2b5 | ![](output_files/rgb/normal/png/sco/bank-card.png) | ![](output_files/rgb/round/png/sco/bank-card.png) | ![](output_files/black/normal/png/sco/bank-card.png) | ![](output_files/black/round/png/sco/bank-card.png) | ![](output_files/white/normal/png/sco/bank-card.png) | ![](output_files/white/round/png/sco/bank-card.png) |
| cryptocurrency-transaction | sco | 222,233,167 | #dee9a7 | ![](output_files/rgb/normal/png/sco/cryptocurrency-transaction.png) | ![](output_files/rgb/round/png/sco/cryptocurrency-transaction.png) | ![](output_files/black/normal/png/sco/cryptocurrency-transaction.png) | ![](output_files/black/round/png/sco/cryptocurrency-transaction.png) | ![](output_files/white/normal/png/sco/cryptocurrency-transaction.png) | ![](output_files/white/round/png/sco/cryptocurrency-transaction.png) |
| cryptocurrency-wallet | sco | 156,218,184 | #9cdab8 | ![](output_files/rgb/normal/png/sco/cryptocurrency-wallet.png) | ![](output_files/rgb/round/png/sco/cryptocurrency-wallet.png) | ![](output_files/black/normal/png/sco/cryptocurrency-wallet.png) | ![](output_files/black/round/png/sco/cryptocurrency-wallet.png) | ![](output_files/white/normal/png/sco/cryptocurrency-wallet.png) | ![](output_files/white/round/png/sco/cryptocurrency-wallet.png) |
| cryptocurrency-exchange | sco | 173,205,255 | #adcdff | ![](output_files/rgb/normal/png/sco/cryptocurrency-exchange.png) | ![](output_files/rgb/round/png/sco/cryptocurrency-exchange.png) | ![](output_files/black/normal/png/sco/cryptocurrency-exchange.png) | ![](output_files/black/round/png/sco/cryptocurrency-exchange.png) | ![](output_files/white/normal/png/sco/cryptocurrency-exchange.png) | ![](output_files/white/round/png/sco/cryptocurrency-exchange.png) |
| phone-number | sco | 226,189,239 | #e2bdef | ![](output_files/rgb/normal/png/sco/phone-number.png) | ![](output_files/rgb/round/png/sco/phone-number.png) | ![](output_files/black/normal/png/sco/phone-number.png) | ![](output_files/black/round/png/sco/phone-number.png) | ![](output_files/white/normal/png/sco/phone-number.png) | ![](output_files/white/round/png/sco/phone-number.png) |
| user-agent | sco | 152,199,239 | #98c7ef | ![](output_files/rgb/normal/png/sco/user-agent.png) | ![](output_files/rgb/round/png/sco/user-agent.png) | ![](output_files/black/normal/png/sco/user-agent.png) | ![](output_files/black/round/png/sco/user-agent.png) | ![](output_files/white/normal/png/sco/user-agent.png) | ![](output_files/white/round/png/sco/user-agent.png) |
| relationship | sro | 255, 20, 147 | #ff1493 | ![](output_files/rgb/normal/png/sro/relationship.png) | ![](output_files/rgb/round/png/sro/relationship.png) | ![](output_files/black/normal/png/sro/relationship.png) | ![](output_files/black/round/png/sro/relationship.png) | ![](output_files/white/normal/png/sro/relationship.png) | ![](output_files/white/round/png/sro/relationship.png) |
| sighting | sro | 57, 255, 20 | #39ff14 | ![](output_files/rgb/normal/png/sro/sighting.png) | ![](output_files/rgb/round/png/sro/sighting.png) | ![](output_files/black/normal/png/sro/sighting.png) | ![](output_files/black/round/png/sro/sighting.png) | ![](output_files/white/normal/png/sro/sighting.png) | ![](output_files/white/round/png/sro/sighting.png) |
| extension-definition | smo | 224,224,224 | #e0e0e0 | ![](output_files/rgb/normal/png/smo/extension-definition.png) | ![](output_files/rgb/round/png/smo/extension-definition.png) | ![](output_files/black/normal/png/smo/extension-definition.png) | ![](output_files/black/round/png/smo/extension-definition.png) | ![](output_files/white/normal/png/smo/extension-definition.png) | ![](output_files/white/round/png/smo/extension-definition.png) |
| marking-definition | smo | 158,158,158 | #9e9e9e | ![](output_files/rgb/normal/png/smo/marking-definition.png) | ![](output_files/rgb/round/png/smo/marking-definition.png) | ![](output_files/black/normal/png/smo/marking-definition.png) | ![](output_files/black/round/png/smo/marking-definition.png) | ![](output_files/white/normal/png/smo/marking-definition.png) | ![](output_files/white/round/png/smo/marking-definition.png) |
| language-content | smo | 97,97,97 | #616161 | ![](output_files/rgb/normal/png/smo/language-content.png) | ![](output_files/rgb/round/png/smo/language-content.png) | ![](output_files/black/normal/png/smo/language-content.png) | ![](output_files/black/round/png/smo/language-content.png) | ![](output_files/white/normal/png/smo/language-content.png) | ![](output_files/white/round/png/smo/language-content.png) |

## Adding your own objects

To start with, clone this repository.

```shell
# clone the latest code
git clone https://github.com/muchdogesec/stix2icons
# create a venv
cd stix2icons
python3 -m venv stix2icons-venv
source stix2icons-venv/bin/activate
# install requirements
pip3 install -r requirements.txt
```

The `input_vectors` contains vector files (`.svg`s) used to automatically generate types/colours/sizrs in `output_files`. The `input_vectors` directory is structured as follows;

```txt
input_vectors/
├── normal/
│   ├── sco/
│   ├── sdo/
│   ├── smo/
│   └── sro/
└── round/
    ├── sco/
    ├── sdo/
    ├── smo/
    └── sro/
```

Where `sco`, `sdo`, `smo` or `sro` is the type of STIX object.

When adding objects you should:

* place it in the the correct type directory (e.g. `sdo`)
* supply both a `normal` and `round` variation.
* keep your `svg` files as simple as possible, using only `paths`, `rect`, `circle`, and `ellipse` tags. This is because the `output_files` are generated automatically and the script that performs the generation is only smart enough to handle these types.

Once you have added a `normal` and `round` variation of your object you need to add an entry for it in `generate_icons.py` under `objects` in the format;

```json
{"object": "<STIX OBJECT>", "type": "<TYPE>", "colour_rgb": "<COLOUR IN R,G,B>"}
```

e.g.

```json
{"object": "attack-pattern", "type": "SDO", "colour_rgb": "34,119,181"},
```

Once done, you can then run the script;

```shell
python3 generate_icons.py
```

This will generate a black, white and colour version of your object as an `svg` and `png` (256x256).

If you want us to publish your icon in this repository for everyone to use, make a pull request after following all the steps above.

## Credits

* [This work is an expansion of the STIX objects created by EclecticIQ](https://github.com/eclecticiq/stix-icons/)
* [It is also heavily inspired by this work from Bret Jordan](https://github.com/freetaxii/stix2-graphics)

## Support

[Minimal support provided via the DOGESEC community](https://community.dogesec.com/).

## Licenses

* Code: [Apache 2.0](/LICENSE)
* Content: [Creative Commons Attribution 4.0 International Public License](/LICENSE-CONTENT)