# History map: events project

The goal is to fill the History page (`history.html`) with important events,
country by country, over a long period. Since 2026-10-07 events are not drawn
as pins on the map: they show in the Events list, on the card of a clicked
country and on the deep-time cards. A way to add pins is planned for later, so
every country event still carries `lat` and `lon`. This file tracks what is done, what is
next, and the rules the data follows.

Started 2026-10-07.

## Status

Counts come from `python check_events.py`; update this table after each batch.

| Country | Events | Years covered | Status | Notes |
| --- | ---: | --- | --- | --- |
| Turkey | 69 | 1048 to 2025 | seeded | Seljuks of Rum, the Ottoman Empire and the republic, with the Balkan Wars and the Kurdish conflict. Has an example article. Manzikert (1071) is in the Greece file; Montenegro opening the Balkan Wars (1912) is in the Montenegro file. |
| Japan | 80 | 14000 BCE to 2026 | seeded | Jōmon to Yamato added 2026-10-16. The Daisen Kofun ("mid-5th century") fails the source script and stands. |
| China | 96 | 3300 BCE to 2026 | seeded | Koxinga is in the Taiwan file. The Sanxingdui pits ("12th–11th centuries BC") fail the source script and stand. The Uyghur move west (840) is in the Mongolia file. |
| Germany | 77 | 9 to 2026 | seeded | Königgrätz (1866) is in the Austria file; the Nuremberg Laws and Kristallnacht are in the Israel file; Legnano (1176) in the Italy file. |
| Russia | 89 | 862 to 2026 | seeded | Dates before 1918 are New Style unless marked. Russian conquests in Central Asia are in the Central Asian files; the Treaty of Georgievsk is in the Georgia file. Oleg's move to Kyiv (882) and St Sophia Kyiv (1037) are in the Ukraine file. Nicholas II's abdication is cut back to "Mar 1917": the page gives both calendar dates only in a form the source script cannot match. |
| Austria | 31 | 976 to 2025 | seeded | The sieges of Vienna (1529, 1683) are in the Turkey file. |
| Switzerland | 24 | 1291 to 2026 | seeded | The Peace of Westphalia (1648) is in the Germany file. |
| Finland | 35 | 1249 to 2024 | seeded | |
| Israel | 47 | 1000 BCE to 2026 | seeded | Includes Jewish history outside the land (expulsions, emancipation, the Holocaust). Biblical dates are marked traditional. |
| Italy | 47 | 753 BCE to 2026 | seeded | Rome, Venice and united Italy. Charlemagne's coronation (800) is in the Germany file, Lepanto in the Turkey file. |
| United States | 68 | 1100 to 2026 | seeded | Little on the West after 1848. |
| United Kingdom | 54 | 43 to 2026 | seeded | Some Scotland and Wales since 2026-10-16; little on Ireland or the empire (the East India Company and Plassey are in the India file). |
| France | 44 | 52 BCE to 2025 | seeded | Waterloo is in the United Kingdom file, Borodino in the Russia file. |
| Korea | 44 | 2333 BCE to 2026 | seeded | Both Koreas after 1948. Thin on the Three Kingdoms. |
| India | 48 | 2600 BCE to 2026 | seeded | Thin on the south and on the centuries between the Guptas and 1192. |
| Spain | 39 | 218 BCE to 2026 | seeded | The conquest of Mexico and Peru is left for those countries' files. |
| Portugal | 27 | 1143 to 2026 | seeded | Vasco da Gama's voyage is in the India file. |
| Netherlands | 30 | 1568 to 2026 | seeded | Nothing before the revolt against Spain. |
| Greece | 36 | 1600 BCE to 2024 | seeded | Includes the Byzantine centuries; 1204 is in the Italy file and 1453 in the Turkey file. |
| Egypt | 31 | 3100 BCE to 2022 | seeded | The 1973 war and the peace with Israel are in the Israel file. |
| Iran | 34 | 550 BCE to 2026 | seeded | Chaldiran (1514) is in the Turkey file. |
| Taiwan | 30 | 1624 to 2025 | seeded | Nothing before the Dutch. Dates checked against the source page's text by script. |
| Mexico | 32 | 1200 BCE to 2026 | seeded | Thin on the Maya and on the colonial centuries. San Jacinto (1836) and the fall of Mexico City (1847) are here, not in the United States file. |
| Brazil | 27 | 1532 to 2026 | seeded | Nothing before the Portuguese settlement. Cabral's landing (1500) is in the Portugal file. |
| Poland | 42 | 966 to 2025 | seeded | Poltava-era and 1612 events are in the Russia file, the siege of Vienna (1683) in the Turkey file, the 1939 invasion in the Germany file, the Warsaw Ghetto Uprising and Auschwitz in the Israel file. Little on Lithuania or Ukraine. |
| Sweden | 44 | 829 to 2026 | seeded | Poltava (1709) is in the Russia file; Nystad (1721) and the loss of Finland (1809) are in the Finland file. Dates before 1753 are Old Style where marked. Nothing on the Viking Age beyond Birka. |
| Ireland | 39 | 432 to 2024 | seeded | The whole island, so the Troubles are here. The Union (1801), the Anglo-Irish Treaty (1921) and the Good Friday Agreement (1998) are in the United Kingdom file. |
| Vietnam | 40 | 111 BCE to 2026 | seeded | Dien Bien Phu (1954) is in the France file. Thin on Champa, the Khmer south and the centuries of Chinese rule. |
| Indonesia | 41 | 683 to 2026 | seeded | Batavia (1619) and the transfer of sovereignty (1949) are in the Netherlands file, Malacca (1511) in the Portugal file. Mostly Java and Sumatra. |
| Ethiopia | 38 | 330 to 2026 | seeded | Adwa (1896) is in the Italy file. Includes Eritrea up to 1993. Dates before 1270 are approximate or traditional. |
| South Africa | 43 | 1220 to 2024 | seeded | Dias (1488) is in the Portugal file and the founding of the Cape Colony (1652) in the Netherlands file. Little before the Dutch. |
| Canada | 48 | 1021 to 2026 | seeded | D-Day is in the United States file. Little on First Nations history before contact. |
| Australia | 43 | 1606 to 2025 | seeded | Nothing on the tens of thousands of years before Europeans. Gallipoli is in the Turkey file. |
| Argentina | 42 | 1516 to 2023 | seeded | The Falklands War (1982) is in the United Kingdom file and the Paraguayan War in the Brazil file. Nothing before the Spanish. |
| Ukraine | 37 | 882 to 2026 | seeded | The baptism of Rus' (988), the sack of Kyiv (1240), Pereiaslav (1654), Chernobyl and the annexation of Crimea (2014) are in the Russia file. The Holodomor is here; the Russia file has the wider Soviet famine. The 2022 invasion is here; the claimed annexations (2022) are in the Russia file. |
| Hungary | 34 | 895 to 2026 | seeded | Lechfeld (955) is in the Germany file, Mohács (1526) and Karlowitz (1699) in the Turkey file, the Compromise of 1867 in the Austria file. |
| Czechia | 36 | 863 to 2025 | seeded | The Defenestration of 1618 and the Munich Agreement are in the Germany file; Austerlitz and Königgrätz in the Austria file. Czechoslovak events are here, so Slovakia is not yet covered on its own. |
| Denmark | 35 | 965 to 2024 | seeded | The Kalmar Union, the Stockholm Bloodbath, Roskilde (1658) and Kiel (1814) are in the Sweden file. Includes Greenland. |
| Norway | 33 | 872 to 2022 | seeded | Kiel (1814) and the end of the union (1905) are in the Sweden file; the Oslo Accords in the Israel file. |
| Thailand | 36 | 1238 to 2026 | seeded | Nothing before Sukhothai (Dvaravati, the Khmer period). |
| Philippines | 34 | 900 to 2026 | seeded | The Treaty of Paris (1898) is in the Spain file. Thin before 1521. |
| Peru | 41 | 2600 BCE to 2026 | seeded | Ayacucho (1824) is in the Spain file. Dates before 1438 are approximate. |
| Iraq | 34 | 3200 BCE to 2023 | seeded | Gaugamela, al-Qadisiyyah, the Mongol sack of Baghdad (1258) and the war of 1980 are in the Iran file; the Babylonian exile in the Israel file. Dates before 600 BCE are approximate. The killing of Soleimani at Baghdad airport (2020) is in the Iran file. |
| Saudi Arabia | 33 | 570 to 2024 | seeded | Covers the life of Muhammad and the holy cities, then the Saudi states. Little on Arabia before Islam. The September 11 attacks are in the United States file. |
| Pakistan | 36 | 127 to 2025 | seeded | The Indus cities, the Hydaspes, Partition and the 1971 war are in the India file. Thin before 1800. The 2025 conflict with India is in the India file. |
| Chile | 34 | 1520 to 2025 | seeded | The crossing of the Andes is in the Argentina file; Angamos, the occupation of Lima and the Treaty of Ancón in the Peru file. Nothing before the Spanish. |
| Colombia | 31 | 1525 to 2026 | seeded | Nothing on the Muisca or other peoples before the conquest. |
| Cuba | 32 | 1492 to 2024 | seeded | The Missile Crisis is in the United States file and the Treaty of Paris (1898) in the Spain file. |
| Nigeria | 34 | 500 BCE to 2026 | seeded | Dates before 1472 are approximate. Thin on Kanem-Bornu and the Hausa states. |
| Morocco | 40 | 40 to 2026 | seeded | Ceuta (1415) and Alcácer Quibir (1578) are in the Portugal file, Las Navas de Tolosa in the Spain file. |
| Afghanistan | 39 | 330 BCE to 2026 | seeded | |
| Albania | 32 | 627 BCE to 2025 | seeded | |
| Algeria | 32 | 202 BCE to 2026 | seeded | |
| Angola | 28 | 1390 to 2022 | seeded | |
| Armenia | 33 | 782 BCE to 2026 | seeded | The 2020 war and the 2023 offensive are in the Azerbaijan file. |
| Azerbaijan | 35 | 84 to 2024 | seeded | |
| Bangladesh | 35 | 300 BCE to 2026 | seeded | Partition and 1971 are in the India file. |
| Belarus | 31 | 862 to 2021 | seeded | |
| Belgium | 32 | 54 BCE to 2025 | seeded | Waterloo is in the United Kingdom file. |
| Bolivia | 32 | 800 to 2025 | seeded | |
| Bosnia and Herzegovina | 31 | 1189 to 2025 | seeded | |
| Bulgaria | 37 | 251 to 2026 | seeded | |
| Cambodia | 31 | 245 to 2023 | seeded | The 2025 border war is in the Thailand file. |
| Croatia | 37 | 305 to 2023 | seeded | |
| Democratic Republic of the Congo | 36 | 900 to 2026 | seeded | |
| Dominican Republic | 35 | 1494 to 2025 | seeded | |
| Ecuador | 32 | 3500 BCE to 2025 | seeded | |
| Estonia | 35 | 1030 to 2026 | seeded | |
| Georgia | 36 | 302 BCE to 2026 | seeded | |
| Ghana | 36 | 2500 BCE to 2025 | seeded | |
| Guatemala | 31 | 300 BCE to 2024 | seeded | |
| Haiti | 33 | 1492 to 2024 | seeded | |
| Iceland | 32 | 874 to 2024 | seeded | |
| Jordan | 31 | 7200 BCE to 2021 | seeded | |
| Kazakhstan | 28 | 3700 BCE to 2026 | seeded | |
| Kenya | 34 | 750 to 2024 | seeded | The Kenyan-led mission to Haiti (2024) is in the Haiti file. |
| Laos | 23 | 1353 to 2021 | seeded | |
| Latvia | 33 | 1186 to 2026 | seeded | |
| Lebanon | 34 | 1000 BCE to 2026 | seeded | |
| Libya | 34 | 631 BCE to 2026 | seeded | |
| Lithuania | 37 | 1009 to 2025 | seeded | |
| Malaysia | 30 | 450 to 2022 | seeded | |
| Mali | 29 | 250 BCE to 2026 | seeded | |
| Mongolia | 35 | 209 BCE to 2022 | seeded | |
| Mozambique | 26 | 1200 to 2024 | seeded | |
| Myanmar | 35 | 832 to 2026 | seeded | |
| Nepal | 31 | 563 BCE to 2026 | seeded | |
| New Zealand | 33 | 1300 to 2026 | seeded | |
| North Macedonia | 29 | 350 BCE to 2025 | seeded | |
| Papua New Guinea | 28 | 5000 BCE to 2024 | seeded | |
| Paraguay | 32 | 1537 to 2023 | seeded | The Paraguayan War is in the Brazil file. |
| Romania | 40 | 106 to 2026 | seeded | |
| Rwanda | 28 | 1600 to 2024 | seeded | |
| Senegal | 30 | 1035 to 2024 | seeded | |
| Serbia | 40 | 269 to 2026 | seeded | |
| Singapore | 30 | 1299 to 2024 | seeded | |
| Slovakia | 34 | 179 to 2024 | seeded | |
| Slovenia | 34 | 14 to 2026 | seeded | |
| Sri Lanka | 34 | 288 BCE to 2024 | seeded | |
| Sudan | 35 | 2500 BCE to 2026 | seeded | Includes South Sudan's independence (2011). |
| Syria | 36 | 2300 BCE to 2026 | seeded | |
| Tanzania | 28 | 960 to 2025 | seeded | |
| Tunisia | 34 | 814 BCE to 2022 | seeded | |
| Uganda | 29 | 1400 to 2026 | seeded | |
| Uruguay | 34 | 1624 to 2025 | seeded | |
| Uzbekistan | 33 | 329 BCE to 2023 | seeded | |
| Venezuela | 33 | 1498 to 2026 | seeded | |
| Yemen | 33 | 685 BCE to 2026 | seeded | |
| Zimbabwe | 27 | 1300 to 2024 | seeded | |
| Bahamas | 19 | 1648 to 2021 | seeded | Columbus's first landfall (1492) is in the Spain file. |
| Bahrain | 19 | 2300 BCE to 2022 | seeded | The Abraham Accords (2020) are in the Israel file. |
| Barbados | 19 | 1625 to 2021 | seeded | |
| Belize | 19 | 1200 BCE to 2020 | seeded | |
| Benin | 24 | 1600 to 2026 | seeded | |
| Bhutan | 25 | 747 to 2023 | seeded | Standing fail: Guru Rinpoche (about 747; the source page says 8th century). |
| Botswana | 24 | 1600 to 2024 | seeded | |
| Brunei | 21 | 977 to 2019 | seeded | |
| Burkina Faso | 26 | 1050 to 2026 | seeded | The Alliance of Sahel States (2023) is in the Mali file. |
| Burundi | 24 | 1680 to 2020 | seeded | |
| Cameroon | 24 | 1394 to 2025 | seeded | |
| Cape Verde | 16 | 1460 to 2024 | seeded | |
| Central African Republic | 21 | 3500 BCE to 2023 | seeded | |
| Chad | 26 | 2000 BCE to 2022 | seeded | |
| Comoros | 19 | 1500 to 2024 | seeded | Standing fail: the sultanates (about 1500; the page says by the 15th century). |
| Costa Rica | 28 | 1502 to 2026 | seeded | |
| Cyprus | 32 | 7000 BCE to 2018 | seeded | Author's own version. |
| Djibouti | 17 | 1577 to 2021 | seeded | |
| East Timor | 24 | 1512 to 2025 | seeded | The 1975 invasion and 1999 referendum are in the Indonesia file. |
| El Salvador | 25 | 600 to 2024 | seeded | The Football War is in the Honduras file. |
| Equatorial Guinea | 20 | 1472 to 2021 | seeded | |
| Eritrea | 21 | 100 to 2018 | seeded | Ethiopia file has Eritrea to 1993. Standing fail: Adulis (about 100; the page says 1st century). |
| Eswatini | 18 | 1815 to 2021 | seeded | |
| Fiji | 22 | 1500 BCE to 2022 | seeded | |
| Gabon | 20 | 1472 to 2025 | seeded | |
| Gambia | 20 | 927 to 2021 | seeded | Senegambia (1982) is in the Senegal file. |
| Guinea | 22 | 1725 to 2023 | seeded | |
| Guinea-Bissau | 22 | 1446 to 2025 | seeded | |
| Guyana | 21 | 1616 to 2023 | seeded | |
| Honduras | 28 | 426 to 2025 | seeded | |
| Ivory Coast | 24 | 1710 to 2024 | seeded | The map name is "Cote D'Ivoire". |
| Jamaica | 28 | 650 to 2025 | seeded | |
| Kosovo | 29 | 1321 to 2018 | seeded | Author's own version. |
| Kuwait | 19 | 2000 BCE to 2024 | seeded | The 1990 invasion and 1991 liberation are in the Iraq file. |
| Kyrgyzstan | 28 | 2500 BCE to 2026 | seeded | The map name is "Kyrgyz Republic". Standing fail: Pishpek and Tokmok (1862; the pages give no year in the text). |
| Lesotho | 24 | 1822 to 2022 | seeded | |
| Liberia | 25 | 1462 to 2023 | seeded | |
| Luxembourg | 25 | 963 to 2014 | seeded | Author's own version. |
| Madagascar | 28 | 1610 to 2025 | seeded | |
| Malawi | 27 | 1480 to 2024 | seeded | |
| Maldives | 20 | 500 BCE to 2023 | seeded | Standing fail: Ibn Battuta (1344; the pages say the 1340s). |
| Malta | 24 | 3600 BCE to 2017 | seeded | Author's own version. |
| Mauritania | 20 | 1076 to 2024 | seeded | The Western Sahara War is in the Morocco file. |
| Mauritius | 24 | 1507 to 2025 | seeded | |
| Moldova | 25 | 1436 to 2019 | seeded | Author's own version. |
| Montenegro | 28 | 1042 to 2017 | seeded | Author's own version. |
| Namibia | 26 | 1872 to 2024 | seeded | |
| Nicaragua | 28 | 1200 to 2023 | seeded | |
| Niger | 25 | 1449 to 2026 | seeded | Sonni Ali and Askia are in the Mali file. The Alliance of Sahel States (2023) is in the Mali file. |
| Oman | 25 | 630 to 2018 | seeded | Author's own version. |
| Palestine | 29 | 691 to 2025 | seeded | Balfour, the mandate, Oslo and Gaza 2005 are in the Israel file. The 7 October attack (2023) is in the Israel file; the Gaza war and the 2025 ceasefire are here. |
| Panama | 26 | 1501 to 2024 | seeded | The 1903 separation is in the Colombia file. |
| Qatar | 23 | 1766 to 2026 | seeded | |
| Republic of the Congo | 22 | 1550 to 2021 | seeded | Congo-Brazzaville; Diogo Cão (1482) is in the Angola file. |
| Sierra Leone | 30 | 1462 to 2023 | seeded | |
| Solomon Islands | 19 | 1568 to 2022 | seeded | Guadalcanal (1942) is in the United States file. |
| Somalia | 31 | 1269 to 2025 | seeded | The Ogaden War is in the Ethiopia file. |
| South Sudan | 22 | 1490 to 2026 | seeded | The 2011 independence referendum is in the Sudan file. |
| Suriname | 20 | 1650 to 2025 | seeded | The map name is "Surinam". |
| Tajikistan | 26 | 3000 BCE to 2025 | seeded | The 2022 border war is in the Kyrgyzstan file. |
| Togo | 20 | 1600 to 2024 | seeded | |
| Trinidad and Tobago | 21 | 5000 BCE to 2025 | seeded | |
| Turkmenistan | 29 | 2200 BCE to 2022 | seeded | |
| United Arab Emirates | 26 | 2600 BCE to 2017 | seeded | Author's own version. The Abraham Accords (2020) are in the Israel file. |
| Zambia | 25 | 1600 to 2026 | seeded | |

Deep time (see the section below); the span is in millions of years ago:

| Scope | File | Events | Span (Ma) | Status | Notes |
| --- | --- | ---: | --- | --- | --- |
| Universe, Milky Way | `deep/universe.json` | 26 | 13800 to 4900 | researched | Weakest date: when the expansion began to speed up (sources say 5 to 6 billion years ago). |
| Solar System | `deep/solar-system.json` | 13 | 4600 to 3700 | researched | No entry for Mars losing its water: no datable source found. |
| Earth | `deep/earth.json` | 39 | 4500 to 0.0117 | researched | Six entries have site coordinates, all taken from Wikipedia. |
| Life | `deep/life.json` | 49 | 4280 to 0.023 | researched | Most dates confirmed on Wikipedia only; journal sites and the ICS chart would not load. |

Status values:

- **not started**: no file yet.
- **seeded**: a first pass of the best-known events, written from general
  knowledge with a source link per event. Dates and coordinates have not been
  checked against the source one by one.
- **researched**: written by a research pass that opened a source for each
  event and looked for the figure on it. Many checks went through a page
  summariser, not the raw text, and some uncertainty notes rest on general
  knowledge, so this is better than seeded but is not a human review.
- **reviewed**: every event checked against its source.
- **done**: reviewed, and the coverage feels complete for now.

## Next up

In rough order, following the reading list on the Books page:

The aim (stated by the author on 2026-10-08) is to cover most countries in
the world. As of 2026-10-09 every country that has a polygon in the 2019
snapshot has an events file: the world is covered. Since 2026-10-28 the time
bar runs to 2026; CShapes ends in 2019, so the stops from 2020 on reuse the
2019 borders. What remains:

- States too small to have a polygon on the 2019 map (Andorra, Liechtenstein,
  Monaco, San Marino, Vatican City, most Pacific microstates) have no file;
  worth adding only if the event list alone justifies them (they would still
  show in the Events list and on a neighbour's card).
- North Korea and South Korea are covered together in the Korea file;
  Western Sahara is folded into the Morocco file.
- Gaps in the seeded countries are listed below; deepening those files is
  the obvious next work.

Gaps in the seeded countries:

- The gaps listed for Turkey, Japan, China, Germany, Russia, the United
  States and the United Kingdom were filled on 2026-10-16 (see the Log).
- United Kingdom: Ireland and the empire.
- United States: the West after 1848.
- 2020 to 2026: the pass of 2026-10-29 added 78 events from 2026 (to 28
  Oct 2026), found by web search; smaller countries still have nothing
  for 2026, and very recent entries (Brazil's runoff, Israel's and
  Serbia's elections, the Toledo collision) should be rechecked once
  results and tolls settle. The eight
  files in the author's own versions (Cyprus, Kosovo, Luxembourg, Malta,
  Moldova, Montenegro, Oman, the United Arab Emirates) and Brunei and
  Eritrea got nothing after 2019.
- Every country file has now had one `check_sources.py` pass; the next
  step up is a review (each event read against its source) to move files
  from seeded to reviewed.

## How to add events

1. Add events to `history/events/<country>.json`. For a new country, create the
   file and add its name to `history/events/list.json`.
2. Run `python check_events.py` and fix anything it reports.
   Then run `python check_sources.py history/events/<country>.json`, which
   looks for each event's year and day on its Wikipedia source page, and
   look at whatever it flags.
3. Update the status table above.

One file per country means the present-day country whose history the event
belongs to, not where it happened: the Treaty of Lausanne is in `turkey.json`
and Pearl Harbor is in `japan.json`.

### Fields

```json
{
  "id": "germany-1871-german-empire-proclaimed",
  "title": "German Empire proclaimed",
  "date": "18 Jan 1871",
  "year-from": 1871,
  "year-to": 1871,
  "place": "Versailles, France",
  "lat": 48.805,
  "lon": 2.12,
  "country": "Germany",
  "polity": "Kingdom of Prussia",
  "importance": 1,
  "description": "One sentence on what happened and why it matters.",
  "source": "https://en.wikipedia.org/wiki/Proclamation_of_the_German_Empire",
  "link": "history/some-article.html#anchor"
}
```

- `id`: `<country>-<year>-<title>` in lowercase with hyphens. Never reuse or
  change one once published.
- `date`: the text shown to the reader. `year-from` and `year-to` decide when
  the event is shown; BCE years are negative. `year-to` is optional.
- `lat`, `lon`: where the event happened, in decimal degrees. For a battle at
  sea or a disputed site, use the conventional location and say so in `place`.
- `importance`: 1 for the events everyone should see, 2 for the next tier, 3
  for details. The deep-time cards show the most important first. Aim for
  roughly a third of a country's events at level 1.
- `source`: required. A page where the date and place can be checked.
- `polity`: optional, the state at the time when it differs from the country.
- `link`: optional, an article on this site; the event's title becomes a link.

### Conventions

- An event needs a specific place and a specific date or short span. Long
  processes ("industrialisation") do not get a dot; pick the moment that stands
  for them.
- Descriptions are one neutral sentence.

## Deep time: universe, Solar System, Earth, life

From 1 billion years ago the map shows the reconstructed land in colour, one
colour and label per part of today's world it belongs to (North America,
Africa, India and so on), with a card beside it listing the main events of the
stretch and naming the supercontinent where there is one. The groups come from
the plate each coastline piece sits on today (GPlates plate ids, first digit);
about 2% of small pieces could not be matched and stay grey. The files are
`history/paleo/<Ma>.json`, with `0.json` (today's positions) used for the 5, 2
and 0.3 million year stops.

The time bar starts at the Big Bang. Stops before 1 billion years ago have no
map: `drawScene` in `history.html` draws a schematic illustration for each
stretch (Big Bang, first stars, early galaxies, the Milky Way, the solar
nebula, the molten Earth and Moon, the early ocean Earth). Every deep-time
stop now has at least one event.

Events before written history live in `history/events/deep/`, one file per
scope: `universe.json` (including the Milky Way), `solar-system.json`,
`earth.json` (geology, atmosphere, climate, impacts, supercontinents) and
`life.json` (origin of life to the first modern humans). They are listed in
`history/events/list.json` like the country files.

```json
{
  "id": "deep-4567-first-solids-in-the-solar-system",
  "title": "First solids in the Solar System",
  "date": "4.567 billion years ago",
  "ma": 4567,
  "ma-to": 4560,
  "scope": "Solar System",
  "importance": 1,
  "description": "One or two neutral sentences on what happened and how we know.",
  "uncertainty": "Dated to within about a million years from meteorite inclusions.",
  "source": "https://...",
  "place": "Jack Hills, Western Australia",
  "lat": -26.17,
  "lon": 116.98
}
```

- `id`: `deep-<ma>-<title>` in lowercase with hyphens.
- `ma`: when it happened or began, in millions of years ago (13800 for the Big
  Bang, 0.3 for 300,000 years ago). `ma-to` is optional, for the end of a span,
  and is the smaller number.
- `date`: the text shown to the reader, in the form "13.8 billion years ago",
  "541 million years ago", "300,000 years ago", or a span "2.4 to 2.1 billion
  years ago". Add "about" when the figure is rough.
- `scope`: one of `Universe`, `Milky Way`, `Solar System`, `Earth`, `Life`. It
  appears in the country filter.
- `importance`: 1 to 3, as for country events.
- `uncertainty`: optional but expected whenever the date or the event itself is
  debated. One sentence saying how firm the figure is or what the range is.
- `source`: required. Prefer a primary or institutional source (a journal
  paper, NASA, ESA, the International Commission on Stratigraphy, a geological
  survey, a university or museum page); Wikipedia is acceptable.
- `place`, `lat`, `lon`: optional, only where the evidence comes from one
  site (an impact crater, a fossil bed). These are today's coordinates. They
  are not drawn as dots yet, because the continents were elsewhere.

## How events show on the map

- Before 1886 the time bar only stops at the available border snapshots, so an
  event shows for the whole stretch up to the next stop (an 1848 event is
  visible from the 1815 stop until 1878).
- From 1886 there is a stop for every year, so a single-year event is visible
  for one step. The stops from 2020 to 2026 show the 2019 borders, labelled
  as such.

- Every deep-time stop has a card with the five most important events of its
  stretch; all of them appear in the Events list with their uncertainty.

### Clicking a country

Clicking a country zooms in on it and opens a card beside it with that
country's events: those of the current stop in full, the rest as a list that
jumps to their year. The map's names are not the event files' names ("Turkey
(Ottoman Empire)", "Holy Roman Empire"), so an event country is matched when:

- the map's name contains it as a word,
- more than half of the country's events happened inside the clicked borders,
- or the name is listed under `COUNTRY_ALIASES` in `history.html`.

Events of the current stop that happened inside the borders are shown whatever
country they belong to. An event whose `polity` is exactly the map's name is
also shown on that card, alone, without bringing in the rest of its country:
clicking Japan lists Taiwan's events under Japanese rule, not all of Taiwan's.

## Ideas, not started

- Let single-year events linger for a few years so they do not flash past
  during auto-play.
- Sort events within the same year by month and day.
- A second map layer for themes that cross countries (trade routes, religions).
- Dots for deep-time events that have a site, by moving today's coordinates
  with the same plate model as the coastlines (GPlates can reconstruct points).

## Log

- 2026-10-29: Added 100 events from web research, 10 per region by ten
  agents: 78 from 2026 (to 28 Oct) and 22 important ones from 2020 to
  2025 that were missing (Navalny's poisoning, Russia's mobilization, the
  fall of Mariupol, Operation Spiderweb, the Gaza famine, El Fasher, the
  Bondi and Wang Fuk Court disasters and others). The 2026 events include
  Maduro's capture, the killing of Ali Khamenei and the Iran war, the
  Lebanon war, Orbán's defeat, Burnham becoming prime minister, Yoon's
  life sentence and elections across every region. Each was confirmed on
  its Wikipedia page by the agent; the author's own files got nothing.
  `check_sources.py` passes all 100 new events. 5708 events in 178
  files; `python3 check_events.py` reports no problems.

- 2026-10-28: Brought the map to 2026. The time bar now runs to 2026;
  CShapes ends in 2019, so `loadYear` in `history.html` reads the 2019
  borders for every later stop and the label says "borders as of 2019 (no
  newer data)". Changes since then, such as Russia's claimed annexations
  in Ukraine, are not drawn. 357 events were added to 164 country files,
  1 to 6 per file, almost all from 2020 to 2025 (plus the Wuhan outbreak
  and the Whakaari eruption from late 2019): COVID-19, the invasion of
  Ukraine, 7 October and the Gaza war, the fall of Assad, coups in the
  Sahel, and elections and disasters everywhere. The only 2026 event is
  Bulgaria adopting the euro (1 Jan); 2026 is otherwise empty, because
  the pass was written from knowledge that ends around mid-2026. The
  eight files in the author's own versions, Brunei and Eritrea got
  nothing new. Finland's NATO accession (2023) and Sweden's (2024) are now
  in. `check_sources.py` flagged 34 of the new events; wrong or missing
  page titles were replaced, and dates were cut back to month or year
  where the page did not show the day (Xi's third term, Astana's
  renaming, the Pope's Bahrain visit, the 222 Nicaraguan prisoners, Costa
  Rica joining the OECD, Togo's new constitution, the Solomon Islands'
  pact with China). A second script checked that each new event's names
  (people, places, the country near the year) appear on its source page;
  all did. Weak source to replace in a review: costa-rica-2021 (the OECD
  article only lists Costa Rica as a member). All new events pass both
  checks. 5608 events in 178 files; `python3 check_events.py` reports no
  problems.
- 2026-10-18 (night): Merged an independent second pass, run on the same
  day as the 2026-10-16 pass without knowledge of it. Both had deepened
  Turkey, Japan, China, Germany and Russia along the listed gaps; events
  written by both were kept once, in the 2026-10-16 pass's words. Kept
  from the second pass: in Turkey, Kapetron (1048), Dorylaeum (1097), the
  PKK's founding (1978), the retaking of Edirne (1913) and 2017 to 2019;
  in Japan, the Jōmon period itself (about 14000 BCE), Yayoi, Jimmu, the
  first keyhole kofun, Michizane's exile and 2013 to 2019; in China, the
  60 BCE Protectorate of the Western Regions, Songtsen Gampo, Quanzhou's
  trade office, the White Lotus Rebellion, the Seventeen Point Agreement,
  Yakub Beg, the Qing reconquest, the PRC takeover of Xinjiang and 2013
  to 2019; in Germany, the Lübeck–Hamburg alliance, Conradin, Siemens,
  Bayer, the nuclear exit and 2015 to 2018; in Russia, the Congress of
  Lyubech, Mstislav the Great's death, Shamil becoming imam, the
  Central-Asian steps of 1853 to 1867 (Ak-Mechet, Turkestan, the
  governor-generalship), Dudayev's declaration, Nemtsov, the Crimean
  bridge and the 2018 World Cup. Filled the four deep-time stops that had
  no events (9, 7 and 5 billion years ago, 880 million years ago):
  universe.json grows to 26 (the cosmic afternoon, the Sequoia merger, a
  Milky Way star-forming episode, Murchison stardust, El Gordo), earth to
  39 (the Boring Billion, Rodinia at its greatest extent) and life to 49
  (the protosterol "lost world"); every stop now has something on its
  card. The source script now accepts thousands separators in a year
  ("14,000 BC"); the movable-type event was respanned 1039 to 1048 and
  Nicholas II's abdication cut back to "Mar 1917", matching their pages.
- 2026-10-18: Recent-history pass. The 74 country files whose latest
  event was before 2015 each gained 2 to 4 events from the years up to
  the map's 2019 snapshot: landmark elections and changes of power,
  referendums and reforms, disasters, conflict milestones and
  international firsts. Events already on the 2026-10-16 side or in
  another country's file were kept out (the bin Laden raid in Pakistan,
  the 2018 Trump–Kim summit in Singapore, Eritrea–Ethiopia peace in
  Ethiopia, Russia's Syria intervention in Syria, the Prespa Agreement in
  North Macedonia, the Habré verdict in Chad, the 2002 euro introduction
  and 2015 refugee decision in Germany). Three dates were cut back where
  the source page did not state the day: Mladić convicted (2017), Merkel
  stepping down as CDU leader (Dec 2018), Mongolia's constitutional
  amendments (2019).   `python3 check_events.py` reports no problems; `check_sources.py`
  passes on the day's additions apart from the earlier standing fails
  (Daisen Kofun, Sanxingdui, Bigo, the Kabaka's palace attack), which
  stand as noted on 2026-10-16; 5251 events in 178 files.
- 2026-10-16: Five agents. (1) Filled the listed gaps: Turkey +16
  (Seljuks of Rum, Balkan Wars, Kurdish conflict), Russia +17 (before
  1240, the Caucasus, the Chechen wars), Japan +16 (Jōmon to Yamato,
  Heian, Meiji economy), China +17 (Shang and earlier, Song economy,
  Ming–Qing, Tibet and Xinjiang), Germany +13, United States +11 and
  United Kingdom +11. Events already in another country's file were
  left there. (2) Ran `check_sources.py` on the 58 files registered on
  2026-10-09 (all but Iceland): 76 events flagged, 64 fixed (wrong days,
  missing or wrong source pages, dates cut back to month or year).
  Some dates moved away from the year in their id, which stays
  unchanged: angola-1483 (now 1482), rwanda-1853 (1867), senegal-1444
  (1445), slovakia-828 (827), sri-lanka-bce250 (247 BCE), zimbabwe-1684
  (1683). Twelve stand because the page gives only a century or range,
  or states the day in a form the script cannot match: Incallajta
  (Bolivia), Begho (Ghana), Shanga and Gedi (Kenya), and the Malaysia
  450, Nepal 250 BCE, North Macedonia 350 BCE, Papua New Guinea 5000
  BCE, Rwanda 1600, Bigo (Uganda), Mozambique 1498 and Uganda 1966
  events. Weak sources to replace in a review: slovakia-1610 (Synod of
  Žilina, no English page) and paraguay-1992 (a year article). With the
  new Daisen Kofun, Sanxingdui and the older Nicholas II abdication,
  those are all the standing fails in the touched files. 4972 events in
  178 files; `python3 check_events.py` reports no problems.
- 2026-10-09 (later): Completed the world. Agents wrote 57 of the last 65
  country files (see the table above); the author committed the other eight
  (Cyprus, Kosovo, Luxembourg, Malta, Moldova, Montenegro, Oman and the
  United Arab Emirates) in their own versions. The whole 2019 map is
  covered: 4871 events in 178 files. `python3 check_events.py` reports no
  problems. The source script passed on the new agent files except five
  events that stand with looser dates, all noted in the table: Guru
  Rinpoche in Bhutan (about 747), the sultanates of the Comoros (about
  1500), Adulis in Eritrea (about 100), Ibn Battuta in the Maldives (1344)
  and Pishpek and Tokmok in Kyrgyzstan (1862). Shared events that already
  lived in another country's file were kept out of the new files; the
  table's notes say where.
- 2026-10-09: Registered 59 country files in `list.json` that were already on
  disk but never listed, from Afghanistan to Zimbabwe (see the table above):
  3477 events in 113 files, `python3 check_events.py` reports no problems.
  The source script was run on Iceland (0 problems); the rest of the batch
  still needs a `check_sources.py` pass. The countries still without a file
  are listed by region under Next up.
- 2026-10-08 (later still): Seeded Iraq (31), Saudi Arabia (31), Pakistan
  (29), Chile (30), Colombia (28), Cuba (30), Nigeria (31) and Morocco (33),
  and ran the source script on them. One event still fails and stands: the
  Igbo-Ukwu bronzes (year 850; the page says 9th century).
- 2026-10-08 (later): Seeded Ukraine (29), Hungary (28), Czechia (29),
  Denmark (29), Norway (28), Thailand (31), Philippines (30) and Peru (33),
  and ran the source script on them. One event still fails and stands: the
  Lord of Sipán ("about 250"; the page says the platform was built before
  300). The remaining countries are now listed by region under Next up.
- 2026-10-08: Seeded Poland (34), Sweden (37), Ireland (36), Vietnam (34),
  Indonesia (34), Ethiopia (33), South Africa (38), Canada (37), Australia
  (35) and Argentina (36). Mexico (25) and Brazil (22), added in an earlier
  session, entered in the table. The source script was rebuilt (it was not in
  the repository; it is now `check_sources.py`) and run on all twelve: every
  source page exists, and where the day was not on the page the date was cut
  back to the month or year, or the source changed. In the Mexico file
  Pakal's death was corrected to 29 Aug 683 and the fall of Mexico City cut
  back to Sep 1847. Two events still fail and stand: Brazil's gold find
  (year 1693; the page says "1690s" and 1695) and the Lalibela churches
  ("about 1200"; the page gives the king's reign as about 1181 to 1221).
- 2026-10-07 (night): Seeded Greece (30), Egypt (26) and Iran (27).
- 2026-10-07 (night): Seeded Spain (30), Portugal (21) and the Netherlands (24).
- 2026-10-07 (night): Japan extended to 51, China to 54, Germany to 50 and
  Russia to 54.
- 2026-10-07 (night): Seeded Korea (35) and India (37).
- 2026-10-07 (night): Seeded Italy (39), the United States (41), the United
  Kingdom (38) and France (40).
- 2026-10-07 (night): Seeded Israel and Jewish history (41). A polity match on
  a country card now brings in only the events with that polity. The source
  check now ignores citations, which caught four dates that were not in the
  page text; three were corrected (Michael Romanov's election, Turkey joining
  NATO, the French emancipation decree).
- 2026-10-07 (night): Seeded Austria (24), Switzerland (18) and Finland (28).
- 2026-10-07 (night): Turkey extended to the whole Ottoman period and the
  republic (41).
- 2026-10-07 (night): Seven deep-time events added so the 280, 120 and 100
  million year stops have something on their cards.
- 2026-10-07 (night): Seeded Taiwan (23). From this batch on, a script checks
  that each source page exists and that the event's year and day appear in
  its text; that is weaker than reading the page, so the status stays seeded.
- 2026-10-07 (evening): Pins removed from the map for now. Deep-time land
  coloured and labelled by present-day region, with a notes card beside it.
- 2026-10-07 (later): Clicking a country zooms in and shows its events on a
  card. Greenland added to the 1886 to 2019 maps. Seeded Russia (23). Time bar
  extended to the Big Bang with illustrations, and 111 deep-time events
  researched by three agents: 201 events in all.
- 2026-10-07: Project set up. Per-country files, validator, country filter,
  grouped dots. Seeded Turkey (moved from the Ottoman example), Japan, China
  and Germany: 67 events.
