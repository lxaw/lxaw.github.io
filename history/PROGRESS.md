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
| Japan | 18 | 710 to 1964 | seeded | Nothing before Nara or after 1964. |
| China | 19 | 221 BCE to 1997 | seeded | |
| Germany | 20 | 9 to 1990 | seeded | |
| Russia | 23 | 862 to 1991 | seeded | Dates before 1918 are New Style unless marked. |
| Austria | 24 | 976 to 1995 | seeded | The sieges of Vienna (1529, 1683) are in the Turkey file. |
| Switzerland | 18 | 1291 to 2002 | seeded | The Peace of Westphalia (1648) is in the Germany file. |
| Finland | 28 | 1249 to 1995 | seeded | Nothing after 1995 (NATO, 2023, is past the map's last year). |
| Taiwan | 23 | 1624 to 2014 | seeded | Nothing before the Dutch. Dates checked against the source page's text by script. |

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

1. Israel and Jewish history
2. Italy (Rome, Venice)
3. United States
4. United Kingdom, France
5. Korea, India

Gaps in the seeded countries:

- Turkey: Seljuks and Byzantium before 1299, Balkan Wars, the Kurdish conflict.
- Japan: Jōmon to Asuka, the Sengoku unifiers, Sino-Japanese War, 1930s, post-1964.
- China: Zhou and Warring States, Three Kingdoms to Sui, Taiping, Long March, Cultural Revolution.
- Germany: Hanseatic League, Thirty Years' War battles, 1866, Weimar crises, postwar division (1949).
- Russia: Novgorod and the other principalities, Time of Troubles, Catherine II, Crimean War, 1930s, Cold War, post-1991.

## How to add events

1. Add events to `history/events/<country>.json`. For a new country, create the
   file and add its name to `history/events/list.json`.
2. Run `python check_events.py` and fix anything it reports.
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
- an event's `polity` is exactly the map's name (so set `polity` to the name
  the map uses for that period where you can),
- more than half of the country's events happened inside the clicked borders,
- or the name is listed under `COUNTRY_ALIASES` in `history.html`.

Events of the current stop that happened inside the borders are shown whatever
country they belong to.

## Ideas, not started

- Let single-year events linger for a few years so they do not flash past
  during auto-play.
- Sort events within the same year by month and day.
- A second map layer for themes that cross countries (trade routes, religions).
- Dots for deep-time events that have a site, by moving today's coordinates
  with the same plate model as the coastlines (GPlates can reconstruct points).

## Log

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
