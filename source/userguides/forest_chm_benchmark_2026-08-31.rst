:orphan:

.. _forest_chm_benchmark_2026-08-31:

.. role:: raw-html(raw)
   :format: html

🌲 Canopy Height Model (CHM) — per-location benchmark (v.2026-08-31)
========================================================================

This page details the **Canopy Height Model (CHM)** produced by the 🌲 Forest and trees
**Height estimation** option. **CHM v.2026-08-31** is compared against **CHM v.2026-07-03** on the most-improved
sample per country, using lidar-derived ground truth aggregated to 5 m hexagons (max height).

The metric is the **mean absolute error (MAE)** of canopy height, in metres, against the lidar
ground truth. Across 38 areas of interest, CHM v.2026-08-31 lowers the mean MAE from **4.70 m to 3.24 m
(−31%)** versus CHM v.2026-07-03, with the largest gains in tall, structurally complex forest.

.. raw:: html

   <style>
   .chm-legend{background:#f4f8f4;border:1px solid #d6e2d8;border-left:5px solid #2e7d32;border-radius:10px;padding:14px 18px;margin:16px 0}
   .chm-legend b{color:#1f6b43}
   .chm-legend img{display:block;max-width:560px;width:100%;margin:12px auto 0}
   .bench-row{display:flex;flex-wrap:wrap;gap:10px;margin:10px 0 2px}
   .bench-fig{flex:1 1 220px;min-width:200px;margin:0}
   .bench-fig img{width:100%;height:auto;border:1px solid #cfd3dc;border-radius:6px;cursor:zoom-in;transition:opacity .15s}
   .bench-fig img:hover{opacity:.9}
   .bench-cap{font-size:.84em;font-weight:600;color:#33463b;text-align:center;padding:5px 2px 0;line-height:1.3}
   .bench-cap span{display:block;color:#6b7d72;font-weight:400;font-size:.92em}
   #blb{display:none;position:fixed;inset:0;background:rgba(0,0,0,.92);z-index:9999;align-items:center;justify-content:center;flex-direction:column;cursor:zoom-out}
   #blb.open{display:flex}
   #blb img{max-width:96%;max-height:88vh;border-radius:4px;box-shadow:0 8px 48px #000;object-fit:contain}
   #blb .blb-cap{color:#ddd;font-size:.85em;padding:12px;text-align:center}
   #blb .blb-hint{position:fixed;top:14px;right:18px;color:#888;font-size:.75em}
   </style>
   <div class="chm-legend">
     <b>How to read these maps.</b> The <b>Ground truth</b> panel shows the lidar-derived canopy height as a green ramp (<b>darker green = taller</b>) over the aerial image.
     Each model panel is an <b>error map</b>: the colour ramp shows the
     <b>absolute difference between the model's predicted canopy height and the lidar ground truth</b>,
     per hexagon — <b>0 = exact match</b>, rising to 15 m. Emptier, cooler maps mean predictions closer to lidar.
     <img src="../_static/benchmarks/chm_2026-08-31/scale.png" alt="CHM error colour scale: 0 = exact, up to 15 m">
   </div>
   <div id="blb"><img id="blb-img" src="" alt=""><div class="blb-cap" id="blb-cap"></div><div class="blb-hint">← → to browse · ESC to close</div></div>
   <script>
   (function(){
     var lb=document.getElementById('blb'),im=document.getElementById('blb-img'),cap=document.getElementById('blb-cap');
     var imgs=[],cur=-1;
     function refresh(){imgs=Array.prototype.slice.call(document.querySelectorAll('.bench-img'));}
     function show(i){if(i<0||i>=imgs.length)return;cur=i;var t=imgs[i];im.src=t.getAttribute('data-full')||t.src;cap.textContent=t.getAttribute('data-cap')||'';}
     function open(t){refresh();show(imgs.indexOf(t));lb.classList.add('open');}
     function close(){lb.classList.remove('open');im.src='';cur=-1;}
     function step(d){if(cur<0)return;show((cur+d+imgs.length)%imgs.length);}
     document.addEventListener('click',function(e){
       var t=e.target;
       if(t&&t.classList&&t.classList.contains('bench-img')){open(t);}
       else if(lb.classList.contains('open')){close();}
     });
     document.addEventListener('keydown',function(e){
       if(!lb.classList.contains('open'))return;
       if(e.key==='Escape')close();
       else if(e.key==='ArrowRight'){step(1);e.preventDefault();}
       else if(e.key==='ArrowLeft'){step(-1);e.preventDefault();}
     });
   })();
   </script>


🇷🇺 Russia — RU_4
~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 40 30 30
   :header-rows: 1

   * - Model
     - MAE (m) ↓
     - vs lidar GT
   * - **CHM v.2026-08-31**
     - **2.73**
     - best
   * - CHM v.2026-07-03
     - 8.06
     - −5.33 m worse

.. raw:: html

   <div class="bench-row">
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/chm_2026-08-31/RU_4_gt.jpg" data-full="../_static/benchmarks/chm_2026-08-31/RU_4_gt.jpg" data-cap="Ground truth — lidar canopy on aerial — Russia RU_4" alt="Ground truth — lidar canopy on aerial — Russia RU_4" loading="lazy"><figcaption class="bench-cap">Ground truth<span>lidar canopy height (darker = taller) on aerial</span></figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/chm_2026-08-31/RU_4_old.jpg" data-full="../_static/benchmarks/chm_2026-08-31/RU_4_old.jpg" data-cap="CHM v.2026-07-03 error — Russia RU_4" alt="CHM v.2026-07-03 error — Russia RU_4" loading="lazy"><figcaption class="bench-cap">CHM v.2026-07-03<span>error vs lidar · MAE 8.06 m</span></figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/chm_2026-08-31/RU_4_new.jpg" data-full="../_static/benchmarks/chm_2026-08-31/RU_4_new.jpg" data-cap="CHM v.2026-08-31 error — Russia RU_4" alt="CHM v.2026-08-31 error — Russia RU_4" loading="lazy"><figcaption class="bench-cap">CHM v.2026-08-31<span>error vs lidar · MAE 2.73 m</span></figcaption></figure>
   </div>

*20,980 ground-truth hexagons. Mean absolute height error reduced by 5.33 m (−66%).*


🇨🇭 Switzerland — SWISS_3
~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 40 30 30
   :header-rows: 1

   * - Model
     - MAE (m) ↓
     - vs lidar GT
   * - **CHM v.2026-08-31**
     - **3.36**
     - best
   * - CHM v.2026-07-03
     - 7.78
     - −4.42 m worse

.. raw:: html

   <div class="bench-row">
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/chm_2026-08-31/SWISS_3_gt.jpg" data-full="../_static/benchmarks/chm_2026-08-31/SWISS_3_gt.jpg" data-cap="Ground truth — lidar canopy on aerial — Switzerland SWISS_3" alt="Ground truth — lidar canopy on aerial — Switzerland SWISS_3" loading="lazy"><figcaption class="bench-cap">Ground truth<span>lidar canopy height (darker = taller) on aerial</span></figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/chm_2026-08-31/SWISS_3_old.jpg" data-full="../_static/benchmarks/chm_2026-08-31/SWISS_3_old.jpg" data-cap="CHM v.2026-07-03 error — Switzerland SWISS_3" alt="CHM v.2026-07-03 error — Switzerland SWISS_3" loading="lazy"><figcaption class="bench-cap">CHM v.2026-07-03<span>error vs lidar · MAE 7.78 m</span></figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/chm_2026-08-31/SWISS_3_new.jpg" data-full="../_static/benchmarks/chm_2026-08-31/SWISS_3_new.jpg" data-cap="CHM v.2026-08-31 error — Switzerland SWISS_3" alt="CHM v.2026-08-31 error — Switzerland SWISS_3" loading="lazy"><figcaption class="bench-cap">CHM v.2026-08-31<span>error vs lidar · MAE 3.36 m</span></figcaption></figure>
   </div>

*1,740 ground-truth hexagons. Mean absolute height error reduced by 4.42 m (−57%).*


🇪🇪 Estonia — EST_473628
~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 40 30 30
   :header-rows: 1

   * - Model
     - MAE (m) ↓
     - vs lidar GT
   * - **CHM v.2026-08-31**
     - **2.75**
     - best
   * - CHM v.2026-07-03
     - 5.42
     - −2.67 m worse

.. raw:: html

   <div class="bench-row">
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/chm_2026-08-31/EST_473628_gt.jpg" data-full="../_static/benchmarks/chm_2026-08-31/EST_473628_gt.jpg" data-cap="Ground truth — lidar canopy on aerial — Estonia EST_473628" alt="Ground truth — lidar canopy on aerial — Estonia EST_473628" loading="lazy"><figcaption class="bench-cap">Ground truth<span>lidar canopy height (darker = taller) on aerial</span></figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/chm_2026-08-31/EST_473628_old.jpg" data-full="../_static/benchmarks/chm_2026-08-31/EST_473628_old.jpg" data-cap="CHM v.2026-07-03 error — Estonia EST_473628" alt="CHM v.2026-07-03 error — Estonia EST_473628" loading="lazy"><figcaption class="bench-cap">CHM v.2026-07-03<span>error vs lidar · MAE 5.42 m</span></figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/chm_2026-08-31/EST_473628_new.jpg" data-full="../_static/benchmarks/chm_2026-08-31/EST_473628_new.jpg" data-cap="CHM v.2026-08-31 error — Estonia EST_473628" alt="CHM v.2026-08-31 error — Estonia EST_473628" loading="lazy"><figcaption class="bench-cap">CHM v.2026-08-31<span>error vs lidar · MAE 2.75 m</span></figcaption></figure>
   </div>

*44,641 ground-truth hexagons. Mean absolute height error reduced by 2.67 m (−49%).*


🇲🇽 Mexico — MEX_4
~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 40 30 30
   :header-rows: 1

   * - Model
     - MAE (m) ↓
     - vs lidar GT
   * - **CHM v.2026-08-31**
     - **1.69**
     - best
   * - CHM v.2026-07-03
     - 2.93
     - −1.24 m worse

.. raw:: html

   <div class="bench-row">
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/chm_2026-08-31/MEX_4_gt.jpg" data-full="../_static/benchmarks/chm_2026-08-31/MEX_4_gt.jpg" data-cap="Ground truth — lidar canopy on aerial — Mexico MEX_4" alt="Ground truth — lidar canopy on aerial — Mexico MEX_4" loading="lazy"><figcaption class="bench-cap">Ground truth<span>lidar canopy height (darker = taller) on aerial</span></figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/chm_2026-08-31/MEX_4_old.jpg" data-full="../_static/benchmarks/chm_2026-08-31/MEX_4_old.jpg" data-cap="CHM v.2026-07-03 error — Mexico MEX_4" alt="CHM v.2026-07-03 error — Mexico MEX_4" loading="lazy"><figcaption class="bench-cap">CHM v.2026-07-03<span>error vs lidar · MAE 2.93 m</span></figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/chm_2026-08-31/MEX_4_new.jpg" data-full="../_static/benchmarks/chm_2026-08-31/MEX_4_new.jpg" data-cap="CHM v.2026-08-31 error — Mexico MEX_4" alt="CHM v.2026-08-31 error — Mexico MEX_4" loading="lazy"><figcaption class="bench-cap">CHM v.2026-08-31<span>error vs lidar · MAE 1.69 m</span></figcaption></figure>
   </div>

*18,248 ground-truth hexagons. Mean absolute height error reduced by 1.24 m (−42%).*


🇩🇰 Denmark — DEN_5
~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 40 30 30
   :header-rows: 1

   * - Model
     - MAE (m) ↓
     - vs lidar GT
   * - **CHM v.2026-08-31**
     - **2.20**
     - best
   * - CHM v.2026-07-03
     - 2.67
     - −0.47 m worse

.. raw:: html

   <div class="bench-row">
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/chm_2026-08-31/DEN_5_gt.jpg" data-full="../_static/benchmarks/chm_2026-08-31/DEN_5_gt.jpg" data-cap="Ground truth — lidar canopy on aerial — Denmark DEN_5" alt="Ground truth — lidar canopy on aerial — Denmark DEN_5" loading="lazy"><figcaption class="bench-cap">Ground truth<span>lidar canopy height (darker = taller) on aerial</span></figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/chm_2026-08-31/DEN_5_old.jpg" data-full="../_static/benchmarks/chm_2026-08-31/DEN_5_old.jpg" data-cap="CHM v.2026-07-03 error — Denmark DEN_5" alt="CHM v.2026-07-03 error — Denmark DEN_5" loading="lazy"><figcaption class="bench-cap">CHM v.2026-07-03<span>error vs lidar · MAE 2.67 m</span></figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/chm_2026-08-31/DEN_5_new.jpg" data-full="../_static/benchmarks/chm_2026-08-31/DEN_5_new.jpg" data-cap="CHM v.2026-08-31 error — Denmark DEN_5" alt="CHM v.2026-08-31 error — Denmark DEN_5" loading="lazy"><figcaption class="bench-cap">CHM v.2026-08-31<span>error vs lidar · MAE 2.20 m</span></figcaption></figure>
   </div>

*1,289 ground-truth hexagons. Mean absolute height error reduced by 0.47 m (−18%).*


Summary
-------

.. list-table::
   :widths: 24 20 16 16 14
   :header-rows: 1

   * - Country
     - Sample
     - CHM v.2026-07-03 MAE
     - CHM v.2026-08-31 MAE
     - Improvement
   * - 🇷🇺 Russia
     - RU_4
     - 8.06
     - **2.73**
     - −66%
   * - 🇨🇭 Switzerland
     - SWISS_3
     - 7.78
     - **3.36**
     - −57%
   * - 🇪🇪 Estonia
     - EST_473628
     - 5.42
     - **2.75**
     - −49%
   * - 🇲🇽 Mexico
     - MEX_4
     - 2.93
     - **1.69**
     - −42%
   * - 🇩🇰 Denmark
     - DEN_5
     - 2.67
     - **2.20**
     - −18%

*Mean absolute canopy-height error vs lidar ground truth · 5 m hexagons, max aggregation · absolute-error ramp 0–15 m.
The US sample is omitted (a single, highly generalised tile).*
