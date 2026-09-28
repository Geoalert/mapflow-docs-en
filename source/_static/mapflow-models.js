/* The models used to live on one long page (userguides/pipelines.html).
   Links from the website, the QGIS plugin and old posts point to its anchors,
   e.g. pipelines.html#forest-and-trees. Send them to the model's own page. */
(function () {
  if (!/\/pipelines\.html$/.test(window.location.pathname)) return;
  var pages = {
    'buildings': 'buildings_model.html',
    'buildings-model': 'buildings_model.html',
    'benchmarks-segmentation': 'buildings_model.html#benchmarks',
    'aerial-imagery': 'buildings_model.html#benchmarks',
    'satellite-imagery': 'buildings_model.html#benchmarks',
    'forest-and-trees': 'forest_model.html',
    'forest-classes': 'forest_model.html#forest-classes',
    'roads': 'roads_model.html',
    'multi-buildings-roads-forest': 'combo_model.html',
    'download-open-data': 'open-data.html',
    'custom-models': 'custom_pipelines.html',
    'constructions-custom': 'construction_model.html',
    'high-density-housing-custom': 'hd_housing_model.html',
    'tractor-agriculture-fields-custom': 'agriculture_fields_model.html',
    'segment-anything-v1-custom': 'sam_model.html',
    'swimming-pools-custom': 'swimming_pools_model.html',
    'sunny-solar-panels-custom': 'solars_model.html'
  };
  var target = pages[decodeURIComponent(window.location.hash.slice(1))];
  if (target) window.location.replace(target);
})();
