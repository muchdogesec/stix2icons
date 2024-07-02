# STIX Icons

## Overview

stix-icons is a collection of icons that represent all the of core STIX objects. The aim is to provide a central source of icons that can be used to represent STIX objects by software tools (or anything else).

This repo is designed so that new icons can be added for custom STIX objects you're developing. See: "Adding your own objects"

## Where to find icons in this repository

The icons are provided in three colour versions: color, black, and white.

There are two variations of each colour provided: with (normal) and without a 'circle' (round) behind the icons.

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

| Object | Type | RGB | RGBCircle | Black | BlackCircle | White | WhiteCircle |
|--------|------|-----|-----------|-------|-------------|-------|-------------|
| attack-pattern | sdo | ![](output_files/rgb/normal/png/attack-pattern.png) | ![](output_files/rgb/round/png/attack-pattern.png) | ![](output_files/black/normal/png/attack-pattern.png) | ![](output_files/black/round/png/attack-pattern.png) | ![](output_files/white/normal/png/attack-pattern.png) | ![](output_files/white/round/png/attack-pattern.png) |
| campaign | sdo | ![](output_files/rgb/normal/png/campaign.png) | ![](output_files/rgb/round/png/campaign.png) | ![](output_files/black/normal/png/campaign.png) | ![](output_files/black/round/png/campaign.png) | ![](output_files/white/normal/png/campaign.png) | ![](output_files/white/round/png/campaign.png) |
| course-of-action | sdo | ![](output_files/rgb/normal/png/course-of-action.png) | ![](output_files/rgb/round/png/course-of-action.png) | ![](output_files/black/normal/png/course-of-action.png) | ![](output_files/black/round/png/course-of-action.png) | ![](output_files/white/normal/png/course-of-action.png) | ![](output_files/white/round/png/course-of-action.png) |
| grouping | sdo | ![](output_files/rgb/normal/png/grouping.png) | ![](output_files/rgb/round/png/grouping.png) | ![](output_files/black/normal/png/grouping.png) | ![](output_files/black/round/png/grouping.png) | ![](output_files/white/normal/png/grouping.png) | ![](output_files/white/round/png/grouping.png) |
| identity | sdo | ![](output_files/rgb/normal/png/identity.png) | ![](output_files/rgb/round/png/identity.png) | ![](output_files/black/normal/png/identity.png) | ![](output_files/black/round/png/identity.png) | ![](output_files/white/normal/png/identity.png) | ![](output_files/white/round/png/identity.png) |
| identity_group | sdo | ![](output_files/rgb/normal/png/identity_group.png) | ![](output_files/rgb/round/png/identity_group.png) | ![](output_files/black/normal/png/identity_group.png) | ![](output_files/black/round/png/identity_group.png) | ![](output_files/white/normal/png/identity_group.png) | ![](output_files/white/round/png/identity_group.png) |
| identity_system | sdo | ![](output_files/rgb/normal/png/identity_system.png) | ![](output_files/rgb/round/png/identity_system.png) | ![](output_files/black/normal/png/identity_system.png) | ![](output_files/black/round/png/identity_system.png) | ![](output_files/white/normal/png/identity_system.png) | ![](output_files/white/round/png/identity_system.png) |
| identity_organization | sdo | ![](output_files/rgb/normal/png/identity_organization.png) | ![](output_files/rgb/round/png/identity_organization.png) | ![](output_files/black/normal/png/identity_organization.png) | ![](output_files/black/round/png/identity_organization.png) | ![](output_files/white/normal/png/identity_organization.png) | ![](output_files/white/round/png/identity_organization.png) |
| identity_individual | sdo | ![](output_files/rgb/normal/png/identity_individual.png) | ![](output_files/rgb/round/png/identity_individual.png) | ![](output_files/black/normal/png/identity_individual.png) | ![](output_files/black/round/png/identity_individual.png) | ![](output_files/white/normal/png/identity_individual.png) | ![](output_files/white/round/png/identity_individual.png) |
| identity_class | sdo | ![](output_files/rgb/normal/png/identity_class.png) | ![](output_files/rgb/round/png/identity_class.png) | ![](output_files/black/normal/png/identity_class.png) | ![](output_files/black/round/png/identity_class.png) | ![](output_files/white/normal/png/identity_class.png) | ![](output_files/white/round/png/identity_class.png) |
| incident | sdo | ![](output_files/rgb/normal/png/incident.png) | ![](output_files/rgb/round/png/incident.png) | ![](output_files/black/normal/png/incident.png) | ![](output_files/black/round/png/incident.png) | ![](output_files/white/normal/png/incident.png) | ![](output_files/white/round/png/incident.png) |
| indicator | sdo | ![](output_files/rgb/normal/png/indicator.png) | ![](output_files/rgb/round/png/indicator.png) | ![](output_files/black/normal/png/indicator.png) | ![](output_files/black/round/png/indicator.png) | ![](output_files/white/normal/png/indicator.png) | ![](output_files/white/round/png/indicator.png) |
| infrastructure | sdo | ![](output_files/rgb/normal/png/infrastructure.png) | ![](output_files/rgb/round/png/infrastructure.png) | ![](output_files/black/normal/png/infrastructure.png) | ![](output_files/black/round/png/infrastructure.png) | ![](output_files/white/normal/png/infrastructure.png) | ![](output_files/white/round/png/infrastructure.png) |
| intrusion-set | sdo | ![](output_files/rgb/normal/png/intrusion-set.png) | ![](output_files/rgb/round/png/intrusion-set.png) | ![](output_files/black/normal/png/intrusion-set.png) | ![](output_files/black/round/png/intrusion-set.png) | ![](output_files/white/normal/png/intrusion-set.png) | ![](output_files/white/round/png/intrusion-set.png) |
| location | sdo | ![](output_files/rgb/normal/png/location.png) | ![](output_files/rgb/round/png/location.png) | ![](output_files/black/normal/png/location.png) | ![](output_files/black/round/png/location.png) | ![](output_files/white/normal/png/location.png) | ![](output_files/white/round/png/location.png) |
| malware | sdo | ![](output_files/rgb/normal/png/malware.png) | ![](output_files/rgb/round/png/malware.png) | ![](output_files/black/normal/png/malware.png) | ![](output_files/black/round/png/malware.png) | ![](output_files/white/normal/png/malware.png) | ![](output_files/white/round/png/malware.png) |
| malware_family | sdo | ![](output_files/rgb/normal/png/malware_family.png) | ![](output_files/rgb/round/png/malware_family.png) | ![](output_files/black/normal/png/malware_family.png) | ![](output_files/black/round/png/malware_family.png) | ![](output_files/white/normal/png/malware_family.png) | ![](output_files/white/round/png/malware_family.png) |
| malware-analysis | sdo | ![](output_files/rgb/normal/png/malware-analysis.png) | ![](output_files/rgb/round/png/malware-analysis.png) | ![](output_files/black/normal/png/malware-analysis.png) | ![](output_files/black/round/png/malware-analysis.png) | ![](output_files/white/normal/png/malware-analysis.png) | ![](output_files/white/round/png/malware-analysis.png) |
| note | sdo | ![](output_files/rgb/normal/png/note.png) | ![](output_files/rgb/round/png/note.png) | ![](output_files/black/normal/png/note.png) | ![](output_files/black/round/png/note.png) | ![](output_files/white/normal/png/note.png) | ![](output_files/white/round/png/note.png) |
| observed-data | sdo | ![](output_files/rgb/normal/png/observed-data.png) | ![](output_files/rgb/round/png/observed-data.png) | ![](output_files/black/normal/png/observed-data.png) | ![](output_files/black/round/png/observed-data.png) | ![](output_files/white/normal/png/observed-data.png) | ![](output_files/white/round/png/observed-data.png) |
| opinion | sdo | ![](output_files/rgb/normal/png/opinion.png) | ![](output_files/rgb/round/png/opinion.png) | ![](output_files/black/normal/png/opinion.png) | ![](output_files/black/round/png/opinion.png) | ![](output_files/white/normal/png/opinion.png) | ![](output_files/white/round/png/opinion.png) |
| report | sdo | ![](output_files/rgb/normal/png/report.png) | ![](output_files/rgb/round/png/report.png) | ![](output_files/black/normal/png/report.png) | ![](output_files/black/round/png/report.png) | ![](output_files/white/normal/png/report.png) | ![](output_files/white/round/png/report.png) |
| threat-actor | sdo | ![](output_files/rgb/normal/png/threat-actor.png) | ![](output_files/rgb/round/png/threat-actor.png) | ![](output_files/black/normal/png/threat-actor.png) | ![](output_files/black/round/png/threat-actor.png) | ![](output_files/white/normal/png/threat-actor.png) | ![](output_files/white/round/png/threat-actor.png) |
| tool | sdo | ![](output_files/rgb/normal/png/tool.png) | ![](output_files/rgb/round/png/tool.png) | ![](output_files/black/normal/png/tool.png) | ![](output_files/black/round/png/tool.png) | ![](output_files/white/normal/png/tool.png) | ![](output_files/white/round/png/tool.png) |
| vulnerability | sdo | ![](output_files/rgb/normal/png/vulnerability.png) | ![](output_files/rgb/round/png/vulnerability.png) | ![](output_files/black/normal/png/vulnerability.png) | ![](output_files/black/round/png/vulnerability.png) | ![](output_files/white/normal/png/vulnerability.png) | ![](output_files/white/round/png/vulnerability.png) |
| weakness | sdo | ![](output_files/rgb/normal/png/weakness.png) | ![](output_files/rgb/round/png/weakness.png) | ![](output_files/black/normal/png/weakness.png) | ![](output_files/black/round/png/weakness.png) | ![](output_files/white/normal/png/weakness.png) | ![](output_files/white/round/png/weakness.png) |
| artifact | sco | ![](output_files/rgb/normal/png/artifact.png) | ![](output_files/rgb/round/png/artifact.png) | ![](output_files/black/normal/png/artifact.png) | ![](output_files/black/round/png/artifact.png) | ![](output_files/white/normal/png/artifact.png) | ![](output_files/white/round/png/artifact.png) |
| autonomous-system | sco | ![](output_files/rgb/normal/png/autonomous-system.png) | ![](output_files/rgb/round/png/autonomous-system.png) | ![](output_files/black/normal/png/autonomous-system.png) | ![](output_files/black/round/png/autonomous-system.png) | ![](output_files/white/normal/png/autonomous-system.png) | ![](output_files/white/round/png/autonomous-system.png) |
| directory | sco | ![](output_files/rgb/normal/png/directory.png) | ![](output_files/rgb/round/png/directory.png) | ![](output_files/black/normal/png/directory.png) | ![](output_files/black/round/png/directory.png) | ![](output_files/white/normal/png/directory.png) | ![](output_files/white/round/png/directory.png) |
| domain-name | sco | ![](output_files/rgb/normal/png/domain-name.png) | ![](output_files/rgb/round/png/domain-name.png) | ![](output_files/black/normal/png/domain-name.png) | ![](output_files/black/round/png/domain-name.png) | ![](output_files/white/normal/png/domain-name.png) | ![](output_files/white/round/png/domain-name.png) |
| email-addr | sco | ![](output_files/rgb/normal/png/email-addr.png) | ![](output_files/rgb/round/png/email-addr.png) | ![](output_files/black/normal/png/email-addr.png) | ![](output_files/black/round/png/email-addr.png) | ![](output_files/white/normal/png/email-addr.png) | ![](output_files/white/round/png/email-addr.png) |
| email-message | sco | ![](output_files/rgb/normal/png/email-message.png) | ![](output_files/rgb/round/png/email-message.png) | ![](output_files/black/normal/png/email-message.png) | ![](output_files/black/round/png/email-message.png) | ![](output_files/white/normal/png/email-message.png) | ![](output_files/white/round/png/email-message.png) |
| file | sco | ![](output_files/rgb/normal/png/file.png) | ![](output_files/rgb/round/png/file.png) | ![](output_files/black/normal/png/file.png) | ![](output_files/black/round/png/file.png) | ![](output_files/white/normal/png/file.png) | ![](output_files/white/round/png/file.png) |
| ipv4-addr | sco | ![](output_files/rgb/normal/png/ipv4-addr.png) | ![](output_files/rgb/round/png/ipv4-addr.png) | ![](output_files/black/normal/png/ipv4-addr.png) | ![](output_files/black/round/png/ipv4-addr.png) | ![](output_files/white/normal/png/ipv4-addr.png) | ![](output_files/white/round/png/ipv4-addr.png) |
| ipv6-addr | sco | ![](output_files/rgb/normal/png/ipv6-addr.png) | ![](output_files/rgb/round/png/ipv6-addr.png) | ![](output_files/black/normal/png/ipv6-addr.png) | ![](output_files/black/round/png/ipv6-addr.png) | ![](output_files/white/normal/png/ipv6-addr.png) | ![](output_files/white/round/png/ipv6-addr.png) |
| mac-addr | sco | ![](output_files/rgb/normal/png/mac-addr.png) | ![](output_files/rgb/round/png/mac-addr.png) | ![](output_files/black/normal/png/mac-addr.png) | ![](output_files/black/round/png/mac-addr.png) | ![](output_files/white/normal/png/mac-addr.png) | ![](output_files/white/round/png/mac-addr.png) |
| mutex | sco | ![](output_files/rgb/normal/png/mutex.png) | ![](output_files/rgb/round/png/mutex.png) | ![](output_files/black/normal/png/mutex.png) | ![](output_files/black/round/png/mutex.png) | ![](output_files/white/normal/png/mutex.png) | ![](output_files/white/round/png/mutex.png) |
| network-traffic | sco | ![](output_files/rgb/normal/png/network-traffic.png) | ![](output_files/rgb/round/png/network-traffic.png) | ![](output_files/black/normal/png/network-traffic.png) | ![](output_files/black/round/png/network-traffic.png) | ![](output_files/white/normal/png/network-traffic.png) | ![](output_files/white/round/png/network-traffic.png) |
| process | sco | ![](output_files/rgb/normal/png/process.png) | ![](output_files/rgb/round/png/process.png) | ![](output_files/black/normal/png/process.png) | ![](output_files/black/round/png/process.png) | ![](output_files/white/normal/png/process.png) | ![](output_files/white/round/png/process.png) |
| software | sco | ![](output_files/rgb/normal/png/software.png) | ![](output_files/rgb/round/png/software.png) | ![](output_files/black/normal/png/software.png) | ![](output_files/black/round/png/software.png) | ![](output_files/white/normal/png/software.png) | ![](output_files/white/round/png/software.png) |
| url | sco | ![](output_files/rgb/normal/png/url.png) | ![](output_files/rgb/round/png/url.png) | ![](output_files/black/normal/png/url.png) | ![](output_files/black/round/png/url.png) | ![](output_files/white/normal/png/url.png) | ![](output_files/white/round/png/url.png) |
| user-account | sco | ![](output_files/rgb/normal/png/user-account.png) | ![](output_files/rgb/round/png/user-account.png) | ![](output_files/black/normal/png/user-account.png) | ![](output_files/black/round/png/user-account.png) | ![](output_files/white/normal/png/user-account.png) | ![](output_files/white/round/png/user-account.png) |
| windows-registry-key | sco | ![](output_files/rgb/normal/png/windows-registry-key.png) | ![](output_files/rgb/round/png/windows-registry-key.png) | ![](output_files/black/normal/png/windows-registry-key.png) | ![](output_files/black/round/png/windows-registry-key.png) | ![](output_files/white/normal/png/windows-registry-key.png) | ![](output_files/white/round/png/windows-registry-key.png) |
| x509-certificate | sco | ![](output_files/rgb/normal/png/x509-certificate.png) | ![](output_files/rgb/round/png/x509-certificate.png) | ![](output_files/black/normal/png/x509-certificate.png) | ![](output_files/black/round/png/x509-certificate.png) | ![](output_files/white/normal/png/x509-certificate.png) | ![](output_files/white/round/png/x509-certificate.png) |
| bank-account | sco | ![](output_files/rgb/normal/png/bank-account.png) | ![](output_files/rgb/round/png/bank-account.png) | ![](output_files/black/normal/png/bank-account.png) | ![](output_files/black/round/png/bank-account.png) | ![](output_files/white/normal/png/bank-account.png) | ![](output_files/white/round/png/bank-account.png) |
| bank-card | sco | ![](output_files/rgb/normal/png/bank-card.png) | ![](output_files/rgb/round/png/bank-card.png) | ![](output_files/black/normal/png/bank-card.png) | ![](output_files/black/round/png/bank-card.png) | ![](output_files/white/normal/png/bank-card.png) | ![](output_files/white/round/png/bank-card.png) |
| cryptocurrency-transaction | sco | ![](output_files/rgb/normal/png/cryptocurrency-transaction.png) | ![](output_files/rgb/round/png/cryptocurrency-transaction.png) | ![](output_files/black/normal/png/cryptocurrency-transaction.png) | ![](output_files/black/round/png/cryptocurrency-transaction.png) | ![](output_files/white/normal/png/cryptocurrency-transaction.png) | ![](output_files/white/round/png/cryptocurrency-transaction.png) |
| cryptocurrency-wallet | sco | ![](output_files/rgb/normal/png/cryptocurrency-wallet.png) | ![](output_files/rgb/round/png/cryptocurrency-wallet.png) | ![](output_files/black/normal/png/cryptocurrency-wallet.png) | ![](output_files/black/round/png/cryptocurrency-wallet.png) | ![](output_files/white/normal/png/cryptocurrency-wallet.png) | ![](output_files/white/round/png/cryptocurrency-wallet.png) |
| phone-number | sco | ![](output_files/rgb/normal/png/phone-number.png) | ![](output_files/rgb/round/png/phone-number.png) | ![](output_files/black/normal/png/phone-number.png) | ![](output_files/black/round/png/phone-number.png) | ![](output_files/white/normal/png/phone-number.png) | ![](output_files/white/round/png/phone-number.png) |
| user-agent | sco | ![](output_files/rgb/normal/png/user-agent.png) | ![](output_files/rgb/round/png/user-agent.png) | ![](output_files/black/normal/png/user-agent.png) | ![](output_files/black/round/png/user-agent.png) | ![](output_files/white/normal/png/user-agent.png) | ![](output_files/white/round/png/user-agent.png) |
| relationship | sro | ![](output_files/rgb/normal/png/relationship.png) | ![](output_files/rgb/round/png/relationship.png) | ![](output_files/black/normal/png/relationship.png) | ![](output_files/black/round/png/relationship.png) | ![](output_files/white/normal/png/relationship.png) | ![](output_files/white/round/png/relationship.png) |
| sighting | sro | ![](output_files/rgb/normal/png/sighting.png) | ![](output_files/rgb/round/png/sighting.png) | ![](output_files/black/normal/png/sighting.png) | ![](output_files/black/round/png/sighting.png) | ![](output_files/white/normal/png/sighting.png) | ![](output_files/white/round/png/sighting.png) |
| language-content | smo | ![](output_files/rgb/normal/png/language-content.png) | ![](output_files/rgb/round/png/language-content.png) | ![](output_files/black/normal/png/language-content.png) | ![](output_files/black/round/png/language-content.png) | ![](output_files/white/normal/png/language-content.png) | ![](output_files/white/round/png/language-content.png) |
| marking-definition | smo | ![](output_files/rgb/normal/png/marking-definition.png) | ![](output_files/rgb/round/png/marking-definition.png) | ![](output_files/black/normal/png/marking-definition.png) | ![](output_files/black/round/png/marking-definition.png) | ![](output_files/white/normal/png/marking-definition.png) | ![](output_files/white/round/png/marking-definition.png) |
| marking-definition_tlpv1_white | smo | ![](output_files/rgb/normal/png/marking-definition_tlpv1_white.png) | ![](output_files/rgb/round/png/marking-definition_tlpv1_white.png) | ![](output_files/black/normal/png/marking-definition_tlpv1_white.png) | ![](output_files/black/round/png/marking-definition_tlpv1_white.png) | ![](output_files/white/normal/png/marking-definition_tlpv1_white.png) | ![](output_files/white/round/png/marking-definition_tlpv1_white.png) |
| marking-definition_tlpv1_green | smo | ![](output_files/rgb/normal/png/marking-definition_tlpv1_green.png) | ![](output_files/rgb/round/png/marking-definition_tlpv1_green.png) | ![](output_files/black/normal/png/marking-definition_tlpv1_green.png) | ![](output_files/black/round/png/marking-definition_tlpv1_green.png) | ![](output_files/white/normal/png/marking-definition_tlpv1_green.png) | ![](output_files/white/round/png/marking-definition_tlpv1_green.png) |
| marking-definition_tlpv1_amber | smo | ![](output_files/rgb/normal/png/marking-definition_tlpv1_amber.png) | ![](output_files/rgb/round/png/marking-definition_tlpv1_amber.png) | ![](output_files/black/normal/png/marking-definition_tlpv1_amber.png) | ![](output_files/black/round/png/marking-definition_tlpv1_amber.png) | ![](output_files/white/normal/png/marking-definition_tlpv1_amber.png) | ![](output_files/white/round/png/marking-definition_tlpv1_amber.png) |
| marking-definition_tlpv1_red | smo | ![](output_files/rgb/normal/png/marking-definition_tlpv1_red.png) | ![](output_files/rgb/round/png/marking-definition_tlpv1_red.png) | ![](output_files/black/normal/png/marking-definition_tlpv1_red.png) | ![](output_files/black/round/png/marking-definition_tlpv1_red.png) | ![](output_files/white/normal/png/marking-definition_tlpv1_red.png) | ![](output_files/white/round/png/marking-definition_tlpv1_red.png) |
| marking-definition_tlpv2_clear | smo | ![](output_files/rgb/normal/png/marking-definition_tlpv2_clear.png) | ![](output_files/rgb/round/png/marking-definition_tlpv2_clear.png) | ![](output_files/black/normal/png/marking-definition_tlpv2_clear.png) | ![](output_files/black/round/png/marking-definition_tlpv2_clear.png) | ![](output_files/white/normal/png/marking-definition_tlpv2_clear.png) | ![](output_files/white/round/png/marking-definition_tlpv2_clear.png) |
| marking-definition_tlpv2_green | smo | ![](output_files/rgb/normal/png/marking-definition_tlpv2_green.png) | ![](output_files/rgb/round/png/marking-definition_tlpv2_green.png) | ![](output_files/black/normal/png/marking-definition_tlpv2_green.png) | ![](output_files/black/round/png/marking-definition_tlpv2_green.png) | ![](output_files/white/normal/png/marking-definition_tlpv2_green.png) | ![](output_files/white/round/png/marking-definition_tlpv2_green.png) |
| marking-definition_tlpv2_amber | smo | ![](output_files/rgb/normal/png/marking-definition_tlpv2_amber.png) | ![](output_files/rgb/round/png/marking-definition_tlpv2_amber.png) | ![](output_files/black/normal/png/marking-definition_tlpv2_amber.png) | ![](output_files/black/round/png/marking-definition_tlpv2_amber.png) | ![](output_files/white/normal/png/marking-definition_tlpv2_amber.png) | ![](output_files/white/round/png/marking-definition_tlpv2_amber.png) |
| marking-definition_tlpv2_amber_strict | smo | ![](output_files/rgb/normal/png/marking-definition_tlpv2_amber_strict.png) | ![](output_files/rgb/round/png/marking-definition_tlpv2_amber_strict.png) | ![](output_files/black/normal/png/marking-definition_tlpv2_amber_strict.png) | ![](output_files/black/round/png/marking-definition_tlpv2_amber_strict.png) | ![](output_files/white/normal/png/marking-definition_tlpv2_amber_strict.png) | ![](output_files/white/round/png/marking-definition_tlpv2_amber_strict.png) |
| marking-definition_tlpv2_red | smo | ![](output_files/rgb/normal/png/marking-definition_tlpv2_red.png) | ![](output_files/rgb/round/png/marking-definition_tlpv2_red.png) | ![](output_files/black/normal/png/marking-definition_tlpv2_red.png) | ![](output_files/black/round/png/marking-definition_tlpv2_red.png) | ![](output_files/white/normal/png/marking-definition_tlpv2_red.png) | ![](output_files/white/round/png/marking-definition_tlpv2_red.png) |
| extension-definition | smo | ![](output_files/rgb/normal/png/extension-definition.png) | ![](output_files/rgb/round/png/extension-definition.png) | ![](output_files/black/normal/png/extension-definition.png) | ![](output_files/black/round/png/extension-definition.png) | ![](output_files/white/normal/png/extension-definition.png) | ![](output_files/white/round/png/extension-definition.png) |


## WIP

### SDOs

1. Weakness
  * https://www.flaticon.com/free-icon/link-break_58899?term=break&page=1&position=29&origin=search&related_id=58899

### SCOs

1. [Artifact Object](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_4jegwl6ojbes)
  * https://www.flaticon.com/free-icon/code_984196?term=code&page=1&position=29&origin=search&related_id=984196
2. [AS Object](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_27gux0aol9e3)
  * https://www.flaticon.com/free-icon/tag_7991247?term=tag&page=1&position=55&origin=search&related_id=7991247
3. [Directory Object](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_lyvpga5hlw52)
  * https://www.flaticon.com/free-icon/open-folder_10303584?term=directory&page=1&position=3&origin=search&related_id=10303584
4. [Domain Name Object](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_prhhksbxbg87)
  * https://www.flaticon.com/free-icon/domains_564917?term=domain&page=1&position=11&origin=search&related_id=564917
5. [Email Address Object](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_wmenahkvqmgj)
  * https://fontawesome.com/icons/at?f=classic&s=solid
6. [Email Message Object](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_grboc7sq5514)
  * https://fontawesome.com/icons/envelope?f=classic&s=solid
7. [File Object](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_99bl2dibcztv)
  * https://fontawesome.com/icons/file?f=classic&s=solid
8. [IPv4 Address Object](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_ki1ufj1ku8s0)
  * https://www.flaticon.com/free-icon/placeholder_1451757?term=ip&page=1&position=21&origin=search&related_id=1451757
9. [IPv6 Address Object](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_oeggeryskriq)
  * https://www.flaticon.com/free-icon/placeholder_1451757?term=ip&page=1&position=21&origin=search&related_id=1451757
10. [MAC Address Object](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_f92nr9plf58y)
  * https://www.flaticon.com/free-icon/barcode_1550324?term=barcode&page=1&position=4&origin=search&related_id=1550324
11. [Mutex Object](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_84hwlkdmev1w)
  * https://www.flaticon.com/free-icon/padlock_25239?term=lock&page=1&position=7&origin=search&related_id=25239
12. [Network Traffic Object](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_rgnc3w40xy)
  * https://fontawesome.com/icons/network-wired?f=classic&s=solid
13. [Process Object](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_hpppnm86a1jm)
  * https://www.flaticon.com/free-icon/flow-chart_16818023?term=process&page=1&position=77&origin=search&related_id=16818023
14. [Software Object](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_7rkyhtkdthok)
  * https://www.flaticon.com/free-icon/option_3018978?term=app&page=1&position=19&origin=search&related_id=3018978
15. [URL Object](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_ah3hict2dez0)
  * https://www.flaticon.com/free-icon/link_15400353?term=url&page=1&position=30&origin=search&related_id=15400353
16. [User Account Object](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_azo70vgj1vm2)
  * https://fontawesome.com/icons/user?f=classic&s=solid
17. [Windows Registry Key Object](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_luvw8wjlfo3y)
  * https://www.flaticon.com/free-icon/cubes_4352471?term=blocks&page=1&position=12&origin=search&related_id=4352471
18. [X.509 Certificate Object](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_8abcy1o5x9w1)
  * https://www.flaticon.com/free-icon/document_73524?term=certificate&page=1&position=31&origin=search&related_id=73524
19. Bank Card
  * https://fontawesome.com/icons/credit-card-front?f=classic&s=solid
20. Bank Account
  * https://www.flaticon.com/free-icon/bank_7710772?term=bank+account&page=1&position=31&origin=search&related_id=7710772
21. Cryptocurrency Wallet
  * https://www.flaticon.com/free-icon/wallet_6826311?term=wallet+digital&page=1&position=6&origin=search&related_id=6826311
22. Cryptocurrency Transaction 
  * https://www.flaticon.com/free-icon/transaction_4166062?term=digital+transaction&page=1&position=23&origin=search&related_id=4166062
23. Phone Number
  * https://fontawesome.com/icons/phone?f=classic&s=solid
24. User Agent
  * https://fontawesome.com/icons/browser?f=classic&s=solid

### SMOs

1. Language Content: https://www.flaticon.com/free-icon/language_484582?term=language&page=1&position=3&origin=search&related_id=484582
2. Marking Definition: https://www.flaticon.com/free-icon/quotation-mark_32371?term=marking&page=1&position=26&origin=search&related_id=32371
  * TLP: https://fontawesome.com/icons/traffic-light?f=classic&s=solid
3. Extension Definition: https://www.flaticon.com/free-icon/full-screen_159121?term=extend&page=1&position=29&origin=search&related_id=159121


## Adding your own objects

To start with, clone this repository.

```shell
# clone the latest code
git clone https://github.com/muchdogesec/stix_icons
# create a venv
cd stix_icons
python3 -m venv stix_icons-venv
source stix_icons-venv/bin/activate
# install requirements
pip3 install -r requirements.txt
```

The `input_vectors` contains vector files structured as follows;

```txt
input_vectors/
├── normal/
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

```

## Credits

[This work is an expansion of the STIX objects created by EclecticIQ](https://github.com/eclecticiq/stix-icons/).

## Licenses

* Code: [Apache 2.0](/LICENSE).
* Content: [Creative Commons Attribution 4.0 International Public License](/LICENSE-CONTENT)