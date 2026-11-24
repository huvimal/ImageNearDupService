# ImageNearDupService — measured local run

Local perceptual-hash retrieval core over authored geometric images. No network service, learned image embedding, general transformation invariance or production service claim.

## Results

```json
{
  "development_selected_hamming_threshold": 22,
  "test_cases": [
    {
      "source": 8,
      "transform": "blur",
      "top_match": 8,
      "distance": 0,
      "correct": true
    },
    {
      "source": 8,
      "transform": "rotate",
      "top_match": 8,
      "distance": 8,
      "correct": true
    },
    {
      "source": 8,
      "transform": "resize",
      "top_match": 8,
      "distance": 0,
      "correct": true
    },
    {
      "source": 9,
      "transform": "blur",
      "top_match": 9,
      "distance": 0,
      "correct": true
    },
    {
      "source": 9,
      "transform": "rotate",
      "top_match": 2,
      "distance": 20,
      "correct": false
    },
    {
      "source": 9,
      "transform": "resize",
      "top_match": 9,
      "distance": 2,
      "correct": true
    },
    {
      "source": 10,
      "transform": "blur",
      "top_match": 10,
      "distance": 0,
      "correct": true
    },
    {
      "source": 10,
      "transform": "rotate",
      "top_match": 10,
      "distance": 8,
      "correct": true
    },
    {
      "source": 10,
      "transform": "resize",
      "top_match": 10,
      "distance": 2,
      "correct": true
    },
    {
      "source": 11,
      "transform": "blur",
      "top_match": 11,
      "distance": 0,
      "correct": true
    },
    {
      "source": 11,
      "transform": "rotate",
      "top_match": 11,
      "distance": 20,
      "correct": true
    },
    {
      "source": 11,
      "transform": "resize",
      "top_match": 11,
      "distance": 0,
      "correct": true
    },
    {
      "source": 12,
      "transform": "blur",
      "top_match": 12,
      "distance": 0,
      "correct": true
    },
    {
      "source": 12,
      "transform": "rotate",
      "top_match": 3,
      "distance": 18,
      "correct": false
    },
    {
      "source": 12,
      "transform": "resize",
      "top_match": 12,
      "distance": 0,
      "correct": true
    },
    {
      "source": 13,
      "transform": "blur",
      "top_match": 13,
      "distance": 0,
      "correct": true
    },
    {
      "source": 13,
      "transform": "rotate",
      "top_match": 13,
      "distance": 20,
      "correct": true
    },
    {
      "source": 13,
      "transform": "resize",
      "top_match": 13,
      "distance": 0,
      "correct": true
    },
    {
      "source": 14,
      "transform": "blur",
      "top_match": 14,
      "distance": 0,
      "correct": true
    },
    {
      "source": 14,
      "transform": "rotate",
      "top_match": 14,
      "distance": 18,
      "correct": true
    },
    {
      "source": 14,
      "transform": "resize",
      "top_match": 14,
      "distance": 0,
      "correct": true
    },
    {
      "source": 15,
      "transform": "blur",
      "top_match": 15,
      "distance": 0,
      "correct": true
    },
    {
      "source": 15,
      "transform": "rotate",
      "top_match": 15,
      "distance": 12,
      "correct": true
    },
    {
      "source": 15,
      "transform": "resize",
      "top_match": 15,
      "distance": 0,
      "correct": true
    }
  ],
  "test_top1": 0.9166666666666666,
  "checks": [
    "Actual DC-excluded DCT perceptual hash",
    "Separate source-image slice for evaluation"
  ],
  "scope": "Local perceptual-hash retrieval core over authored geometric images. No network service, learned image embedding, general transformation invariance or production service claim."
}
```

Local experiment assertions passed. This does not establish production readiness or performance on real customer data. Source fingerprints and dependency versions are in results.json.
