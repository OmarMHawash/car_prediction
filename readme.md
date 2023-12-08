## Packages Used:

### - For scraping & training:

BeautifulSoup, pandas, sklearn, matplotlib

### - For API:

Flask, logging

## APIS:

**note**: you can import postman collection from `CarPrediction.postman_collection.json` file

### 1.`/api` :

- `GET`: Gives info about app

- `POST`: Makes a prediction using, **accepts**:

```json
{"features": [[year, power, driven_mk, passengers, second_hand_count]]}
```
