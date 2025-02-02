LLM Based Movie RecSys

## Configuration

Create a `.env` file in the root directory of the project to store your MongoDB connection string: 
```
MONGO_URI=mongodb://your-username:your-password@cluster-url/your-database
```

## Exporting the Movies Dataset

To export the `movies` dataset from the `sample_mlfix` collection in your MongoDB database and save it as a `movies.json` file, you can execute the `db_export.py` script. This script connects to your MongoDB instance, retrieves the dataset, and writes it to a JSON file for easy sharing and analysis.
