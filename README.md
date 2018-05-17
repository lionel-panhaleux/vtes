# vtes

This repository contains a compilation of rules with all registered rulings
[V:TES Comprehensive Rules](vtes_comprehensive_rules.md).

It also contains the ``fame`` application, a command-line python tool based on
the TWDA archive and cards lists hosted by VEKN.

## Installation

Use pip to install th ``fame`` tool:

```shell
pip install fame
```

Then initialize the tool using the ``init`` subcommand:

```shell
fame init
```

## Usage

Use the help command for a full documentation of the tool:

```shell
fame --help
```

## Examples

Get a card text:

```shell
$> fame card "Fame"
Fame
[Master] -- (Jyhad:U, VTES:U, SW:PB, CE:PB, Anarchs:PG, BH:PN2, KMW:PAl, Third:PTz, KoT:U/PT2, HttB:PGar/PSal)
Unique master.
Put this card on a ready vampire. If this vampire goes to torpor, his or her controller burns 3 pool. While this vampire is in torpor, each Methuselah burns 1 pool during his or her unlock phase.
```

List TWDA decks containing this card:

```shell
$> fame deck "Fame"
[2016gncbg] weenie animalism minimal: "Ich bin eine von wir"
[2016amfb] Gangrel e Garou
[2016ukncle] (No Name)
[2016ecday1gi] (No Name)
[2016saclcqspb] "Choquinho"
...
```

Display any TWDA deck:

```shell
$> fame deck 2016gncbg
German NC 2016
Bochum, Germany
December 3rd 2016
3R+F
19 players
Bram van Stappen

Deck Name: weenie animalism minimal: "Ich bin eine von wir"
Description:
played (untested) at the German Nationals 03.12.2016, Bochum


-- Crypt: (12 cards)
---------------------------------------
2  Stick                               3  ANI                       Nosferatu antitribu:4
1  Janey Pickman                       6  for ANI PRO               Gangrel antitribu:4
1  Célèste Lamontagne                  5  for ANI PRO               Gangrel antitribu:4
1  Effie Lowery                        5  obf ANI SPI               Ahrimane:4
1  Sahana                              5  pre pro spi ANI           Ahrimane:4
1  Yuri Kerezenski                     5  aus for vic ANI           Tzimisce:4
1  Beetleman                           4  obf ANI                   Nosferatu:4
1  Bobby Lemon                         4  pro ANI                   Gangrel:3
1  Mouse                               2  ani                       Nosferatu:3
1  Zip                                 2  ani                       Ravnos:3
1  Lisa Noble                          1  ani                       Caitiff:3
-- Library (90)
-- Master (12)
5  Blood Doll
2  Powerbase: Montreal
1  Direct Intervention
1  Fame
1  KRCG News Radio
1  Pentex(TM) Subversion
1  Rack, The
-- Action (14)
10 Deep Song
2  Abbot
1  Aranthebes, The Immortal
1  Army of Rats
-- Combat (38)
16 Aid from Bats
11 Carrion Crows
6  Taste of Vitae
2  Canine Horde
2  Terror Frenzy
1  Pack Alpha
-- Reaction (18)
5  Cats' Guidance
5  On the Qui Vive
4  Forced Awakening
3  Delaying Tactics
1  Wake with Evening's Freshness
-- Equipment (1)
1  Sniper Rifle
-- Retainer (7)
6  Raven Spy
1  Mr. Winthrop
```

List cards most associated with a given card in TWD:

```shell
fame affinity "Fame"
Taste of Vitae                 (score: 276.00)
On the Qui Vive                (score: 250.00)
Blood Doll                     (score: 247.00)
Dreams of the Sphinx           (score: 208.00)
Pentex(TM) Subversion          (score: 202.00)
Direct Intervention            (score: 176.00)
Dragonbound                    (score: 164.00)
Delaying Tactics               (score: 163.00)
Giant's Blood                  (score: 162.00)
Deflection                     (score: 155.00)
```

List most played cards of a given type, clan or discipline:

```shell
fame top -d Animalism
Carrion Crows                  (played in 301 decks)
Cats' Guidance                 (played in 284 decks)
Raven Spy                      (played in 244 decks)
Canine Horde                   (played in 214 decks)
Army of Rats                   (played in 187 decks)
Aid from Bats                  (played in 179 decks)
Deep Song                      (played in 159 decks)
Sense the Savage Way           (played in 129 decks)
Guard Dogs                     (played in 99 decks)
Owl Companion                  (played in 81 decks)
```

Build a deck from any given cards based on TWDA:

```shell
fame build "Fame" "Carrion Crows"

Created by: Fame
Description:
Inspired by:
 - 2016gncbg            weenie animalism minimal: "Ich bin eine von wir"
 - 2016sncss            Vampire-SM 2016. Field Training Bats v.3
 - 2016ecqmmf           Weenie Animalism v1.2
 - 2016ncqmmf           New Nana (27)
 - 2015saclcqfb         Cidade em Chamas
 ...

-- Crypt: (12 cards)
---------------------------------------
3  Nana Buruku                         8  ANI POT PRE               Guruhi:4
1  Stick                               3  ANI                       Nosferatu antitribu:4
1  Beetleman                           4  obf ANI                   Nosferatu:4
1  Bobby Lemon                         4  pro ANI                   Gangrel:3
1  Petra                               5  aus ANI OBF               Nosferatu:4
1  Célèste Lamontagne                  5  for ANI PRO               Gangrel antitribu:4
1  Zip                                 2  ani                       Ravnos:3
1  Lisa Noble                          1  ani                       Caitiff:3
1  Mouse                               2  ani                       Nosferatu:3
1  Fish                                5  pre ANI POT               Guruhi:4
-- Library (90)
-- Master (25)
8  Ashur Tablets
3  Blood Doll
2  Animalism
2  Dreams of the Sphinx
2  Haven Uncovered
2  Vessel
1  Archon Investigation
1  Direct Intervention
1  Fame
1  Pentex(TM) Subversion
1  Powerbase: Montreal
1  Wider View
-- Action (11)
10 Deep Song
1  Army of Rats
-- Combat (37)
13 Aid from Bats
10 Carrion Crows
5  Taste of Vitae
4  Target Vitals
3  Terror Frenzy
2  Canine Horde
-- Reaction (11)
4  Cats' Guidance
3  On the Qui Vive
2  Delaying Tactics
2  Sense the Savage Way
-- Retainer (5)
5  Raven Spy
-- Event (1)
1  Dragonbound
```

## Contribute

Feel free to submit pull requests, they will be merged as long as they pass the tests.
Do not hestitate to submit issues or vote on them if you want a feature implemented.
