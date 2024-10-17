
# Data Product Canvas - Berlin Electoral Districts geodata

## Metadata

* owner: Open Lifeworlds
* description: Data product providing Berlin geodata of electoral districts
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-electoral-districts-geodata
* license: CC-BY 4.0
* updated: 2025-03-14

## Input Ports

### Wahllokale zur Bundestagswahl 2013 in Berlin
* owner: Amt für Statistik Berlin-Brandenburg
* url: https://daten.berlin.de/datensaetze/wahllokale-zur-bundestagswahl-2013-in-berlin
* license: Creative Commons Attribution License (cc-by)
* updated: 2019-05-13

**Schema**

| Name | Description |
| --- | --- |
| Schlüssel | identifier |
| Bezirk | district |
| Wahlbezirk | electoral district |
| Lokal | polling station |
| Bezeichnung | description |
| PLZ | zip code |
| Ort | city |
| Zugang | access |

**Files**

* [BTW2013_BE_Wahllokale_Schluessel.csv](https://download.statistik-berlin-brandenburg.de/c1cbf6968ccbb352/189fc1ad462e/BTW2013_BE_Wahllokale_Schluessel.csv)
* [BTW2013_BE_Wahllokale_Beschreibung.pdf](https://download.statistik-berlin-brandenburg.de/17e5dee65d363229/db408945d106/BTW2013_BE_Wahllokale_Beschreibung.pdf)
### Geometrien der Europawahl Berlin 2014
* owner: Amt für Statistik Berlin-Brandenburg
* url: https://daten.berlin.de/datensaetze/geometrien-der-europawahl-berlin-2014
* license: Creative Commons Attribution License (cc-by)
* updated: 2020-10-12

**Schema**

| Name | Description |
| --- | --- |
| FID | random identifier |
| shape | geometry of a electoral district |
| STI (Wahlbezirk) | ID of the electoral district (5 digits) |
| BRFW (Briefwahlbezirk) | ID of the postal voting district (3 digits + 1 letter) |
| WKR (Wahlkreis) | ID of the constituency for Berlin election (4 digits) |
| BEZ (Bezirk) | ID of the district (2 digits) |

**Files**

* [RBS_OD_STI_EU1405.zip](https://download.statistik-berlin-brandenburg.de/c029f84035837945/ebbe3670345d/RBS_OD_STI_EU1405.zip)
* [Beschreibung_RBS_OD_STI.pdf](https://download.statistik-berlin-brandenburg.de/43f4a582730c778d/0006b4c1facc/Beschreibung_RBS_OD_STI.pdf)
### Geometrien der Wahlbezirke für die Wahl zum Abgeordnetenhaus von Berlin und zu den Bezirksversammlungen 2016
* owner: Amt für Statistik Berlin-Brandenburg
* url: https://daten.berlin.de/datensaetze/geometrien-der-wahlbezirke-fur-die-wahl-zum-abgeordnetenhaus-von-berlin-undbvv
* license: Creative Commons Attribution License (cc-by)
* updated: 2019-05-13

**Schema**

| Name | Description |
| --- | --- |
| FID | random identifier |
| shape | geometry of a electoral district |
| UWB (Urnen-Wahlbezirk) | ID of the polling district (5 digits) |
| BWB (Briefwahlbezirk) | ID of the postal voting district (3 digits + 1 letter) |
| AWK (Abgenordnetenhaus-Wahlkreis) | ID of the electoral district for the election of House of Representatives (4 digits) |
| BEZ (Bezirk) | ID of the district (2 digits) |

**Files**

* [RBS_OD_UWB_AGH_09_2016.zip](https://download.statistik-berlin-brandenburg.de/151935287e405aaa/c7bcebf1a199/RBS_OD_UWB_AGH_09_2016.zip)
* [Beschreibung_RBS_OD_UWB.pdf](https://download.statistik-berlin-brandenburg.de/c812862e8c2d0b56/64ec5e81c7bd/Beschreibung_RBS_OD_UWB.pdf)
### Geometrien der Wahlbezirke für die Bundestagswahl in Berlin 2017
* owner: Amt für Statistik Berlin-Brandenburg
* url: https://daten.berlin.de/datensaetze/geometrien-der-wahlbezirke-fuer-die-bundestagswahl-in-berlin-2017
* license: Creative Commons Attribution License (cc-by)
* updated: 2019-05-13

**Schema**

| Name | Description |
| --- | --- |
| FID | random identifier |
| UWB (Urnen-Wahlbezirk) | ID of polling district (5 digits) |
| UWB3 (Urnen-Wahlbezirk) | ID of polling district (3 digits), unique for each district |
| BWB (Briefwahlbezirk) | ID of postal voting district (3 digits + 1 letter), first 2 digits represent the district |
| BWB2 (Briefwahlbezirk) | ID of postal voting district (1 digit + 1 letter) |
| AWK (Abgenordnetenhaus-Wahlkreis) | ID of House of Representatives electoral district (4 digits) |
| BEZ (Bezirk) | ID of the district (2 digits) |

**Files**

* [RBS_OD_Wahlgebiete_BTW17.zip](https://download.statistik-berlin-brandenburg.de/253a62a4ec4bd715/d2a5ad97d6f3/RBS_OD_Wahlgebiete_BTW17.zip)
* [RBS_OD_Wahlgebiete_BTW17_Beschreibung.pdf](https://download.statistik-berlin-brandenburg.de/348d8f8843e9fcb5/e56c0825471c/RBS_OD_Wahlgebiete_BTW17_Beschreibung.pdf)
### Geometrien der Wahlbezirke für die Europawahl 2019 in Berlin
* owner: Amt für Statistik Berlin-Brandenburg
* url: https://daten.berlin.de/datensaetze/geometrien-der-wahlbezirke-fur-die-europawahl-2019-in-berlin
* license: Creative Commons Attribution License (cc-by)
* updated: 2019-03-04

**Schema**

| Name | Description |
| --- | --- |
| FID | random identifier |
| UWB (Urnen-Wahlbezirk) | ID of the polling district (5 digits) |
| UWB3 (Urnen-Wahlbezirk) | ID of the polling district (3 digits), unique for each district |
| BWB (Briefwahlbezirk) | ID of the postal voting district (3 digits + 1 letter), first 2 digits represent the district |
| BWB2 (Briefwahlbezirk) | ID of the postal voting district (1 digit + 1 letter) |
| AWK (Abgenordnetenhaus-Wahlkreis) | ID of the electoral district for the election of House of Representatives (4 digits) |
| BEZ (Bezirk) | ID of the district (2 digits) |
| BWK (Bundestagswahlkreis) | ID of the electoral district for the federal election (3 digits) |
| OW (OstWest) | part of the city, gW geographically West, gO geographically East |
| shape | geometry of a electoral district |

**Files**

* [RBS_OD_UWB_EU2019.zip](https://download.statistik-berlin-brandenburg.de/b77e4aac570fd7b5/f5f517e4330d/RBS_OD_UWB_EU2019.zip)
* [Beschreibung_RBS_OD_Wahlgebiete_EU2019.pdf](https://download.statistik-berlin-brandenburg.de/7cf803f14f8229be/737117910c21/Beschreibung_RBS_OD_Wahlgebiete_EU2019.pdf)
### Geometrien der Wahllokale für die Wahlen zum Deutschen Bundestag in Berlin und zum Abgeordnetenhaus von Berlin 2021
* owner: Amt für Statistik Berlin-Brandenburg
* url: https://daten.berlin.de/datensaetze/geometrien-wahllokale-bundestagswahl-abgeordnetenhaus-berlin-2021
* license: Creative Commons Attribution License (cc-by)
* updated: 2021-02-26

**Schema**

| Name | Description |
| --- | --- |
| BEZ (Bezirk) | ID of the district (2 digits) |
| BWK (Bundestagswahlkreis) | ID of the electoral district for the federal election (2 digits) |
| WB (Wahlbezirk) | ID of the electoral district (3 digits) or ID postal voting district (1 digit + 1 or 2 digits) |
| Briefwahl | postal voting, 0 = no, 1 = yes |
| Bezeich1 (Bezeichnung des Wahllokals) | name of the facility, as specified by electoral office |
| Bezeich2 (Bezeichnung Zusatz) | additional information about the name of the facility, as specified by electoral office |
| Raum | room, as specified by electoral office |
| Etage | floor, as specified by electoral office |
| STR (Straßenname) | street, as specified by electoral office |
| HNr (Hausnummer mit Zusatz) | house number, as specified by electoral office |
| PLZ (Postleitzahl) | zip code, as specified by electoral office |
| Barrierefr (Barrierefrei) | barrier-free, 0 = no, 1 = yes, 2 = yes with assistant |
| Lat_WGS84 | latitude |
| Lon_WGS84 | longitude |

**Files**

* [RBS_OD_UWB_AH21.zip](https://download.statistik-berlin-brandenburg.de/db8c83613aceb93e/14a42eb32a76/RBS_OD_UWB_AH21.zip)
* [RBS_OD_Wahllokal_BTW_AH2021_Beschreibung.pdf](https://download.statistik-berlin-brandenburg.de/ee24f01b9875e3cb/7a7df27ba4aa/RBS_OD_Wahllokal_BTW_AH2021_Beschreibung.pdf)
### Geometrien der Wahllokale für die Wahlen zum Deutschen Bundestag in Berlin und zum Abgeordnetenhaus von Berlin 2021
* owner: Amt für Statistik Berlin-Brandenburg
* url: https://daten.berlin.de/datensaetze/geometrien-wahllokale-bundestagswahl-abgeordnetenhaus-berlin-2021
* license: Creative Commons Attribution License (cc-by)
* updated: 2021-02-26

**Schema**

| Name | Description |
| --- | --- |
| BEZ (Bezirk) | ID of the district (2 digits) |
| BWK (Bundestagswahlkreis) | ID of the electoral district for the federal election (2 digits) |
| WB (Wahlbezirk) | ID of the electoral district (3 digits) or ID postal voting district (1 digit + 1 or 2 digits) |
| Briefwahl | postal voting, 0 = no, 1 = yes |
| Bezeich1 (Bezeichnung des Wahllokals) | name of the facility, as specified by electoral office |
| Bezeich2 (Bezeichnung Zusatz) | additional information about the name of the facility, as specified by electoral office |
| Raum | room, as specified by electoral office |
| Etage | floor, as specified by electoral office |
| STR (Straßenname) | street, as specified by electoral office |
| HNr (Hausnummer mit Zusatz) | house number, as specified by electoral office |
| PLZ (Postleitzahl) | zip code, as specified by electoral office |
| Barrierefr (Barrierefrei) | barrier-free, 0 = no, 1 = yes, 2 = yes with assistant |
| Lat_WGS84 | latitude |
| Lon_WGS84 | longitude |

**Files**

* [RBS_OD_UWB_AH21.zip](https://download.statistik-berlin-brandenburg.de/db8c83613aceb93e/14a42eb32a76/RBS_OD_UWB_AH21.zip)
* [RBS_OD_Wahllokal_BTW_AH2021_Beschreibung.pdf](https://download.statistik-berlin-brandenburg.de/ee24f01b9875e3cb/7a7df27ba4aa/RBS_OD_Wahllokal_BTW_AH2021_Beschreibung.pdf)
### Wahlbezirke der Teilwahlwiederholung für die Wahl des Deutschen Bundestag 2024 in Berlin
* owner: Amt für Statistik Berlin-Brandenburg
* url: https://daten.berlin.de/datensaetze/wahlbezirke-der-teilwahlwiederholung-fur-die-wahl-des-deutschen-bundestag-2024-in-berlin
* license: Creative Commons Attribution License (cc-by)
* updated: 2024-01-11

**Schema**

| Name | Description |
| --- | --- |
| Adresse | key ID |
| OstWest | part of the city (Berlin-Ost, Berlin-West) |
| Bezirk | ID of the district |
| BunWkr | ID of the electoral district for the federal election |
| AghWkr | ID of the Berlin election electoral district |
| BriefWbz | ID of the postal voting district |
| WBezArt | type of the electoral district, B = Briefwahlbezirk, W = Urnenwahlbezirk |
| Wahlbezirk | ID of the electoral district |
| Wbz | ID of the electoral district, to be used when joining with geometry |
| Hinweis | hint whether the electoral district is affected by the partial repetition |

**Files**

* [Berlin_BT21_Teilwiederholungs23_Wahlbezirke.csv](https://download.statistik-berlin-brandenburg.de/5706ea3c21816a95/699dfdb61d85/Berlin_BT21_Teilwiederholungs23_Wahlbezirke.csv)
* [Berlin_BT21_Teilwiederholung23_Wahlbezirke_Meta.pdf](https://download.statistik-berlin-brandenburg.de/7504e8613c562b94/113f5bf39a22/Berlin_BT21_Teilwiederholung23_Wahlbezirke_Meta.pdf)
### Geometrien der Wahllokale für die Wahl des Europäischen Parlaments in Berlin 2024
* owner: Amt für Statistik Berlin-Brandenburg
* url: https://daten.berlin.de/datensaetze/geometrien-der-wahllokale-fur-die-wahl-des-europaischen-parlaments-in-berlin-2024
* license: Creative Commons Attribution License (cc-by)
* updated: 2024-02-29

**Schema**

| Name | Description |
| --- | --- |
| BEZ (Bezirk) | ID of the district (2 digits) |
| BWK (Bundestagswahlkreis) | ID of the electoral district for the federal election (2 digits) |
| WB (Wahlbezirk) | ID of the electoral district (3 digits) or ID postal voting district (1 digit + 1 or 2 digits) |
| Briefwahl | postal voting, 0 = no, 1 = yes |
| Bezeich1 (Bezeichnung des Wahllokals) | name of the facility, as specified by electoral office |
| Bezeich2 (Bezeichnung Zusatz) | additional information about the name of the facility, as specified by electoral office |
| Raum | room, as specified by electoral office |
| Etage | floor, as specified by electoral office |
| STR (Straßenname) | street, as specified by electoral office |
| HNr (Hausnummer mit Zusatz) | house number, as specified by electoral office |
| PLZ (Postleitzahl) | zip code, as specified by electoral office |
| Barrierefr (Barrierefrei) | barrier-free, 0 = no, 1 = yes, 2 = yes with assistant |

**Files**

* [RBS_OD_Wahllokale_UWB_EU24.zip](https://download.statistik-berlin-brandenburg.de/7ea18662c6e242f0/9e03e4e983eb/RBS_OD_Wahllokale_UWB_EU24.zip)
* [RBS_OD_Wahllokal_EU24_Beschreibung.pdf](https://download.statistik-berlin-brandenburg.de/5994c00f44d7329a/f38e17070942/RBS_OD_Wahllokal_EU24_Beschreibung.pdf)

## Transformation Steps

* [Geojson converter](../lib/transform/data_geojson_converter.py) converts shape files into geojson
* [Property converter](../lib/transform/data_property_converter.py) renames and removes properties of geojson features
* [Geometry converter](../lib/transform/data_geometry_converter.py) converts inconsistent geometry
* [Projection converter](../lib/transform/data_projection_converter.py) converts geojson to polar projection (epsg:4326)
* [Bounding box converter](../lib/transform/data_bounding_box_converter.py) adds a bounding box to each feature

## Output Ports

### Berlin Electoral Districts Berlin Election 2016
* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-electoral-districts-geodata/tree/main/data/02-silver/berlin-electoral-districts-berlin-election-2016
* license: CC-BY 4.0
* updated: 2025-03-14

**Schema**

| Name | Description |
| --- | --- |
| electoral_district_id | ID of the electoral district (5 digits) |
| postal_voting_district_id | ID of the postal voting district (3 digits + 1 letter) |
| electoral_district_berlin_election_id | ID of the electoral district for the election of House of Representatives (4 digits) |

**Files**

* [berlin-electoral-districts-berlin-election-2016.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-electoral-districts-geodata/main/data/02-silver/berlin-electoral-districts-berlin-election-2016/berlin-electoral-districts-berlin-election-2016.geojson)
### Berlin Electoral Districts Berlin Election 2021
* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-electoral-districts-geodata/tree/main/data/02-silver/berlin-electoral-districts-berlin-election-2021
* license: CC-BY 4.0
* updated: 2025-03-14

**Schema**

| Name | Description |
| --- | --- |
| electoral_district_id | ID of the electoral district (5 digits) |
| electoral_district_id_3 | ID of the polling district (3 digits), unique for each district |
| postal_voting_district_id | ID of the postal voting district (3 digits + 1 letter), first 2 digits represent the district |
| postal_voting_district_id_2 | ID of the postal voting district (1 digit + 1 letter) |
| electoral_district_berlin_election_id | ID of the electoral district for the election of House of Representatives (4 digits) |
| electoral_district_federal_election_id | ID of the electoral district for the federal election (3 digits) |

**Files**

* [berlin-electoral-districts-berlin-election-2021.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-electoral-districts-geodata/main/data/02-silver/berlin-electoral-districts-berlin-election-2021/berlin-electoral-districts-berlin-election-2021.geojson)
### Berlin Electoral Districts European Election 2014
* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-electoral-districts-geodata/tree/main/data/02-silver/berlin-electoral-districts-european-election-2014
* license: CC-BY 4.0
* updated: 2025-03-14

**Schema**

| Name | Description |
| --- | --- |
| electoral_district_id | ID of the electoral district (5 digits) |
| constituency_id | ID of the constituency for Berlin election (4 digits) |
| postal_voting_district_id | ID of the postal voting district (3 digits + 1 letter), first 2 digits represent the district |

**Files**

* [berlin-electoral-districts-european-election-2014.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-electoral-districts-geodata/main/data/02-silver/berlin-electoral-districts-european-election-2014/berlin-electoral-districts-european-election-2014.geojson)
### Berlin Electoral Districts European Election 2019
* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-electoral-districts-geodata/tree/main/data/02-silver/berlin-electoral-districts-european-election-2019
* license: CC-BY 4.0
* updated: 2025-03-14

**Schema**

| Name | Description |
| --- | --- |
| electoral_district_id | ID of the electoral district (5 digits) |
| electoral_district_id_3 | ID of the polling district (3 digits), unique for each district |
| postal_voting_district_id | ID of the postal voting district (3 digits + 1 letter), first 2 digits represent the district |
| postal_voting_district_id_2 | ID of the postal voting district (1 digit + 1 letter) |
| electoral_district_berlin_election_id | ID of the electoral district for the election of House of Representatives (4 digits) |
| electoral_district_federal_election_id | ID of the electoral district for the federal election (3 digits) |

**Files**

* [berlin-electoral-districts-european-election-2019.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-electoral-districts-geodata/main/data/02-silver/berlin-electoral-districts-european-election-2019/berlin-electoral-districts-european-election-2019.geojson)
### Berlin Electoral Districts European Election 2024
* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-electoral-districts-geodata/tree/main/data/02-silver/berlin-electoral-districts-european-election-2024
* license: CC-BY 4.0
* updated: 2025-03-14

**Schema**

| Name | Description |
| --- | --- |
| electoral_district_id | ID of the electoral district (5 digits) |
| electoral_district_id_3 | ID of the polling district (3 digits), unique for each district |
| postal_voting_district_id | ID of the postal voting district (3 digits + 1 letter), first 2 digits represent the district |
| postal_voting_district_id_2 | ID of the postal voting district (1 digit + 1 letter) |
| electoral_district_berlin_election_id | ID of the electoral district for the election of House of Representatives (4 digits) |
| electoral_district_federal_election_id | ID of the electoral district for the federal election (3 digits) |

**Files**

* [berlin-electoral-districts-european-election-2024.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-electoral-districts-geodata/main/data/02-silver/berlin-electoral-districts-european-election-2024/berlin-electoral-districts-european-election-2024.geojson)
### Berlin Electoral Districts Federal Election 2017
* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-electoral-districts-geodata/tree/main/data/02-silver/berlin-electoral-districts-federal-election-2017
* license: CC-BY 4.0
* updated: 2025-03-14

**Schema**

| Name | Description |
| --- | --- |
| electoral_district_id | ID of the electoral district (5 digits) |
| electoral_district_id_3 | ID of the polling district (3 digits), unique for each district |
| postal_voting_district_id | ID of the postal voting district (3 digits + 1 letter), first 2 digits represent the district |
| postal_voting_district_id_2 | ID of the postal voting district (1 digit + 1 letter) |
| electoral_district_berlin_election_id | ID of the electoral district for the election of House of Representatives (4 digits) |
| electoral_district_federal_election_id | ID of the electoral district for the federal election (3 digits) |

**Files**

* [berlin-electoral-districts-federal-election-2017.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-electoral-districts-geodata/main/data/02-silver/berlin-electoral-districts-federal-election-2017/berlin-electoral-districts-federal-election-2017.geojson)
### Berlin Electoral Districts Federal Election 2021
* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-electoral-districts-geodata/tree/main/data/02-silver/berlin-electoral-districts-federal-election-2021
* license: CC-BY 4.0
* updated: 2025-03-14

**Schema**

| Name | Description |
| --- | --- |
| electoral_district_id | ID of the electoral district (5 digits) |
| electoral_district_id_3 | ID of the polling district (3 digits), unique for each district |
| postal_voting_district_id | ID of the postal voting district (3 digits + 1 letter), first 2 digits represent the district |
| postal_voting_district_id_2 | ID of the postal voting district (1 digit + 1 letter) |
| electoral_district_berlin_election_id | ID of the electoral district for the election of House of Representatives (4 digits) |
| electoral_district_federal_election_id | ID of the electoral district for the federal election (3 digits) |

**Files**

* [berlin-electoral-districts-federal-election-2021.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-electoral-districts-geodata/main/data/02-silver/berlin-electoral-districts-federal-election-2021/berlin-electoral-districts-federal-election-2021.geojson)

## Consumers

**Who is the consumer of the Data Product?**

Consumers of this data product may include

* projects that display electoral districts

* other data products that combine geospatial data with statistics data

## Use Cases

**We believe that ...**
**We help achieving ...**
**We know, we are getting there based on ..., ..., ...**

We believe that this data product can be used

* to display data related to electoral districts in Berlin on an interactive map

## Classification

**The nature of the exposed data (source-aligned, aggregate, consumer-aligned)**

source-aligned

## Ubiquitous Language

**Context-specific domain terminology (relevant for Data Product), Data Product polysemes which are used to create the current Data Product**

| Name | Description |
| --- | --- |
| electoral district | German: (Urnen-)Wahlbezirk, UWB |
| postal voting district | German: Briefwahlbezirk, BWB |

---
This data product canvas uses the template of [datamesh-architecture.com](https://www.datamesh-architecture.com/data-product-canvas).