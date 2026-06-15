:orphan:

.. _buildings_benchmark_07-06:

.. role:: raw-html(raw)
   :format: html

🏠 Buildings v.07-06 — per-location benchmark
==============================================

This page details the validation of the **🏠 Buildings v.07-06** segmentation model
(Global domain, 0.3 m / z19) on a set of 9 areas of interest (AOI), compared against the
**previous version** (the current production 🏠 Buildings model). For each AOI the two
prediction masks are shown side by side; click any image to open it full size, and use
the ← / → arrow keys to browse between them.

All metrics are area-based: **IoU** is the intersection-over-union of the predicted and
ground-truth building masks, and **F1 / Precision / Recall** are computed on the
overlapping mask area. Evaluation run: 2026-06-13.

.. raw:: html

   <style>
   .mchip{display:inline-block;width:12px;height:12px;border-radius:2px;margin-right:6px;vertical-align:middle;border:1px solid rgba(0,0,0,.25);}
   .bench-row{display:flex;flex-wrap:wrap;gap:12px;margin:10px 0 4px;}
   .bench-fig{flex:1 1 320px;min-width:280px;margin:0;}
   .bench-fig img{width:100%;height:auto;border:1px solid #cfd3dc;border-radius:4px;cursor:zoom-in;transition:opacity .15s;}
   .bench-fig img:hover{opacity:.9;}
   .bench-cap{font-size:.86em;font-weight:600;color:#444;padding:5px 2px;text-align:center;}
   #blb{display:none;position:fixed;inset:0;background:rgba(0,0,0,.92);z-index:9999;align-items:center;justify-content:center;flex-direction:column;cursor:zoom-out;}
   #blb.open{display:flex;}
   #blb img{max-width:96%;max-height:88vh;border-radius:4px;box-shadow:0 8px 48px #000;object-fit:contain;}
   #blb .blb-cap{color:#ddd;font-size:.85em;padding:12px;text-align:center;}
   #blb .blb-hint{position:fixed;top:14px;right:18px;color:#888;font-size:.75em;}
   </style>
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

**Mask colour legend:** :raw-html:`<span class="mchip" style="background:#ff5028"></span>` **v.07-06**  ·  :raw-html:`<span class="mchip" style="background:#2878ff"></span>` **🏠 Buildings (previous)**


United States — Fort Myers
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 34 16 16 16 16
   :header-rows: 1

   * - Model
     - IoU
     - F1
     - Precision
     - Recall
   * - :raw-html:`<span class="mchip" style="background:#ff5028"></span>` **v.07-06**
     - **0.907**
     - **0.951**
     - **0.983**
     - **0.921**
   * - :raw-html:`<span class="mchip" style="background:#2878ff"></span>` 🏠 Buildings (previous)
     - 0.880
     - 0.936
     - 0.974
     - 0.901

.. raw:: html

   <div class="bench-row">
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/US_v0706.jpg" data-full="../_static/benchmarks/buildings_07-06/US_v0706.jpg" data-cap="v.07-06 — United States — Fort Myers" alt="v.07-06 — United States — Fort Myers" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#ff5028"></span>v.07-06</figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/US_prev.jpg" data-full="../_static/benchmarks/buildings_07-06/US_prev.jpg" data-cap="Buildings (previous) — United States — Fort Myers" alt="Buildings (previous) — United States — Fort Myers" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#2878ff"></span>🏠 Buildings (previous)</figcaption></figure>
   </div>


Canada — Rigaud
~~~~~~~~~~~~~~~

.. list-table::
   :widths: 34 16 16 16 16
   :header-rows: 1

   * - Model
     - IoU
     - F1
     - Precision
     - Recall
   * - :raw-html:`<span class="mchip" style="background:#ff5028"></span>` **v.07-06**
     - **0.870**
     - **0.930**
     - **0.934**
     - **0.927**
   * - :raw-html:`<span class="mchip" style="background:#2878ff"></span>` 🏠 Buildings (previous)
     - 0.842
     - 0.914
     - 0.923
     - 0.907

.. raw:: html

   <div class="bench-row">
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/Canada_v0706.jpg" data-full="../_static/benchmarks/buildings_07-06/Canada_v0706.jpg" data-cap="v.07-06 — Canada — Rigaud" alt="v.07-06 — Canada — Rigaud" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#ff5028"></span>v.07-06</figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/Canada_prev.jpg" data-full="../_static/benchmarks/buildings_07-06/Canada_prev.jpg" data-cap="Buildings (previous) — Canada — Rigaud" alt="Buildings (previous) — Canada — Rigaud" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#2878ff"></span>🏠 Buildings (previous)</figcaption></figure>
   </div>


South Africa — Worcester
~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 34 16 16 16 16
   :header-rows: 1

   * - Model
     - IoU
     - F1
     - Precision
     - Recall
   * - :raw-html:`<span class="mchip" style="background:#ff5028"></span>` **v.07-06**
     - 0.495
     - 0.662
     - 0.767
     - **0.582**
   * - :raw-html:`<span class="mchip" style="background:#2878ff"></span>` 🏠 Buildings (previous)
     - **0.500**
     - **0.666**
     - **0.799**
     - 0.572

.. raw:: html

   <div class="bench-row">
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/South_Africa_v0706.jpg" data-full="../_static/benchmarks/buildings_07-06/South_Africa_v0706.jpg" data-cap="v.07-06 — South Africa — Worcester" alt="v.07-06 — South Africa — Worcester" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#ff5028"></span>v.07-06</figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/South_Africa_prev.jpg" data-full="../_static/benchmarks/buildings_07-06/South_Africa_prev.jpg" data-cap="Buildings (previous) — South Africa — Worcester" alt="Buildings (previous) — South Africa — Worcester" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#2878ff"></span>🏠 Buildings (previous)</figcaption></figure>
   </div>


New Zealand — Wellington
~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 34 16 16 16 16
   :header-rows: 1

   * - Model
     - IoU
     - F1
     - Precision
     - Recall
   * - :raw-html:`<span class="mchip" style="background:#ff5028"></span>` **v.07-06**
     - **0.838**
     - **0.912**
     - **0.900**
     - **0.924**
   * - :raw-html:`<span class="mchip" style="background:#2878ff"></span>` 🏠 Buildings (previous)
     - 0.790
     - 0.883
     - 0.888
     - 0.878

.. raw:: html

   <div class="bench-row">
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/New_Zealand_v0706.jpg" data-full="../_static/benchmarks/buildings_07-06/New_Zealand_v0706.jpg" data-cap="v.07-06 — New Zealand — Wellington" alt="v.07-06 — New Zealand — Wellington" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#ff5028"></span>v.07-06</figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/New_Zealand_prev.jpg" data-full="../_static/benchmarks/buildings_07-06/New_Zealand_prev.jpg" data-cap="Buildings (previous) — New Zealand — Wellington" alt="Buildings (previous) — New Zealand — Wellington" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#2878ff"></span>🏠 Buildings (previous)</figcaption></figure>
   </div>


Côte d'Ivoire — Bangolo
~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 34 16 16 16 16
   :header-rows: 1

   * - Model
     - IoU
     - F1
     - Precision
     - Recall
   * - :raw-html:`<span class="mchip" style="background:#ff5028"></span>` **v.07-06**
     - **0.663**
     - **0.797**
     - 0.844
     - **0.755**
   * - :raw-html:`<span class="mchip" style="background:#2878ff"></span>` 🏠 Buildings (previous)
     - 0.642
     - 0.782
     - **0.927**
     - 0.676

.. raw:: html

   <div class="bench-row">
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/Cote_d_Ivoire_v0706.jpg" data-full="../_static/benchmarks/buildings_07-06/Cote_d_Ivoire_v0706.jpg" data-cap="v.07-06 — Côte d'Ivoire — Bangolo" alt="v.07-06 — Côte d'Ivoire — Bangolo" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#ff5028"></span>v.07-06</figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/Cote_d_Ivoire_prev.jpg" data-full="../_static/benchmarks/buildings_07-06/Cote_d_Ivoire_prev.jpg" data-cap="Buildings (previous) — Côte d'Ivoire — Bangolo" alt="Buildings (previous) — Côte d'Ivoire — Bangolo" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#2878ff"></span>🏠 Buildings (previous)</figcaption></figure>
   </div>


United Kingdom — London
~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 34 16 16 16 16
   :header-rows: 1

   * - Model
     - IoU
     - F1
     - Precision
     - Recall
   * - :raw-html:`<span class="mchip" style="background:#ff5028"></span>` **v.07-06**
     - **0.813**
     - **0.897**
     - **0.873**
     - **0.922**
   * - :raw-html:`<span class="mchip" style="background:#2878ff"></span>` 🏠 Buildings (previous)
     - 0.730
     - 0.844
     - 0.800
     - 0.892

.. raw:: html

   <div class="bench-row">
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/United_Kingdom_v0706.jpg" data-full="../_static/benchmarks/buildings_07-06/United_Kingdom_v0706.jpg" data-cap="v.07-06 — United Kingdom — London" alt="v.07-06 — United Kingdom — London" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#ff5028"></span>v.07-06</figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/United_Kingdom_prev.jpg" data-full="../_static/benchmarks/buildings_07-06/United_Kingdom_prev.jpg" data-cap="Buildings (previous) — United Kingdom — London" alt="Buildings (previous) — United Kingdom — London" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#2878ff"></span>🏠 Buildings (previous)</figcaption></figure>
   </div>


Australia — Adelaide
~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 34 16 16 16 16
   :header-rows: 1

   * - Model
     - IoU
     - F1
     - Precision
     - Recall
   * - :raw-html:`<span class="mchip" style="background:#ff5028"></span>` **v.07-06**
     - **0.868**
     - **0.929**
     - **0.914**
     - **0.945**
   * - :raw-html:`<span class="mchip" style="background:#2878ff"></span>` 🏠 Buildings (previous)
     - 0.830
     - 0.907
     - 0.899
     - 0.915

.. raw:: html

   <div class="bench-row">
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/Australia_v0706.jpg" data-full="../_static/benchmarks/buildings_07-06/Australia_v0706.jpg" data-cap="v.07-06 — Australia — Adelaide" alt="v.07-06 — Australia — Adelaide" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#ff5028"></span>v.07-06</figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/Australia_prev.jpg" data-full="../_static/benchmarks/buildings_07-06/Australia_prev.jpg" data-cap="Buildings (previous) — Australia — Adelaide" alt="Buildings (previous) — Australia — Adelaide" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#2878ff"></span>🏠 Buildings (previous)</figcaption></figure>
   </div>


United States — Phoenix
~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 34 16 16 16 16
   :header-rows: 1

   * - Model
     - IoU
     - F1
     - Precision
     - Recall
   * - :raw-html:`<span class="mchip" style="background:#ff5028"></span>` **v.07-06**
     - **0.903**
     - **0.949**
     - **0.944**
     - **0.953**
   * - :raw-html:`<span class="mchip" style="background:#2878ff"></span>` 🏠 Buildings (previous)
     - 0.847
     - 0.917
     - 0.902
     - 0.933

.. raw:: html

   <div class="bench-row">
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/US_Phoenix_v0706.jpg" data-full="../_static/benchmarks/buildings_07-06/US_Phoenix_v0706.jpg" data-cap="v.07-06 — United States — Phoenix" alt="v.07-06 — United States — Phoenix" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#ff5028"></span>v.07-06</figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/US_Phoenix_prev.jpg" data-full="../_static/benchmarks/buildings_07-06/US_Phoenix_prev.jpg" data-cap="Buildings (previous) — United States — Phoenix" alt="Buildings (previous) — United States — Phoenix" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#2878ff"></span>🏠 Buildings (previous)</figcaption></figure>
   </div>


New Zealand — Lower Hutt
~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 34 16 16 16 16
   :header-rows: 1

   * - Model
     - IoU
     - F1
     - Precision
     - Recall
   * - :raw-html:`<span class="mchip" style="background:#ff5028"></span>` **v.07-06**
     - **0.867**
     - **0.929**
     - **0.956**
     - **0.903**
   * - :raw-html:`<span class="mchip" style="background:#2878ff"></span>` 🏠 Buildings (previous)
     - 0.814
     - 0.898
     - 0.931
     - 0.867

.. raw:: html

   <div class="bench-row">
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/NZ_Wellington_v0706.jpg" data-full="../_static/benchmarks/buildings_07-06/NZ_Wellington_v0706.jpg" data-cap="v.07-06 — New Zealand — Lower Hutt" alt="v.07-06 — New Zealand — Lower Hutt" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#ff5028"></span>v.07-06</figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/NZ_Wellington_prev.jpg" data-full="../_static/benchmarks/buildings_07-06/NZ_Wellington_prev.jpg" data-cap="Buildings (previous) — New Zealand — Lower Hutt" alt="Buildings (previous) — New Zealand — Lower Hutt" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#2878ff"></span>🏠 Buildings (previous)</figcaption></figure>
   </div>


Summary
~~~~~~~~

Across the 9 AOIs, **v.07-06** improves on the **previous version** (the current
production 🏠 Buildings model) on every metric on average: mean area-based **F1 rises
from 0.861 to 0.884** (+0.023) and mean **IoU from 0.764 to 0.803** (+0.039), driven
mainly by higher recall (0.838 → 0.870) at slightly higher precision (0.894 → 0.902).
It wins on 8 of the 9 AOIs — including the two newly added sites, Phoenix (F1 0.949 vs
0.917) and Lower Hutt (0.929 vs 0.898) — and is only marginally behind on
South Africa (F1 0.662 vs 0.666), where the dense / informal pattern remains the
hardest case.
