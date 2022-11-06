# Repository style

import pymongo

class StockRepository:
    def __init__(self, connStr, database):
        self.client = pymongo.MongoClient(connStr)
        self.db = self.client[database]
        self.infos = self.db['stocks']   # collection
        self.prices = self.db["stockPrices"]
    
    def replaceInfos(self, doc):
        result = self.infos.replace_one({'symbol': doc['symbol']}, doc, upsert=True)
        # See ReplaceOneResult
        return {
            # 'acknowledged': result.acknowledged,
            'matched_count': result.matched_count,
            'modified_count': result.modified_count,   # 0 if insert
            # 'raw_result': result.raw_result,
            'upserted_id': result.upserted_id,         # None if update
        }
    
    def insertPrices(self, docs):
        result = self.prices.insert_many(docs)
        # See InsertManyResult
        return {
            # 'acknowledged': result.acknowledged,
            # 'inserted_ids': result.inserted_ids ,
            'len(inserted_ids)': len(result.inserted_ids)
        } 
        
    def truncatePrices(self):
        self.prices.drop()
        return {}
        
if __name__ == '__main__':
    connStr = "mongodb://localhost27017"
    database = "myProjectDB"
    repo = StockRepository(connStr, database)