:orphan:

.. _buildings_benchmark_07-06:

.. role:: raw-html(raw)
   :format: html

🏠 Buildings v.07-06 — per-location benchmark
==============================================

This page details the validation of the **🏠 Buildings v.07-06** segmentation model
(Global domain, 0.3 m / z19) on a set of 7 areas of interest (AOI), compared against the
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


United States
~~~~~~~~~~~~~

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
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/US_v0706.jpg" data-full="../_static/benchmarks/buildings_07-06/US_v0706.jpg" data-cap="v.07-06 — United States" alt="v.07-06 — United States" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#ff5028"></span>v.07-06</figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/US_prev.jpg" data-full="../_static/benchmarks/buildings_07-06/US_prev.jpg" data-cap="Buildings (previous) — United States" alt="Buildings (previous) — United States" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#2878ff"></span>🏠 Buildings (previous)</figcaption></figure>
   </div>


Canada
~~~~~~

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
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/Canada_v0706.jpg" data-full="../_static/benchmarks/buildings_07-06/Canada_v0706.jpg" data-cap="v.07-06 — Canada" alt="v.07-06 — Canada" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#ff5028"></span>v.07-06</figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/Canada_prev.jpg" data-full="../_static/benchmarks/buildings_07-06/Canada_prev.jpg" data-cap="Buildings (previous) — Canada" alt="Buildings (previous) — Canada" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#2878ff"></span>🏠 Buildings (previous)</figcaption></figure>
   </div>


South Africa
~~~~~~~~~~~~

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
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/South_Africa_v0706.jpg" data-full="../_static/benchmarks/buildings_07-06/South_Africa_v0706.jpg" data-cap="v.07-06 — South Africa" alt="v.07-06 — South Africa" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#ff5028"></span>v.07-06</figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/South_Africa_prev.jpg" data-full="../_static/benchmarks/buildings_07-06/South_Africa_prev.jpg" data-cap="Buildings (previous) — South Africa" alt="Buildings (previous) — South Africa" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#2878ff"></span>🏠 Buildings (previous)</figcaption></figure>
   </div>


New Zealand
~~~~~~~~~~~

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
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/New_Zealand_v0706.jpg" data-full="../_static/benchmarks/buildings_07-06/New_Zealand_v0706.jpg" data-cap="v.07-06 — New Zealand" alt="v.07-06 — New Zealand" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#ff5028"></span>v.07-06</figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/New_Zealand_prev.jpg" data-full="../_static/benchmarks/buildings_07-06/New_Zealand_prev.jpg" data-cap="Buildings (previous) — New Zealand" alt="Buildings (previous) — New Zealand" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#2878ff"></span>🏠 Buildings (previous)</figcaption></figure>
   </div>


Côte d'Ivoire
~~~~~~~~~~~~~

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
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/Cote_d_Ivoire_v0706.jpg" data-full="../_static/benchmarks/buildings_07-06/Cote_d_Ivoire_v0706.jpg" data-cap="v.07-06 — Côte d'Ivoire" alt="v.07-06 — Côte d'Ivoire" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#ff5028"></span>v.07-06</figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/Cote_d_Ivoire_prev.jpg" data-full="../_static/benchmarks/buildings_07-06/Cote_d_Ivoire_prev.jpg" data-cap="Buildings (previous) — Côte d'Ivoire" alt="Buildings (previous) — Côte d'Ivoire" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#2878ff"></span>🏠 Buildings (previous)</figcaption></figure>
   </div>


United Kingdom
~~~~~~~~~~~~~~

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
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/United_Kingdom_v0706.jpg" data-full="../_static/benchmarks/buildings_07-06/United_Kingdom_v0706.jpg" data-cap="v.07-06 — United Kingdom" alt="v.07-06 — United Kingdom" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#ff5028"></span>v.07-06</figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/United_Kingdom_prev.jpg" data-full="../_static/benchmarks/buildings_07-06/United_Kingdom_prev.jpg" data-cap="Buildings (previous) — United Kingdom" alt="Buildings (previous) — United Kingdom" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#2878ff"></span>🏠 Buildings (previous)</figcaption></figure>
   </div>


Australia
~~~~~~~~~

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
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/Australia_v0706.jpg" data-full="../_static/benchmarks/buildings_07-06/Australia_v0706.jpg" data-cap="v.07-06 — Australia" alt="v.07-06 — Australia" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#ff5028"></span>v.07-06</figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/Australia_prev.jpg" data-full="../_static/benchmarks/buildings_07-06/Australia_prev.jpg" data-cap="Buildings (previous) — Australia" alt="Buildings (previous) — Australia" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#2878ff"></span>🏠 Buildings (previous)</figcaption></figure>
   </div>


Summary
~~~~~~~~

Compared with the **previous version** (the current production 🏠 Buildings model),
**v.07-06** lifts the mean area-based **F1 from 0.847 to 0.868** (+0.021) and mean
**IoU from 0.745 to 0.779** (+0.034), driven mainly by higher recall (0.820 → 0.854)
at essentially unchanged precision (0.887 → 0.888). It now improves on 6 of the 7 AOIs —
including the previously weaker Côte d'Ivoire (F1 0.797 vs 0.782) and the United Kingdom
(0.897 vs 0.844) — and is only marginally behind on South Africa (F1 0.662 vs 0.666),
where the dense / informal pattern remains the hardest case.
