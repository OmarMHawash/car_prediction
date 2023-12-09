## Packages Used:

### - For scraping & training:

BeautifulSoup, pandas, sklearn, matplotlib

### - For API:

Flask, logging

### Models:

1. **model_v1**: only numeric features, Accuracy: 0.61
2. **model_v2**: numeric + categorical features. Accuracy: 0.71

note: only **model_v1** is used in the api.

## APIS:

**note**: you can import postman collection from `CarPrediction.postman_collection.json` file

### 1.`/api` :

- `GET`: Gives info about app

- `POST`: Makes a prediction using, **accepts**:

```json
{"features": [[year, power, driven_mk, passengers, second_hand_count]]}
```
