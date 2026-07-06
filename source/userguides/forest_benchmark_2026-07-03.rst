:orphan:

.. _forest_benchmark_2026-07-03:

.. role:: raw-html(raw)
   :format: html

🌲 Forest and trees v.2026-07-03 — per-location benchmark
================================================================

This page details the validation of the **🌲 Forest and trees v.2026-07-03** segmentation model
on 8 areas of interest (AOI), compared against the **previous version v.2025-06-14**. For each AOI the two prediction masks are shown side by
side; click any image to open it full size, and use the ← / → arrow keys to browse
between them.

All metrics are area-based: **IoU** is the intersection-over-union of the predicted and
ground-truth vegetation masks, and **F1 / Precision / Recall** are computed on the
overlapping mask area. Evaluation run: 2026-07-03.

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

**Mask colour legend:** :raw-html:`<span class="mchip" style="background:#ff5028"></span>` **v.2026-07-03**  ·  :raw-html:`<span class="mchip" style="background:#2878ff"></span>` **v.2025-06-14**


Philippines — Balanga
~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 30 16 16 16 16
   :header-rows: 1

   * - Model
     - IoU
     - F1
     - Precision
     - Recall
   * - :raw-html:`<span class="mchip" style="background:#ff5028"></span>` **v.2026-07-03**
     - **0.806**
     - **0.892**
     - 0.864
     - **0.923**
   * - :raw-html:`<span class="mchip" style="background:#2878ff"></span>` v.2025-06-14
     - 0.593
     - 0.745
     - **0.914**
     - 0.628

.. raw:: html

   <div class="bench-row">
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/forest_2026-07-03/Balanga_new.jpg" data-full="../_static/benchmarks/forest_2026-07-03/Balanga_new.jpg" data-cap="v.2026-07-03 — Philippines — Balanga" alt="v.2026-07-03 — Philippines — Balanga" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#ff5028"></span>v.2026-07-03</figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/forest_2026-07-03/Balanga_old.jpg" data-full="../_static/benchmarks/forest_2026-07-03/Balanga_old.jpg" data-cap="v.2025-06-14 — Philippines — Balanga" alt="v.2025-06-14 — Philippines — Balanga" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#2878ff"></span>v.2025-06-14</figcaption></figure>
   </div>


Spain — Velilla de San Antonio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 30 16 16 16 16
   :header-rows: 1

   * - Model
     - IoU
     - F1
     - Precision
     - Recall
   * - :raw-html:`<span class="mchip" style="background:#ff5028"></span>` **v.2026-07-03**
     - **0.784**
     - **0.879**
     - 0.894
     - **0.864**
   * - :raw-html:`<span class="mchip" style="background:#2878ff"></span>` v.2025-06-14
     - 0.008
     - 0.015
     - **0.989**
     - 0.008

.. raw:: html

   <div class="bench-row">
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/forest_2026-07-03/Velilla_new.jpg" data-full="../_static/benchmarks/forest_2026-07-03/Velilla_new.jpg" data-cap="v.2026-07-03 — Spain — Velilla de San Antonio" alt="v.2026-07-03 — Spain — Velilla de San Antonio" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#ff5028"></span>v.2026-07-03</figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/forest_2026-07-03/Velilla_old.jpg" data-full="../_static/benchmarks/forest_2026-07-03/Velilla_old.jpg" data-cap="v.2025-06-14 — Spain — Velilla de San Antonio" alt="v.2025-06-14 — Spain — Velilla de San Antonio" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#2878ff"></span>v.2025-06-14</figcaption></figure>
   </div>


Spain — Madrid
~~~~~~~~~~~~~~

.. list-table::
   :widths: 30 16 16 16 16
   :header-rows: 1

   * - Model
     - IoU
     - F1
     - Precision
     - Recall
   * - :raw-html:`<span class="mchip" style="background:#ff5028"></span>` **v.2026-07-03**
     - **0.813**
     - **0.897**
     - 0.880
     - **0.915**
   * - :raw-html:`<span class="mchip" style="background:#2878ff"></span>` v.2025-06-14
     - 0.447
     - 0.618
     - **0.973**
     - 0.453

.. raw:: html

   <div class="bench-row">
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/forest_2026-07-03/Madrid_new.jpg" data-full="../_static/benchmarks/forest_2026-07-03/Madrid_new.jpg" data-cap="v.2026-07-03 — Spain — Madrid" alt="v.2026-07-03 — Spain — Madrid" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#ff5028"></span>v.2026-07-03</figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/forest_2026-07-03/Madrid_old.jpg" data-full="../_static/benchmarks/forest_2026-07-03/Madrid_old.jpg" data-cap="v.2025-06-14 — Spain — Madrid" alt="v.2025-06-14 — Spain — Madrid" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#2878ff"></span>v.2025-06-14</figcaption></figure>
   </div>


Italy — Crotone
~~~~~~~~~~~~~~~

.. list-table::
   :widths: 30 16 16 16 16
   :header-rows: 1

   * - Model
     - IoU
     - F1
     - Precision
     - Recall
   * - :raw-html:`<span class="mchip" style="background:#ff5028"></span>` **v.2026-07-03**
     - **0.862**
     - **0.926**
     - 0.944
     - **0.909**
   * - :raw-html:`<span class="mchip" style="background:#2878ff"></span>` v.2025-06-14
     - 0.803
     - 0.890
     - **0.988**
     - 0.811

.. raw:: html

   <div class="bench-row">
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/forest_2026-07-03/Crotone_new.jpg" data-full="../_static/benchmarks/forest_2026-07-03/Crotone_new.jpg" data-cap="v.2026-07-03 — Italy — Crotone" alt="v.2026-07-03 — Italy — Crotone" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#ff5028"></span>v.2026-07-03</figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/forest_2026-07-03/Crotone_old.jpg" data-full="../_static/benchmarks/forest_2026-07-03/Crotone_old.jpg" data-cap="v.2025-06-14 — Italy — Crotone" alt="v.2025-06-14 — Italy — Crotone" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#2878ff"></span>v.2025-06-14</figcaption></figure>
   </div>


Spain — Rus
~~~~~~~~~~~

.. list-table::
   :widths: 30 16 16 16 16
   :header-rows: 1

   * - Model
     - IoU
     - F1
     - Precision
     - Recall
   * - :raw-html:`<span class="mchip" style="background:#ff5028"></span>` **v.2026-07-03**
     - **0.617**
     - **0.763**
     - 0.699
     - **0.841**
   * - :raw-html:`<span class="mchip" style="background:#2878ff"></span>` v.2025-06-14
     - 0.057
     - 0.108
     - **0.964**
     - 0.057

.. raw:: html

   <div class="bench-row">
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/forest_2026-07-03/Rus_new.jpg" data-full="../_static/benchmarks/forest_2026-07-03/Rus_new.jpg" data-cap="v.2026-07-03 — Spain — Rus" alt="v.2026-07-03 — Spain — Rus" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#ff5028"></span>v.2026-07-03</figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/forest_2026-07-03/Rus_old.jpg" data-full="../_static/benchmarks/forest_2026-07-03/Rus_old.jpg" data-cap="v.2025-06-14 — Spain — Rus" alt="v.2025-06-14 — Spain — Rus" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#2878ff"></span>v.2025-06-14</figcaption></figure>
   </div>


Spain — Cuenca
~~~~~~~~~~~~~~

.. list-table::
   :widths: 30 16 16 16 16
   :header-rows: 1

   * - Model
     - IoU
     - F1
     - Precision
     - Recall
   * - :raw-html:`<span class="mchip" style="background:#ff5028"></span>` **v.2026-07-03**
     - **0.763**
     - **0.865**
     - 0.859
     - **0.872**
   * - :raw-html:`<span class="mchip" style="background:#2878ff"></span>` v.2025-06-14
     - 0.459
     - 0.629
     - **0.873**
     - 0.492

.. raw:: html

   <div class="bench-row">
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/forest_2026-07-03/Cuenca_new.jpg" data-full="../_static/benchmarks/forest_2026-07-03/Cuenca_new.jpg" data-cap="v.2026-07-03 — Spain — Cuenca" alt="v.2026-07-03 — Spain — Cuenca" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#ff5028"></span>v.2026-07-03</figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/forest_2026-07-03/Cuenca_old.jpg" data-full="../_static/benchmarks/forest_2026-07-03/Cuenca_old.jpg" data-cap="v.2025-06-14 — Spain — Cuenca" alt="v.2025-06-14 — Spain — Cuenca" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#2878ff"></span>v.2025-06-14</figcaption></figure>
   </div>


Argentina — La Banda
~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 30 16 16 16 16
   :header-rows: 1

   * - Model
     - IoU
     - F1
     - Precision
     - Recall
   * - :raw-html:`<span class="mchip" style="background:#ff5028"></span>` **v.2026-07-03**
     - **0.576**
     - **0.731**
     - 0.653
     - **0.829**
   * - :raw-html:`<span class="mchip" style="background:#2878ff"></span>` v.2025-06-14
     - 0.233
     - 0.378
     - **0.958**
     - 0.235

.. raw:: html

   <div class="bench-row">
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/forest_2026-07-03/LaBanda_new.jpg" data-full="../_static/benchmarks/forest_2026-07-03/LaBanda_new.jpg" data-cap="v.2026-07-03 — Argentina — La Banda" alt="v.2026-07-03 — Argentina — La Banda" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#ff5028"></span>v.2026-07-03</figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/forest_2026-07-03/LaBanda_old.jpg" data-full="../_static/benchmarks/forest_2026-07-03/LaBanda_old.jpg" data-cap="v.2025-06-14 — Argentina — La Banda" alt="v.2025-06-14 — Argentina — La Banda" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#2878ff"></span>v.2025-06-14</figcaption></figure>
   </div>


Uzbekistan — Tashkent
~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 30 16 16 16 16
   :header-rows: 1

   * - Model
     - IoU
     - F1
     - Precision
     - Recall
   * - :raw-html:`<span class="mchip" style="background:#ff5028"></span>` **v.2026-07-03**
     - **0.730**
     - **0.844**
     - 0.905
     - **0.791**
   * - :raw-html:`<span class="mchip" style="background:#2878ff"></span>` v.2025-06-14
     - 0.568
     - 0.724
     - **0.981**
     - 0.574

.. raw:: html

   <div class="bench-row">
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/forest_2026-07-03/Tashkent_new.jpg" data-full="../_static/benchmarks/forest_2026-07-03/Tashkent_new.jpg" data-cap="v.2026-07-03 — Uzbekistan — Tashkent" alt="v.2026-07-03 — Uzbekistan — Tashkent" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#ff5028"></span>v.2026-07-03</figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/forest_2026-07-03/Tashkent_old.jpg" data-full="../_static/benchmarks/forest_2026-07-03/Tashkent_old.jpg" data-cap="v.2025-06-14 — Uzbekistan — Tashkent" alt="v.2025-06-14 — Uzbekistan — Tashkent" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#2878ff"></span>v.2025-06-14</figcaption></figure>
   </div>


Summary
-------

**v.2026-07-03** improves substantially over the previous **v.2025-06-14** across all 8 AOIs. Mean
area-based **F1 rises from 0.513 to 0.850** and **IoU from 0.396 to 0.744**, driven by a
large recall gain (0.407 → **0.868**). The previous version was highly conservative —
mean precision 0.955, but it missed most vegetation and collapsed on several AOIs
(e.g. Velilla de San Antonio F1 0.015, Rus F1 0.108, La Banda F1 0.378). v.2026-07-03 keeps
precision high (0.837) while recovering the missed canopy, and leads on F1 in every
location.
