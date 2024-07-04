# stix2icons

## Overview

stix2icons is a collection of icons that represent all the of core STIX objects. The aim is to provide a central source of icons that can be used to represent STIX objects by software tools (or anything else).

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

## WIP

### SDOs

1. Weakness

### SCOs

1. Artifact Object
2. AS Object
3. Directory Object
4. Domain Name Object
5. Email Address Object
6. Email Message Object
7. File Object
8. IPv4 Address Object
9. IPv6 Address Object
10. MAC Address Object
11. Mutex Object
12. Network Traffic Object
13. Process Object
14. Software Object
15. URL Object
16. User Account Object
17. Windows Registry Key Object
18. X.509 Certificate Object
19. Bank Card
20. Bank Account
21. Cryptocurrency Wallet
22. Cryptocurrency Transaction 
23. Phone Number
24. User Agent
  * https://fontawesome.com/icons/browser?f=classic&s=solid

### SMOs

1. Language Content
2. Marking Definition
  * TLP
3. Extension Definition

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

```shell
python3 generate_icons.py
```

## Credits

* [This work is an expansion of the STIX objects created by EclecticIQ](https://github.com/eclecticiq/stix-icons/).
* [It is also heavily inspired by this work from Bret Jordan](https://github.com/freetaxii/stix2-graphics)

## Licenses

* Code: [Apache 2.0](/LICENSE).
* Content: [Creative Commons Attribution 4.0 International Public License](/LICENSE-CONTENT)