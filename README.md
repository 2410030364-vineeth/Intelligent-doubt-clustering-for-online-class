# Intelligent Doubt Clustering System for Online Classes

A full-stack system that accepts student doubts, embeds them with Sentence Transformers, finds semantically similar questions using cosine similarity, stores everything in MongoDB, and groups related doubts into clusters for a live classroom view.

## Tech Stack

- Backend: FastAPI
- Database: MongoDB at `mongodb://localhost:27017`
- ML/NLP: `sentence-transformers/all-MiniLM-L6-v2`
- Similarity: cosine similarity
- Clustering: DBSCAN over sentence embeddings
- Frontend: React + Vite

## Folder Structure

```text
.
├── backend
│   ├── app
│   │   ├── main.py
│   │   ├── db.py
│   │   ├── models.py
│   │   ├── ml.py
│   │   └── routes
│   │       ├── ask.py
│   │       ├── clusters.py
│   │       └── questions.py
│   ├── requirements.txt
│   └── .env.example
└── frontend
    ├── src
    │   ├── App.jsx
    │   ├── api.js
    │   ├── main.jsx
    │   └── styles.css
    ├── index.html
    ├── package.json
    └── vite.config.js
```

## Run Locally

### 1. Start MongoDB

Make sure MongoDB is running locally:

```bash
mongod --dbpath <your-mongodb-data-folder>
```

The app uses:

```text
mongodb://localhost:27017
Database: doubtDB
Collection: questions
```

### 2. Start Backend

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The first backend start may take longer because the Sentence Transformer model is downloaded and cached.

### 3. Start Frontend

```bash
cd frontend
npm install
npm run dev
```

Open the Vite URL shown in the terminal, usually:

```text
http://localhost:5173
```

## API Endpoints

### `POST /ask`

Request:

```json
{
  "question": "Why is quicksort faster than bubble sort?",
  "class_id": "cs101"
}
```

Response includes the inserted question, top similar doubts, and refreshed cluster assignment.

### `GET /clusters/{class_id}`

Returns grouped questions by cluster, including generated cluster names and repeated-doubt signals.

### `GET /questions/{class_id}`

Returns all questions submitted for a class.

## Notes

- No static or dummy classroom data is used.
- Similarity is semantic embedding similarity, not keyword matching.
- Embeddings are stored once in MongoDB and reused for similarity and clustering.
- Clusters are updated after each insertion for the affected class.
