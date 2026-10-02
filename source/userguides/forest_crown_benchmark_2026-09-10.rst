:orphan:

.. _forest_crown_benchmark_2026-09-10:

.. role:: raw-html(raw)
   :format: html

🌲 Forest and trees v.2026-09-10 — tree crown benchmark
================================================================

This page details the validation of tree **crown polygons** produced by the
**🌲 Forest and trees v.2026-09-10** model on 7 areas of interest (AOI), compared against the
**previous version v.2026-07-03**. For each AOI the two crown-mask results are shown side by
side; click any image to open it full size, and use the ← / → arrow keys to browse
between them.

Metrics are area-based on the crown masks: **IoU** is the intersection-over-union of the
predicted and ground-truth crown masks, and **F1 / Precision / Recall** are computed on
the overlapping mask area. **Crowns** is the number of detected crown polygons; the
ground-truth crown count and the relative count error are reported below each AOI (see
also the *Tree count accuracy* table on the model page). Evaluation run: 2026-10-01.

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

**Mask colour legend:** :raw-html:`<span class="mchip" style="background:#ff5028"></span>` **v.2026-09-10**  ·  :raw-html:`<span class="mchip" style="background:#2878ff"></span>` **v.2026-07-03**


Italy — Crotone
~~~~~~~~~~~~~~~

.. list-table::
   :widths: 28 14 14 14 14 16
   :header-rows: 1

   * - Model
     - IoU
     - F1
     - Precision
     - Recall
     - Crowns
   * - :raw-html:`<span class="mchip" style="background:#ff5028"></span>` **v.2026-09-10**
     - **0.842**
     - **0.914**
     - **0.930**
     - **0.898**
     - 254
   * - :raw-html:`<span class="mchip" style="background:#2878ff"></span>` v.2026-07-03
     - 0.825
     - 0.904
     - 0.925
     - 0.884
     - 254



.. raw:: html

   <div class="bench-row">
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/forest_crown_2026-09-10/Crotone_new.jpg" data-full="../_static/benchmarks/forest_crown_2026-09-10/Crotone_new.jpg" data-cap="v.2026-09-10 — Italy — Crotone" alt="v.2026-09-10 — Italy — Crotone" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#ff5028"></span>v.2026-09-10</figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/forest_crown_2026-09-10/Crotone_old.jpg" data-full="../_static/benchmarks/forest_crown_2026-09-10/Crotone_old.jpg" data-cap="v.2026-07-03 — Italy — Crotone" alt="v.2026-07-03 — Italy — Crotone" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#2878ff"></span>v.2026-07-03</figcaption></figure>
   </div>


Argentina — La Banda
~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 28 14 14 14 14 16
   :header-rows: 1

   * - Model
     - IoU
     - F1
     - Precision
     - Recall
     - Crowns
   * - :raw-html:`<span class="mchip" style="background:#ff5028"></span>` **v.2026-09-10**
     - **0.624**
     - **0.769**
     - **0.700**
     - **0.852**
     - 111
   * - :raw-html:`<span class="mchip" style="background:#2878ff"></span>` v.2026-07-03
     - 0.575
     - 0.730
     - 0.691
     - 0.774
     - 83



.. raw:: html

   <div class="bench-row">
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/forest_crown_2026-09-10/LaBanda_new.jpg" data-full="../_static/benchmarks/forest_crown_2026-09-10/LaBanda_new.jpg" data-cap="v.2026-09-10 — Argentina — La Banda" alt="v.2026-09-10 — Argentina — La Banda" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#ff5028"></span>v.2026-09-10</figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/forest_crown_2026-09-10/LaBanda_old.jpg" data-full="../_static/benchmarks/forest_crown_2026-09-10/LaBanda_old.jpg" data-cap="v.2026-07-03 — Argentina — La Banda" alt="v.2026-07-03 — Argentina — La Banda" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#2878ff"></span>v.2026-07-03</figcaption></figure>
   </div>


Spain — Rus
~~~~~~~~~~~

.. list-table::
   :widths: 28 14 14 14 14 16
   :header-rows: 1

   * - Model
     - IoU
     - F1
     - Precision
     - Recall
     - Crowns
   * - :raw-html:`<span class="mchip" style="background:#ff5028"></span>` **v.2026-09-10**
     - **0.689**
     - **0.816**
     - **0.759**
     - **0.883**
     - 239
   * - :raw-html:`<span class="mchip" style="background:#2878ff"></span>` v.2026-07-03
     - 0.567
     - 0.723
     - 0.671
     - 0.785
     - 249



.. raw:: html

   <div class="bench-row">
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/forest_crown_2026-09-10/Rus_new.jpg" data-full="../_static/benchmarks/forest_crown_2026-09-10/Rus_new.jpg" data-cap="v.2026-09-10 — Spain — Rus" alt="v.2026-09-10 — Spain — Rus" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#ff5028"></span>v.2026-09-10</figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/forest_crown_2026-09-10/Rus_old.jpg" data-full="../_static/benchmarks/forest_crown_2026-09-10/Rus_old.jpg" data-cap="v.2026-07-03 — Spain — Rus" alt="v.2026-07-03 — Spain — Rus" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#2878ff"></span>v.2026-07-03</figcaption></figure>
   </div>


Philippines — Balanga
~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 28 14 14 14 14 16
   :header-rows: 1

   * - Model
     - IoU
     - F1
     - Precision
     - Recall
     - Crowns
   * - :raw-html:`<span class="mchip" style="background:#ff5028"></span>` **v.2026-09-10**
     - 0.780
     - 0.876
     - 0.849
     - **0.904**
     - 309
   * - :raw-html:`<span class="mchip" style="background:#2878ff"></span>` v.2026-07-03
     - **0.782**
     - **0.878**
     - **0.860**
     - 0.896
     - 220



.. raw:: html

   <div class="bench-row">
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/forest_crown_2026-09-10/Balanga_new.jpg" data-full="../_static/benchmarks/forest_crown_2026-09-10/Balanga_new.jpg" data-cap="v.2026-09-10 — Philippines — Balanga" alt="v.2026-09-10 — Philippines — Balanga" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#ff5028"></span>v.2026-09-10</figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/forest_crown_2026-09-10/Balanga_old.jpg" data-full="../_static/benchmarks/forest_crown_2026-09-10/Balanga_old.jpg" data-cap="v.2026-07-03 — Philippines — Balanga" alt="v.2026-07-03 — Philippines — Balanga" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#2878ff"></span>v.2026-07-03</figcaption></figure>
   </div>


Spain — Cuenca
~~~~~~~~~~~~~~

.. list-table::
   :widths: 28 14 14 14 14 16
   :header-rows: 1

   * - Model
     - IoU
     - F1
     - Precision
     - Recall
     - Crowns
   * - :raw-html:`<span class="mchip" style="background:#ff5028"></span>` **v.2026-09-10**
     - **0.732**
     - **0.846**
     - **0.875**
     - **0.818**
     - 433
   * - :raw-html:`<span class="mchip" style="background:#2878ff"></span>` v.2026-07-03
     - 0.728
     - 0.842
     - 0.868
     - 0.818
     - 409



.. raw:: html

   <div class="bench-row">
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/forest_crown_2026-09-10/Cuenca_new.jpg" data-full="../_static/benchmarks/forest_crown_2026-09-10/Cuenca_new.jpg" data-cap="v.2026-09-10 — Spain — Cuenca" alt="v.2026-09-10 — Spain — Cuenca" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#ff5028"></span>v.2026-09-10</figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/forest_crown_2026-09-10/Cuenca_old.jpg" data-full="../_static/benchmarks/forest_crown_2026-09-10/Cuenca_old.jpg" data-cap="v.2026-07-03 — Spain — Cuenca" alt="v.2026-07-03 — Spain — Cuenca" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#2878ff"></span>v.2026-07-03</figcaption></figure>
   </div>


Spain — Velilla de San Antonio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 28 14 14 14 14 16
   :header-rows: 1

   * - Model
     - IoU
     - F1
     - Precision
     - Recall
     - Crowns
   * - :raw-html:`<span class="mchip" style="background:#ff5028"></span>` **v.2026-09-10**
     - **0.694**
     - **0.819**
     - **0.855**
     - **0.786**
     - 1,134
   * - :raw-html:`<span class="mchip" style="background:#2878ff"></span>` v.2026-07-03
     - 0.667
     - 0.800
     - 0.831
     - 0.771
     - 1,070



.. raw:: html

   <div class="bench-row">
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/forest_crown_2026-09-10/Velilla_new.jpg" data-full="../_static/benchmarks/forest_crown_2026-09-10/Velilla_new.jpg" data-cap="v.2026-09-10 — Spain — Velilla de San Antonio" alt="v.2026-09-10 — Spain — Velilla de San Antonio" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#ff5028"></span>v.2026-09-10</figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/forest_crown_2026-09-10/Velilla_old.jpg" data-full="../_static/benchmarks/forest_crown_2026-09-10/Velilla_old.jpg" data-cap="v.2026-07-03 — Spain — Velilla de San Antonio" alt="v.2026-07-03 — Spain — Velilla de San Antonio" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#2878ff"></span>v.2026-07-03</figcaption></figure>
   </div>


Spain — Madrid
~~~~~~~~~~~~~~

.. list-table::
   :widths: 28 14 14 14 14 16
   :header-rows: 1

   * - Model
     - IoU
     - F1
     - Precision
     - Recall
     - Crowns
   * - :raw-html:`<span class="mchip" style="background:#ff5028"></span>` **v.2026-09-10**
     - **0.823**
     - **0.903**
     - **0.907**
     - 0.899
     - 398
   * - :raw-html:`<span class="mchip" style="background:#2878ff"></span>` v.2026-07-03
     - 0.801
     - 0.889
     - 0.879
     - **0.900**
     - 368


.. raw:: html

   <div class="bench-row">
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/forest_crown_2026-09-10/Madrid_new.jpg" data-full="../_static/benchmarks/forest_crown_2026-09-10/Madrid_new.jpg" data-cap="v.2026-09-10 — Spain — Madrid" alt="v.2026-09-10 — Spain — Madrid" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#ff5028"></span>v.2026-09-10</figcaption></figure>
     <figure class="bench-fig"><img class="bench-img" src="../_static/benchmarks/forest_crown_2026-09-10/Madrid_old.jpg" data-full="../_static/benchmarks/forest_crown_2026-09-10/Madrid_old.jpg" data-cap="v.2026-07-03 — Spain — Madrid" alt="v.2026-07-03 — Spain — Madrid" loading="lazy"><figcaption class="bench-cap"><span class="mchip" style="background:#2878ff"></span>v.2026-07-03</figcaption></figure>
   </div>


Summary
-------

For tree crown polygons, **v.2026-09-10** improves on **v.2026-07-03** across the 7 AOIs: mean
area-based **F1 rises from 0.824 to 0.849** and **IoU from 0.706 to 0.741**, with gains
in both precision (0.818 → 0.839) and recall (0.833 → 0.863). It leads on F1 in 6 of the
7 AOIs and is on par at Balanga (0.876 vs 0.878).

On **tree count accuracy** the picture is mixed. We will provide more evidence on the later benchmarks based on results against the validated  mapping surveys.
