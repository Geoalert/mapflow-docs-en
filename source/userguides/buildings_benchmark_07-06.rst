:orphan:

.. _buildings_benchmark_07-06:

.. role:: raw-html(raw)
   :format: html

🏠 Buildings v.2026-07-06 — per-location benchmark
============================================================

This page details the validation of the **🏠 Buildings v.2026-07-06** segmentation model
(Global domain, 0.3 m / z19) on 14 areas of interest (AOI), compared against the
**previous version v.2025-12-10** (the current production 🏠 Buildings model). For each AOI the two
prediction masks are shown side by side; click any image to open it full size, and use
the ← / → arrow keys to browse between them.

All metrics are area-based: **IoU** is the intersection-over-union of the predicted and
ground-truth building masks, and **F1 / Precision / Recall** are computed on the
overlapping mask area. Evaluation runs: 2026-06-13 (global set) and 2026-06-16 (satellite set).

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

**Mask colour legend:** :raw-html:`<span class="mchip" style="background:#ff5028"></span>` **v.2026-07-06**  ·  :raw-html:`<span class="mchip" style="background:#2878ff"></span>` **v.2025-12-10**


Aerial imagery validation set
------------------------------

Validation on the global set of 9 areas of interest (mixed urban / suburban / rural).


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
   * - :raw-html:`<span class="mchip" style="background:#ff5028"></span>` **v.2026-07-06**
     - **0.907**
     - **0.951**
     - **0.983**
     - **0.921**
   * - :raw-html:`<span class="mchip" style="background:#2878ff"></span>` v.2025-12-10
     - 0.880
     - 0.936
     - 0.974
     - 0.901

.. raw:: html

   <div class="bench-row">
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/US_v0706.jpg" data-full="../_static/benchmarks/buildings_07-06/US_v0706.jpg" data-cap="v.2026-07-06 — United States — Fort Myers" alt="v.2026-07-06 — United States — Fort Myers" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#ff5028"></span>v.2026-07-06</figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/US_prev.jpg" data-full="../_static/benchmarks/buildings_07-06/US_prev.jpg" data-cap="v.2025-12-10 — United States — Fort Myers" alt="v.2025-12-10 — United States — Fort Myers" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#2878ff"></span>v.2025-12-10</figcaption></figure>
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
   * - :raw-html:`<span class="mchip" style="background:#ff5028"></span>` **v.2026-07-06**
     - **0.870**
     - **0.930**
     - **0.934**
     - **0.927**
   * - :raw-html:`<span class="mchip" style="background:#2878ff"></span>` v.2025-12-10
     - 0.842
     - 0.914
     - 0.923
     - 0.907

.. raw:: html

   <div class="bench-row">
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/Canada_v0706.jpg" data-full="../_static/benchmarks/buildings_07-06/Canada_v0706.jpg" data-cap="v.2026-07-06 — Canada — Rigaud" alt="v.2026-07-06 — Canada — Rigaud" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#ff5028"></span>v.2026-07-06</figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/Canada_prev.jpg" data-full="../_static/benchmarks/buildings_07-06/Canada_prev.jpg" data-cap="v.2025-12-10 — Canada — Rigaud" alt="v.2025-12-10 — Canada — Rigaud" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#2878ff"></span>v.2025-12-10</figcaption></figure>
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
   * - :raw-html:`<span class="mchip" style="background:#ff5028"></span>` **v.2026-07-06**
     - **0.592**
     - **0.744**
     - **0.867**
     - **0.651**
   * - :raw-html:`<span class="mchip" style="background:#2878ff"></span>` v.2025-12-10
     - 0.385
     - 0.556
     - 0.845
     - 0.415

.. raw:: html

   <div class="bench-row">
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/South_Africa_v0706.jpg" data-full="../_static/benchmarks/buildings_07-06/South_Africa_v0706.jpg" data-cap="v.2026-07-06 — South Africa — Worcester" alt="v.2026-07-06 — South Africa — Worcester" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#ff5028"></span>v.2026-07-06</figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/South_Africa_prev.jpg" data-full="../_static/benchmarks/buildings_07-06/South_Africa_prev.jpg" data-cap="v.2025-12-10 — South Africa — Worcester" alt="v.2025-12-10 — South Africa — Worcester" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#2878ff"></span>v.2025-12-10</figcaption></figure>
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
   * - :raw-html:`<span class="mchip" style="background:#ff5028"></span>` **v.2026-07-06**
     - **0.838**
     - **0.912**
     - **0.900**
     - **0.924**
   * - :raw-html:`<span class="mchip" style="background:#2878ff"></span>` v.2025-12-10
     - 0.790
     - 0.883
     - 0.888
     - 0.878

.. raw:: html

   <div class="bench-row">
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/New_Zealand_v0706.jpg" data-full="../_static/benchmarks/buildings_07-06/New_Zealand_v0706.jpg" data-cap="v.2026-07-06 — New Zealand — Wellington" alt="v.2026-07-06 — New Zealand — Wellington" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#ff5028"></span>v.2026-07-06</figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/New_Zealand_prev.jpg" data-full="../_static/benchmarks/buildings_07-06/New_Zealand_prev.jpg" data-cap="v.2025-12-10 — New Zealand — Wellington" alt="v.2025-12-10 — New Zealand — Wellington" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#2878ff"></span>v.2025-12-10</figcaption></figure>
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
   * - :raw-html:`<span class="mchip" style="background:#ff5028"></span>` **v.2026-07-06**
     - **0.663**
     - **0.797**
     - 0.844
     - **0.755**
   * - :raw-html:`<span class="mchip" style="background:#2878ff"></span>` v.2025-12-10
     - 0.642
     - 0.782
     - **0.927**
     - 0.676

.. raw:: html

   <div class="bench-row">
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/Cote_d_Ivoire_v0706.jpg" data-full="../_static/benchmarks/buildings_07-06/Cote_d_Ivoire_v0706.jpg" data-cap="v.2026-07-06 — Côte d'Ivoire — Bangolo" alt="v.2026-07-06 — Côte d'Ivoire — Bangolo" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#ff5028"></span>v.2026-07-06</figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/Cote_d_Ivoire_prev.jpg" data-full="../_static/benchmarks/buildings_07-06/Cote_d_Ivoire_prev.jpg" data-cap="v.2025-12-10 — Côte d'Ivoire — Bangolo" alt="v.2025-12-10 — Côte d'Ivoire — Bangolo" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#2878ff"></span>v.2025-12-10</figcaption></figure>
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
   * - :raw-html:`<span class="mchip" style="background:#ff5028"></span>` **v.2026-07-06**
     - **0.813**
     - **0.897**
     - **0.873**
     - **0.922**
   * - :raw-html:`<span class="mchip" style="background:#2878ff"></span>` v.2025-12-10
     - 0.730
     - 0.844
     - 0.800
     - 0.892

.. raw:: html

   <div class="bench-row">
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/United_Kingdom_v0706.jpg" data-full="../_static/benchmarks/buildings_07-06/United_Kingdom_v0706.jpg" data-cap="v.2026-07-06 — United Kingdom — London" alt="v.2026-07-06 — United Kingdom — London" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#ff5028"></span>v.2026-07-06</figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/United_Kingdom_prev.jpg" data-full="../_static/benchmarks/buildings_07-06/United_Kingdom_prev.jpg" data-cap="v.2025-12-10 — United Kingdom — London" alt="v.2025-12-10 — United Kingdom — London" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#2878ff"></span>v.2025-12-10</figcaption></figure>
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
   * - :raw-html:`<span class="mchip" style="background:#ff5028"></span>` **v.2026-07-06**
     - **0.868**
     - **0.929**
     - **0.914**
     - **0.945**
   * - :raw-html:`<span class="mchip" style="background:#2878ff"></span>` v.2025-12-10
     - 0.830
     - 0.907
     - 0.899
     - 0.915

.. raw:: html

   <div class="bench-row">
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/Australia_v0706.jpg" data-full="../_static/benchmarks/buildings_07-06/Australia_v0706.jpg" data-cap="v.2026-07-06 — Australia — Adelaide" alt="v.2026-07-06 — Australia — Adelaide" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#ff5028"></span>v.2026-07-06</figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/Australia_prev.jpg" data-full="../_static/benchmarks/buildings_07-06/Australia_prev.jpg" data-cap="v.2025-12-10 — Australia — Adelaide" alt="v.2025-12-10 — Australia — Adelaide" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#2878ff"></span>v.2025-12-10</figcaption></figure>
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
   * - :raw-html:`<span class="mchip" style="background:#ff5028"></span>` **v.2026-07-06**
     - **0.903**
     - **0.949**
     - **0.944**
     - **0.953**
   * - :raw-html:`<span class="mchip" style="background:#2878ff"></span>` v.2025-12-10
     - 0.847
     - 0.917
     - 0.902
     - 0.933

.. raw:: html

   <div class="bench-row">
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/US_Phoenix_v0706.jpg" data-full="../_static/benchmarks/buildings_07-06/US_Phoenix_v0706.jpg" data-cap="v.2026-07-06 — United States — Phoenix" alt="v.2026-07-06 — United States — Phoenix" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#ff5028"></span>v.2026-07-06</figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/US_Phoenix_prev.jpg" data-full="../_static/benchmarks/buildings_07-06/US_Phoenix_prev.jpg" data-cap="v.2025-12-10 — United States — Phoenix" alt="v.2025-12-10 — United States — Phoenix" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#2878ff"></span>v.2025-12-10</figcaption></figure>
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
   * - :raw-html:`<span class="mchip" style="background:#ff5028"></span>` **v.2026-07-06**
     - **0.867**
     - **0.929**
     - **0.956**
     - **0.903**
   * - :raw-html:`<span class="mchip" style="background:#2878ff"></span>` v.2025-12-10
     - 0.814
     - 0.898
     - 0.931
     - 0.867

.. raw:: html

   <div class="bench-row">
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/NZ_Wellington_v0706.jpg" data-full="../_static/benchmarks/buildings_07-06/NZ_Wellington_v0706.jpg" data-cap="v.2026-07-06 — New Zealand — Lower Hutt" alt="v.2026-07-06 — New Zealand — Lower Hutt" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#ff5028"></span>v.2026-07-06</figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/NZ_Wellington_prev.jpg" data-full="../_static/benchmarks/buildings_07-06/NZ_Wellington_prev.jpg" data-cap="v.2025-12-10 — New Zealand — Lower Hutt" alt="v.2025-12-10 — New Zealand — Lower Hutt" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#2878ff"></span>v.2025-12-10</figcaption></figure>
   </div>


Satellite imagery validation set
-----------------------------------

Validation on the global set of satellite imagery across 5 dense urban areas.


United Arab Emirates — Abu Dhabi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 34 16 16 16 16
   :header-rows: 1

   * - Model
     - IoU
     - F1
     - Precision
     - Recall
   * - :raw-html:`<span class="mchip" style="background:#ff5028"></span>` **v.2026-07-06**
     - **0.751**
     - **0.858**
     - **0.828**
     - **0.890**
   * - :raw-html:`<span class="mchip" style="background:#2878ff"></span>` v.2025-12-10
     - 0.717
     - 0.835
     - 0.817
     - 0.854

.. raw:: html

   <div class="bench-row">
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/AbuDhabi_v0706.jpg" data-full="../_static/benchmarks/buildings_07-06/AbuDhabi_v0706.jpg" data-cap="v.2026-07-06 — United Arab Emirates — Abu Dhabi" alt="v.2026-07-06 — United Arab Emirates — Abu Dhabi" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#ff5028"></span>v.2026-07-06</figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/AbuDhabi_prev.jpg" data-full="../_static/benchmarks/buildings_07-06/AbuDhabi_prev.jpg" data-cap="v.2025-12-10 — United Arab Emirates — Abu Dhabi" alt="v.2025-12-10 — United Arab Emirates — Abu Dhabi" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#2878ff"></span>v.2025-12-10</figcaption></figure>
   </div>


India — Bangalore
~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 34 16 16 16 16
   :header-rows: 1

   * - Model
     - IoU
     - F1
     - Precision
     - Recall
   * - :raw-html:`<span class="mchip" style="background:#ff5028"></span>` **v.2026-07-06**
     - **0.779**
     - **0.876**
     - **0.859**
     - **0.894**
   * - :raw-html:`<span class="mchip" style="background:#2878ff"></span>` v.2025-12-10
     - 0.735
     - 0.847
     - 0.848
     - 0.846

.. raw:: html

   <div class="bench-row">
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/Bangalore_v0706.jpg" data-full="../_static/benchmarks/buildings_07-06/Bangalore_v0706.jpg" data-cap="v.2026-07-06 — India — Bangalore" alt="v.2026-07-06 — India — Bangalore" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#ff5028"></span>v.2026-07-06</figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/Bangalore_prev.jpg" data-full="../_static/benchmarks/buildings_07-06/Bangalore_prev.jpg" data-cap="v.2025-12-10 — India — Bangalore" alt="v.2025-12-10 — India — Bangalore" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#2878ff"></span>v.2025-12-10</figcaption></figure>
   </div>


Saudi Arabia — Riyadh
~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 34 16 16 16 16
   :header-rows: 1

   * - Model
     - IoU
     - F1
     - Precision
     - Recall
   * - :raw-html:`<span class="mchip" style="background:#ff5028"></span>` **v.2026-07-06**
     - **0.817**
     - **0.899**
     - **0.920**
     - 0.879
   * - :raw-html:`<span class="mchip" style="background:#2878ff"></span>` v.2025-12-10
     - 0.654
     - 0.791
     - 0.687
     - **0.931**

.. raw:: html

   <div class="bench-row">
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/Riyadh_v0706.jpg" data-full="../_static/benchmarks/buildings_07-06/Riyadh_v0706.jpg" data-cap="v.2026-07-06 — Saudi Arabia — Riyadh" alt="v.2026-07-06 — Saudi Arabia — Riyadh" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#ff5028"></span>v.2026-07-06</figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/Riyadh_prev.jpg" data-full="../_static/benchmarks/buildings_07-06/Riyadh_prev.jpg" data-cap="v.2025-12-10 — Saudi Arabia — Riyadh" alt="v.2025-12-10 — Saudi Arabia — Riyadh" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#2878ff"></span>v.2025-12-10</figcaption></figure>
   </div>


India — Thane
~~~~~~~~~~~~~

.. list-table::
   :widths: 34 16 16 16 16
   :header-rows: 1

   * - Model
     - IoU
     - F1
     - Precision
     - Recall
   * - :raw-html:`<span class="mchip" style="background:#ff5028"></span>` **v.2026-07-06**
     - **0.768**
     - **0.869**
     - **0.889**
     - **0.849**
   * - :raw-html:`<span class="mchip" style="background:#2878ff"></span>` v.2025-12-10
     - 0.722
     - 0.839
     - 0.871
     - 0.809

.. raw:: html

   <div class="bench-row">
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/Thane_v0706.jpg" data-full="../_static/benchmarks/buildings_07-06/Thane_v0706.jpg" data-cap="v.2026-07-06 — India — Thane" alt="v.2026-07-06 — India — Thane" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#ff5028"></span>v.2026-07-06</figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/Thane_prev.jpg" data-full="../_static/benchmarks/buildings_07-06/Thane_prev.jpg" data-cap="v.2025-12-10 — India — Thane" alt="v.2025-12-10 — India — Thane" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#2878ff"></span>v.2025-12-10</figcaption></figure>
   </div>


Russia — Ufa
~~~~~~~~~~~~

.. list-table::
   :widths: 34 16 16 16 16
   :header-rows: 1

   * - Model
     - IoU
     - F1
     - Precision
     - Recall
   * - :raw-html:`<span class="mchip" style="background:#ff5028"></span>` **v.2026-07-06**
     - **0.821**
     - **0.902**
     - **0.897**
     - **0.907**
   * - :raw-html:`<span class="mchip" style="background:#2878ff"></span>` v.2025-12-10
     - 0.818
     - 0.900
     - 0.897
     - 0.903

.. raw:: html

   <div class="bench-row">
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/Ufa_v0706.jpg" data-full="../_static/benchmarks/buildings_07-06/Ufa_v0706.jpg" data-cap="v.2026-07-06 — Russia — Ufa" alt="v.2026-07-06 — Russia — Ufa" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#ff5028"></span>v.2026-07-06</figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/buildings_07-06/Ufa_prev.jpg" data-full="../_static/benchmarks/buildings_07-06/Ufa_prev.jpg" data-cap="v.2025-12-10 — Russia — Ufa" alt="v.2025-12-10 — Russia — Ufa" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#2878ff"></span>v.2025-12-10</figcaption></figure>
   </div>


Summary
-------

**v.2026-07-06** leads the previous production model on F1 in **all 14 AOIs**. On the global
validation set of aerial imagery (9 AOIs) the mean area-based F1 rises from 0.849 to **0.893** (IoU 0.751 →
**0.813**); on the 5 dense-urban satellite imagery AOIs the mean F1 rises from 0.842 to **0.881**
(IoU 0.729 → **0.787**), driven mainly by higher recall and precision in informal and
high-density built-up areas such as Riyadh, Bangalore and Thane.