Here’s the updated README for **Fantasy-Football-Helper**:

---

# **Fantasy-Football-Helper**

### **Your Ultimate Interactive Fantasy Football Assistant**

Fantasy-Football-Helper is a cool, interactive tool designed to help you make smarter decisions about who to start in your fantasy football lineup. Leveraging **Retrieval-Augmented Generation (RAG)** technology, and relevant articles using **Weaviate** and its **text-to-vector transformers**. If you have an ESPN Fantasy League, this tool takes it a step further by integrating directly with your league data for tailored recommendations!

---

## **Features**

- **Player Comparisons**: Select two players to compare and get detailed projections, stats, and context to make the best choice.
- **League Integration**: Use your exact ESPN Fantasy League data to further personalize recommendations.
- **RAG**: Combines player stats with contextual data from articles for smarter, data-backed advice.

---

## **Setup**

### **1. Clone the Repository**
```bash
git clone <repo-url>
cd Fantasy-Football-Helper
```

### **2. Create a `.env` File**
```bash
touch .env
```

Fill in the following details in the `.env` file:
```
SWID=<Your ESPN SWID>
ESPN_2=<Your ESPN_2 Key>
API_KEY_OPENAI=<Your OpenAI API Key>
LEAGUE_ID=<Your ESPN League ID>
```

### **3. Start the Application**
Use Docker to quickly get started:
```bash
docker-compose up -d
```

---

## **Adding Player URLs**

To build your Weaviate database, you'll need to add player-related articles:

1. **Run the Schema Setup**:
   ```bash
   python3 wev_db/create_tranformer_dataSchema.py
   ```

2. **Add URLs to Weaviate**:
   - **Add a Whole Directory**:
     ```bash
     python3 wev_db/add_url_to_transformerDB.py --directory wev_db/player_urls/[category_directory]
     ```
   - **Add a Specific File**:
     ```bash
     python3 wev_db/add_url_to_transformerDB.py --file wev_db/player_urls/[category_directory]/[player_name]
     ```

---

## **Running the Application**

Once the data is set up:
```bash
python3 run.py
```

Visit the app in your browser at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## **How It Works**

- Select two players to compare, and the app will show their projections, stats, and relevant context.
- Ask questions about a specific player, and get tailored advice based on stats and contextual articles.
- Enjoy a streamlined, data-driven fantasy football experience!

---

**Get ready to dominate your fantasy league with Fantasy-Football-Helper!** 🏈🎉
