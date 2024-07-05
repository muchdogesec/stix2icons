# stix2icons

## Overview

stix2icons is a collection of icons that represent all the of core STIX objects. The aim is to provide a central source of icons that can be used to represent STIX objects by software tools (or anything else).

This repo is designed so that new icons can be added for custom STIX objects you're developing. See: "Adding your own objects"

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

| Object | Type | RGB | RGB Circle | Black | Black Circle | White | White Circle |
|--------|------|-----|-----------|-------|-------------|-------|-------------|
| attack-pattern | sdo | ![](output_files/rgb/normal/png/sdo/attack-pattern.png) | ![](output_files/rgb/round/png/sdo/attack-pattern.png) | ![](output_files/black/normal/png/sdo/attack-pattern.png) | ![](output_files/black/round/png/sdo/attack-pattern.png) | ![](output_files/white/normal/png/sdo/attack-pattern.png) | ![](output_files/white/round/png/sdo/attack-pattern.png) |
| campaign | sdo | ![](output_files/rgb/normal/png/sdo/campaign.png) | ![](output_files/rgb/round/png/sdo/campaign.png) | ![](output_files/black/normal/png/sdo/campaign.png) | ![](output_files/black/round/png/sdo/campaign.png) | ![](output_files/white/normal/png/sdo/campaign.png) | ![](output_files/white/round/png/sdo/campaign.png) |
| course-of-action | sdo | ![](output_files/rgb/normal/png/sdo/course-of-action.png) | ![](output_files/rgb/round/png/sdo/course-of-action.png) | ![](output_files/black/normal/png/sdo/course-of-action.png) | ![](output_files/black/round/png/sdo/course-of-action.png) | ![](output_files/white/normal/png/sdo/course-of-action.png) | ![](output_files/white/round/png/sdo/course-of-action.png) |
| grouping | sdo | ![](output_files/rgb/normal/png/sdo/grouping.png) | ![](output_files/rgb/round/png/sdo/grouping.png) | ![](output_files/black/normal/png/sdo/grouping.png) | ![](output_files/black/round/png/sdo/grouping.png) | ![](output_files/white/normal/png/sdo/grouping.png) | ![](output_files/white/round/png/sdo/grouping.png) |
| identity | sdo | ![](output_files/rgb/normal/png/sdo/identity.png) | ![](output_files/rgb/round/png/sdo/identity.png) | ![](output_files/black/normal/png/sdo/identity.png) | ![](output_files/black/round/png/sdo/identity.png) | ![](output_files/white/normal/png/sdo/identity.png) | ![](output_files/white/round/png/sdo/identity.png) |
| identity_group | sdo | ![](output_files/rgb/normal/png/sdo/identity_group.png) | ![](output_files/rgb/round/png/sdo/identity_group.png) | ![](output_files/black/normal/png/sdo/identity_group.png) | ![](output_files/black/round/png/sdo/identity_group.png) | ![](output_files/white/normal/png/sdo/identity_group.png) | ![](output_files/white/round/png/sdo/identity_group.png) |
| identity_system | sdo | ![](output_files/rgb/normal/png/sdo/identity_system.png) | ![](output_files/rgb/round/png/sdo/identity_system.png) | ![](output_files/black/normal/png/sdo/identity_system.png) | ![](output_files/black/round/png/sdo/identity_system.png) | ![](output_files/white/normal/png/sdo/identity_system.png) | ![](output_files/white/round/png/sdo/identity_system.png) |
| identity_organization | sdo | ![](output_files/rgb/normal/png/sdo/identity_organization.png) | ![](output_files/rgb/round/png/sdo/identity_organization.png) | ![](output_files/black/normal/png/sdo/identity_organization.png) | ![](output_files/black/round/png/sdo/identity_organization.png) | ![](output_files/white/normal/png/sdo/identity_organization.png) | ![](output_files/white/round/png/sdo/identity_organization.png) |
| identity_individual | sdo | ![](output_files/rgb/normal/png/sdo/identity_individual.png) | ![](output_files/rgb/round/png/sdo/identity_individual.png) | ![](output_files/black/normal/png/sdo/identity_individual.png) | ![](output_files/black/round/png/sdo/identity_individual.png) | ![](output_files/white/normal/png/sdo/identity_individual.png) | ![](output_files/white/round/png/sdo/identity_individual.png) |
| identity_class | sdo | ![](output_files/rgb/normal/png/sdo/identity_class.png) | ![](output_files/rgb/round/png/sdo/identity_class.png) | ![](output_files/black/normal/png/sdo/identity_class.png) | ![](output_files/black/round/png/sdo/identity_class.png) | ![](output_files/white/normal/png/sdo/identity_class.png) | ![](output_files/white/round/png/sdo/identity_class.png) |
| incident | sdo | ![](output_files/rgb/normal/png/sdo/incident.png) | ![](output_files/rgb/round/png/sdo/incident.png) | ![](output_files/black/normal/png/sdo/incident.png) | ![](output_files/black/round/png/sdo/incident.png) | ![](output_files/white/normal/png/sdo/incident.png) | ![](output_files/white/round/png/sdo/incident.png) |
| indicator | sdo | ![](output_files/rgb/normal/png/sdo/indicator.png) | ![](output_files/rgb/round/png/sdo/indicator.png) | ![](output_files/black/normal/png/sdo/indicator.png) | ![](output_files/black/round/png/sdo/indicator.png) | ![](output_files/white/normal/png/sdo/indicator.png) | ![](output_files/white/round/png/sdo/indicator.png) |
| infrastructure | sdo | ![](output_files/rgb/normal/png/sdo/infrastructure.png) | ![](output_files/rgb/round/png/sdo/infrastructure.png) | ![](output_files/black/normal/png/sdo/infrastructure.png) | ![](output_files/black/round/png/sdo/infrastructure.png) | ![](output_files/white/normal/png/sdo/infrastructure.png) | ![](output_files/white/round/png/sdo/infrastructure.png) |
| intrusion-set | sdo | ![](output_files/rgb/normal/png/sdo/intrusion-set.png) | ![](output_files/rgb/round/png/sdo/intrusion-set.png) | ![](output_files/black/normal/png/sdo/intrusion-set.png) | ![](output_files/black/round/png/sdo/intrusion-set.png) | ![](output_files/white/normal/png/sdo/intrusion-set.png) | ![](output_files/white/round/png/sdo/intrusion-set.png) |
| location | sdo | ![](output_files/rgb/normal/png/sdo/location.png) | ![](output_files/rgb/round/png/sdo/location.png) | ![](output_files/black/normal/png/sdo/location.png) | ![](output_files/black/round/png/sdo/location.png) | ![](output_files/white/normal/png/sdo/location.png) | ![](output_files/white/round/png/sdo/location.png) |
| malware | sdo | ![](output_files/rgb/normal/png/sdo/malware.png) | ![](output_files/rgb/round/png/sdo/malware.png) | ![](output_files/black/normal/png/sdo/malware.png) | ![](output_files/black/round/png/sdo/malware.png) | ![](output_files/white/normal/png/sdo/malware.png) | ![](output_files/white/round/png/sdo/malware.png) |
| malware_family | sdo | ![](output_files/rgb/normal/png/sdo/malware_family.png) | ![](output_files/rgb/round/png/sdo/malware_family.png) | ![](output_files/black/normal/png/sdo/malware_family.png) | ![](output_files/black/round/png/sdo/malware_family.png) | ![](output_files/white/normal/png/sdo/malware_family.png) | ![](output_files/white/round/png/sdo/malware_family.png) |
| malware-analysis | sdo | ![](output_files/rgb/normal/png/sdo/malware-analysis.png) | ![](output_files/rgb/round/png/sdo/malware-analysis.png) | ![](output_files/black/normal/png/sdo/malware-analysis.png) | ![](output_files/black/round/png/sdo/malware-analysis.png) | ![](output_files/white/normal/png/sdo/malware-analysis.png) | ![](output_files/white/round/png/sdo/malware-analysis.png) |
| note | sdo | ![](output_files/rgb/normal/png/sdo/note.png) | ![](output_files/rgb/round/png/sdo/note.png) | ![](output_files/black/normal/png/sdo/note.png) | ![](output_files/black/round/png/sdo/note.png) | ![](output_files/white/normal/png/sdo/note.png) | ![](output_files/white/round/png/sdo/note.png) |
| observed-data | sdo | ![](output_files/rgb/normal/png/sdo/observed-data.png) | ![](output_files/rgb/round/png/sdo/observed-data.png) | ![](output_files/black/normal/png/sdo/observed-data.png) | ![](output_files/black/round/png/sdo/observed-data.png) | ![](output_files/white/normal/png/sdo/observed-data.png) | ![](output_files/white/round/png/sdo/observed-data.png) |
| opinion | sdo | ![](output_files/rgb/normal/png/sdo/opinion.png) | ![](output_files/rgb/round/png/sdo/opinion.png) | ![](output_files/black/normal/png/sdo/opinion.png) | ![](output_files/black/round/png/sdo/opinion.png) | ![](output_files/white/normal/png/sdo/opinion.png) | ![](output_files/white/round/png/sdo/opinion.png) |
| report | sdo | ![](output_files/rgb/normal/png/sdo/report.png) | ![](output_files/rgb/round/png/sdo/report.png) | ![](output_files/black/normal/png/sdo/report.png) | ![](output_files/black/round/png/sdo/report.png) | ![](output_files/white/normal/png/sdo/report.png) | ![](output_files/white/round/png/sdo/report.png) |
| threat-actor | sdo | ![](output_files/rgb/normal/png/sdo/threat-actor.png) | ![](output_files/rgb/round/png/sdo/threat-actor.png) | ![](output_files/black/normal/png/sdo/threat-actor.png) | ![](output_files/black/round/png/sdo/threat-actor.png) | ![](output_files/white/normal/png/sdo/threat-actor.png) | ![](output_files/white/round/png/sdo/threat-actor.png) |
| tool | sdo | ![](output_files/rgb/normal/png/sdo/tool.png) | ![](output_files/rgb/round/png/sdo/tool.png) | ![](output_files/black/normal/png/sdo/tool.png) | ![](output_files/black/round/png/sdo/tool.png) | ![](output_files/white/normal/png/sdo/tool.png) | ![](output_files/white/round/png/sdo/tool.png) |
| vulnerability | sdo | ![](output_files/rgb/normal/png/sdo/vulnerability.png) | ![](output_files/rgb/round/png/sdo/vulnerability.png) | ![](output_files/black/normal/png/sdo/vulnerability.png) | ![](output_files/black/round/png/sdo/vulnerability.png) | ![](output_files/white/normal/png/sdo/vulnerability.png) | ![](output_files/white/round/png/sdo/vulnerability.png) |
| weakness | sdo | ![](output_files/rgb/normal/png/sdo/weakness.png) | ![](output_files/rgb/round/png/sdo/weakness.png) | ![](output_files/black/normal/png/sdo/weakness.png) | ![](output_files/black/round/png/sdo/weakness.png) | ![](output_files/white/normal/png/sdo/weakness.png) | ![](output_files/white/round/png/sdo/weakness.png) |
| artifact | sco | ![](output_files/rgb/normal/png/sco/artifact.png) | ![](output_files/rgb/round/png/sco/artifact.png) | ![](output_files/black/normal/png/sco/artifact.png) | ![](output_files/black/round/png/sco/artifact.png) | ![](output_files/white/normal/png/sco/artifact.png) | ![](output_files/white/round/png/sco/artifact.png) |
| autonomous-system | sco | ![](output_files/rgb/normal/png/sco/autonomous-system.png) | ![](output_files/rgb/round/png/sco/autonomous-system.png) | ![](output_files/black/normal/png/sco/autonomous-system.png) | ![](output_files/black/round/png/sco/autonomous-system.png) | ![](output_files/white/normal/png/sco/autonomous-system.png) | ![](output_files/white/round/png/sco/autonomous-system.png) |
| directory | sco | ![](output_files/rgb/normal/png/sco/directory.png) | ![](output_files/rgb/round/png/sco/directory.png) | ![](output_files/black/normal/png/sco/directory.png) | ![](output_files/black/round/png/sco/directory.png) | ![](output_files/white/normal/png/sco/directory.png) | ![](output_files/white/round/png/sco/directory.png) |
| domain-name | sco | ![](output_files/rgb/normal/png/sco/domain-name.png) | ![](output_files/rgb/round/png/sco/domain-name.png) | ![](output_files/black/normal/png/sco/domain-name.png) | ![](output_files/black/round/png/sco/domain-name.png) | ![](output_files/white/normal/png/sco/domain-name.png) | ![](output_files/white/round/png/sco/domain-name.png) |
| email-addr | sco | ![](output_files/rgb/normal/png/sco/email-addr.png) | ![](output_files/rgb/round/png/sco/email-addr.png) | ![](output_files/black/normal/png/sco/email-addr.png) | ![](output_files/black/round/png/sco/email-addr.png) | ![](output_files/white/normal/png/sco/email-addr.png) | ![](output_files/white/round/png/sco/email-addr.png) |
| email-message | sco | ![](output_files/rgb/normal/png/sco/email-message.png) | ![](output_files/rgb/round/png/sco/email-message.png) | ![](output_files/black/normal/png/sco/email-message.png) | ![](output_files/black/round/png/sco/email-message.png) | ![](output_files/white/normal/png/sco/email-message.png) | ![](output_files/white/round/png/sco/email-message.png) |
| file | sco | ![](output_files/rgb/normal/png/sco/file.png) | ![](output_files/rgb/round/png/sco/file.png) | ![](output_files/black/normal/png/sco/file.png) | ![](output_files/black/round/png/sco/file.png) | ![](output_files/white/normal/png/sco/file.png) | ![](output_files/white/round/png/sco/file.png) |
| ipv4-addr | sco | ![](output_files/rgb/normal/png/sco/ipv4-addr.png) | ![](output_files/rgb/round/png/sco/ipv4-addr.png) | ![](output_files/black/normal/png/sco/ipv4-addr.png) | ![](output_files/black/round/png/sco/ipv4-addr.png) | ![](output_files/white/normal/png/sco/ipv4-addr.png) | ![](output_files/white/round/png/sco/ipv4-addr.png) |
| ipv6-addr | sco | ![](output_files/rgb/normal/png/sco/ipv6-addr.png) | ![](output_files/rgb/round/png/sco/ipv6-addr.png) | ![](output_files/black/normal/png/sco/ipv6-addr.png) | ![](output_files/black/round/png/sco/ipv6-addr.png) | ![](output_files/white/normal/png/sco/ipv6-addr.png) | ![](output_files/white/round/png/sco/ipv6-addr.png) |
| mac-addr | sco | ![](output_files/rgb/normal/png/sco/mac-addr.png) | ![](output_files/rgb/round/png/sco/mac-addr.png) | ![](output_files/black/normal/png/sco/mac-addr.png) | ![](output_files/black/round/png/sco/mac-addr.png) | ![](output_files/white/normal/png/sco/mac-addr.png) | ![](output_files/white/round/png/sco/mac-addr.png) |
| mutex | sco | ![](output_files/rgb/normal/png/sco/mutex.png) | ![](output_files/rgb/round/png/sco/mutex.png) | ![](output_files/black/normal/png/sco/mutex.png) | ![](output_files/black/round/png/sco/mutex.png) | ![](output_files/white/normal/png/sco/mutex.png) | ![](output_files/white/round/png/sco/mutex.png) |
| network-traffic | sco | ![](output_files/rgb/normal/png/sco/network-traffic.png) | ![](output_files/rgb/round/png/sco/network-traffic.png) | ![](output_files/black/normal/png/sco/network-traffic.png) | ![](output_files/black/round/png/sco/network-traffic.png) | ![](output_files/white/normal/png/sco/network-traffic.png) | ![](output_files/white/round/png/sco/network-traffic.png) |
| process | sco | ![](output_files/rgb/normal/png/sco/process.png) | ![](output_files/rgb/round/png/sco/process.png) | ![](output_files/black/normal/png/sco/process.png) | ![](output_files/black/round/png/sco/process.png) | ![](output_files/white/normal/png/sco/process.png) | ![](output_files/white/round/png/sco/process.png) |
| software | sco | ![](output_files/rgb/normal/png/sco/software.png) | ![](output_files/rgb/round/png/sco/software.png) | ![](output_files/black/normal/png/sco/software.png) | ![](output_files/black/round/png/sco/software.png) | ![](output_files/white/normal/png/sco/software.png) | ![](output_files/white/round/png/sco/software.png) |
| url | sco | ![](output_files/rgb/normal/png/sco/url.png) | ![](output_files/rgb/round/png/sco/url.png) | ![](output_files/black/normal/png/sco/url.png) | ![](output_files/black/round/png/sco/url.png) | ![](output_files/white/normal/png/sco/url.png) | ![](output_files/white/round/png/sco/url.png) |
| user-account | sco | ![](output_files/rgb/normal/png/sco/user-account.png) | ![](output_files/rgb/round/png/sco/user-account.png) | ![](output_files/black/normal/png/sco/user-account.png) | ![](output_files/black/round/png/sco/user-account.png) | ![](output_files/white/normal/png/sco/user-account.png) | ![](output_files/white/round/png/sco/user-account.png) |
| windows-registry-key | sco | ![](output_files/rgb/normal/png/sco/windows-registry-key.png) | ![](output_files/rgb/round/png/sco/windows-registry-key.png) | ![](output_files/black/normal/png/sco/windows-registry-key.png) | ![](output_files/black/round/png/sco/windows-registry-key.png) | ![](output_files/white/normal/png/sco/windows-registry-key.png) | ![](output_files/white/round/png/sco/windows-registry-key.png) |
| x509-certificate | sco | ![](output_files/rgb/normal/png/sco/x509-certificate.png) | ![](output_files/rgb/round/png/sco/x509-certificate.png) | ![](output_files/black/normal/png/sco/x509-certificate.png) | ![](output_files/black/round/png/sco/x509-certificate.png) | ![](output_files/white/normal/png/sco/x509-certificate.png) | ![](output_files/white/round/png/sco/x509-certificate.png) |
| bank-account | sco | ![](output_files/rgb/normal/png/sco/bank-account.png) | ![](output_files/rgb/round/png/sco/bank-account.png) | ![](output_files/black/normal/png/sco/bank-account.png) | ![](output_files/black/round/png/sco/bank-account.png) | ![](output_files/white/normal/png/sco/bank-account.png) | ![](output_files/white/round/png/sco/bank-account.png) |
| bank-card | sco | ![](output_files/rgb/normal/png/sco/bank-card.png) | ![](output_files/rgb/round/png/sco/bank-card.png) | ![](output_files/black/normal/png/sco/bank-card.png) | ![](output_files/black/round/png/sco/bank-card.png) | ![](output_files/white/normal/png/sco/bank-card.png) | ![](output_files/white/round/png/sco/bank-card.png) |
| cryptocurrency-transaction | sco | ![](output_files/rgb/normal/png/sco/cryptocurrency-transaction.png) | ![](output_files/rgb/round/png/sco/cryptocurrency-transaction.png) | ![](output_files/black/normal/png/sco/cryptocurrency-transaction.png) | ![](output_files/black/round/png/sco/cryptocurrency-transaction.png) | ![](output_files/white/normal/png/sco/cryptocurrency-transaction.png) | ![](output_files/white/round/png/sco/cryptocurrency-transaction.png) |
| cryptocurrency-wallet | sco | ![](output_files/rgb/normal/png/sco/cryptocurrency-wallet.png) | ![](output_files/rgb/round/png/sco/cryptocurrency-wallet.png) | ![](output_files/black/normal/png/sco/cryptocurrency-wallet.png) | ![](output_files/black/round/png/sco/cryptocurrency-wallet.png) | ![](output_files/white/normal/png/sco/cryptocurrency-wallet.png) | ![](output_files/white/round/png/sco/cryptocurrency-wallet.png) |
| phone-number | sco | ![](output_files/rgb/normal/png/sco/phone-number.png) | ![](output_files/rgb/round/png/sco/phone-number.png) | ![](output_files/black/normal/png/sco/phone-number.png) | ![](output_files/black/round/png/sco/phone-number.png) | ![](output_files/white/normal/png/sco/phone-number.png) | ![](output_files/white/round/png/sco/phone-number.png) |
| user-agent | sco | ![](output_files/rgb/normal/png/sco/user-agent.png) | ![](output_files/rgb/round/png/sco/user-agent.png) | ![](output_files/black/normal/png/sco/user-agent.png) | ![](output_files/black/round/png/sco/user-agent.png) | ![](output_files/white/normal/png/sco/user-agent.png) | ![](output_files/white/round/png/sco/user-agent.png) |
| relationship | sro | ![](output_files/rgb/normal/png/sro/relationship.png) | ![](output_files/rgb/round/png/sro/relationship.png) | ![](output_files/black/normal/png/sro/relationship.png) | ![](output_files/black/round/png/sro/relationship.png) | ![](output_files/white/normal/png/sro/relationship.png) | ![](output_files/white/round/png/sro/relationship.png) |
| sighting | sro | ![](output_files/rgb/normal/png/sro/sighting.png) | ![](output_files/rgb/round/png/sro/sighting.png) | ![](output_files/black/normal/png/sro/sighting.png) | ![](output_files/black/round/png/sro/sighting.png) | ![](output_files/white/normal/png/sro/sighting.png) | ![](output_files/white/round/png/sro/sighting.png) |

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
│   └── sro/
└── round/
    ├── sco/
    ├── sdo/
    └── sro/
```

Where `sco`, `sdo`, or `sro` is the type of STIX object.

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
{"object": "attack-pattern", "type": "sdo", "colour_rgb": "34,119,181"},
```

Once done, you can then run the script;

```shell
python3 generate_icons.py
```

This will generate a black, white and colour version of your object as an `svg` and `png` (256x256).

## Credits

* [This work is an expansion of the STIX objects created by EclecticIQ](https://github.com/eclecticiq/stix-icons/)
* [It is also heavily inspired by this work from Bret Jordan](https://github.com/freetaxii/stix2-graphics)

## Support

[Minimal support provided via the DOGESEC community](https://community.dogesec.com/).

## Licenses

* Code: [Apache 2.0](/LICENSE)
* Content: [Creative Commons Attribution 4.0 International Public License](/LICENSE-CONTENT)