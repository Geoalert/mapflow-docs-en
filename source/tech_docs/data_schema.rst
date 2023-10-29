GeoJSON Output results
----------------------

.. code:: json

  {
    "type": "object",
    "properties": {
        "type": {
        "type": "string"
        },
        "name": {
        "type": "string"
        },
        "features": {
        "type": "array",
        "items": [
            {
            "type": "object",
            "properties": {
                "type": {
                "type": "string"
                },
                "properties": {
                "type": "object",
                "properties": {
                    "area": {
                    "type": "integer"
                    },
                    "object_type": {
                    "type": "string"
                    },
                    "id": {
                    "type": "integer"
                    }
                },
                "required": [
                    "area",
                    "object_type",
                    "id"
                ]
                },
                "geometry": {
                "type": "object",
                "properties": {
                    "type": {
                    "type": "string"
                    },
                    "coordinates": {
                    "type": "array",
                    "items": [
                        {
                        "type": "array",
                        "items": [
                            {
                            "type": "array",
                            "items": [
                                {
                                "type": "number"
                                },
                                {
                                "type": "number"
                                }
                            ]
                            },
                            {
                            "type": "array",
                            "items": [
                                {
                                "type": "number"
                                },
                                {
                                "type": "number"
                                }
                            ]
                            },
                            {
                            "type": "array",
                            "items": [
                                {
                                "type": "number"
                                },
                                {
                                "type": "number"
                                }
                            ]
                            },
                            {
                            "type": "array",
                            "items": [
                                {
                                "type": "number"
                                },
                                {
                                "type": "number"
                                }
                            ]
                            },
                            {
                            "type": "array",
                            "items": [
                                {
                                "type": "number"
                                },
                                {
                                "type": "number"
                                }
                            ]
                            },
                            {
                            "type": "array",
                            "items": [
                                {
                                "type": "number"
                                },
                                {
                                "type": "number"
                                }
                            ]
                            },
                            {
                            "type": "array",
                            "items": [
                                {
                                "type": "number"
                                },
                                {
                                "type": "number"
                                }
                            ]
                            }
                        ]
                        }
                    ]
                    }
                },
                "required": [
                    "type",
                    "coordinates"
                ]
                }
            },
            "required": [
                "type",
                "properties",
                "geometry"
            ]
            },
            {
            "type": "object",
            "properties": {
                "type": {
                "type": "string"
                },
                "properties": {
                "type": "object",
                "properties": {
                    "area": {
                    "type": "integer"
                    },
                    "simplification_confidence_score": {
                    "type": "number"
                    },
                    "object_type": {
                    "type": "string"
                    },
                    "class_id": {
                    "type": "string"
                    },
                    "shape_type": {
                    "type": "string"
                    },
                    "id": {
                    "type": "integer"
                    }
                },
                "required": [
                    "area",
                    "simplification_confidence_score",
                    "object_type",
                    "class_id",
                    "shape_type",
                    "id"
                ]
                },
                "geometry": {
                "type": "object",
                "properties": {
                    "type": {
                    "type": "string"
                    },
                    "coordinates": {
                    "type": "array",
                    "items": [
                        {
                        "type": "array",
                        "items": [
                            {
                            "type": "array",
                            "items": [
                                {
                                "type": "number"
                                },
                                {
                                "type": "number"
                                }
                            ]
                            },
                            {
                            "type": "array",
                            "items": [
                                {
                                "type": "number"
                                },
                                {
                                "type": "number"
                                }
                            ]
                            },
                            {
                            "type": "array",
                            "items": [
                                {
                                "type": "number"
                                },
                                {
                                "type": "number"
                                }
                            ]
                            },
                            {
                            "type": "array",
                            "items": [
                                {
                                "type": "number"
                                },
                                {
                                "type": "number"
                                }
                            ]
                            },
                            {
                            "type": "array",
                            "items": [
                                {
                                "type": "number"
                                },
                                {
                                "type": "number"
                                }
                            ]
                            },
                            {
                            "type": "array",
                            "items": [
                                {
                                "type": "number"
                                },
                                {
                                "type": "number"
                                }
                            ]
                            },
                            {
                            "type": "array",
                            "items": [
                                {
                                "type": "number"
                                },
                                {
                                "type": "number"
                                }
                            ]
                            }
                        ]
                        }
                    ]
                    }
                },
                "required": [
                    "type",
                    "coordinates"
                ]
                }
            },
            "required": [
                "type",
                "properties",
                "geometry"
            ]
            },
            {
            "type": "object",
            "properties": {
                "type": {
                "type": "string"
                },
                "properties": {
                "type": "object",
                "properties": {
                    "object_type": {
                    "type": "string"
                    },
                    "id": {
                    "type": "integer"
                    }
                },
                "required": [
                    "object_type",
                    "id"
                ]
                },
                "geometry": {
                "type": "object",
                "properties": {
                    "type": {
                    "type": "string"
                    },
                    "coordinates": {
                    "type": "array",
                    "items": [
                        {
                        "type": "array",
                        "items": [
                            {
                            "type": "array",
                            "items": [
                                {
                                "type": "number"
                                },
                                {
                                "type": "number"
                                }
                            ]
                            },
                            {
                            "type": "array",
                            "items": [
                                {
                                "type": "number"
                                },
                                {
                                "type": "number"
                                }
                            ]
                            },
                            {
                            "type": "array",
                            "items": [
                                {
                                "type": "number"
                                },
                                {
                                "type": "number"
                                }
                            ]
                            },
                            {
                            "type": "array",
                            "items": [
                                {
                                "type": "number"
                                },
                                {
                                "type": "number"
                                }
                            ]
                            }
                        ]
                        }
                    ]
                    }
                },
                "required": [
                    "type",
                    "coordinates"
                ]
                }
            },
            "required": [
                "type",
                "properties",
                "geometry"
            ]
            }
        ]
        }
    },
    "required": [
        "type",
        "name",
        "features"
    ]
  }


Data sample
^^^^^^^^^^^^^

.. code:: json

    {
        "type": "FeatureCollection",
        "name": "Кобяки_33",
        "features": [
            {
            "type": "Feature",
            "properties": { "area": 272, "object_type": "forest", "id": 46393048 },
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                [
                    [39.507248455367197, 56.036204620276962],
                    [39.50724828091905, 56.03620445905856],
                    [39.50724791675961, 56.036204138538935],
                    [39.507243491470142, 56.03620043013116],
                    [39.507242187932107, 56.036198733024193],
                    [39.507241414453681, 56.036197075687035],
                    [39.50724095094769, 56.03619498653751]
                ]
                ]
            }
            },
            {
            "type": "Feature",
            "properties": {
                "area": 79,
                "simplification_confidence_score": 0.81,
                "GAN": "False",
                "object_type": "buildings",
                "class_id": "105",
                "shape_type": "L-SHAPE",
                "processing_date": "2023-08-29",
                "id": 46393101
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                [
                    [39.507708805145697, 56.036416517299713],
                    [39.507688783737969, 56.036431547997914],
                    [39.507740133942896, 56.036452986105068],
                    [39.50768651688356, 56.036493238078421],
                    [39.507540076090251, 56.036432100613929],
                    [39.507613714642311, 56.036376818020727],
                    [39.507708805145697, 56.036416517299713]
                ]
                ]
            }
            },
            {
            "type": "Feature",
            "properties": { "object_type": "roads", "id": 46393205 },
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                [
                    [39.507254677652867, 56.036134165458982],
                    [39.50587539801684, 56.035906610362908],
                    [39.505872699534379, 56.035905201099204],
                    [39.505861446692045, 56.035893636547563]
                ]
                ]
            }
            }
        ]
    }


Processing MetaDATA
--------------------


.. code:: json
    

    {
        "type": "object",
        "properties": {
        "id": {
            "type": "string"
        },
        "name": {
            "type": "string"
        },
        "description": {
            "type": "string"
        },
        "projectId": {
            "type": "string"
        },
        "vectorLayer": {
            "type": "object",
            "properties": {
            "id": {
                "type": "string"
            },
            "name": {
                "type": "string"
            },
            "tileJsonUrl": {
                "type": "string"
            },
            "tileUrl": {
                "type": "string"
            }
            },
            "required": [
            "id",
            "name",
            "tileJsonUrl",
            "tileUrl"
            ]
        },
        "rasterLayer": {
            "type": "object",
            "properties": {
            "id": {
                "type": "string"
            },
            "tileJsonUrl": {
                "type": "string"
            },
            "tileUrl": {
                "type": "string"
            }
            },
            "required": [
            "id",
            "tileJsonUrl",
            "tileUrl"
            ]
        },
        "workflowDef": {
            "type": "object",
            "properties": {
            "id": {
                "type": "string"
            },
            "name": {
                "type": "string"
            },
            "description": {
                "type": "string"
            },
            "created": {
                "type": "string"
            },
            "updated": {
                "type": "string"
            },
            "pricePerSqKm": {
                "type": "number"
            },
            "blocks": {
                "type": "array",
                "items": []
            }
            },
            "required": [
            "id",
            "name",
            "description",
            "created",
            "updated",
            "pricePerSqKm",
            "blocks"
            ]
        },
        "aoiCount": {
            "type": "integer"
        },
        "aoiArea": {
            "type": "integer"
        },
        "area": {
            "type": "integer"
        },
        "cost": {
            "type": "integer"
        },
        "status": {
            "type": "string"
        },
        "reviewStatus": {
            "type": "string"
        },
        "rating": {
            "type": "string"
        },
        "percentCompleted": {
            "type": "integer"
        },
        "params": {
            "type": "object",
            "properties": {
            "url": {
                "type": "string"
            }
            },
            "required": [
            "url"
            ]
        },
        "blocks": {
            "type": "array",
            "items": []
        },
        "meta": {
            "type": "object",
            "properties": {
            "customer": {
                "type": "string"
            }
            },
            "required": [
            "customer"
            ]
        },
        "messages": {
            "type": "array",
            "items": []
        },
        "created": {
            "type": "string"
        },
        "updated": {
            "type": "string"
        }
        },
        "required": [
        "id",
        "name",
        "description",
        "projectId",
        "vectorLayer",
        "rasterLayer",
        "workflowDef",
        "aoiCount",
        "aoiArea",
        "area",
        "cost",
        "status",
        "reviewStatus",
        "rating",
        "percentCompleted",
        "params",
        "blocks",
        "meta",
        "messages",
        "created",
        "updated"
        ]
    }


Data sample
^^^^^^^^^^^^^

.. code:: json

    {
        "id": "79a3b2ed-5ddd-4ba3-ac55-0a7595ea1fa2",
        "name": "Test processing",
        "description": null,
        "projectId": "caa4de85-1d5e-4e5a-8da8-7cb45ee65bae",
        "vectorLayer": {
            "id": "253d3440-01be-4815-8d39-61aaac64b324",
            "name": "Выползово_33",
            "tileJsonUrl": "https://mapflow.ai/api/layers/97852e7b-896e-495a-a29c-041bc149ab69.json",
            "tileUrl": "https://mapflow.ai/api/layers/97852e7b-896e-495a-a29c-041bc149ab69/tiles/{z}/{x}/{y}.vector.pbf"
        },
        "rasterLayer": {
            "id": "81bf4b2f-2f53-49d2-88c1-4f9a394f3fdc",
            "tileJsonUrl": "https://mapflow.ai/api/v0/cogs/tiles.json?uri=s3://white-maps-rasters/fa0cf35c-4390-4f13-8c43-21bbab15cb32",
            "tileUrl": "https://mapflow.ai/api/v0/cogs/tiles/{z}/{x}/{y}.png?uri=s3://white-maps-rasters/fa0cf35c-4390-4f13-8c43-21bbab15cb32"
        },
        "workflowDef": {
            "id": "4e66b409-72b7-4a6f-a48a-d2c36cb2c2ca",
            "name": "[debug] Combo (Forest Roads Buildings)",
            "description": "",
            "created": "2023-08-01T12:42:40.197118Z",
            "updated": "2023-09-03T08:04:29.706784Z",
            "pricePerSqKm": 33.0,
            "blocks": []
        },
        "aoiCount": 1,
        "aoiArea": 78601,
        "area": 78601,
        "cost": 33,
        "status": "OK",
        "reviewStatus": null,
        "rating": null,
        "percentCompleted": 100,
        "params": {
            "url": "https://api.tiles.mapbox.com/v4/mapbox.satellite/{z}/{x}/{y}.jpg?access_token={token}"
        },
        "blocks": [],
        "meta": {
            "project": "test"
        },
        "messages": [],
        "created": "2023-08-29T04:22:37.184553Z",
        "updated": "2023-08-29T04:22:37.184554Z"
    }