# news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/arsheearanjbar-sudo/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/arsheearanjbar-sudo/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

A newspaper front page that sums up the world's news of Tuesday 24 November 2026 in one image: Nvidia reinstates Jensen Huang as chief executive after President Trump's push, Ukraine's war reaches new seas, a deadly factory fire in Indonesia, US states suing over AI-made images, a Russian jet triggering a South Korean alert, a new India-Nepal train, and the world chess title defence opening in Geneva. The page is drawn entirely in code with PIL, so every headline is typeset exactly, with a hand-drawn pictogram per story and a By the Numbers strip that reuses only figures already stated in the stories.

## Run it

```sh
node main.ts   # Node 22; writes /output/entry.png
```

## Stories

| Headline | Fact | Source |
| --- | --- | --- |
| Huang back at Nvidia after Trump push | Nvidia's board reinstated Jensen Huang as CEO, 11 days after he resigned; shares jumped more than 30%. | https://www.aljazeera.com/amp/economy/2026/11/23/nvidia-board-reinstates-jensen-huang-as-ceo |
| Ukraine sinks Russian warship in Libya | Kyiv said sea drones sank a Russian corvette in a Libyan port, days after the cargo ship Sparta II was hit off Finland. | https://www.devdiscourse.com/article/international/4011043-reuters-world-news-summary |
| 24 killed in Indonesia factory fire | A blaze at a candy factory in Banten killed at least 24 people; rescuers still search for about 30 missing. | https://www.jagranjosh.com/articles/school-assembly-news-headlines-november-24-2026-kamla-express-super-tet-spicejet-ferrari-296-and-other-news-1800019603-1 |
| US states sue Musk firms over Grok images | States sued over sexualised images made with the Grok chatbot, in a new test of AI firms' duties. | https://beta.manilatimes.net/world/page/4276 |
| Russian jet sparks Korea alert | South Korea briefly warned Ulleung island after a Russian aircraft entered its airspace on Tuesday. | https://www.devdiscourse.com/article/international/4011043-reuters-world-news-summary |
| India-Nepal launch new cross-border train | Modi and Nepal PM Balendra Shah flagged off the Saryu-Kamala Express, with a Rs 15,000 crore package. | https://www.jagranjosh.com/articles/school-assembly-news-headlines-november-24-2026-kamla-express-super-tet-spicejet-ferrari-296-and-other-news-1800019603-1 |
| Gukesh begins world title defence | India's D Gukesh defends his world chess crown against Javokhir Sindarov in Geneva from 24 November. | https://www.educationtimes.com/news/school-assembly-news-headlines-for-24-november-2026-top-indian-international-sports-and-business-news/articleshow/136100381.cms |

## Files

- `draw_news.py` — draws `entry.png` (1024x1024) with PIL; run it to regenerate the image.
- `entry.png` — the front page image (1024x1024, under 1 MiB).
- `main.ts` — copies `entry.png` to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR`) and verifies the copy byte-for-byte with SHA-256.
- `LICENSE` — MIT.
- `README.md` — this file.

---

<sub>Entered on [make.fun](https://make.fun/?ref=sh01ee1y&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
