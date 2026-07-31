# Wanted Trading Cards

This file is the source list for the wanted-card listing automation in `os/automations/wanted-card-listings.md`.

Add one section per wanted card. Scheduled runs should process only cards with `Status` set to `Active`.

When a new wanted card is added or an existing wanted-card section is changed from `Draft` to `Active`, immediately run the `find-card-listings` skill for all active wanted cards, not just the newly added card. This keeps the latest report fresh and re-sorts every monitored opportunity against the full list.

## Card Template

Copy this section for each card Kyle wants to monitor.

### Card Name

| Field | Value |
|---|---|
| Status | Draft |
| Game | OverPower or Magic: The Gathering |
| Card name |  |
| Description |  |
| Set / edition / variant |  |
| Must-have details |  |
| Nice-to-have details |  |
| Exclude |  |
| Image |  |
| Seed/reference URLs |  |
| Ended auction comparables |  |
| Search terms |  |
| Negative terms |  |
| Retail baseline source | The Orange King retail site for OverPower; Brute Force MTG for Magic |
| Retail baseline price |  |
| Retail baseline checked |  |
| Retail baseline URL |  |
| Notes |  |

## Active Wanted Cards

### Stinging Study

| Field | Value |
|---|---|
| Status | Active |
| Game | Magic: The Gathering |
| Card name | Stinging Study |
| Description | Official physical Magic: The Gathering printing of Stinging Study. |
| Set / edition / variant | Any official paper printing is acceptable, including Commander 2021 #44 regular art, Commander 2021 #371 extended art, Secret Lair Drop #2481 borderless, foil/non-foil, and official language variants. |
| Must-have details | Official physical MTG card named Stinging Study; not a proxy, custom, altered card, art card, oversized card, or digital-only item. |
| Nice-to-have details | Near mint or lightly played condition; seller photo or item specifics confirm an official set/collector number. The saved image shows the C21 #371 extended-art version but is no longer a hard matching requirement. |
| Exclude | Magic Online/digital-only listings; proxy, custom, altered, playtest, oversized, or art-card listings; unrelated cards with similar names such as Rhystic Study. |
| Image | `os/context/assets/wanted-trading-cards/mtg-stinging-study-c21-371-extended-art.png` |
| Seed/reference URLs | <https://www.bruteforcemtg.com/products/search?q=stinging+study&c=1> |
| Ended auction comparables |  |
| Search terms | `Stinging Study`; `MTG Stinging Study`; `Stinging Study Commander 2021`; `Stinging Study C21`; `Stinging Study 44`; `Stinging Study 371`; `Stinging Study extended art`; `Stinging Study Secret Lair`; `Stinging Study borderless` |
| Negative terms | `Magic Online`; `MTGO`; `digital`; `proxy`; `custom`; `altered`; `playtest`; `art card`; `oversized`; `Rhystic Study`; `study guide`; `book` |
| Retail baseline source | Brute Force MTG |
| Retail baseline price | $18.15 |
| Retail baseline checked | 2026-07-17 |
| Retail baseline URL | <https://www.bruteforcemtg.com/products/search?q=stinging+study&c=1> |
| Notes | Added from Kyle-provided image on 2026-07-17. Updated on 2026-07-17: regular art and any official physical printing are acceptable. Brute Force MTG search shows regular Stinging Study at $18.15 and Stinging Study - Extended Art at $20.59; both were out of stock when checked. |

### Mjölnir, Hammer of Thor

| Field | Value |
|---|---|
| Status | Active |
| Game | Magic: The Gathering |
| Card name | Mjölnir, Hammer of Thor |
| Description | Official physical Magic: The Gathering card from Marvel Super Heroes, collector number 146. |
| Set / edition / variant | Marvel Super Heroes (MSH) #146, English, nonfoil or foil. |
| Must-have details | Official paper Magic card named `Mjölnir, Hammer of Thor`; Marvel Super Heroes set code `MSH`; collector number 146; Legendary Artifact — Equipment. |
| Nice-to-have details | Near mint or lightly played; seller photo or item specifics confirm the MSH set and #146. |
| Exclude | Digital-only/MTGO listings; proxies, custom cards, altered cards, art cards, oversized cards, unrelated Thor or Mjölnir items, and listings not for the physical card. |
| Image | <https://cards.scryfall.io/normal/front/e/0/e0c7f566-5351-44e3-a346-b84b0eb10209.jpg?1783902926> |
| Seed/reference URLs | <https://scryfall.com/card/msh/146/mj%C3%B6lnir-hammer-of-thor> |
| Ended auction comparables |  |
| Search terms | `Mjölnir Hammer of Thor MSH 146`; `Mjolnir Hammer of Thor MSH 146`; `Mjölnir Hammer of Thor Marvel Super Heroes`; `MTG Mjolnir Hammer of Thor 146` |
| Negative terms | `MTGO`; `digital`; `proxy`; `custom`; `altered`; `art card`; `oversized`; `Thor hammer replica`; `Marvel Legends`; `comic`; `Mjolnir card sleeve` |
| Retail baseline source | Brute Force MTG |
| Retail baseline price | $28.08 |
| Retail baseline checked | 2026-07-27 |
| Retail baseline URL | <https://www.bruteforcemtg.com/catalog/magic_the_gathering_singles-universes_beyond_marvel_super_heroes_singles-marvel_super_heroes/mjolnir_hammer_of_thor/521370> |
| Notes | Added from Kyle-provided Scryfall reference on 2026-07-19. Scryfall confirms Marvel Super Heroes #146, mythic, released 2026-06-26. Brute Force MTG exact product price refreshed to $30.00 on 2026-07-24; stock state was not captured. |

### Iron Man, Tony Stark

| Field | Value |
|---|---|
| Status | Active |
| Game | Magic: The Gathering |
| Card name | Iron Man, Tony Stark |
| Description | Official physical Magic card from Marvel Super Heroes Commander, collector number 851. |
| Set / edition / variant | Marvel Super Heroes Commander (MSC) #851, English, nonfoil. |
| Must-have details | Exact official paper `Iron Man, Tony Stark`, set code `MSC`, collector number `851`; regular/nonfoil printing. |
| Nice-to-have details | Near mint or lightly played; seller photo or item specifics confirm MSC #851. |
| Exclude | MTGO/digital, proxy, custom, altered, art-card, oversized, or other Iron Man printings. |
| Image | <https://cards.scryfall.io/normal/front/e/c/ec18d8cd-67ed-4338-8ae7-69628469cd43.jpg?1783902992> |
| Seed/reference URLs | <https://scryfall.com/card/msc/851/iron-man-tony-stark> |
| Ended auction comparables |  |
| Search terms | `Iron Man Tony Stark MSC 851`; `Iron Man Tony Stark Marvel Super Heroes Commander 851` |
| Negative terms | `MTGO`; `digital`; `proxy`; `custom`; `altered`; `art card`; `oversized`; `Iron Man 851 comic` |
| Retail baseline source | Brute Force MTG |
| Retail baseline price | $6.21 |
| Retail baseline checked | 2026-07-27 |
| Retail baseline URL | <https://www.bruteforcemtg.com/catalog/magic_the_gathering_singles-universes_beyond_marvel_super_heroes_singles-marvel_super_heroes_commander/iron_man_tony_stark/522513> |
| Notes | Added from Kyle-provided Scryfall URL on 2026-07-20. Brute Force exact product price refreshed to $6.54 on 2026-07-24; stock state was not captured. |

### Namor the Sub-Mariner

| Field | Value |
|---|---|
| Status | Active |
| Game | Magic: The Gathering |
| Card name | Namor the Sub-Mariner |
| Description | Official physical Magic card from Marvel Super Heroes, collector number 69. |
| Set / edition / variant | Marvel Super Heroes (MSH) #69, English, nonfoil or foil. |
| Must-have details | Exact official paper `Namor the Sub-Mariner`, set code `MSH`, collector number `69`. |
| Nice-to-have details | Near mint or lightly played; seller photo or item specifics confirm MSH #69. |
| Exclude | MTGO/digital, proxy, custom, altered, art-card, oversized, or other Namor printings. |
| Image | <https://cards.scryfall.io/normal/front/7/a/7aaefcf9-fbe1-4767-92a5-09825761d116.jpg?1783902956> |
| Seed/reference URLs | <https://scryfall.com/card/msh/69/namor-the-sub-mariner> |
| Ended auction comparables |  |
| Search terms | `Namor the Sub-Mariner MSH 69`; `Namor Sub-Mariner Marvel Super Heroes 69 MTG` |
| Negative terms | `MTGO`; `digital`; `proxy`; `custom`; `altered`; `art card`; `oversized`; `Namor comic` |
| Retail baseline source | Brute Force MTG |
| Retail baseline price | $10.62 |
| Retail baseline checked | 2026-07-27 |
| Retail baseline URL | <https://www.bruteforcemtg.com/catalog/magic_the_gathering_singles-universes_beyond_marvel_super_heroes_singles-marvel_super_heroes/namor_the_submariner/521065> |
| Notes | Added from Kyle-provided Scryfall URL on 2026-07-20. Brute Force exact product price refreshed to $10.40 on 2026-07-24; stock state was not captured. |

### The Vision and Scarlet Witch

| Field | Value |
|---|---|
| Status | Active |
| Game | Magic: The Gathering |
| Card name | The Vision and Scarlet Witch |
| Description | Official physical Magic card from Marvel Super Heroes Commander, collector number 707. |
| Set / edition / variant | Marvel Super Heroes Commander (MSC) #707, English, nonfoil or foil. |
| Must-have details | Exact official paper `The Vision and Scarlet Witch`, set code `MSC`, collector number `707`. |
| Nice-to-have details | Near mint or lightly played; seller photo or item specifics confirm MSC #707. |
| Exclude | MTGO/digital, proxy, custom, altered, art-card, oversized, or other Vision/Scarlet Witch printings. |
| Image | <https://cards.scryfall.io/normal/front/9/3/930afb5f-54b7-4cca-8c28-3e48938f3a43.jpg?1783903042> |
| Seed/reference URLs | <https://scryfall.com/card/msc/707/the-vision-and-scarlet-witch> |
| Ended auction comparables |  |
| Search terms | `The Vision and Scarlet Witch MSC 707`; `Vision Scarlet Witch Marvel Super Heroes Commander 707 MTG` |
| Negative terms | `MTGO`; `digital`; `proxy`; `custom`; `altered`; `art card`; `oversized`; `Vision Scarlet Witch comic` |
| Retail baseline source | Brute Force MTG |
| Retail baseline price | $64.79 |
| Retail baseline checked | 2026-07-27 |
| Retail baseline URL | <https://www.bruteforcemtg.com/catalog/magic_the_gathering_singles-universes_beyond_marvel_super_heroes_singles-marvel_super_heroes_commander/the_vision_and_scarlet_witch/522704> |
| Notes | Added from Kyle-provided Scryfall URL on 2026-07-20. Brute Force exact product price refreshed to $66.15 on 2026-07-24; stock state was not captured. |

### Ultron, Artificial Malevolence

| Field | Value |
|---|---|
| Status | Active |
| Game | Magic: The Gathering |
| Card name | Ultron, Artificial Malevolence |
| Description | Official physical Magic card from Marvel Super Heroes, collector number 252. |
| Set / edition / variant | Marvel Super Heroes (MSH) #252, English, nonfoil or foil. |
| Must-have details | Exact official paper `Ultron, Artificial Malevolence`, set code `MSH`, collector number `252`. |
| Nice-to-have details | Near mint or lightly played; seller photo or item specifics confirm MSH #252. |
| Exclude | MTGO/digital, proxy, custom, altered, art-card, oversized, or other Ultron printings. |
| Image | <https://cards.scryfall.io/normal/front/3/2/32ddd5ac-57ed-4e78-8932-a65980191f6e.jpg?1783902889> |
| Seed/reference URLs | <https://scryfall.com/card/msh/252/ultron-artificial-malevolence> |
| Ended auction comparables |  |
| Search terms | `Ultron Artificial Malevolence MSH 252`; `Ultron Artificial Malevolence Marvel Super Heroes 252 MTG` |
| Negative terms | `MTGO`; `digital`; `proxy`; `custom`; `altered`; `art card`; `oversized`; `Ultron comic` |
| Retail baseline source | Brute Force MTG |
| Retail baseline price | $15.10 |
| Retail baseline checked | 2026-07-27 |
| Retail baseline URL | <https://www.bruteforcemtg.com/catalog/magic_the_gathering_singles-universes_beyond_marvel_super_heroes_singles-marvel_super_heroes/ultron_artificial_malevolence/521683> |
| Notes | Added from Kyle-provided Scryfall URL on 2026-07-20. Brute Force exact product price refreshed to $15.57 on 2026-07-24; stock state was not captured. |

### Hulk, Brutal Brawler

| Field | Value |
|---|---|
| Status | Active |
| Game | Magic: The Gathering |
| Card name | Hulk, Brutal Brawler |
| Description | Official physical Magic card from Marvel Super Heroes Commander, collector number 833. |
| Set / edition / variant | Marvel Super Heroes Commander (MSC) #833, English, nonfoil or foil. |
| Must-have details | Exact official paper `Hulk, Brutal Brawler`, set code `MSC`, collector number `833`. |
| Nice-to-have details | Near mint or lightly played; seller photo or item specifics confirm MSC #833. |
| Exclude | MTGO/digital, proxy, custom, altered, art-card, oversized, or other Hulk printings. |
| Image | <https://cards.scryfall.io/normal/front/4/6/46d9f159-715e-4450-9f83-0fd050e2382e.jpg?1783902999> |
| Seed/reference URLs | <https://scryfall.com/card/msc/833/hulk-brutal-brawler> |
| Ended auction comparables |  |
| Search terms | `Hulk Brutal Brawler MSC 833`; `Hulk Brutal Brawler Marvel Super Heroes Commander 833 MTG` |
| Negative terms | `MTGO`; `digital`; `proxy`; `custom`; `altered`; `art card`; `oversized`; `Hulk comic` |
| Retail baseline source | Brute Force MTG |
| Retail baseline price | $25.27 |
| Retail baseline checked | 2026-07-27 |
| Retail baseline URL | <https://www.bruteforcemtg.com/catalog/magic_the_gathering_singles-universes_beyond_marvel_super_heroes_singles-marvel_super_heroes_commander/hulk_brutal_brawler/522526> |
| Notes | Added from Kyle-provided Scryfall URL on 2026-07-20. Brute Force exact product price refreshed to $30.10 on 2026-07-24; stock state was not captured. |

### Onslaught Promo Character

| Field | Value |
|---|---|
| Status | Active |
| Game | OverPower |
| Card name | Onslaught |
| Description | Onslaught character card from the OverPower promo set. |
| Set / edition / variant | Promo character card; not the regular/non-promo Onslaught character. |
| Must-have details | Promo image with Onslaught shown against blue lightning background; vertical stat bars showing Energy 8, Fighting 2, Strength 6, Intellect 7. |
| Nice-to-have details | Seller photo confirms exact promo card; listings that include other OverPower promo cards or X-Men/Marvel OverPower bulk lots are relevant if this card is visible or explicitly named. |
| Exclude | Regular/non-promo Onslaught character card; Onslaught-related specials/events/missions; Marvel cards from games other than OverPower; lots where the promo character card is not visible or named. |
| Image | `os/context/assets/wanted-trading-cards/overpower-onslaught-promo-character.png` |
| Ended auction comparables | <https://www.ebay.com/itm/178048550321?_skw=overpower+onslaught+character&itmmeta=01KXQGNK162KF9SKV0A51XM7EC&hash=item29748545b1:g:-mEAAeSw9Nlp3loN&itmprp=enc%3AAQALAAABAGfYFPkwiKCW4ZNSs2u11xBAxKin%2FsSspIa%2F1EQ19edI9keyXmDRoNBOl3p4bYSL9CyhxdKULxtf9Vc8ifuftJv8VC1SaMFxlTXe3lyaj30LrstbTUvsNA3pO%2BBUc%2BUSvHDYJO22a6Yqo6oPG%2BTFCeum6vY16MgXnUYyYxIec4T2zzR%2BU47mzzGgyUZyGBvUMmSP%2BdguQr9lsi%2Flbdyro%2Fq0ZfmVEuwkq9g84Be8EYpWfE%2FGZvE9QDnssKo5s4bAP2yMS0SvFvLc8gG0jA0TGxXLVo%2Fg74o3YrWy5CQjHTlkxeEDc7NsAKcXjTZFcup1iAaUyX8W2uPkw1e4wbSoCNw%3D%7Ctkp%3ABk9SR9qw1vDtZw> |
| Search terms | `overpower onslaught promo character`; `overpower onslaught character promo`; `onslaught overpower promo`; `marvel overpower onslaught promo`; `overpower promo character lot`; `overpower promo cards onslaught`; `overpower x-men promo lot onslaught` |
| Negative terms | `regular`; `non-promo`; `special`; `mission`; `event`; `mtg`; `heroclix`; `vs system`; `custom`; `proxy` |
| Retail baseline source | The Orange King retail site |
| Retail baseline price | $15.00 |
| Retail baseline checked | 2026-07-17 |
| Retail baseline URL | <https://theorangeking.com/collections/promos> |
| Notes | Added from Kyle-provided image and ended eBay comparable on 2026-07-17. |

### Beyonder Infinity Promo Character

| Field | Value |
|---|---|
| Status | Active |
| Game | OverPower |
| Card name | Beyonder |
| Description | Beyonder Infinity promo character card from Marvel OverPower. |
| Set / edition / variant | Infinity promo character card; very rare. |
| Must-have details | Promo character card titled Beyonder; white-jacket Beyonder portrait with glowing eyes on dark blue cosmic background; horizontal character layout; stat icons showing Energy infinity, Fighting infinity, Strength infinity, Intellect infinity; bottom text says `May play any Special cards.` |
| Nice-to-have details | Seller photo confirms exact Beyonder Infinity promo character card; listings that include rare OverPower promo characters are relevant if Beyonder is visible or explicitly named. |
| Exclude | Beyonder mission cards such as Secret Wars mission cards; Beyonder comics or Marvel trading cards from games other than OverPower; VS System Beyonder cards; specials, power cards, teamworks, or non-character cards; lots where the Beyonder promo character card is not visible or named; custom/proxy/reprint cards. |
| Image | `os/context/assets/wanted-trading-cards/overpower-beyonder-infinity-promo-character.png` |
| Seed/reference URLs | <https://theorangeking.com/products/beyonder-promo-character-vr-w-bonus>; <https://www.ebay.com/itm/188353640036> |
| Ended auction comparables | <https://www.ebay.com/itm/188353640036?_skw=overpower+beyonder&itmmeta=01KXWA0MJT6D1HBPRW9KD765DD&hash=item2bdac07664:g:mesAAeSwPw9p-t7Q&itmprp=enc%3AAQALAAAA8GfYFPkwiKCW4ZNSs2u11xCJ%2F5%2FMLWSN%2BY%2Bv4ZZaf7p2j8TfBHhaKps9hj9RJIp8f09ft4QJmxZlHJOUNLj94ktpHtTh0kJQJ4jUu%2BHiliQ2MTkeyDIycLCbH4IpLiL6rq6HEfu7AMtUNEkT8J%2FYi5uHERILbIEsckJuISVknuYsDeOTvrDR0%2Bjv1APpUAsXnVGDbKIq6l6cIgS1FFV9SKeEzfgClaiZao0j6PNZZ8wlzTpOAsvFILG85GqmQloriISd0a2oyc%2FA8DVZlKV%2FaASysikz3fX2HKTrHl1ws8ch79%2FAbcz2TmoTrEj2g8f54w%3D%3D%7Ctkp%3ABk9SR9bJgorvZw> |
| Search terms | `overpower beyonder promo character`; `overpower beyonder infinity promo`; `marvel overpower beyonder infinity`; `marvel overpower beyonder character`; `beyonder overpower promo`; `overpower promo character beyonder`; `overpower rare promo character beyonder`; `overpower beyonder infinity character` |
| Negative terms | `mission`; `Secret Wars`; `Beyonder & Dr. Doom`; `comic`; `Defenders Beyond`; `Fleer`; `VS System`; `TCG`; `Inhuman`; `mtg`; `heroclix`; `custom`; `proxy`; `reprint` |
| Retail baseline source | The Orange King retail site only; do not use The Orange King eBay listings |
| Retail baseline price | $399.00 |
| Retail baseline checked | 2026-07-27 |
| Retail baseline URL | <https://theorangeking.com/products/beyonder-promo-character-vr-w-bonus> |
| Notes | Added from Kyle-provided image and eBay seed link on 2026-07-19. The Orange King product page showed `BEYONDER Promo character - VR + bonus (see pictures)` at $399.00 and sold out when checked. |

### Devourer of Worlds Any Character Special

| Field | Value |
|---|---|
| Status | Active |
| Game | OverPower |
| Card name | Any Character - Devourer of Worlds |
| Description | Devourer of Worlds Any Character special card from X-Men OverPower, featuring Galactus. |
| Set / edition / variant | X-Men OverPower Any Character special; OPD / One Per Deck; very rare. |
| Must-have details | Yellow vertical Any Character special card titled Devourer of Worlds; Galactus art with purple helmet/armor and a yellow energy blast; card code `OD`; bottom text says `One Per Deck`; rules text begins `Play during battle. Opponent cannot use Activator cards...` and says the Special may not be negated. |
| Nice-to-have details | Seller photo confirms exact yellow Any Character card and visible `OD` / `One Per Deck` cues; listings from X-Men OverPower special lots are relevant if this card is visible or explicitly named. |
| Exclude | Galactus character cards; Galactus specials other than Devourer of Worlds; mission cards, location cards, comics, toys, statues, HeroClix, VS System cards, Marvel trading cards from games other than OverPower, custom/proxy/reprint cards, and lots where Devourer of Worlds is not visible or named. |
| Image | `os/context/assets/wanted-trading-cards/overpower-devourer-of-worlds-any-character-special.png` |
| Seed/reference URLs | <https://theorangeking.com/products/ac-devourer-of-worlds-od-xm-opd-vr>; <https://www.ebay.com/sch/i.html?_nkw=devourer+of+worlds+overpower&_sacat=0&_from=R40&_trksid=p4624852.m570.l1313>; <https://www.ebay.com/itm/202873207451> |
| Ended auction comparables |  |
| Search terms | `devourer of worlds overpower`; `overpower devourer of worlds`; `any character devourer of worlds`; `overpower any character devourer`; `marvel overpower devourer of worlds`; `x-men overpower devourer of worlds`; `galactus devourer of worlds overpower`; `overpower OD devourer worlds`; `overpower OPD devourer worlds` |
| Negative terms | `character card`; `mission`; `location`; `comic`; `toy`; `statue`; `Heroclix`; `VS System`; `Fleer Ultra`; `Marvel Masterpieces`; `custom`; `proxy`; `reprint` |
| Retail baseline source | The Orange King retail site only; do not use The Orange King eBay listings |
| Retail baseline price | $130.00 |
| Retail baseline checked | 2026-07-27 |
| Retail baseline URL | <https://theorangeking.com/products/ac-devourer-of-worlds-od-xm-opd-vr> |
| Notes | Added from Kyle-provided image and eBay search link on 2026-07-19. The Orange King product search showed `ANY CHARACTER - DEVOURER OF WORLDS - X-MEN - Galactus - OPD - VR` at $130.00 and unavailable when checked. |

### Iron Man IQ Character

| Field | Value |
|---|---|
| Status | Active |
| Game | OverPower |
| Card name | Iron Man |
| Description | Iron Man character card from the OverPower IQ set. |
| Set / edition / variant | IQ Character card; very rare. |
| Must-have details | IQ Character card titled Iron Man; red/gold Iron Man armor in side-profile pose on blue background; horizontal character layout; stat boxes showing Energy 5, Fighting 3, Strength 7, Intellect 7. |
| Nice-to-have details | Seller photo confirms exact IQ character card; listings that include IQ character lots or full Iron Man OverPower groups are relevant if the IQ character card is visible or explicitly named. |
| Exclude | Original/OP Iron Man character card; PowerSurge Iron Man cards; Iron Man specials, power cards, placards, teamworks, or non-character cards; Marvel cards from games other than OverPower; lots where the IQ character card is not visible or named; custom/proxy/reprint cards. |
| Image | `os/context/assets/wanted-trading-cards/overpower-iron-man-iq-character.png` |
| Seed/reference URLs | <https://theorangeking.com/products/iron-man-iq-hero-vr>; <https://www.ebay.com/itm/298438687673> |
| Ended auction comparables | <https://www.ebay.com/itm/298438687673?_skw=overpower+iron+man+character&itmmeta=01KXRPC0Q6CKFCW6YQ9C3SJFVE&hash=item457c54fbb9:g:r2AAAeSwU3ZqOBLN&itmprp=enc%3AAQALAAABAGfYFPkwiKCW4ZNSs2u11xCrXhsJM1e5e%2BI29Z99Me4yrjKHwPEVO%2BWZ3k2ZCiJm7ZhD4m1VxPAqzdEPtmokMldAJzRxMYkx7zBAyyA0QtDaRCHwljckzmoTy2EfhsefAKtR4PTSUWUHqFQccmHAAGvi88PCiC96i%2BUdUqS51sqvpDGAeKqHz6qalXNhgZqHVSIMCCdtnx3vYeS3%2FnW1XG%2Bd9ihE5bBtyd42M0jKI66mU2rAIE04LeemiGUk2gpkj1nPX4hrxm%2FT2AocCJx%2Bkdtu%2BA4CEw1qhB0PjeyEUBnpYLlZMMf30QeHlhBVdIreBKTn0yCb9FLu%2FJotwMY4t3k%3D%7Ctkp%3ABk9SR-CLsJbuZw> |
| Search terms | `overpower iron man iq character`; `iron man iq character overpower`; `iron man iq hero vr`; `marvel overpower iron man iq`; `overpower iq iron man`; `overpower iq character lot iron man`; `overpower iron man character iq`; `iron man iq hero` |
| Negative terms | `original`; `OP character`; `PowerSurge`; `special`; `concealed arsenal`; `industrial waste`; `heat seeking missile`; `tactical computer`; `stealth armor`; `weapons inventor`; `teamwork`; `power card`; `placard`; `heroclix`; `vs system`; `mtg`; `custom`; `proxy`; `reprint` |
| Retail baseline source | The Orange King retail site |
| Retail baseline price | $52.50 |
| Retail baseline checked | 2026-07-27 |
| Retail baseline URL | <https://theorangeking.com/products/iron-man-iq-hero-vr> |
| Notes | Added from Kyle-provided image and eBay seed link on 2026-07-17. The Orange King product page <https://theorangeking.com/products/iron-man-iq-hero-vr> is the primary seed/reference for the exact IQ Character target; it showed `IRON MAN - IQ Character - VR` at $52.50 with available quantity 1 when checked. |

### Thor IQ Character

| Field | Value |
|---|---|
| Status | Active |
| Game | OverPower |
| Card name | Thor |
| Description | Thor character card from the OverPower IQ set. |
| Set / edition / variant | IQ character card; very rare. |
| Must-have details | IQ character card titled Thor; Thor holding Mjolnir over a lightning background; horizontal character layout; stat boxes showing Energy 7, Fighting 5, Strength 7, Intellect 4. |
| Nice-to-have details | Seller photo confirms exact IQ character card; listings that include IQ character lots or Thor OverPower groups are relevant if the IQ character card is visible or explicitly named. |
| Exclude | Original/OP Thor character card; PowerSurge Thor cards; Thor specials, power cards, teamworks, or non-character cards; Marvel cards from games other than OverPower; lots where the IQ character card is not visible or named; custom/proxy/reprint cards. |
| Image | `os/context/assets/wanted-trading-cards/overpower-thor-iq-character.jpg` |
| Seed/reference URLs | <https://theorangeking.com/products/thor-iq-hero-vr> |
| Ended auction comparables |  |
| Search terms | `overpower thor iq character`; `thor iq character overpower`; `thor iq hero vr`; `marvel overpower thor iq`; `overpower iq thor`; `overpower iq character lot thor`; `overpower thor character iq`; `thor iq hero` |
| Negative terms | `original`; `OP character`; `PowerSurge`; `special`; `teamwork`; `power card`; `heroclix`; `vs system`; `mtg`; `custom`; `proxy`; `reprint` |
| Retail baseline source | The Orange King retail site |
| Retail baseline price | $65.00 |
| Retail baseline checked | 2026-07-27 |
| Retail baseline URL | <https://theorangeking.com/products/thor-iq-hero-vr> |
| Notes | Added from The Orange King product page on 2026-07-17. The Orange King product page showed `THOR - IQ character - VR` at $65.00 and available when checked. |

### Rogue IQ Character

| Field | Value |
|---|---|
| Status | Active |
| Game | OverPower |
| Card name | Rogue |
| Description | Rogue character card from the OverPower IQ set. |
| Set / edition / variant | IQ Character card; rare. |
| Must-have details | IQ Character card titled Rogue; Rogue flying on a blue/green background; horizontal character layout; stat boxes showing Energy 4, Fighting 4, Strength 7, Intellect 2; bottom text says `May not be Spectrum KO'd with Special cards.` |
| Nice-to-have details | Seller photo confirms exact IQ Character card; listings that include IQ character lots or Rogue OverPower groups are relevant if the IQ Character card is visible or explicitly named. |
| Exclude | Original/OP Rogue character card; PowerSurge Rogue cards; Rogue specials, power cards, teamworks, or non-character cards; Rogue: Brotherhood of Evil Mutants IQ Character variant; Marvel cards from games other than OverPower; lots where this IQ Character card is not visible or named; custom/proxy/reprint cards. |
| Image | `os/context/assets/wanted-trading-cards/overpower-rogue-iq-character.png` |
| Seed/reference URLs | <https://theorangeking.com/products/rogue-iq-hero-r> |
| Ended auction comparables |  |
| Search terms | `overpower rogue iq character`; `rogue iq character overpower`; `rogue iq hero r`; `marvel overpower rogue iq`; `overpower iq rogue`; `overpower iq character lot rogue`; `overpower rogue character iq`; `rogue iq hero`; `Marvel Overpower Rogue Iq Hero Card` |
| Negative terms | `original`; `OP character`; `PowerSurge`; `special`; `teamwork`; `power card`; `Brotherhood of Evil Mutants`; `heroclix`; `vs system`; `mtg`; `custom`; `proxy`; `reprint` |
| Retail baseline source | The Orange King retail site |
| Retail baseline price | $25.00 |
| Retail baseline checked | 2026-07-27 |
| Retail baseline URL | <https://theorangeking.com/products/rogue-iq-hero-r> |
| Notes | Added from Kyle-provided image and The Orange King product page on 2026-07-17. The Orange King product page showed `ROGUE - IQ character - R` at $25.00 and available when checked. |

### Brass Chrome/Holofoil Promo Character

| Field | Value |
|---|---|
| Status | Active |
| Game | OverPower |
| Card name | Brass |
| Description | Brass character card from a WildStorm OverPower trading card promo/chrome/holofoil set. |
| Set / edition / variant | WildStorm chrome/holofoil/shiny promo character card. |
| Must-have details | Shiny chrome/holofoil finish; Brass name in gold at top right; golden armored character art; horizontal character layout; stat boxes showing Energy 7, Fighting 5, Strength 6, Intellect 3. |
| Nice-to-have details | Seller photo confirms shiny/chrome WildStorm card; lots containing WildStorm OverPower chrome/holofoil character cards are relevant if Brass is visible or explicitly named. |
| Exclude | Non-shiny/non-chrome Brass cards; Brass cards from games other than OverPower; unrelated WildStorm trading cards that are not OverPower; lots where the Brass character card is not visible or named; custom/proxy/reprint cards. |
| Image | `os/context/assets/wanted-trading-cards/overpower-brass-chrome-holofoil-character.png` |
| Ended auction comparables | <https://www.ebay.com/itm/355889782815?_skw=overpower+brass&itmmeta=01KXQHJJVG9QNDKKTSBBD9QE2M&hash=item52dcaf201f:g:jN8AAOSwtGtmnhFx&itmprp=enc%3AAQALAAAA0GfYFPkwiKCW4ZNSs2u11xD3UF5tpftHjRJjsIniPym%2FDhrlT%2F4Rd%2BePUwOD8FKUi6x7wR%2B7kw2t8FXcWsWJFzBeBwitQEr2ZdpyUiF%2FAWLSxBPLhsk3oBfLjIKkqHC8big9K%2FxVSQ%2F56Q7V5nG9YiX5tN8tCtFuW7786mVDejnXy1ALNZGUplpnpXnwvUOm4Tlj%2BpCEKWLtQxkLUHQ6qU6ahHHvrg%2Fq6bdesZTVIR41POZSX%2FHcugUAse%2Bfn1LnkMSNd6gjP4E14fCqFgMygDo%3D%7Ctkp%3ABk9SR_qtyvHtZw> |
| Search terms | `overpower brass`; `overpower brass character`; `overpower brass chrome`; `overpower brass holofoil`; `wildstorm overpower brass`; `wildstorm overpower chrome brass`; `wildstorm overpower holofoil brass`; `overpower wildstorm chrome character`; `overpower wildstorm holofoil lot brass` |
| Negative terms | `non-chrome`; `non foil`; `non-foil`; `regular`; `mtg`; `heroclix`; `vs system`; `custom`; `proxy`; `reprint` |
| Retail baseline source | The Orange King retail site only; do not use The Orange King eBay listings |
| Retail baseline price | $9.00 |
| Retail baseline checked | 2026-07-27 |
| Retail baseline URL | <https://theorangeking.com/products/brass-chrome-promo-character-x-r> |
| Notes | Added from Kyle-provided image and eBay comparable on 2026-07-17. |

### Post Promo Character

| Field | Value |
|---|---|
| Status | Active |
| Game | OverPower |
| Card name | Post |
| Description | Post character card from the OverPower promo set. |
| Set / edition / variant | Promo character card. |
| Must-have details | Promo image with Post on an orange/gold background, rocky character art, and stat boxes showing Energy 1, Fighting 6, Strength 4, Intellect 6. |
| Nice-to-have details | Seller photo confirms exact Post promo character card; listings that include other OverPower promo characters such as Onslaught or Dark Beast are relevant if Post is visible or explicitly named. |
| Exclude | Post special cards such as Lethal Tester, Herald of Onslaught, Strategic Assault, Gather Info, Protective Plates, or Obfuscate; X-Men comics featuring Post; Marvel cards from games other than OverPower; lots where the Post promo character card is not visible or named. |
| Image | `os/context/assets/wanted-trading-cards/overpower-post-promo-character.png` |
| Ended auction comparables | <https://www.ebay.com/itm/203036892366?_skw=overpower+post+character+promo&itmmeta=01KXQJKZ0D6B364C89RC4TZN4X&hash=item2f45f11cce:g:yBUAAOSwU9Ne~L7f&itmprp=enc%3AAQALAAABAGfYFPkwiKCW4ZNSs2u11xDtFU2yeq1O4HAOQZqAZCJwxcYU9MNlDM9J32BQRjTyrk2q2lMKYIjg5FMRZVgBdmNGV1N4ro42Afm3nJcdMN0DsOl%2FMtowGKg4FVtodxb6gtqXb3vj8C8O79AGEqEnpY3xDQP3m02GFNYpVVAQeu84yxkjSOE7%2FZ8lfkHe1XWMr3onI0tCXaSWZW7bMY56RkRFIQaAttNjnLi%2Flkr%2FhmuqMShsIHRoCPW2OHMEzsG2BPbVNH7%2Bo41Sqw70y1zmYjOdUxsMe4%2BULbKqntFgofqdZGcSOx2hQxx9vFG0jNop0pl6FZJQNTO2ic6%2B8hV1s1I%3D%7Ctkp%3ABk9SR7zwz_LtZw> |
| Search terms | `overpower post promo character`; `overpower post character promo`; `post overpower promo`; `marvel overpower post promo`; `overpower promo character lot`; `overpower promo cards post`; `overpower onslaught post dark beast promo set` |
| Negative terms | `lethal tester`; `herald of onslaught`; `strategic assault`; `gather info`; `protective plates`; `obfuscate`; `comic`; `x-men #50`; `mtg`; `heroclix`; `vs system`; `custom`; `proxy` |
| Retail baseline source | The Orange King retail site |
| Retail baseline price | $5.00 |
| Retail baseline checked | 2026-07-27 |
| Retail baseline URL | <https://theorangeking.com/collections/promos> |
| Notes | Added from Kyle-provided image and eBay comparable on 2026-07-17. |
