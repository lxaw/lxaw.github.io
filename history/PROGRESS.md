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
| Turkey | 41 | 1299 to 2016 | seeded | Ottoman Empire and the republic. Has an example article. |
| Japan | 51 | 538 to 2011 | seeded | Nothing before the arrival of Buddhism. |
| China | 54 | 1250 BCE to 2008 | seeded | |
| Germany | 50 | 9 to 1990 | seeded | Königgrätz (1866) is in the Austria file; the Nuremberg Laws and Kristallnacht are in the Israel file. |
| Russia | 54 | 862 to 2014 | seeded | Dates before 1918 are New Style unless marked. |
| Austria | 24 | 976 to 1995 | seeded | The sieges of Vienna (1529, 1683) are in the Turkey file. |
| Switzerland | 18 | 1291 to 2002 | seeded | The Peace of Westphalia (1648) is in the Germany file. |
| Finland | 28 | 1249 to 1995 | seeded | Nothing after 1995 (NATO, 2023, is past the map's last year). |
| Israel | 41 | 1000 BCE to 2005 | seeded | Includes Jewish history outside the land (expulsions, emancipation, the Holocaust). Biblical dates are marked traditional. |
| Italy | 39 | 753 BCE to 1992 | seeded | Rome, Venice and united Italy. Charlemagne's coronation (800) is in the Germany file, Lepanto in the Turkey file. |
| United States | 41 | 1100 to 2008 | seeded | Little before 1607 and nothing on the West before 1848. |
| United Kingdom | 38 | 43 to 2016 | seeded | Mostly England before 1707; little on Scotland, Wales, Ireland or the empire. |
| France | 40 | 52 BCE to 2015 | seeded | Waterloo is in the United Kingdom file, Borodino in the Russia file. |
| Korea | 35 | 2333 BCE to 2006 | seeded | Both Koreas after 1948. Thin on the Three Kingdoms. |
| India | 37 | 2600 BCE to 1992 | seeded | Thin on the south and on the centuries between the Guptas and 1192. |
| Spain | 30 | 218 BCE to 2004 | seeded | The conquest of Mexico and Peru is left for those countries' files. |
| Portugal | 21 | 1143 to 1999 | seeded | Vasco da Gama's voyage is in the India file. |
| Netherlands | 24 | 1568 to 2001 | seeded | Nothing before the revolt against Spain. |
| Greece | 30 | 1600 BCE to 2010 | seeded | Includes the Byzantine centuries; 1204 is in the Italy file and 1453 in the Turkey file. |
| Egypt | 26 | 3100 BCE to 2013 | seeded | The 1973 war and the peace with Israel are in the Israel file. |
| Iran | 27 | 550 BCE to 2015 | seeded | Chaldiran (1514) is in the Turkey file. |
| Taiwan | 23 | 1624 to 2014 | seeded | Nothing before the Dutch. Dates checked against the source page's text by script. |
| Mexico | 25 | 1200 BCE to 2000 | seeded | Thin on the Maya and on the colonial centuries. San Jacinto (1836) and the fall of Mexico City (1847) are here, not in the United States file. |
| Brazil | 22 | 1532 to 2016 | seeded | Nothing before the Portuguese settlement. Cabral's landing (1500) is in the Portugal file. |
| Poland | 34 | 966 to 2010 | seeded | Poltava-era and 1612 events are in the Russia file, the siege of Vienna (1683) in the Turkey file, the 1939 invasion in the Germany file, the Warsaw Ghetto Uprising and Auschwitz in the Israel file. Little on Lithuania or Ukraine. |
| Sweden | 37 | 829 to 2003 | seeded | Poltava (1709) is in the Russia file; Nystad (1721) and the loss of Finland (1809) are in the Finland file. Dates before 1753 are Old Style where marked. Nothing on the Viking Age beyond Birka. |
| Ireland | 36 | 432 to 2015 | seeded | The whole island, so the Troubles are here. The Union (1801), the Anglo-Irish Treaty (1921) and the Good Friday Agreement (1998) are in the United Kingdom file. |
| Vietnam | 34 | 111 BCE to 1995 | seeded | Dien Bien Phu (1954) is in the France file. Thin on Champa, the Khmer south and the centuries of Chinese rule. |
| Indonesia | 34 | 683 to 2004 | seeded | Batavia (1619) and the transfer of sovereignty (1949) are in the Netherlands file, Malacca (1511) in the Portugal file. Mostly Java and Sumatra. |
| Ethiopia | 33 | 330 to 2018 | seeded | Adwa (1896) is in the Italy file. Includes Eritrea up to 1993. Dates before 1270 are approximate or traditional. |
| South Africa | 38 | 1220 to 2013 | seeded | Dias (1488) is in the Portugal file and the founding of the Cape Colony (1652) in the Netherlands file. Little before the Dutch. |
| Canada | 37 | 1021 to 2008 | seeded | D-Day is in the United States file. Little on First Nations history before contact. |
| Australia | 35 | 1606 to 2008 | seeded | Nothing on the tens of thousands of years before Europeans. Gallipoli is in the Turkey file. |
| Argentina | 36 | 1516 to 2013 | seeded | The Falklands War (1982) is in the United Kingdom file and the Paraguayan War in the Brazil file. Nothing before the Spanish. |
| Ukraine | 29 | 882 to 2019 | seeded | The baptism of Rus' (988), the sack of Kyiv (1240), Pereiaslav (1654), Chernobyl and the annexation of Crimea (2014) are in the Russia file. The Holodomor is here; the Russia file has the wider Soviet famine. |
| Hungary | 28 | 895 to 2012 | seeded | Lechfeld (955) is in the Germany file, Mohács (1526) and Karlowitz (1699) in the Turkey file, the Compromise of 1867 in the Austria file. |
| Czechia | 29 | 863 to 2004 | seeded | The Defenestration of 1618 and the Munich Agreement are in the Germany file; Austerlitz and Königgrätz in the Austria file. Czechoslovak events are here, so Slovakia is not yet covered on its own. |
| Denmark | 29 | 965 to 2000 | seeded | The Kalmar Union, the Stockholm Bloodbath, Roskilde (1658) and Kiel (1814) are in the Sweden file. Includes Greenland. |
| Norway | 28 | 872 to 2011 | seeded | Kiel (1814) and the end of the union (1905) are in the Sweden file; the Oslo Accords in the Israel file. |
| Thailand | 31 | 1238 to 2016 | seeded | Nothing before Sukhothai (Dvaravati, the Khmer period). |
| Philippines | 30 | 900 to 2016 | seeded | The Treaty of Paris (1898) is in the Spain file. Thin before 1521. |
| Peru | 33 | 2600 BCE to 2003 | seeded | Ayacucho (1824) is in the Spain file. Dates before 1438 are approximate. |
| Iraq | 31 | 3200 BCE to 2017 | seeded | Gaugamela, al-Qadisiyyah, the Mongol sack of Baghdad (1258) and the war of 1980 are in the Iran file; the Babylonian exile in the Israel file. Dates before 600 BCE are approximate. |
| Saudi Arabia | 31 | 570 to 2018 | seeded | Covers the life of Muhammad and the holy cities, then the Saudi states. Little on Arabia before Islam. The September 11 attacks are in the United States file. |
| Pakistan | 29 | 127 to 2014 | seeded | The Indus cities, the Hydaspes, Partition and the 1971 war are in the India file. Thin before 1800. |
| Chile | 30 | 1520 to 2019 | seeded | The crossing of the Andes is in the Argentina file; Angamos, the occupation of Lima and the Treaty of Ancón in the Peru file. Nothing before the Spanish. |
| Colombia | 28 | 1525 to 2016 | seeded | Nothing on the Muisca or other peoples before the conquest. |
| Cuba | 30 | 1492 to 2016 | seeded | The Missile Crisis is in the United States file and the Treaty of Paris (1898) in the Spain file. |
| Nigeria | 31 | 500 BCE to 2015 | seeded | Dates before 1472 are approximate. Thin on Kanem-Bornu and the Hausa states. |
| Morocco | 33 | 40 to 2011 | seeded | Ceuta (1415) and Alcácer Quibir (1578) are in the Portugal file, Las Navas de Tolosa in the Spain file. |
| Afghanistan | 31 | 330 BCE to 2014 | seeded | |
| Albania | 28 | 627 BCE to 2009 | seeded | |
| Algeria | 29 | 202 BCE to 2019 | seeded | |
| Angola | 26 | 1390 to 2017 | seeded | |
| Armenia | 30 | 782 BCE to 2018 | seeded | |
| Azerbaijan | 31 | 84 to 2016 | seeded | |
| Bangladesh | 32 | 300 BCE to 2017 | seeded | Partition and 1971 are in the India file. |
| Belarus | 26 | 862 to 2010 | seeded | |
| Belgium | 30 | 54 BCE to 2016 | seeded | Waterloo is in the United Kingdom file. |
| Bolivia | 29 | 800 to 2019 | seeded | |
| Bosnia and Herzegovina | 27 | 1189 to 2014 | seeded | |
| Bulgaria | 31 | 251 to 2007 | seeded | |
| Cambodia | 30 | 245 to 2017 | seeded | |
| Croatia | 31 | 305 to 2013 | seeded | |
| Democratic Republic of the Congo | 32 | 900 to 2019 | seeded | |
| Dominican Republic | 30 | 1494 to 2013 | seeded | |
| Ecuador | 29 | 3500 BCE to 2019 | seeded | |
| Estonia | 28 | 1030 to 2011 | seeded | |
| Georgia | 30 | 302 BCE to 2008 | seeded | |
| Ghana | 31 | 2500 BCE to 2007 | seeded | |
| Guatemala | 30 | 300 BCE to 2018 | seeded | |
| Haiti | 30 | 1492 to 2016 | seeded | |
| Iceland | 26 | 874 to 2010 | seeded | |
| Jordan | 27 | 7200 BCE to 2012 | seeded | |
| Kazakhstan | 25 | 3500 BCE to 2019 | seeded | |
| Kenya | 32 | 750 to 2017 | seeded | |
| Laos | 22 | 1353 to 2018 | seeded | |
| Latvia | 27 | 1186 to 2004 | seeded | |
| Lebanon | 30 | 1000 BCE to 2019 | seeded | |
| Libya | 31 | 631 BCE to 2019 | seeded | |
| Lithuania | 32 | 1009 to 2004 | seeded | |
| Malaysia | 28 | 450 to 2018 | seeded | |
| Mali | 25 | 250 BCE to 2019 | seeded | |
| Mongolia | 30 | 209 BCE to 2008 | seeded | |
| Mozambique | 24 | 1200 to 2019 | seeded | |
| Myanmar | 31 | 832 to 2017 | seeded | |
| Nepal | 27 | 563 BCE to 2015 | seeded | |
| New Zealand | 29 | 1300 to 2019 | seeded | |
| North Macedonia | 27 | 350 BCE to 2019 | seeded | |
| Papua New Guinea | 26 | 5000 BCE to 2019 | seeded | |
| Paraguay | 29 | 1537 to 2012 | seeded | The Paraguayan War is in the Brazil file. |
| Romania | 32 | 106 to 2007 | seeded | |
| Rwanda | 26 | 1600 to 2015 | seeded | |
| Senegal | 26 | 1035 to 2012 | seeded | |
| Serbia | 32 | 269 to 2008 | seeded | |
| Singapore | 29 | 1299 to 2018 | seeded | |
| Slovakia | 32 | 179 to 2018 | seeded | |
| Slovenia | 28 | 14 to 2004 | seeded | |
| Sri Lanka | 32 | 288 BCE to 2019 | seeded | |
| Sudan | 31 | 2500 BCE to 2019 | seeded | Includes South Sudan's independence (2011). |
| Syria | 32 | 2300 BCE to 2019 | seeded | |
| Tanzania | 26 | 960 to 2015 | seeded | |
| Tunisia | 32 | 814 BCE to 2015 | seeded | |
| Uganda | 24 | 1400 to 2010 | seeded | |
| Uruguay | 29 | 1624 to 2013 | seeded | |
| Uzbekistan | 31 | 329 BCE to 2016 | seeded | |
| Venezuela | 30 | 1498 to 2019 | seeded | |
| Yemen | 30 | 685 BCE to 2017 | seeded | |
| Zimbabwe | 25 | 1300 to 2017 | seeded | |

Deep time (see the section below); the span is in millions of years ago:

| Scope | File | Events | Span (Ma) | Status | Notes |
| --- | --- | ---: | --- | --- | --- |
| Universe, Milky Way | `deep/universe.json` | 20 | 13800 to 5700 | researched | Weakest date: when the expansion began to speed up (sources say 5 to 6 billion years ago). |
| Solar System | `deep/solar-system.json` | 13 | 4600 to 3700 | researched | No entry for Mars losing its water: no datable source found. |
| Earth | `deep/earth.json` | 37 | 4500 to 0.0117 | researched | Six entries have site coordinates, all taken from Wikipedia. |
| Life | `deep/life.json` | 48 | 4280 to 0.023 | researched | Most dates confirmed on Wikipedia only; journal sites and the ICS chart would not load. |

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
the world. Countries not yet started, by region, roughly in the order to take
them within each region (updated 2026-10-09; every other country on the
2019 map now has a file):

- Europe: Cyprus, Kosovo, Luxembourg, Malta, Montenegro, Moldova.
- Middle East: Bahrain, Kuwait, Oman, Qatar, United Arab Emirates, Palestine.
- Central and South Asia: Kyrgyzstan, Tajikistan, Turkmenistan, Bhutan,
  Maldives.
- Southeast Asia and Oceania: Brunei, East Timor, Fiji, Solomon Islands.
- Americas: Belize, Costa Rica, El Salvador, Honduras, Nicaragua, Panama,
  Jamaica, Trinidad and Tobago, Bahamas, Barbados, Guyana, Suriname.
- Africa: Benin, Botswana, Burkina Faso, Burundi, Cameroon, Cape Verde,
  Central African Republic, Chad, Comoros, Republic of the Congo, Ivory
  Coast, Djibouti, Equatorial Guinea, Eritrea, Eswatini, Gabon, Gambia,
  Guinea, Guinea-Bissau, Lesotho, Liberia, Madagascar, Malawi, Mauritania,
  Mauritius, Namibia, Niger, Sierra Leone, Somalia, South Sudan, Togo,
  Zambia.

Smaller countries can have shorter files (15 to 25 events). States too small
to have a polygon on the 2019 map (Andorra, Liechtenstein, Monaco, San
Marino, Vatican City, most Pacific microstates) are left out for now; North
Korea and South Korea are covered together in the Korea file.

Gaps in the seeded countries:

- Turkey: Seljuks and Byzantium before 1299, Balkan Wars, the Kurdish conflict.
- Japan: Jōmon, Yayoi and the Yamato state; Heian politics; the Meiji economy.
- China: Shang and earlier, the Song economy, Ming–Qing transition detail, Tibet and Xinjiang.
- Germany: Hanseatic League, the Staufer emperors, industrialisation, post-1990.
- Russia: the principalities before 1240, expansion into Central Asia and the Caucasus, the Chechen wars.

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
nebula, the molten Earth and Moon, the early ocean Earth). Four deep-time
stops have no events yet: 9, 7 and 5 billion years ago, and 880 million years
ago.

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
  for one step.

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
