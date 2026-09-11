# Mapflow models — Telegram brief

---

## 🇬🇧 English version

🛰 **Mapflow AI models — the line-up**

Mapflow turns satellite and aerial imagery into ready-to-use vector maps. Here's what's in the box:

🏠 **Buildings** — global, 0.3 m / z19. Extracts rooftops, plus optional building-type classification, contour regularization, simplification, merge with OSM, and **height estimation (beta)** that projects the roof down to ground level for true 3D footprints.
📊 v.2026-07-06: mean F1 **0.893** (aerial), **0.881** (satellite)

🌲 **Forest & trees** — global, 0.6–0.3 m. A solid vegetation mask covering sparse forest, shrubland, small tree groups and narrow tree lines. Options: height classes (<4 m / 4–10 m / >10 m) and individual **tree crowns** as polygons or points.
📊 v.2026-07-03: mean F1 **0.850** — up from 0.513 in the previous version

🚗 **Roads** — 0.3–0.5 m, tuned for rural and suburban areas. Multi-task learning keeps the mask connected where roads hide under trees; centerline extraction plus graph cleanup (gap merging, simplification, removal of stray segments).

🧩 **Buildings + Roads + Forest** — all three in a single run, returned as one topology-corrected GeoJSON.

🗺 **Open Data** — pull OpenStreetMap and Overture layers with no AI involved, as a complement to model output.

⚙️ **Custom models, on request:** construction sites, high-density housing, agriculture fields, Segment Anything (zoom-dependent, from land use down to single trees), swimming pools (F1 > 0.95), solar panels. You can also bring your own model — or ask us to train one for your use case.

Run it all in the web app, the QGIS plugin, or via API.
🔗 mapflow.ai/models · docs.mapflow.ai

---

## 🇷🇺 Русская версия

🛰 **Модели Mapflow — что есть в линейке**

Mapflow превращает спутниковые и аэроснимки в готовые векторные карты. Что внутри:

🏠 **Здания** — глобально, 0,3 м / z19. Выделяет крыши зданий, плюс опции: классификация по типам, регуляризация контуров, упрощение геометрии, слияние с OSM и **оценка высоты (beta)** — контур проецируется на землю, получаются настоящие 3D-футпринты.
📊 v.2026-07-06: средний F1 **0,893** (аэро), **0,881** (спутник)

🌲 **Лес и деревья** — глобально, 0,6–0,3 м. Сплошная маска растительности: разреженный лес, кустарники, небольшие группы деревьев и узкие лесополосы. Опции: классы высоты (<4 м / 4–10 м / >10 м) и отдельные **кроны деревьев** — полигонами или точками.
📊 v.2026-07-03: средний F1 **0,850** — против 0,513 у прошлой версии

🚗 **Дороги** — 0,3–0,5 м, обучена в первую очередь на сельской и пригородной местности. Multi-task learning помогает не рвать маску там, где дорогу закрывают деревья; выделяется осевая линия, затем чистится граф (склейка разрывов, упрощение, удаление коротких и висячих сегментов).

🧩 **Здания + Дороги + Лес** — все три модели за один запуск, результат — единый GeoJSON с исправленной топологией.

🗺 **Открытые данные** — выгрузка слоёв OpenStreetMap и Overture без ИИ, как дополнение к результатам моделей.

⚙️ **Кастомные модели, по запросу:** стройплощадки, плотная застройка, сельхозполя, Segment Anything (результат зависит от зума — от типов землепользования до отдельных деревьев), бассейны (F1 > 0,95), солнечные панели. Можно подключить и свою модель — или заказать обучение под вашу задачу.

Всё это доступно в веб-приложении, плагине для QGIS и через API.
🔗 mapflow.ai/models · docs.mapflow.ai
