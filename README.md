# stix2icons

## Overview

stix2icons is a collection of icons that represent all the of core STIX objects. The aim is to provide a central source of icons that can be used to represent STIX objects by software tools (or anything else).

This repo is designed so that new icons can be added for custom STIX objects you're developing. See: "Adding your own objects".

## tl;dr

[![stix2icons](https://img.youtube.com/vi/U5KIsulBN9E/0.jpg)](https://www.youtube.com/watch?v=U5KIsulBN9E)

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
| attack-pattern | sdo | 34,119,181 | #2277b5 | ![](output_files/rgb/normal/png/sdo/attack-pattern.png) | ![](output_files/rgb/round/png/sdo/attack-pattern.png) | ![](output_files/black/normal/png/sdo/attack-pattern.png) | ![](output_files/black/round/png/sdo/attack-pattern.png) | ![](output_files/white/normal/png/sdo/attack-pattern.png) | ![](output_files/white/round/png/sdo/attack-pattern.png) |
| campaign | sdo | 80,182,30 | #50b61e | ![](output_files/rgb/normal/png/sdo/campaign.png) | ![](output_files/rgb/round/png/sdo/campaign.png) | ![](output_files/black/normal/png/sdo/campaign.png) | ![](output_files/black/round/png/sdo/campaign.png) | ![](output_files/white/normal/png/sdo/campaign.png) | ![](output_files/white/round/png/sdo/campaign.png) |
| course-of-action | sdo | 161,198,40 | #a1c628 | ![](output_files/rgb/normal/png/sdo/course-of-action.png) | ![](output_files/rgb/round/png/sdo/course-of-action.png) | ![](output_files/black/normal/png/sdo/course-of-action.png) | ![](output_files/black/round/png/sdo/course-of-action.png) | ![](output_files/white/normal/png/sdo/course-of-action.png) | ![](output_files/white/round/png/sdo/course-of-action.png) |
| grouping | sdo | 163,53,139 | #a3358b | ![](output_files/rgb/normal/png/sdo/grouping.png) | ![](output_files/rgb/round/png/sdo/grouping.png) | ![](output_files/black/normal/png/sdo/grouping.png) | ![](output_files/black/round/png/sdo/grouping.png) | ![](output_files/white/normal/png/sdo/grouping.png) | ![](output_files/white/round/png/sdo/grouping.png) |
| identity | sdo | 156,154,254 | #9c9afe | ![](output_files/rgb/normal/png/sdo/identity.png) | ![](output_files/rgb/round/png/sdo/identity.png) | ![](output_files/black/normal/png/sdo/identity.png) | ![](output_files/black/round/png/sdo/identity.png) | ![](output_files/white/normal/png/sdo/identity.png) | ![](output_files/white/round/png/sdo/identity.png) |
| incident | sdo | 251,182,22 | #fbb616 | ![](output_files/rgb/normal/png/sdo/incident.png) | ![](output_files/rgb/round/png/sdo/incident.png) | ![](output_files/black/normal/png/sdo/incident.png) | ![](output_files/black/round/png/sdo/incident.png) | ![](output_files/white/normal/png/sdo/incident.png) | ![](output_files/white/round/png/sdo/incident.png) |
| indicator | sdo | 220,149,71 | #dc9547 | ![](output_files/rgb/normal/png/sdo/indicator.png) | ![](output_files/rgb/round/png/sdo/indicator.png) | ![](output_files/black/normal/png/sdo/indicator.png) | ![](output_files/black/round/png/sdo/indicator.png) | ![](output_files/white/normal/png/sdo/indicator.png) | ![](output_files/white/round/png/sdo/indicator.png) |
| infrastructure | sdo | 174,215,191 | #aed7bf | ![](output_files/rgb/normal/png/sdo/infrastructure.png) | ![](output_files/rgb/round/png/sdo/infrastructure.png) | ![](output_files/black/normal/png/sdo/infrastructure.png) | ![](output_files/black/round/png/sdo/infrastructure.png) | ![](output_files/white/normal/png/sdo/infrastructure.png) | ![](output_files/white/round/png/sdo/infrastructure.png) |
| intrusion-set | sdo | 56,178,193 | #38b2c1 | ![](output_files/rgb/normal/png/sdo/intrusion-set.png) | ![](output_files/rgb/round/png/sdo/intrusion-set.png) | ![](output_files/black/normal/png/sdo/intrusion-set.png) | ![](output_files/black/round/png/sdo/intrusion-set.png) | ![](output_files/white/normal/png/sdo/intrusion-set.png) | ![](output_files/white/round/png/sdo/intrusion-set.png) |
| location | sdo | 252,159,157 | #fc9f9d | ![](output_files/rgb/normal/png/sdo/location.png) | ![](output_files/rgb/round/png/sdo/location.png) | ![](output_files/black/normal/png/sdo/location.png) | ![](output_files/black/round/png/sdo/location.png) | ![](output_files/white/normal/png/sdo/location.png) | ![](output_files/white/round/png/sdo/location.png) |
| malware | sdo | 212,163,203 | #d4a3cb | ![](output_files/rgb/normal/png/sdo/malware.png) | ![](output_files/rgb/round/png/sdo/malware.png) | ![](output_files/black/normal/png/sdo/malware.png) | ![](output_files/black/round/png/sdo/malware.png) | ![](output_files/white/normal/png/sdo/malware.png) | ![](output_files/white/round/png/sdo/malware.png) |
| malware-analysis | sdo | 231,118,172 | #e776ac | ![](output_files/rgb/normal/png/sdo/malware-analysis.png) | ![](output_files/rgb/round/png/sdo/malware-analysis.png) | ![](output_files/black/normal/png/sdo/malware-analysis.png) | ![](output_files/black/round/png/sdo/malware-analysis.png) | ![](output_files/white/normal/png/sdo/malware-analysis.png) | ![](output_files/white/round/png/sdo/malware-analysis.png) |
| note | sdo | 136,200,129 | #88c881 | ![](output_files/rgb/normal/png/sdo/note.png) | ![](output_files/rgb/round/png/sdo/note.png) | ![](output_files/black/normal/png/sdo/note.png) | ![](output_files/black/round/png/sdo/note.png) | ![](output_files/white/normal/png/sdo/note.png) | ![](output_files/white/round/png/sdo/note.png) |
| observed-data | sdo | 252,204,184 | #fcccb8 | ![](output_files/rgb/normal/png/sdo/observed-data.png) | ![](output_files/rgb/round/png/sdo/observed-data.png) | ![](output_files/black/normal/png/sdo/observed-data.png) | ![](output_files/black/round/png/sdo/observed-data.png) | ![](output_files/white/normal/png/sdo/observed-data.png) | ![](output_files/white/round/png/sdo/observed-data.png) |
| opinion | sdo | 144,157,199 | #909dc7 | ![](output_files/rgb/normal/png/sdo/opinion.png) | ![](output_files/rgb/round/png/sdo/opinion.png) | ![](output_files/black/normal/png/sdo/opinion.png) | ![](output_files/black/round/png/sdo/opinion.png) | ![](output_files/white/normal/png/sdo/opinion.png) | ![](output_files/white/round/png/sdo/opinion.png) |
| report | sdo | 119,146,121 | #779279 | ![](output_files/rgb/normal/png/sdo/report.png) | ![](output_files/rgb/round/png/sdo/report.png) | ![](output_files/black/normal/png/sdo/report.png) | ![](output_files/black/round/png/sdo/report.png) | ![](output_files/white/normal/png/sdo/report.png) | ![](output_files/white/round/png/sdo/report.png) |
| threat-actor | sdo | 230,27,92 | #e61b5c | ![](output_files/rgb/normal/png/sdo/threat-actor.png) | ![](output_files/rgb/round/png/sdo/threat-actor.png) | ![](output_files/black/normal/png/sdo/threat-actor.png) | ![](output_files/black/round/png/sdo/threat-actor.png) | ![](output_files/white/normal/png/sdo/threat-actor.png) | ![](output_files/white/round/png/sdo/threat-actor.png) |
| tool | sdo | 87,80,157 | #57509d | ![](output_files/rgb/normal/png/sdo/tool.png) | ![](output_files/rgb/round/png/sdo/tool.png) | ![](output_files/black/normal/png/sdo/tool.png) | ![](output_files/black/round/png/sdo/tool.png) | ![](output_files/white/normal/png/sdo/tool.png) | ![](output_files/white/round/png/sdo/tool.png) |
| vulnerability | sdo | 255,209,0 | #ffd100 | ![](output_files/rgb/normal/png/sdo/vulnerability.png) | ![](output_files/rgb/round/png/sdo/vulnerability.png) | ![](output_files/black/normal/png/sdo/vulnerability.png) | ![](output_files/black/round/png/sdo/vulnerability.png) | ![](output_files/white/normal/png/sdo/vulnerability.png) | ![](output_files/white/round/png/sdo/vulnerability.png) |
| weakness | sdo | 94,49,128 | #5e3180 | ![](output_files/rgb/normal/png/sdo/weakness.png) | ![](output_files/rgb/round/png/sdo/weakness.png) | ![](output_files/black/normal/png/sdo/weakness.png) | ![](output_files/black/round/png/sdo/weakness.png) | ![](output_files/white/normal/png/sdo/weakness.png) | ![](output_files/white/round/png/sdo/weakness.png) |
| artifact | sco | 149,229,250 | #95e5fa | ![](output_files/rgb/normal/png/sco/artifact.png) | ![](output_files/rgb/round/png/sco/artifact.png) | ![](output_files/black/normal/png/sco/artifact.png) | ![](output_files/black/round/png/sco/artifact.png) | ![](output_files/white/normal/png/sco/artifact.png) | ![](output_files/white/round/png/sco/artifact.png) |
| autonomous-system | sco | 161,248,128 | #a1f880 | ![](output_files/rgb/normal/png/sco/autonomous-system.png) | ![](output_files/rgb/round/png/sco/autonomous-system.png) | ![](output_files/black/normal/png/sco/autonomous-system.png) | ![](output_files/black/round/png/sco/autonomous-system.png) | ![](output_files/white/normal/png/sco/autonomous-system.png) | ![](output_files/white/round/png/sco/autonomous-system.png) |
| directory | sco | 183,245,206 | #b7f5ce | ![](output_files/rgb/normal/png/sco/directory.png) | ![](output_files/rgb/round/png/sco/directory.png) | ![](output_files/black/normal/png/sco/directory.png) | ![](output_files/black/round/png/sco/directory.png) | ![](output_files/white/normal/png/sco/directory.png) | ![](output_files/white/round/png/sco/directory.png) |
| domain-name | sco | 255,185,167 | #ffb9a7 | ![](output_files/rgb/normal/png/sco/domain-name.png) | ![](output_files/rgb/round/png/sco/domain-name.png) | ![](output_files/black/normal/png/sco/domain-name.png) | ![](output_files/black/round/png/sco/domain-name.png) | ![](output_files/white/normal/png/sco/domain-name.png) | ![](output_files/white/round/png/sco/domain-name.png) |
| email-addr | sco | 145,128,242 | #9180f2 | ![](output_files/rgb/normal/png/sco/email-addr.png) | ![](output_files/rgb/round/png/sco/email-addr.png) | ![](output_files/black/normal/png/sco/email-addr.png) | ![](output_files/black/round/png/sco/email-addr.png) | ![](output_files/white/normal/png/sco/email-addr.png) | ![](output_files/white/round/png/sco/email-addr.png) |
| email-message | sco | 249,129,229 | #f981e5 | ![](output_files/rgb/normal/png/sco/email-message.png) | ![](output_files/rgb/round/png/sco/email-message.png) | ![](output_files/black/normal/png/sco/email-message.png) | ![](output_files/black/round/png/sco/email-message.png) | ![](output_files/white/normal/png/sco/email-message.png) | ![](output_files/white/round/png/sco/email-message.png) |
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
| cryptocurrency-exchange.svg | sco | 0,0,255 | #0000ff | ![](output_files/rgb/normal/png/sco/cryptocurrency-exchange.svg.png) | ![](output_files/rgb/round/png/sco/cryptocurrency-exchange.svg.png) | ![](output_files/black/normal/png/sco/cryptocurrency-exchange.svg.png) | ![](output_files/black/round/png/sco/cryptocurrency-exchange.svg.png) | ![](output_files/white/normal/png/sco/cryptocurrency-exchange.svg.png) | ![](output_files/white/round/png/sco/cryptocurrency-exchange.svg.png) |
| phone-number | sco | 226,189,239 | #e2bdef | ![](output_files/rgb/normal/png/sco/phone-number.png) | ![](output_files/rgb/round/png/sco/phone-number.png) | ![](output_files/black/normal/png/sco/phone-number.png) | ![](output_files/black/round/png/sco/phone-number.png) | ![](output_files/white/normal/png/sco/phone-number.png) | ![](output_files/white/round/png/sco/phone-number.png) |
| user-agent | sco | 152,199,239 | #98c7ef | ![](output_files/rgb/normal/png/sco/user-agent.png) | ![](output_files/rgb/round/png/sco/user-agent.png) | ![](output_files/black/normal/png/sco/user-agent.png) | ![](output_files/black/round/png/sco/user-agent.png) | ![](output_files/white/normal/png/sco/user-agent.png) | ![](output_files/white/round/png/sco/user-agent.png) |
| relationship | sro | 148,243,139 | #94f38b | ![](output_files/rgb/normal/png/sro/relationship.png) | ![](output_files/rgb/round/png/sro/relationship.png) | ![](output_files/black/normal/png/sro/relationship.png) | ![](output_files/black/round/png/sro/relationship.png) | ![](output_files/white/normal/png/sro/relationship.png) | ![](output_files/white/round/png/sro/relationship.png) |
| sighting | sro | 235,94,42 | #eb5e2a | ![](output_files/rgb/normal/png/sro/sighting.png) | ![](output_files/rgb/round/png/sro/sighting.png) | ![](output_files/black/normal/png/sro/sighting.png) | ![](output_files/black/round/png/sro/sighting.png) | ![](output_files/white/normal/png/sro/sighting.png) | ![](output_files/white/round/png/sro/sighting.png) |

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

If you want us to publish your icon in this repository for everyone to use, make a pull request after following all the steps above.

## Credits

* [This work is an expansion of the STIX objects created by EclecticIQ](https://github.com/eclecticiq/stix-icons/)
* [It is also heavily inspired by this work from Bret Jordan](https://github.com/freetaxii/stix2-graphics)

## Support

[Minimal support provided via the DOGESEC community](https://community.dogesec.com/).

## Licenses

* Code: [Apache 2.0](/LICENSE)
* Content: [Creative Commons Attribution 4.0 International Public License](/LICENSE-CONTENT)